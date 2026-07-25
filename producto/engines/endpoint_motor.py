"""
Endpoint REST de respaldo — Motor de Scoring Colsubsidio
Servidor HTTP stdlib-only: cero dependencias pip.
Uso: python3 endpoint_motor.py
Puerto por defecto: 8090 (configurable con variable de entorno PORT).
"""

import importlib.util
import json
import os
import sys
import traceback
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# ---------------------------------------------------------------------------
# Resolución de rutas: este archivo vive en producto/engines/
# ---------------------------------------------------------------------------
_ENGINES_DIR = Path(__file__).resolve().parent
_PRODUCT_DIR = _ENGINES_DIR.parent
_DB_DIR = _PRODUCT_DIR / "db"

# Añade producto/db al path para importar trazabilidad
if str(_DB_DIR) not in sys.path:
    sys.path.insert(0, str(_DB_DIR))

# Carga motor-colsubsidio.py como módulo (nombre con guiones, importlib requerido)
_MOTOR_PATH = _ENGINES_DIR / "motor-colsubsidio.py"
_spec = importlib.util.spec_from_file_location("motor_colsubsidio", _MOTOR_PATH)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["motor_colsubsidio"] = _mod
_spec.loader.exec_module(_mod)

MotorScoring = _mod.MotorScoring

# Versión declarada por el módulo, si existe; de lo contrario vacío
MOTOR_VERSION = getattr(_mod, "VERSION", "")

# Instancia compartida del motor (stateless, seguro para threads)
_motor = MotorScoring()

# ---------------------------------------------------------------------------
# Trazabilidad (best-effort)
# ---------------------------------------------------------------------------
try:
    import trazabilidad as _traz

    _traz.init_db()
    _TRAZ_OK = True
except Exception:
    _TRAZ_OK = False


def _registrar(perfil: dict, resultado, session_id: str) -> None:
    """Escribe sesión + features + outputs en la DB. Lanza excepción si falla."""
    if not _TRAZ_OK:
        raise RuntimeError("módulo trazabilidad no disponible")

    _traz.crear_sesion(canal="api_rest", origen="endpoint_respaldo", session_id=session_id)

    for code, valor in perfil.items():
        _traz.registrar_feature(session_id, code, valor, "api_rest")

    for r in resultado.top_3:
        # Construye el 'porque' con las variables de alto peso del producto
        idx = _motor._product_index[r.key]
        razones = [
            d.code
            for d in resultado.desglose
            if d.pesos[idx] >= 3
        ]
        porque = ", ".join(razones) if razones else "scoring"
        _traz.registrar_output(
            session_id,
            MOTOR_VERSION or "v1.0",
            r.key,
            r.score,
            r.pct,
            r.rank,
            r.modo_cierre,
            porque,
        )

    _traz.cerrar_sesion(session_id, "cerrada")


# ---------------------------------------------------------------------------
# Handler HTTP
# ---------------------------------------------------------------------------
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}


class MotorHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):  # silencia el log por defecto
        pass

    def _send(self, status: int, body: dict) -> None:
        payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(payload)

    def _read_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        return json.loads(raw)

    # ------------------------------------------------------------------
    # OPTIONS — preflight CORS
    # ------------------------------------------------------------------
    def do_OPTIONS(self):
        self.send_response(204)
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()

    # ------------------------------------------------------------------
    # GET /salud
    # ------------------------------------------------------------------
    def do_GET(self):
        if self.path.rstrip("/") == "/salud":
            body = {"ok": True}
            if MOTOR_VERSION:
                body["motor"] = MOTOR_VERSION
            self._send(200, body)
        else:
            self._send(404, {"error": "ruta no encontrada"})

    # ------------------------------------------------------------------
    # POST /recomendar
    # ------------------------------------------------------------------
    def do_POST(self):
        if self.path.rstrip("/") != "/recomendar":
            self._send(404, {"error": "ruta no encontrada"})
            return

        # 1. Parsear body
        try:
            data = self._read_body()
        except Exception:
            self._send(400, {"error": "JSON inválido o Content-Length ausente"})
            return

        # 2. Extraer campos
        perfil = data.get("perfil")
        producto_explicito = data.get("producto_explicito")  # opcional

        if not isinstance(perfil, dict):
            self._send(400, {"error": "Campo 'perfil' requerido (objeto con V1-V11)"})
            return

        # 3. Llamar al motor
        try:
            resultado = _motor.calcular_scores(perfil, producto_explicito)
        except ValueError as exc:
            self._send(400, {"error": str(exc)})
            return
        except Exception:
            self._send(500, {"error": "Error interno del motor"})
            return

        # 4. Construir respuesta — los números salen 100% del motor
        top_3 = [r.to_dict() for r in resultado.top_3]
        response: dict = {"top_3": top_3}

        # 5. Trazabilidad (best-effort)
        session_id = str(uuid.uuid4())
        try:
            _registrar(perfil, resultado, session_id)
            response["trazabilidad"] = "ok"
            response["session_id"] = session_id
        except Exception:
            response["trazabilidad"] = "error"

        self._send(200, response)


# ---------------------------------------------------------------------------
# Arranque
# ---------------------------------------------------------------------------
def main():
    port = int(os.environ.get("PORT", 8090))
    server = ThreadingHTTPServer(("0.0.0.0", port), MotorHandler)
    print(f"Motor endpoint escuchando en http://0.0.0.0:{port}")
    print("  GET  /salud      → health check")
    print("  POST /recomendar → scoring top-3")
    print("Ctrl-C para detener.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

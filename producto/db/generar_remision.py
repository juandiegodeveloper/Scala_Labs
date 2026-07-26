"""Informe de remisión a la aseguradora — el "por detrás" de Amparito.

Capa 2 de la narrativa: el usuario solo ve "tu solicitud está en trámite";
este script genera lo que viaja por detrás hacia la aseguradora del convenio,
que asume la póliza y solo recauda. Produce:

  1. El informe en formato correo (asunto + cuerpo) por stdout — listo para
     pegarse en el canal que se acuerde.
  2. La misma remisión como fila en `remisiones.csv` (junto a la DB), porque
     la infraestructura actual Colsubsidio ↔ aseguradoras es Excel.

La ruta definitiva de entrega (correo / Excel / API) está por validar con los
mentores del reto — este artefacto demuestra que el dato ya sale estructurado
y auditable desde la DB de trazabilidad, sin importar el transporte.

CERO PII: la identidad viaja únicamente como hash SHA-256 (Ley 1581); el
perfil son las variables V1–V11 con valores categóricos.

Uso:
    python3 generar_remision.py [session_id]
    # sin argumento: usa la sesión cerrada más reciente de interactions.db
"""

import csv
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent / "interactions.db"
CSV_PATH = Path(__file__).parent / "remisiones.csv"

CSV_COLUMNAS = [
    "fecha_remision", "session_id", "id_hash", "canal", "origen",
    "producto_id", "pct_afinidad", "score", "modo_cierre", "porque",
    "motor_version",
] + [f"V{i}" for i in range(1, 12)]


def _conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def cargar_sesion(session_id=None):
    """Trae sesión + features + output rank 1. Sin argumento: la más reciente cerrada."""
    with _conn() as con:
        if session_id:
            ses = con.execute(
                "SELECT * FROM sessions WHERE session_id=?", (session_id,)
            ).fetchone()
        else:
            ses = con.execute(
                "SELECT * FROM sessions WHERE estado_final IS NOT NULL "
                "ORDER BY started_at DESC LIMIT 1"
            ).fetchone()
        if ses is None:
            raise SystemExit(f"Sesión no encontrada en {DB_PATH.name}: {session_id or '(ninguna cerrada)'}")

        sid = ses["session_id"]
        features = {
            r["variable"]: (r["valor"], r["fuente"])
            for r in con.execute("SELECT * FROM features WHERE session_id=?", (sid,))
        }
        top1 = con.execute(
            "SELECT * FROM outputs WHERE session_id=? ORDER BY rank LIMIT 1", (sid,)
        ).fetchone()
        if top1 is None:
            raise SystemExit(f"La sesión {sid} no tiene outputs del motor — nada que remitir.")
        return ses, features, top1


def informe_correo(ses, features, top1):
    """Arma el informe formato correo. Todas las cifras vienen de la DB (motor)."""
    identidad = ses["id_hash"] or "sin identificación registrada"
    lineas = [
        f"ASUNTO: Remisión de solicitud aprobada — {top1['producto_id']} · sesión {ses['session_id'][:8]}",
        "",
        "Equipo aseguradora del convenio:",
        "",
        "Adjuntamos una solicitud aprobada por el cliente en el canal digital de",
        "Colsubsidio (asistente Amparito). El lead llega validado, calificado por el",
        "motor determinista de reglas y con consentimiento registrado.",
        "",
        f"  Producto aprobado : {top1['producto_id']}",
        f"  Afinidad del motor: {top1['pct_afinidad']}% (score {top1['score']}, "
        f"rank {top1['rank']}, cierre '{top1['modo_cierre']}')",
        f"  Porqué del motor  : {top1['porque']}",
        f"  Motor             : {top1['motor_version']}",
        "",
        f"  Sesión            : {ses['session_id']}",
        f"  Canal / origen    : {ses['canal']} / {ses['origen']}",
        f"  Inicio / cierre   : {ses['started_at']} → {ses['ended_at'] or 'en curso'}",
        f"  Identidad (hash)  : {identidad}",
        f"  Consentimientos   : datos={ses['consent_datos']} · compra={ses['consent_compra']}",
        "",
        "  Perfil (variables V1–V11, valores categóricos):",
    ]
    for i in range(1, 12):
        var = f"V{i}"
        valor, fuente = features.get(var, ("—", "—"))
        lineas.append(f"    {var:<4}: {valor}  [{fuente}]")
    lineas += [
        "",
        f"Remisión generada: {_now()}",
        "— Amparito · Scala Labs · Hackathon Colsubsidio × 30X",
    ]
    return "\n".join(lineas)


def fila_csv(ses, features, top1):
    fila = {
        "fecha_remision": _now(),
        "session_id": ses["session_id"],
        "id_hash": ses["id_hash"] or "",
        "canal": ses["canal"],
        "origen": ses["origen"],
        "producto_id": top1["producto_id"],
        "pct_afinidad": top1["pct_afinidad"],
        "score": top1["score"],
        "modo_cierre": top1["modo_cierre"],
        "porque": top1["porque"],
        "motor_version": top1["motor_version"],
    }
    for i in range(1, 12):
        fila[f"V{i}"] = features.get(f"V{i}", ("", ""))[0]
    return fila


def registrar_csv(fila, destino=CSV_PATH):
    nuevo = not Path(destino).exists()
    with open(destino, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNAS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)
    return destino


if __name__ == "__main__":
    session_id = sys.argv[1] if len(sys.argv) > 1 else None
    ses, features, top1 = cargar_sesion(session_id)
    print(informe_correo(ses, features, top1))
    destino = registrar_csv(fila_csv(ses, features, top1))
    print(f"\n[csv] Remisión registrada en {destino}")

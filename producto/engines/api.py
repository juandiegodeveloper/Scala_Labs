# -*- coding: utf-8 -*-
"""
API del motor de scoring — Amparito / Scala Labs.
Envuelve motor-colsubsidio.py como un endpoint REST para que el chat (o Make) lo consuma.

Correr local:   uvicorn api:app --host 0.0.0.0 --port 8000
En Render:      Start Command  ->  uvicorn api:app --host 0.0.0.0 --port $PORT
"""
import importlib.util, os, sys
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# El motor tiene guion en el nombre de archivo, así que no es importable normal:
# se carga a mano y se registra en sys.modules (necesario por los @dataclass).
_ruta = os.path.join(os.path.dirname(__file__), "motor-colsubsidio.py")
_spec = importlib.util.spec_from_file_location("motor_colsubsidio", _ruta)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["motor_colsubsidio"] = _mod
_spec.loader.exec_module(_mod)

motor = _mod.MotorScoring()

app = FastAPI(title="Amparito — Motor de scoring", version="1.0")

# CORS abierto: permite que el chat (aunque esté alojado en otro dominio) llame a la API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

@app.get("/")
def health():
    return {
        "ok": True,
        "servicio": "Amparito — motor de scoring de seguros",
        "variables": [v["code"] for v in motor.variables],
    }

@app.post("/recomendar")
async def recomendar(req: Request):
    """Recibe {perfil:{V1..V11}, producto_explicito?, afiliado?} y devuelve el top 3 con su porqué."""
    try:
        body = await req.json()
    except Exception:
        return JSONResponse(status_code=400, content={"error": "El body debe ser JSON."})
    perfil = body.get("perfil") or {}
    explicito = body.get("producto_explicito")
    afiliado = body.get("afiliado")
    try:
        r = motor.calcular_scores(perfil, explicito)
    except ValueError as e:
        return JSONResponse(status_code=422, content={"error": str(e)})
    return {
        "top": r.top.to_dict(),
        "top_3": [p.to_dict() for p in r.top_3],
        "ficha": motor.ficha_texto(perfil, explicito, afiliado),
    }

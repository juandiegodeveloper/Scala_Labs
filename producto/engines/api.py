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

# --- LLM (Gemini) para la conversación de Amparito ---
import json
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
try:
    import google.generativeai as genai
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
except Exception:
    genai = None

def _system_prompt():
    reglas_vars = "\n".join(
        f'- {v["code"]} = {v["label"]} · categorías válidas EXACTAS: {v["categorias"]}'
        for v in motor.variables
    )
    return (
        "Eres Amparito, la asesora digital de seguros de Colsubsidio: cálida, cercana, honesta, "
        "sin tecnicismos, como una señora colombiana que de verdad te cuida. Conversas de forma "
        "natural, UNA sola pregunta por mensaje, nunca como un formulario. No repitas datos ya "
        "dados; reacciona a lo que dice la persona; máximo un emoji ocasional; si te preguntan "
        "algo, respóndelo antes de seguir; NUNCA inventes cifras ni precios (de eso se encarga "
        "el motor). Tu meta es llenar el perfil de 11 variables, mapeando lo que diga la persona "
        "a UNA categoría válida EXACTA de cada una:\n"
        f"{reglas_vars}\n\n"
        "El género (V2) y la jefatura femenina (V11) NO se preguntan directo: se infieren del "
        "nombre y el contexto. La cédula y datos sensibles van al final.\n\n"
        "Responde SIEMPRE en JSON válido, sin texto extra, con esta forma:\n"
        '{"reply": "lo que le dices (2-4 líneas)", "perfil": {"V1": "categoría exacta", ...solo '
        'las que ya conoces...}, "completo": true|false}\n'
        "completo=true SOLO cuando tengas las 11 variables con categoría válida."
    )

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

@app.post("/chat")
async def chat(req: Request):
    """Conversación con Amparito (LLM Gemini). Recibe {historial:[{rol,texto}]} y devuelve
    {reply, perfil, completo, recomendacion?}. Si el LLM no está configurado, avisa sin romper."""
    if genai is None or not GEMINI_API_KEY:
        return {"reply": "El asistente conversacional aún no está configurado.", "completo": False, "perfil": {}}
    try:
        body = await req.json()
    except Exception:
        return JSONResponse(status_code=400, content={"error": "El body debe ser JSON."})
    historial = body.get("historial") or []
    contents = []
    for msg in historial:
        rol = "user" if msg.get("rol") == "usuario" else "model"
        contents.append({"role": rol, "parts": [str(msg.get("texto", ""))]})
    if not contents:
        contents = [{"role": "user", "parts": ["Hola"]}]
    try:
        model = genai.GenerativeModel(GEMINI_MODEL, system_instruction=_system_prompt())
        resp = model.generate_content(contents, generation_config={"response_mime_type": "application/json"})
        data = json.loads(resp.text)
    except Exception as e:
        return {"reply": "Uy, se me cruzaron los cables un segundo. ¿Me lo repites?", "completo": False, "perfil": {}, "error": str(e)[:150]}
    perfil = data.get("perfil") or {}
    if data.get("completo") and all(v["code"] in perfil for v in motor.variables):
        try:
            r = motor.calcular_scores(perfil)
            data["recomendacion"] = {"top": r.top.to_dict(), "top_3": [p.to_dict() for p in r.top_3]}
        except ValueError:
            data["completo"] = False
    return data

# MVP local de punta a punta — Amparito (Scala Labs)

Demo funcional completa corriendo en local, sin instalar nada (Python 3 estándar):
**front → endpoint REST → motor determinista → DB de trazabilidad → export → pantalla de aprendizaje.**

## Cómo correrlo (2 comandos)

Desde la raíz del repo:

```bash
# 1. Motor + trazabilidad (endpoint REST en el puerto 8090)
python3 producto/engines/endpoint_motor.py

# 2. Front demo + pantalla de aprendizaje (en otra terminal)
python3 -m http.server 8123 --directory producto
```

Luego abre en el navegador:

- **Demo (Amparito):** http://localhost:8123/demo/index.html → pestaña "Cotiza tu seguro"
- **Pantalla de aprendizaje:** http://localhost:8123/pantalla-aprendizaje/index.html

Para refrescar la pantalla con las sesiones reales acumuladas en la DB:

```bash
python3 -c "import sys; sys.path.insert(0,'producto/db'); import trazabilidad; \
trazabilidad.exportar_interactions_json('producto/pantalla-aprendizaje/interactions.json')"
```

## Qué demuestra

1. **Comprensión de lenguaje colombiano (regla 16 del MD):** escribe *"quiero asegurar
   mi casa"*, *"mi apto"*, *"la nave"* o *"mi peludito"* — el front homologa el sinónimo
   al producto oficial y arranca el flujo correcto, sin loops ni aclaraciones.
2. **La IA nunca pone cifras:** al llegar a la recomendación, el front arma el perfil
   V1–V11 (lo conversado + defaults documentados en el código) y llama
   `POST http://localhost:8090/recomendar`. El top 3 con porcentaje de afinidad y modo
   de cierre que se muestra en el chat viene tal cual del JSON del motor determinista.
3. **Trazabilidad real:** cada llamada al motor crea una sesión en
   `producto/db/interactions.db` (features V1–V11 + outputs top 3 con su porqué).
4. **Cierre honesto (discovery 25-jul):** la venta directa cierra con
   *"¡Listo! Tu solicitud va directo a la aseguradora — te llega la confirmación al
   correo"* — remisión del lead validado, no emisión ni recaudo en el chat.
5. **Flywheel visible:** la pantalla de aprendizaje consume el export de la DB y muestra
   la sesión real: perfil capturado, recomendación del motor y estado de consentimientos.
6. **Fallback limpio:** si el endpoint no está corriendo, el demo sigue funcionando
   standalone con sus guiones — nunca se ve roto.

## Flujo (diagrama en texto)

```
Usuario ("quiero asegurar mi casa")
   │
   ▼
demo/index.html ── sinónimos regla 16 ──► producto identificado (hogar)
   │  conversación guiada (front)                 │
   │  perfil V1–V11 (conversado + defaults)       │
   ▼                                              │
POST localhost:8090/recomendar  ◄─────────────────┘
   │        (endpoint_motor.py, stdlib-only)
   ▼
motor-colsubsidio.py ──► top 3 {pct, score, modo_cierre}  ─► burbuja en el chat
   │
   ▼
trazabilidad.py ──► interactions.db (sessions + features + outputs)
   │
   ▼  exportar_interactions_json()
interactions.json ──► pantalla-aprendizaje/index.html ("Esto aprendió el sistema")
```

## Notas

- Sin pip, sin Node, sin Docker: todo es Python 3 estándar + HTML/JS plano.
- Cero PII: las cédulas del demo son ficticias y jamás viajan al motor ni a la DB
  en claro (la DB solo guarda hash SHA-256 cuando aplica).
- Puerto del endpoint configurable con `PORT=9000 python3 producto/engines/endpoint_motor.py`
  (recuerda actualizar `MOTOR_URL` en `demo/index.html` si lo cambias).

---

> Construido con Claude (agente delegado supervisado por Fable 5) — 25 jul 2026, noche.

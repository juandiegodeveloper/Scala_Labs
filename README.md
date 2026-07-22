# Scala Labs — Hackathon Colsubsidio 30X

Repositorio **privado** del equipo Scala Labs para la Hackathon Colsubsidio 30X (22–26 jul 2026).
Trabajo colaborativo y documentación del reto. Parte de los activos son **preexistentes** (ver Bitácora de PI en Notion) y el resto se construye durante el evento.

## Retos
- **Reto 01** — Crédito Hiperpersonalizado
- **Reto 02** — Venta Automatizada de Seguros _(foco principal según el diagnóstico Montecarlo)_

## Estructura
- `montecarlo_decision.py` — modelo de decisión de reto (200.000 escenarios)
- `mvp/reto01-credito/` — motor de scoring, esquema SQL, flujo n8n, prompts Gemini
- `mvp/reto02-seguros/` — motor de cotización, esquema SQL, flujo n8n, prompts Gemini
- `mvp/demo/index.html` — demo navegable de ambos flujos (abre en el navegador)
- `01_…`, `02_…`, `03_…` — checklist, dossier y arranque de MVP (documentación)

## Cómo correr
```bash
python3 montecarlo_decision.py
python3 mvp/reto01-credito/scoring_engine.py
python3 mvp/reto02-seguros/quote_engine.py
# Demo: abrir mvp/demo/index.html en el navegador
```

## Reglas del repo
- **Nunca** subir llaves ni archivos `.env`. Las API keys (Gemini, etc.) van en variables de entorno o en n8n, jamás en el código.
- El código vive aquí; las decisiones y documentación viva, en Notion.
- Decisión que no queda escrita, no se tomó.

## Centro de mando
Notion (página raíz del equipo): _pega aquí el link_

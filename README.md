# Scala Labs — Hackathon Colsubsidio 30X

Repositorio **privado** del equipo Scala Labs para la Hackathon Colsubsidio 30X (22–26 jul 2026).
Trabajo colaborativo y documentación del reto. Parte de los activos son **preexistentes** (ver Bitácora de PI en Notion) y el resto se construye durante el evento.

## Retos
- **Reto 01** — Crédito Hiperpersonalizado
- **Reto 02** — Venta Automatizada de Seguros _(foco principal según el diagnóstico Montecarlo)_

## Estructura

Scala_Labs/
├── README.md              ← este archivo
├── producto/              ← lo que CORRE (demo + motores + marca)
│   ├── demo/              (index.html, se abre en el navegador)
│   ├── engines/           (scoring/quote en Python, schemas, n8n, prompts)
│   └── recursos-marca/    (brandbook: logos + paleta)
├── proceso-dt/            ← la HISTORIA para el pitch (design thinking)
│   ├── 1-ideacion/        (ideas, matriz de escenarios, montecarlo)
|   |────Montecarlo model
## Cómo correr
```
- `montecarlo_decision.py` — modelo de decisión de reto (200.000 escenarios)
- `mvp/reto01-credito/` — motor de scoring, esquema SQL, flujo n8n, prompts Gemini
- `mvp/reto02-seguros/` — motor de cotización, esquema SQL, flujo n8n, prompts Gemini
- `mvp/demo/index.html` — demo navegable de ambos flujos (abre en el navegador)
- `01_…`, `02_…`, `03_…` — checklist, dossier y arranque de MVP (documentación)
- `hustler/` — investigación de sector, catálogo de seguros y reporte navegable Días 1–2 (Juan Pablo)
- `recursos-marca/` — brandbook Colsubsidio: logos, paleta oficial y tokens listos para usar (`BRAND.md`)
## Cómo correr
```bash
python3 montecarlo_decision.py
python3 mvp/reto01-credito/scoring_engine.py
python3 mvp/reto02-seguros/quote_engine.py
# Demo: abrir mvp/demo/index.html en el navegador
```
│   ├── 2-definicion/      (reto elegido, dossier, análisis de la base)
│   ├── 3-diseno/          (journey, blueprint, diseño de motores)
│   └── 4-testing/         (pruebas del demo, feedback)
└── pi-preexistente/       ← IP previa al evento, registrada (autor + fecha)

## Reglas del repo
- **Nunca** subir llaves ni archivos `.env`. Las API keys (Gemini, etc.) van en variables de entorno o en n8n, jamás en el código.
- El código vive aquí; las decisiones y documentación viva, en Notion.
- Decisión que no queda escrita, no se tomó.

## Centro de mando
Notion (página raíz del equipo): https://app.notion.com/p/jddevs/Hackathon-Colsubsidio-2026-Scala-Labs-3a4aaa9c5e0b818cb1d0f13475744ca1?source=copy_link

# Motor de Scoring de Seguros — Colsubsidio

Motor de reglas determinista que ordena 12 pólizas para un perfil de 11
variables. Sin entrenamiento y sin probabilidades: los pesos son declarados y
auditables contra fuentes públicas (DANE, Fasecolda, INC, SURA).

## Archivos

| Archivo | Rol | Qué expone |
| --- | --- | --- |
| `models.py` | Objetos de valor del dominio (dataclasses `frozen`). Base común, sin lógica. | `ProductDef`, `VariableDef`, `TriggerDef`, `ChecklistDef`, `Baseline`, `AporteVariable`, `ResultadoProducto`, `ResultadoScoring` |
| `catalog.py` | Capa de datos: productos, variables, matriz de pesos, racionales, checklist y disparadores. Constantes puras, sin lógica. | `PRODUCTS`, `VARIABLES`, `WEIGHTS`, `RATIONALE`, `CHECKLIST`, `TRIGGERS`, `CASE_PRESETS` |
| `baseline.py` | Calcula el piso teórico (E[score]) por producto usando solo variables estructurales. Patrón *Strategy* para poder cambiar la distribución. | `BaselineProvider` (Protocol), `UniformBaseline`, `es_estructural` |
| `ranking.py` | Política de ordenamiento + reglas de post-proceso (gate por trigger, promoción por trigger, promoción explícita). Patrones *Strategy* + *Chain*. | `RankingStrategy`, `LiftRanking`, `RankingPostProcessor`, `TriggerGate`, `TriggerPromoter`, `ExplicitProductPromoter` |
| `engine.py` | Orquestador. Envuelve el catálogo, valida perfil, corre el pipeline y arma el resultado auditable. Es el único punto de entrada público. | `ScoringCatalog`, `MotorScoring` |
| `reporting.py` | Formateo a texto plano para consola / asesor (tablas y ficha de cierre). Desacoplado del motor porque la presentación cambia más rápido que el cálculo. | `tabla_baselines`, `tabla_ranking`, `ficha_texto` |
| `cli.py` | Demo por consola: imprime pisos, ranking de cada caso preset, ficha del primer caso e influencia de variables. | `main` (invocable con `python -m motor_scoring.cli`) |
| `test_motor_scoring.py` | Suite `pytest`: cubre validación, aritmética, baseline, ranking, triggers y promoción explícita. | Casos de test |
| `pyproject.toml` | Empaquetado (Python ≥ 3.11), extras `dev` (pytest, ruff) y config de lint (ruff con convención Google). | Config del paquete `motor-scoring-colsubsidio` |
| `PULL_REQUEST.md` | Justificación del diseño de `lift`, disparadores y separación estructural / condicional. Lectura obligada antes de cambiar pesos. | Documentación de decisiones |

## Flujo de ejecución

Todo pasa por `MotorScoring.calcular(perfil, producto_explicito=None)` en
`engine.py`. El pipeline es determinista y siempre en el mismo orden:

```
                                                       [ archivo responsable ]
perfil (dict V1..V11)
   │
   ▼
[1] validar_perfil           ──────────────────────────  engine.py
        │  faltantes / categorías inválidas → ValueError
   ▼
[2] _aportes                 ──────────────────────────  engine.py + catalog.py
        │  lee pesos y racionales por respuesta
   ▼
[3] _triggers_activos        ──────────────────────────  engine.py + catalog.py
        │  match respuesta == categoría del TriggerDef
   ▼
[4] _puntuar                 ──────────────────────────  engine.py
        │  score = Σ pesos ; pct = score / MAXS * 100
        │  lift = pct − baseline_pct  (baseline precalculado en __init__
        │                              usando baseline.py)
   ▼
[5] strategy.ordenar         ──────────────────────────  ranking.py (LiftRanking)
        │  sort por (lift, pct, score) desc
   ▼
[6] post_processors          ──────────────────────────  ranking.py
        │  TriggerGate       → baja lo que exige trigger no activado
        │  TriggerPromoter   → sube al top_n los productos con trigger
        │  ExplicitProductPromoter → fuerza al 1º el pedido por nombre
   ▼
[7] asignar rank             ──────────────────────────  engine.py
        │
   ▼
ResultadoScoring (ranking + aportes)
```

Los pasos 1–4 son **aritmética pura**: mismo perfil ⇒ mismo score, siempre. Los
pasos 5–6 son **política de negocio inyectable**: se cambian por constructor
sin tocar el cálculo (esto es lo que hace `tests/` verificable en aislamiento).

El **piso** (`baseline_pct`) se calcula una sola vez al construir el motor,
no por cada perfil.

Salida y presentación:

```
ResultadoScoring ──► reporting.py ──► tabla_ranking / ficha_texto
                                            │
                                            ▼
                                       stdout (cli.py)
```

## Instalación

```bash
python -m pip install -e ".[dev]"
```

Requiere Python 3.11+. El motor en sí no tiene dependencias.

## Uso

```python
from motor_scoring import MotorScoring

motor = MotorScoring()
resultado = motor.calcular({
    "V1": "36-45 años",
    "V2": "Femenino",
    "V3": "Formal independiente / profesional",
    "V4": "Alto (> $4.6M)",
    "V5": "Pareja sin hijos",
    "V6": "Propia financiada (hipoteca)",
    "V7": "No",
    "V8": "Carro",
    "V9": "Sí",
    "V10": "No",
    "V11": "No",
})

print(resultado.top.nombre, resultado.top.lift)
```

## Demostración

```bash
python -m motor_scoring.cli
```

## Tests

```bash
python -m pytest tests -v
ruff check .
```

## Documentación

- Contrato de entrada/salida y flujo de ejecución: docstring de
  `motor_scoring/engine.py`.
- Justificación del diseño de lift y disparadores: `PULL_REQUEST.md`.

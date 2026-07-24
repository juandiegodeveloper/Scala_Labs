# Motor de Scoring de Seguros — Colsubsidio

Motor de reglas determinista que ordena 12 pólizas para un perfil de 11
variables. Sin entrenamiento y sin probabilidades: los pesos son declarados y
auditables contra fuentes públicas (DANE, Fasecolda, INC, SURA).

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

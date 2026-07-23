# Constitución — Scala Labs · Reto 02 (Venta Automatizada de Seguros)

Reglas de desarrollo del equipo. Fuente: dossier, daily 23-jul y regla de oro del
arranque de MVP. Toda spec, plan y tarea debe respetarlas.

## Core Principles

### I. El motor determinista manda las cifras (NON-NEGOTIABLE)
La IA (Gemini/Claude) conversa, redacta y explica; **nunca calcula ni inventa
cifras**. Precio, prima, score, idoneidad y elegibilidad salen SIEMPRE de
`quote_engine.py` (Python determinista). Si el jurado pregunta "¿por qué esta
cifra?", la respuesta está trazada en código y datos, no en un prompt.

### II. Cumplimiento embebido, no decorativo
Ninguna póliza se emite sin: (1) evaluación de idoneidad registrada, (2)
consentimiento explícito del afiliado, (3) registro trazable en la base de datos
(número de póliza + hash). El consentimiento se presenta inline en el flujo, en
lenguaje simple — no como cláusula legal al final. La venta adecuada es el
diferenciador, no un estorbo.

### III. Cero PII
Se trabaja solo por SERIE. Nunca nombres ni datos personales reales en código,
demos, logs o repositorio. La base oficial de afiliados NO entra al repo (vive en
el Drive del reto). Los datos de personas en demos son sintéticos.

### IV. La base v2 tiene valores enmascarados — no asumir semántica
Los valores categóricos de la base oficial (SIGMA, LAMBDA, RHO…) están
enmascarados. El mapeo inferido vive en
`hustler/investigacion/2026-07-23_analisis-base-afiliados-v3.md` y se usa
declarándolo. Columnas sin diccionario (SEGMENTO_POBLACIONAL, PIRAMIDE_NUEVA,
EMPRESA_FOCO) no se usan hasta tener semántica oficial.

### V. Demo primero: P1 completa vale más que P1+P2 a medias
Cada user story se prioriza (P1, P2, P3) y debe ser demostrable de punta a punta
por sí sola. Si el domingo solo existe la P1, hay demo. No se empieza una
prioridad inferior si la superior no corre end-to-end.

### VI. Lo que no queda escrito, no se decidió
Regla del Notion del equipo, extendida al código: las decisiones de producto viven
en specs (`specs/`), las de arquitectura en plans, y el trabajo en tasks. El código
implementa lo especificado; si el código necesita desviarse, primero se actualiza
la spec.

## Governance

- La constitución prevalece sobre cualquier práctica individual.
- Cambios a este documento se proponen por PR y los aprueba el Product Owner (JD).
- Verificación: /speckit-analyze antes de implementar; /speckit-converge antes de
  congelar el domingo.

**Version**: 1.0.0 | **Ratified**: propuesta 2026-07-23, pendiente de aprobación
del equipo | **Last Amended**: 2026-07-23

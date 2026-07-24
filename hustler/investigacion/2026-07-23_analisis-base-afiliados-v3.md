# Análisis de la base de afiliados v3 — base ACTUALIZADA por la organización (23-jul)

Fuente: `Usos_Productos_Afiliados_SIN_ID.xlsx` (versión actualizada anunciada por la
organización el 23-jul). **500.000 filas, 15 columnas.** Procesado por código (pandas).
Reemplaza como fuente activa al CSV de 1.566.028 filas analizado el 22-jul
([[2026-07-22_analisis-base-afiliados]] queda como registro histórico de la v1 de la base).

> Construido con Fable 5 (alto). Recomputado desde cero sobre el archivo nuevo;
> mapeo de valores enmascarados verificado por 4 dimensiones independientes.

## Qué cambió respecto a la base anterior

| Cambio | Antes (CSV 22-jul) | Ahora (XLSX 23-jul) | Implicación |
|---|---|---|---|
| Tamaño | 1.566.028 filas | **500.000 filas** (muestra) | Los porcentajes se sostienen; los conteos absolutos ya no son "toda la base" |
| PII | Traía `NOMBRE_COMPLETO` con nombres reales | **Columna eliminada** | El hallazgo que reportamos fue atendido — la base ahora sí es anónima |
| Valores categóricos | Legibles (A/B/C, "sin grupo familiar"…) | **Enmascarados con letras griegas** (SIGMA, LAMBDA, RHO…) | Hay que trabajar con mapeo inferido (abajo) y pedir el diccionario a la organización |
| Columnas nuevas | — | **RANGO_SALARIAL** (16 bandas SMLV), SEGMENTO_POBLACIONAL, PIRAMIDE_NUEVA, EMPRESA_FOCO | RANGO_SALARIAL es el activo nuevo más valioso (ver abajo) |
| Columnas eliminadas | ESTADOAFILIADO (constante), NOMBRE_COMPLETO | ya no están | Sin pérdida real |
| PISCILAGO | 4,9% SI (señal usable) | **100% NO** | Señal perdida — sacarla del motor |
| DROGUERIA | 5,6% SI | **17,6% SI** | La marca se reconstruyó y creció, pero el acantilado de edad PERSISTE |

## Mapeo inferido de valores enmascarados (verificado, no oficial)

Cada equivalencia se verificó contra la base v1 por 4 dimensiones simultáneas
(% del total, % categoría A, % mujeres, % >55 / edad dominante). Coincidencia
consistente en todas:

**CATEGORIA:** SIGMA = A (72,8%) · PI = B (16,4%) · ZETA = C (9,8%) · MU = sin dato (1,0%)

**SEGMENTO_GRUPO_FAMILIAR:**

| Código | Equivale a (inferido) | n | % base | % cat A (SIGMA) | % F | % >55 | % 20–35 | Edad dominante |
|---|---|---|---|---|---|---|---|---|
| LAMBDA | Sin grupo familiar registrado | 286.457 | 57,3% | 72,3% | 42,7% | 9,8% | 59,3% | 20–35 |
| RHO | Familia monoparental | 121.478 | 24,3% | 80,3% | 58,5% | 3,0% | 44,8% | 20–35 |
| EPSILON | Familia nuclear | 46.999 | 9,4% | 68,8% | 37,4% | 8,7% | 23,5% | 36–45 |
| IOTA | Pareja conyugal | 25.263 | 5,1% | 65,7% | 39,3% | **51,2%** | 11,4% | **>55** |
| CHI | Monoparental ampliada | 11.843 | 2,4% | 64,2% | 58,8% | 7,6% | 41,1% | 20–35 |
| THETA | Sin dato | 7.933 | 1,6% | 34,7% | 44,5% | 4,0% | 61,7% | 20–35 |
| PI | (residuo nuevo, 27 filas) | 27 | 0,0% | — | — | — | — | — |

⚠️ Este mapeo es **inferencia nuestra**, no diccionario oficial. Es sólido (4
dimensiones coinciden con la v1), pero hay que **pedir el diccionario de valores a la
organización** antes del pitch. Mientras tanto, todos los entregables lo declaran.

## Distribuciones clave (v3)

- **Categoría:** A 72,8% · B 16,4% · C 9,8% · sin dato 1,0% — *(v1: 75,8/14,5/8,8)*.
  El titular "3 de cada 4 afiliados son categoría A" **se sostiene**.
- **Edad:** <19 → 1,4% · 20–35 → 49,6% · 36–45 → 25,7% · 46–55 → 13,3% · >55 → 10,0%.
- **Género:** M 53,7% · F 46,3%.
- **Ciudad:** 57,7% vacía; de las filas con ciudad, Bogotá D.C. = 82,1% (34,7% del
  total). Municipios reales (no enmascarados): Soacha, Fusagasugá, Mosquera…

## EL ACTIVO NUEVO: RANGO_SALARIAL (asequibilidad calculable)

Por primera vez tenemos ingreso declarado por bandas SMLV:

- **Entre 1 y 1,5 SMLV: 60,5%** · Menor al SMLV: 6,8% → **~67% gana ≤1,5 SMLV**
- Entre 1,5 y 2: 8,4% · 2–2,5: 5,5% · 2,5–3: 3,9% · 3–4: 4,8% · 4–6: 4,6% · >6: ~4,9%
- Sin dato: 1,0% (+ bandas residuales con pocos registros: "Menor a 2", "Entre 2 y 4",
  "Entre 4 y 8", "Entre 8 y 19" — parecen restos de otra codificación; reportar)

**Por qué importa:** el motor puede calcular la prima como **% del ingreso real** del
afiliado — la hiperpersonalización de asequibilidad deja de ser proxy por categoría y
se vuelve un cálculo directo. Es el insumo que le faltaba a la pregunta 3 del chat
("¿cuánto puedes pagar al mes?"): el sistema puede validar que la prima recomendada
no exceda un umbral responsable del ingreso. Conecta directo con el argumento de
inclusión (microseguro para el 67% que gana ≤1,5 SMLV).

## Columnas nuevas sin diccionario (preguntar a la organización)

- **SEGMENTO_POBLACIONAL** (5 valores): TAU 46,2% (97% cat A) · PI 26,9% · ETA 25,5%
  · OMEGA 1,0% (96% "sin dato" de categoría — parece el "sin dato" poblacional) ·
  XI 0,3% (99% cat C — ¿segmento premium/especial?). Semántica desconocida.
- **PIRAMIDE_NUEVA** (10 valores): distribución amplia (ETA 31,2%, XI 21,7%,
  UPSILON 20,4%…). Semántica desconocida.
- **EMPRESA_FOCO**: EMP_000001 = 81,7% · EMP_000002 = 18,3%. ¿Empresa priorizada?
  Semántica desconocida.

Estas tres columnas pueden traer señal útil para el motor — sin diccionario son
inutilizables. **Primera pregunta para los mentores/organización.**

## Señales de consumo (v3)

- **DROGUERIA (única marca con señal): la anomalía PERSISTE y se amplificó.**
  % SI por edad: 20–35 → 24,0% · 36–45 → 21,3% · **46–55 → 0,35%** · >55 → 1,25%.
  El acantilado a los 46 años sigue siendo implausible como comportamiento real.
  Regla vigente: usarla solo en menores de 46.
- **Lift familiar dentro de 20–35 (confirmado y más fuerte):** sin grupo 21,8% →
  monoparental 28,4% → nuclear 32,4% → pareja 39,4%. La señal familiar es real.
- **PISCILAGO: muerta** (100% NO — antes 4,9% SI). Sacarla del motor y del mapa
  segmento→producto si se usaba.
- HOTELES (0,03%), AGENCIAS (0,02%), VIVIENDA (0,01%): siguen vacías, inservibles.

## Qué se sostiene y qué cambia en los entregables

**Se sostiene (los titulares del pitch siguen válidos):**
- 3 de cada 4 afiliados = categoría A (72,8%)
- Los segmentos grandes: sin grupo (57,3%) + monoparental (24,3%, 58,5% mujeres,
  80,3% cat A) — la persona del pitch no cambia
- El ejemplo del brief ("casado con hijos") sigue siendo ~9,4%
- Mitad de las parejas conyugales >55 → la edad modula el producto
- Bogotá ~82% de las filas con ciudad

**Cambia (corregir en todos los entregables):**
- "1,56M analizados" → **"muestra oficial de 500.000"** (los 1,6M de afiliados de
  Colsubsidio siguen siendo ciertos como contexto de mercado — Informe 2024 —, pero
  la base entregada ya no es censo)
- El hallazgo de PII pasa de "pendiente" a **"atendido por la organización en la v2
  de la base"** (registro histórico nuestro se mantiene)
- Nueva limitación: valores enmascarados → mapeo inferido, pedir diccionario
- Piscilago fuera del motor; Droguería con % nuevos
- Nueva oportunidad: RANGO_SALARIAL → prima como % del ingreso

## Preguntas actualizadas para la organización

1. ¿Diccionario de valores enmascarados? (CATEGORIA, SEGMENTO_GRUPO_FAMILIAR,
   SEGMENTO_POBLACIONAL, PIRAMIDE_NUEVA, EMPRESA_FOCO)
2. La anomalía de DROGUERIA a los 46 años persiste en la v2 — ¿artefacto confirmado?
3. ¿La muestra de 500K es aleatoria de la base de 1,56M? (afecta si podemos
   extrapolar conteos absolutos)
4. ¿Las bandas residuales de RANGO_SALARIAL ("Menor a 2", "Entre 2 y 4"…) son
   errores de codificación?

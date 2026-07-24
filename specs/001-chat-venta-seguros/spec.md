# Feature Specification: Chat de venta automatizada de seguros

**Feature Branch**: `001-chat-venta-seguros`

**Created**: 2026-07-23

**Status**: Borrador del hustler (JP) — para `/speckit-clarify` con el equipo el viernes temprano

**Input**: Reto 02 Colsubsidio: chat de máx. 5 preguntas → detecta necesidad → recomienda producto → calcula prima → muestra idoneidad → con consentimiento deja al afiliado asegurado con número de póliza. Sin humano, 24/7.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Compra de un seguro simple por chat (Priority: P1)

Un afiliado de Colsubsidio (perfil demo sintético, ej. mujer 29 años, monoparental,
categoría A, ingreso 1–1,5 SMLV) entra al chat, responde máximo 5 preguntas y sale
asegurada con número de póliza, sin intervención humana.

**Why this priority**: Es la promesa literal del brief y lo que el jurado evalúa en
el demo de 3 minutos. Sin esto no hay nada.

**Independent Test**: Correr el flujo completo con 2 perfiles demo distintos y
verificar que producen recomendación, prima y póliza distintas, con registro en DB.

**Acceptance Scenarios**:

1. **Given** un afiliado nuevo en el chat, **When** responde las 5 preguntas (qué
   proteger → quién depende de ti → cuánto puede pagar/mes → cobertura actual →
   contacto), **Then** recibe UNA recomendación de producto del catálogo con
   justificación en lenguaje simple ("te recomiendo esto porque…") y prima
   calculada por `quote_engine.py` — nunca por el LLM.
2. **Given** la recomendación en pantalla, **When** el afiliado pregunta "¿por qué
   este seguro?", **Then** el sistema explica la idoneidad con las variables
   usadas (necesidad declarada, dependientes, capacidad de pago) sin jerga.
3. **Given** que el afiliado acepta, **When** confirma el consentimiento explícito
   (checkbox/frase con producto + prima + link al resumen), **Then** se emite
   póliza con número visible (formato COL-2026-XXXXX), se registra en DB con hash
   de trazabilidad y se muestra pantalla de cierre celebratoria.
4. **Given** un afiliado cuyo presupuesto declarado es menor que la prima del
   producto ideal, **When** el motor evalúa idoneidad, **Then** recomienda la
   alternativa asequible (microseguro/AP) — nunca fuerza la venta del producto
   caro. La prima recomendada no supera un umbral responsable del ingreso
   declarado (usar RANGO_SALARIAL de la base v2 como referencia del cálculo).
5. **Given** cualquier paso del flujo, **When** el afiliado responde, **Then** el
   dato queda escrito en la DB de trazabilidad (señal → score → oferta → decisión).

---

### User Story 2 - Paquete sugerido post-compra (Priority: P2)

Tras emitirse la póliza, la pantalla final ofrece "tu paquete sugerido": 2–3
pólizas complementarias al perfil con un precio mensual único simulado.

**Why this priority**: Es la semilla del marketplace (visión del equipo) y el
argumento de cross-sell/CAC negativo del pitch, sin reescribir el motor. Media
jornada de trabajo si la P1 ya corre.

**Independent Test**: Con la P1 cerrada para un perfil, verificar que el paquete
sugerido cambia según el perfil (monoparental ≠ soltero joven) y muestra un único
total mensual.

**Acceptance Scenarios**:

1. **Given** una póliza emitida para un perfil monoparental, **When** aparece la
   pantalla final, **Then** el paquete sugiere productos coherentes con el mapa
   segmento→producto (ej. vida con beneficiarios + exequial) con precio mensual
   único marcado como simulado.
2. **Given** el paquete en pantalla, **When** el afiliado lo ignora, **Then** el
   cierre de la P1 no se degrada (el paquete es opcional, no bloquea).

---

### User Story 3 - El abandono es señal + derivación a humano (Priority: P3)

Si el afiliado abandona el flujo, el sistema registra el punto de fuga y la
objeción; si la necesidad detectada es de póliza compleja (vida con asesoría,
educación), ofrece explícitamente "hablar con una persona".

**Why this priority**: Sustenta el flywheel (cada conversación deja data, incluso
la que no cierra) y el matiz de Carolina (no todas las pólizas son autoservicio).
Es narrable en el pitch aunque se implemente mínimo.

**Independent Test**: Abandonar el flujo en la pantalla de precio y verificar el
registro en DB (paso + motivo si lo dio); pedir un seguro de vida con asesoría y
verificar la oferta de derivación.

**Acceptance Scenarios**:

1. **Given** un afiliado que llegó hasta el precio, **When** cierra el chat sin
   comprar, **Then** la DB registra el punto de fuga y la última interacción.
2. **Given** una necesidad clasificada como compleja, **When** el motor lo
   detecta, **Then** el chat ofrece continuar solo o "hablar con un asesor"
   (derivación simulada) sin abandonar al usuario.

---

### Edge Cases

- Respuestas ambiguas o fuera de opción en las 5 preguntas → el chat re-pregunta
  con opciones cerradas; máximo 2 reintentos por pregunta.
- El afiliado pide un producto que el catálogo no cubre → el chat lo dice
  explícitamente y ofrece lo más cercano (constitución: no inventar).
- Petición de datos personales sensibles → no se piden; solo lo definido en las 5
  preguntas (constitución III).
- El LLM no responde o falla → mensaje de reintento; el motor y la DB nunca
  dependen del LLM para las cifras.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El flujo completo (inicio → póliza emitida) debe tener máximo 5
  preguntas al afiliado y debe poder completarse en menos de 3 minutos.
- **FR-002**: Toda cifra mostrada (prima, cobertura, score) proviene de
  `quote_engine.py`; el LLM solo redacta alrededor de valores ya calculados.
- **FR-003**: El catálogo de productos se carga desde
  `hustler/catalogo-seguros/productos-seguros.json` (precios simulados, salvo
  SOAT que tiene tarifa pública).
- **FR-004**: La recomendación usa como mínimo: necesidad declarada, dependientes,
  capacidad de pago declarada, y el mapa segmento→producto; la asequibilidad se
  valida contra el ingreso (bandas SMLV).
- **FR-005**: El consentimiento y la idoneidad quedan registrados junto a la
  póliza (schema existente `schema_seguros.sql` + hash).
- **FR-006**: Cada interacción escribe en la DB de trazabilidad (incluido el
  abandono). Un solo esquema, una sola DB.
- **FR-007**: La UI es un chat web responsive (simula móvil); sin integraciones
  reales de pago ni aseguradoras (exclusión del brief).
- **FR-008**: Textos del chat en español simple, sin jerga técnica de seguros
  (patrones del playbook: una pregunta a la vez, precio como recompensa, cierre
  celebratorio).

### Key Entities

- **Afiliado (demo)**: SERIE sintética, segmento, categoría, banda salarial,
  respuestas del chat. Sin PII.
- **Producto**: del catálogo JSON (26 productos, 7 familias, aseguradora, URL).
- **Cotización**: producto + prima + variables usadas + veredicto de idoneidad.
- **Póliza**: número, afiliado (SERIE), producto, prima, consentimiento, hash,
  timestamp.
- **Evento de trazabilidad**: paso del flujo, dato capturado, timestamp (incluye
  abandonos).

## Success Criteria *(mandatory)*

- **SC-001**: 2 perfiles demo distintos completan el flujo end-to-end en vivo, con
  recomendaciones y primas distintas y explicables.
- **SC-002**: Demo completo cabe en el guion de 3 minutos con al menos 60 segundos
  de flujo en vivo sin cortes.
- **SC-003**: Ante la pregunta del jurado "¿por qué esta cifra/este producto?", la
  respuesta es demostrable en pantalla (evidencia en DB) en menos de 30 segundos.
- **SC-004**: Cero datos personales reales visibles en todo el demo.

## Assumptions

- El "quedó hecho" del MVP definido por el equipo puede ajustar prioridades P2/P3
  en el `/speckit-clarify` del viernes — esta spec es el borrador de partida.
- La billetera (Caro) y WhatsApp real (JD) son interfaces de la visión; el MVP usa
  chat web que simula la conversación (constitución V: demo primero).
- El "paquete sugerido" (P2) usa precios simulados y no requiere lógica de
  suscripción real.

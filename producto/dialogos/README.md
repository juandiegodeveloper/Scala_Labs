# Diálogos del asistente — fuente de verdad conversacional

Artefactos de **Carolina Pinzón** (experta en seguros), versionados aquí para que
el orquestador (Make) y la capa LLM los consuman sin que Caro toque flujos ni código.

| Archivo | Qué es |
|---|---|
| `especificacion-asistente-colsubsidio.md` | Prompt general (tono, reglas de conversación, flujo de 4 pasos con rama afiliado/no afiliado) + especificación por póliza (datos que pide cada producto y cómo cierra) |
| `asistente-venta-colsubsidio.html` | Prototipo interactivo del asistente (referencia de la experiencia esperada) |
| `flujo-proceso-venta.mermaid` | Diagrama de flujo de la conversación (9 productos, rama afiliado, diálogos de respaldo, venta directa vs. intermediario). ⚠️ Pendiente v2: agregar el consentimiento como paso propio antes del cierre (condición del DoR) |

## Flujo de trabajo acordado (25-jul)

1. Caro edita/actualiza su documento y lo envía por WhatsApp.
2. JP lo versiona aquí vía rama + PR (historial = trazabilidad de cada versión).
3. Make/LLM consumen SIEMPRE la versión de `main`.

## Cierre real del proceso (discovery 25-jul)

Colsubsidio es canal de comercialización: quien cotiza, valida y recauda es la
aseguradora del convenio. En producción, Amparito entrega a la aseguradora un lead
validado, calificado y con consentimiento **en segundos** — versus el correo manual de
una vez al día del proceso actual. El pago en chat es visión si la aseguradora habilita
su pasarela. Para el mensaje final de venta directa del demo, el copy puede cerrar con:
*"tu solicitud quedó lista y va directo a la aseguradora — te llega la confirmación al correo"*.

## Regla de oro (innegociable)

**Las cifras (prima, score, % de afinidad) y su porqué los pone el motor
determinista vía endpoint — el LLM y estas plantillas solo conversan.**
Ningún texto de este directorio debe contener cifras de negocio hardcodeadas.

---
Artefacto original de Carolina Pinzón · versionado por JP (sesión Claude Fable 5, 2026-07-25).

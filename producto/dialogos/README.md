# Diálogos del asistente — fuente de verdad conversacional

Artefactos de **Carolina Pinzón** (experta en seguros), versionados aquí para que
el orquestador (Make) y la capa LLM los consuman sin que Caro toque flujos ni código.

| Archivo | Qué es |
|---|---|
| `especificacion-asistente-colsubsidio.md` | Prompt general (tono, reglas de conversación, flujo de 4 pasos con rama afiliado/no afiliado) + especificación por póliza (datos que pide cada producto y cómo cierra) |
| `asistente-venta-colsubsidio.html` | Prototipo interactivo del asistente (referencia de la experiencia esperada) |

## Flujo de trabajo acordado (25-jul)

1. Caro edita/actualiza su documento y lo envía por WhatsApp.
2. JP lo versiona aquí vía rama + PR (historial = trazabilidad de cada versión).
3. Make/LLM consumen SIEMPRE la versión de `main`.

## Regla de oro (innegociable)

**Las cifras (prima, score, % de afinidad) y su porqué los pone el motor
determinista vía endpoint — el LLM y estas plantillas solo conversan.**
Ningún texto de este directorio debe contener cifras de negocio hardcodeadas.

---
Artefacto original de Carolina Pinzón · versionado por JP (sesión Claude Fable 5, 2026-07-25).

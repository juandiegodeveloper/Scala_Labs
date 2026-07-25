# Diálogos del asistente — fuente de verdad conversacional

Todo lo que el asistente dice vive aquí, versionado, para que el orquestador (Make)
y la capa LLM lo consuman desde `main` sin que Caro toque flujos ni código.

| Archivo | Qué es |
|---|---|
| `especificacion-asistente-colsubsidio.md` | Prompt general (tono, reglas de conversación, flujo de 4 pasos con rama afiliado/no afiliado) + especificación por póliza (datos que pide cada producto y cómo cierra) — **Carolina Pinzón** |
| `asistente-venta-colsubsidio.html` | Prototipo interactivo del asistente (referencia de la experiencia esperada) |
| `flujo-proceso-venta.mermaid` | Diagrama de flujo de la conversación (9 productos, rama afiliado, diálogos de respaldo, venta directa vs. intermediario). ⚠️ Pendiente v2: agregar el consentimiento como paso propio antes del cierre (condición del DoR) |
| `perfilamiento-y-comunicacion-colsubsidio.xlsx` / `.json` | 35 perfiles × 9 pólizas con "por qué" + 3 ángulos de mensaje (riesgo/tranquilidad/cobertura) — fuente xlsx de Caro + JSON para el motor |
| `plantillas-dialogos-v1.json` | **Plantillas de respaldo que Make consume** (HTTP GET al raw de GitHub o copia en el escenario): base de tono por paso + fallback literal si el LLM falla + variantes afiliado/no_afiliado y auto/asesor |

## Cómo se usan las plantillas (Make/LLM)

1. **Base de tono:** el LLM recibe la plantilla del paso actual como referencia de
   tono y estructura, y puede parafrasear **sin tocar las variables del motor**.
2. **Fallback puro:** si el LLM falla o se demora (`respaldo.error_motor`, timeout),
   Make envía la plantilla literal con las variables ya resueltas. El chat nunca
   se queda mudo.
3. **Variantes:** cada paso tiene variante `afiliado` / `no_afiliado` cuando aplica
   (la bifurcación se decide en la pregunta 1 del flujo) y `auto` / `asesor` según
   el modo de cierre que entrega el motor.

## Flujo de trabajo acordado (25-jul)

1. Caro edita/actualiza sus documentos y los envía por WhatsApp (en las plantillas
   JSON: solo los textos dentro de `"plantillas"`, sin cambiar claves ni `{{...}}`).
2. JP los versiona aquí vía rama + PR (historial = trazabilidad de cada versión).
3. Make/LLM consumen SIEMPRE la versión de `main`.

## Regla de oro (innegociable)

**Las cifras (prima, score, % de afinidad) y su porqué los pone el motor
determinista vía endpoint — el LLM y estas plantillas solo conversan.**
Las plantillas insertan las variables `{{...}}` tal cual las entrega el motor;
nadie inventa, redondea ni reescribe números. Ningún texto de este directorio
lleva cifras de negocio hardcodeadas.

---
Artefactos de Carolina Pinzón · versionados por JP (sesión Claude Fable 5, 2026-07-25).

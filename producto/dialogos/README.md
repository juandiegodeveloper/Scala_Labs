# Diálogos de respaldo — plantillas versionadas

**Qué es esto:** las plantillas de conversación del asistente de venta, en un JSON
que **Make consume directamente** (HTTP GET al raw de GitHub o copia en el escenario).
Viven en el repo para que tengan trazabilidad y para que **Caro pueda editar los
textos sin tocar los flujos de Make**.

## Regla de oro (innegociable)

> **Las cifras y el porqué los pone SIEMPRE el motor determinista.**
> Las plantillas solo insertan las variables `{{...}}` tal cual las entrega el
> motor. Ni el LLM ni las plantillas inventan, redondean o reescriben números.

## Cómo se usa

1. **Base de tono:** el LLM recibe la plantilla del paso actual como referencia de
   tono y estructura, y puede parafrasear **sin tocar las variables del motor**.
2. **Fallback puro:** si el LLM falla o se demora (`respaldo.error_motor`, timeout),
   Make envía la plantilla literal con las variables ya resueltas. El chat nunca
   se queda mudo.
3. **Variantes:** cada paso tiene variante `afiliado` / `no_afiliado` cuando aplica
   (la bifurcación se decide en la pregunta 1 del flujo) y `auto` / `asesor` según
   el modo de cierre que entrega el motor.

## Cómo editar (Caro)

- Edita solo los textos dentro de `"plantillas"`. No cambies las claves ni las
  variables `{{...}}`.
- Los arrays son variantes: Make rota o elige una — agrega las que quieras.
- Toda edición va por rama + PR (JD mergea), igual que el resto del repo.

## Pendiente v1.1

- Incorporar el lenguaje del doc **"Asistente de venta (lenguaje)"** de Caro
  (Notion, In Review) cuando esté descargado al repo.
- Validar `confianza.me_pagaran` con Carolina (dato de <24 h por confirmar).

---
*Construido con Claude Fable 5 (sesión central del sábado 25-jul), a partir del
backlog Jarvis (journey + EPICs 3/5/6) y las decisiones pactadas con JD el 25-jul.*

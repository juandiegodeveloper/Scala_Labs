# PITCH — video pregrabado 2:00 (guion v2 · hook congelado 24-jul)

**Formato decidido (JP)**: tipo Loom — cámara de JP en burbuja sobre la pantalla,
un solo take si sale bueno. Hook híbrido (persona + dato). Cierre piloto + flywheel.

**Regla de oro del guion**: cada bloque tiene SU tiempo. Ensayar con cronómetro
hasta que suene natural (consejo literal de la jurado). ~2,6 palabras/segundo.

---

## Guion por bloques

### ⏱ 0:00–0:20 · HOOK + PROBLEMA (~64 palabras — ensayar brisk, tolerancia +2s)

> Nadie se despierta queriendo comprar un seguro. Camila tampoco: 29 años,
> 2 hijos. La idea le suena cara, enredada, llena de papeleo y asesores. Y como
> el 62% de los colombianos, nunca ha cotizado uno. Por eso, en 2026, 9 de cada
> 10 hogares siguen desprotegidos. Esto no es falta de necesidad: **es que nadie
> les ha mostrado lo simple que puede ser.**

*[TEXTO CONGELADO por JP (24-jul tarde) — redacción final suya. Ángulo: el
paradigma (nadie piensa en seguros; los cree caros/complejos), no "falla de
canal". Camila = persona 100% sintética (nombre inventado, rostro generado).
Cifras y fuentes: **62% nunca cotiza** (Aseguradora Solidaria, campo dic-2024→
may-2025, vía El Tiempo/El Colombiano) · **90,7% hogares sin seguro de hogar**
(Fasecolda mar-2026 × viviendas DANE, vía Semana). El 0,24% queda RETIRADO
(dato 2017, Superfinanciera vía El Tiempo — desactualizado: en 2023 el 27,5% ya
se comercializó no presencial, URF+PNUD). Detalle completo:
`investigacion/2026-07-24_verbalizacion-problema-pitch.md`.]*

### ⏱ 0:20–0:40 · QUÉ CONSTRUIMOS (~56 palabras · CONGELADO 24-jul tarde)

> Por eso construimos un asesor que funciona como una conversación y decide como
> un actuario. Le hablas con tus palabras; él cruza tu edad, tu familia y tu
> ingreso, y te entrega la mejor recomendación posible — explicándote por qué
> ese seguro y no otro. Sin letra pequeña. Y en 3 minutos, tienes tu primera
> póliza — con todas las de la ley.

*[Ajuste JP 24-jul noche: cierre "tu primera póliza — con todas las de la ley"
(antes "la póliza está a tu nombre"). En pantalla, al decir "las de la ley",
aparecen 3 sellos REALES del repo: ✓ Consentimiento explícito (gate en
quote_engine.emitir) · ✓ Venta adecuada (nota de idoneidad del motor) ·
✓ Datos protegidos · Ley 1581. NO mostrar firma Ley 527 / PCI / retracto /
verificación de identidad (no existen; el brief los excluye). Inventario
completo para Q&A: `investigacion/2026-07-24_inventario-cumplimiento-legal.md`.]*

*[TEXTO CONGELADO por JP. Decisiones: (1) "decide como un actuario" carga el
rigor técnico — "motor determinista" se reserva para el Q&A (si preguntan "¿cómo
decide?": motor determinista, reglas trazables, la IA nunca pone cifras);
(2) "cruza tu edad, tu familia y tu ingreso" = variables reales del motor que
corre hoy (quote_engine.py); (3) "WhatsApp" sale de la voz (no hay conector en
el repo) — la promesa de canal se muda a la E4 como tesis de infraestructura
("cambiar de chat a WhatsApp es cambiar un conector, no el motor", SC-006);
(4) coletilla pendiente del veredicto de Jorge (meet 24-jul 5:15pm): si
firma/pasarela REALES entran → insertar "con firma digital y pago en el mismo
chat" antes de "Tres minutos"; si SIMULADO → la frase queda como está;
(5) si el sábado se integran los 26 seguros del catálogo al motor → puede
insertarse "contra 26 seguros" tras "tu ingreso". En pantalla: mockup del chat
(escena E2).]*

### ⏱ 0:40–1:30 · DEMO EN DOS ACTOS (CONGELADO 25-jul madrugada)

**Acto 1 — La venta (0:40–1:05):**

> Míralo en vivo. Camila no sabe qué necesita — el asesor se lo descubre en
> 5 preguntas. Prima ajustada a su ingreso, el porqué claro, consentimiento…
> y su primera póliza.

**Acto 2 — El expediente (1:05–1:30):**

> Pero en esos mismos 3 minutos pasó algo más: el asesor construyó el expediente
> de Camila. Sus datos de siempre — familia, trabajo, contacto — y los que nadie
> captura: qué la hizo decidir, con qué palabras habla, qué la preocupa y qué
> sueña. Y eso es oro.

*[Pantalla: mockup animado calidad-final (`escenas/E3-demo.html`) → se reemplaza
por screen recording real cuando el demo esté grabable. Cronómetro visible
cerrando en ~2:47. Acto 2 = la pantalla "esto aprendió el sistema de Camila"
(el equipo la hace visible el sábado). ⚠️ "Míralo en vivo" solo es válido con
material real — si al final queda mockup, cambiar a "Así funciona".]*

### ⏱ 1:30–1:40 · POR QUÉ IMPORTA (CONGELADO — el stack se muda a la pantalla)

> Porque vender seguros 24/7 no es atender un chat: es saber a quién venderle
> y cómo hablarle. Cada conversación se lo enseña al sistema: entre más
> conversa, mejor vende.

*[El diagrama del flywheel (`escenas/E4-flywheel.html`) carga el stack en labels
(Python · DANE · Fasecolda · trazabilidad): la voz dice el porqué, la pantalla
el cómo. "Motor determinista" se reserva para el Q&A.]*

### ⏱ 1:40–2:00 · CIERRE (CONGELADO con ajustes de JP)

> ¿Y los asesores humanos? Son el corazón del piloto: 3 meses entrenando al
> agente — y quedándose con los casos que merecen su tiempo. Somos Scala Labs,
> y esto es lo que creemos: la transacción la resuelve cualquier chatbot. La
> venta real es valor genuino y transparente — Colsubsidio lo entiende desde
> hace 69 años. Y eso fue exactamente lo que construimos.

*[**69 años** verificado: fundada en 1957 (ANDI, Bogotá; personería Res. 3.286
del 4-dic-1957 — Wikipedia/SuperSubsidio). "Estamos listos" ELIMINADO (decisión
JP). 💡 Idea GUARDADA para el pitch EN VIVO de finalistas: cerrar con QR de
"agenda nuestra reunión de onboarding" — el siguiente paso natural de
contratarnos. NO va en el video pregrabado.]*

---

## Storyboard para el video (Claude Design + screen recording)

La cámara de JP va en burbuja SIEMPRE (formato Loom). Esto es lo que va en pantalla:

| Escena | Tiempo | Visual en pantalla | Fuente |
|---|---|---|---|
| E1 | 0:00–0:20 | Apertura 0–3s: pantalla oscura solo con "Nadie se despierta queriendo comprar un seguro." → avatar sintético de Camila + chips (`29 años` `2 hijos`) → creencias apareciendo alrededor ("cara" "enredada" "papeleo" "asesores") → dato **62%** (Solidaria 2025) → cifra grande contador **90,7%** (Fasecolda · mar 2026) → remate en amarillo "nadie les ha mostrado lo simple que puede ser" | Claude Design (animación) — v2 sobre E1-hook.html |
| E2 | 0:20–0:40 | El chat aparece (mockup animado mientras no exista; screenshot real después) con la conversación iniciando | Claude Design → reemplazar por screenshot real |
| E3 | 0:40–1:30 | **Screen recording real del demo**, sin cortes, siguiendo el guion. Zoom suave en: pantalla de precio, consentimiento, número de póliza, consulta de DB | Grabación del demo (depende de T018) |
| E4 | 1:30–1:40 | Diagrama animado del flywheel: conversación → data → motor → mejor venta → (loop). Paleta de marca | Claude Design (animación) |
| E5 | 1:40–2:00 | Equipo (foto/avatares + roles en 1 línea) → cierre con logo Colsubsidio×30X y "Estamos listos" | Claude Design |

**Especificaciones**: 16:9 · paleta `recursos-marca/` (fondo oscuro — no hay logo
para fondo claro) · texto en pantalla mínimo y grande (la jurado: bullets, no
paredes de texto) · subtítulos quemados (se ve sin audio en la plataforma).

## Producción — checklist

- [ ] Guion v2 con la voz de JP (leerlo en voz alta y marcar lo que no suene a él)
- [ ] Ensayo con cronómetro: cada bloque en su tiempo (tolerancia ±2s)
- [ ] Escenas E1/E2/E4/E5 generadas con Claude Design (se pueden hacer YA, sin demo)
- [ ] E3: screen recording del demo real sin cortes (bloqueado por T018 — integración)
- [ ] Grabación Loom: buena luz, micrófono cerca, energía alta, contacto a cámara
- [ ] Edición: burbuja + escenas + subtítulos (CapCut o similar)
- [ ] Backup: exportar y subir ANTES del cierre del domingo; probar reproducción
- [ ] Página de preguntas de finalistas (¿3 meses? ¿stack? ¿mercado? ¿competidores?) — el dossier ya las responde; condensar en 1 página

## Pendientes de decisión

- Link de la plataforma del evento (registro del equipo + subida) — buscar en el grupo general
- ¿Quién graba la voz/cámara de respaldo si JP queda como finalista presencial?

---

*Guion v1 asistido por Claude Fable 5 (esfuerzo alto) sobre decisiones creativas
de JP (hook híbrido, formato Loom, cierre piloto+flywheel) · 2026-07-24*

## ⏱ Tiempos v3 — escenas retimeadas a la voz real (El Faraón, 25-jul)

| Escena | Duración | Audio | Acumulado |
|---|---|---|---|
| E1 Hook | 26,5s | `voz/bloque-1-hook.mp3` | 0:00–0:26 |
| E2 Qué construimos | 25,4s | `voz/bloque-2-que-construimos.mp3` | 0:26–0:52 |
| E3 Demo (2 actos) | 30,0s (voz 26,7 + aire) | `voz/bloque-3-demo.mp3` | 0:52–1:22 |
| E4 Flywheel | 13,8s | `voz/bloque-4-flywheel.mp3` | 1:22–1:36 |
| E5 Cierre | 23,9s | `voz/bloque-5-cierre.mp3` | 1:36–2:00 |

**Total: 119,6s ≈ 2:00** ✅. Los beats de cada escena están sincronizados a las
pausas reales del audio (analizadas con silencedetect). E3 acto 1 quedó en modo
"timelapse" (ráfaga rápida de chat — la voz lo cubre: "se lo descubre en 5
preguntas"). Si se cambia a la voz de JP (decisión post-feedback), se repite el
retiming con el mismo método.

## Ruta de producción acordada (JP, madrugada 25-jul)

1. **Voz en off ElevenLabs** (estilo comercial emotivo) sobre el guion congelado
   → `guion-voz-elevenlabs.md`. Pendiente: API key de JP (no hay en el sistema)
   o generar en la web de ElevenLabs pegando el guion anotado.
2. **Animaciones calidad-final** de TODAS las escenas (E3 con mockup de producto
   suficientemente bueno para pasar como final; solo se intercambian los mockups
   por renders/grabación real después).
3. **Sábado:** ronda de feedback del pitch (equipo + mentora Emmy) → ajustes.
4. **Después del feedback:** efectos de sonido + música de fondo.
5. **Decisión final:** mantener VO de ElevenLabs o JP graba tipo Loom (burbuja
   de cámara) acompañando las animaciones.
6. Ajuste fino de timing voz↔animación: AL FINAL, con la voz definitiva.

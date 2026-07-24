# PITCH — video pregrabado 2:00 (guion v1 · en construcción)

**Formato decidido (JP)**: tipo Loom — cámara de JP en burbuja sobre la pantalla,
un solo take si sale bueno. Hook híbrido (persona + dato). Cierre piloto + flywheel.

**Regla de oro del guion**: cada bloque tiene SU tiempo. Ensayar con cronómetro
hasta que suene natural (consejo literal de la jurado). ~2,6 palabras/segundo.

---

## Guion por bloques

### ⏱ 0:00–0:20 · HOOK + PROBLEMA (~52 palabras)

> Ella tiene 29 años, dos hijos y gana un salario mínimo. Nadie le ha ofrecido
> jamás un seguro que pueda pagar. Y como ella, 9 de cada 10 hogares en Colombia
> no tienen seguro de hogar — y solo el 0,24% de las pólizas se vende por canal
> digital. No es falta de necesidad: **es falla de canal.**

*[JP: dilo mirando a cámara, sin nada más en pantalla que ella — ver storyboard E1.
Ajusta las palabras a como TÚ hablas; lo intocable son los 3 datos y "falla de canal".]*

### ⏱ 0:20–0:40 · QUÉ CONSTRUIMOS (~52 palabras)

> Construimos un asesor de seguros por WhatsApp para Colsubsidio: se interesa en
> conocerte, entiende qué buscas — o lo descubre con máximo 5 preguntas — y te
> propone el seguro correcto con un porqué basado en tus datos reales. Y te deja
> asegurado, con número de póliza, en menos de 3 minutos. Sin humanos, 24/7.

*[Usa la frase congelada del equipo — es esta. En pantalla entra el chat (E2).]*

### ⏱ 0:40–1:30 · DEMO (~130 palabras, sobre el flujo real grabado)

Camino a mostrar: **el perfil ancla end-to-end** (afiliada, monoparental, cat. A).

> Ella es afiliada, así que el sistema ya la conoce: no le pedimos lo que
> Colsubsidio ya sabe. — *(paso 0 en pantalla)* — Dice que no sabe qué necesita;
> el chat se lo descubre en 5 preguntas simples. — *(preguntas corriendo)* — El
> motor calcula: no la IA — un motor determinista con las reglas de nuestras
> expertas en seguros. Le recomienda proteger a los suyos, con la prima ajustada
> a SU ingreso: nunca le vendemos lo que no puede pagar. — *(pantalla de precio)* —
> Acepta, consiente en lenguaje claro, y… asegurada. Póliza, hash, trazabilidad.
> — *(cierre celebratorio + consulta a la DB en vivo)* — Y si el jurado pregunta
> "¿por qué esta cifra?": aquí está, trazada en la base de datos, paso a paso.

*[JP: la consulta de trazabilidad en vivo es nuestro momento "wow" ante jurado
técnico — SC-003. Grabar el flujo SIN cortes cuando el demo esté (T018).]*

### ⏱ 1:30–1:40 · STACK + POR QUÉ IMPORTA (~26 palabras)

> Motor determinista en Python, scoring con datos DANE y Fasecolda, y la IA solo
> conversa — nunca calcula. **Y cada conversación, cierre o no, deja data que
> reentrena el motor.**

*[Aquí vive tu flywheel — la frase que quedó en la definición oficial del equipo.]*

### ⏱ 1:40–2:00 · EQUIPO + QUÉ SIGUE + CIERRE (~50 palabras)

> Somos Scala Labs: seguros, datos, producto y desarrollo. El siguiente paso: un
> piloto de 3 meses con afiliados reales — y cada conversación de ese piloto
> entrena al motor: **entre más vende, mejor vende.** Si funciona con los
> afiliados, funciona para los 9 de cada 10 hogares que hoy no tienen protección.
> Estamos listos.

*[JP: presenta al equipo por fortalezas, no por nombres (no caben 6 nombres en 20s).]*

---

## Storyboard para el video (Claude Design + screen recording)

La cámara de JP va en burbuja SIEMPRE (formato Loom). Esto es lo que va en pantalla:

| Escena | Tiempo | Visual en pantalla | Fuente |
|---|---|---|---|
| E1 | 0:00–0:20 | Ilustración/animación sobria del perfil ancla + los 2 datos apareciendo como texto grande (90,7% · 0,24%) sobre fondo grafito con amarillo Colsubsidio | Claude Design (animación) |
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

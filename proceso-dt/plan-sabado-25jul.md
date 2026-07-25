# Plan del sábado 25 — un solo objetivo

> **A las 5 de la tarde, todo lo que construimos por separado funciona junto,
> de principio a fin, en un solo lugar. Después de las 5 no agregamos nada
> nuevo: solo probamos, grabamos y subimos.**

Esto es una hackathon: no necesitamos el producto más robusto del mundo.
Necesitamos un MVP completo que demuestre potencial de negocio y que puede
crecer sin riesgo. Como dijo JD: **mejor un MVP completo que uno a medias.**
El domingo es solo para ponerlo bonito, ensayar y entregar.

---

## Priorización (idea de JD: matriz de Eisenhower)

**✅ MAÑANA (lo único que importa):** unir el motor + el chat + los datos en un
solo flujo que corra completo · la pantalla de pago de prueba · la opción de
hablar con una persona · subir el demo a internet · grabar el video del demo.

**📅 DOMINGO (si mañana cerramos bien):** pulir textos y colores · ensayar el
pitch · revisión final · entrega en la plataforma.

**⏳ SOLO SI SOBRA TIEMPO (nadie lo arranca sin avisar):** probar el modelo
contra la base de datos de Colsubsidio · sugerir seguros adicionales después de
la compra.

**❌ NO VAMOS A HACER (y está bien así):** meter los 26 seguros al motor (con
los 11 que pesaron Caro y Meli basta y sobra) · entrenar modelos de machine
learning (eso se CUENTA como visión, no se construye) · automatizar la conexión
Notion–GitHub · cualquier idea nueva que aparezca mañana (se anota para el lunes).

---

## Qué hace cada quien (máximo 3 cosas por persona)

### 🧠 Daniel (desde las 11am)
1. Enseñarle al chat a entender qué seguro pide la persona cuando escribe con
   sus palabras ("quiero un SOAT", "algo para mi perro"). **No es machine
   learning**: es comparar contra una lista de palabras que arma Caro. La guía
   exacta de cómo hacerlo ya está escrita — Juan Pablo te la pasa.
2. Dejar el motor listo para que n8n (o Make) lo pueda llamar y recibir la
   respuesta.
3. Apoyar la conexión final de la tarde.

### 🔧 Sebas
1. La pantalla de pago de prueba: se ve real, pero no cobra (modo demo).
2. El cierre de la compra: número de póliza + comprobante que queda guardado.
3. Apoyar a JD con el canal (WhatsApp o chat web).

### 🎛 JD
1. Armar el "director de orquesta" en n8n o Make: recibe el mensaje de la
   persona, le pregunta al motor, y devuelve la respuesta. *(Elige la
   herramienta con la que avances más rápido HOY — hay créditos de Make del
   evento, y Juan Pablo tiene "skills" de n8n para Claude que aceleran mucho;
   te las comparte.)*
2. Los textos que dice el asesor, con textos de respaldo por si la IA falla.
3. **El intento de WhatsApp de prueba, SOLO hasta la 1:30pm.** Si a esa hora no
   entra y sale un mensaje, lo soltamos sin drama: el demo va con el chat web
   (que ya existe) y WhatsApp se cuenta como el siguiente paso. El pitch no
   cambia nada.

### 🎨 Caro
1. Dibujar las pantallas del chat, paso a paso, como se las mostraríamos a un
   usuario (a mano, en Canva, o como te sea más fácil — son los "planos" para
   la reunión con Emmy y para que JD arme la interfaz igual a lo que diseñes).
2. La lista de palabras por seguro: cómo pide la gente cada producto ("SOAT",
   "moto", "carro", "perro", "gato", "mi familia"…). Es el insumo de la tarea 1
   de Daniel.
3. Definir en qué casos el asesor ofrece "¿quieres hablar con una persona?" y
   con qué palabras lo dice.

### 📊 Melissa (1 hora, cuando puedas)
1. Escribir 2 personas de ejemplo (edad, familia, ingreso…) con el resultado
   EXACTO que el motor debe darles. Es nuestra prueba de que nada se dañó al
   conectar todo.

### ✅ Lizeth (por chat, sin reuniones)
1. Cuando el flujo esté conectado (tarde), revisarlo contra los requisitos que
   definiste y comentar qué falta o qué sobra.

### 🎬 Juan Pablo
1. Reunión con Emmy: avance del pitch + los dibujos de pantallas de Caro.
2. Conectar y probar todo de punta a punta (con los 2 ejemplos de Melissa).
3. Subir el demo a internet con un link que cualquiera pueda abrir + grabar el
   video del recorrido para el pitch.

---

## La venta con ayuda humana (queda COMPLETA en el MVP)

La idea, en simple: **el asesor digital puede llamar a una persona como un
recurso más** — igual que consulta el motor o el catálogo. Es una dupla, no un
reemplazo: la persona entra solo cuando de verdad aporta (un seguro complejo, o
si el usuario lo pide), nunca por defecto ni a cada rato. En el demo se muestra
así: en el momento indicado el chat ofrece "¿prefieres que te acompañe una
persona?" y se ve el traspaso (simulado). Caro define el cuándo y el cómo se
dice; JD/Sebas lo montan en el flujo.

---

## Horario del día

| Hora | Qué pasa |
|---|---|
| 9:00 | Daily: validamos este plan (10 min) y arrancamos |
| 1:30 | Punto de control de 15 min: ¿WhatsApp sí o no? ¿algún frente trabado? |
| 5:00 | **Se congela**: no entra nada nuevo. Solo conectar, probar, grabar |
| Noche | Demo en internet + video grabado + revisión de que lo construido cumple lo prometido |

## No se nos puede olvidar

- **Registro en la plataforma (Hackradar)**: confirmar que están registradas
  las 5 personas correctas (el cupo es de 5; Lizeth acordó entrar como apoyo).
  Falta 1 cupo — confirmar quién es "Juan Muñoz" y que Sebas quede dentro.
- Si alguien se siente saturado o trabado más de 30 minutos: lo dice en el
  grupo. Nadie pierde una tarde peleando solo con algo.

---

*Plan preparado por JP (Scrum Master) con Claude Fable 5 (esfuerzo alto) ·
2026-07-24 noche · se valida en el daily del sábado 9:00am*

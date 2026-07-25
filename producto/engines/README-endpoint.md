# Endpoint REST de respaldo — Motor de Scoring Colsubsidio

Servidor HTTP mínimo que expone el motor de reglas `motor-colsubsidio.py` por REST.
Se construyó como **plan B**: si el endpoint titular del equipo no llega a tiempo para
el demo, este corre sin instalar nada.

Usa únicamente la biblioteca estándar de Python 3 (`http.server`, `json`, `uuid`).
No requiere `pip install`.

---

## Requisitos

- Python 3.8 o superior
- El archivo `producto/db/trazabilidad.py` y `schema.sql` deben estar presentes
  (ya están en el repo — la DB SQLite se crea sola al primer request)

---

## Cómo correrlo

```bash
# Desde la raíz del repo:
python3 producto/engines/endpoint_motor.py

# Puerto personalizado:
PORT=9000 python3 producto/engines/endpoint_motor.py
```

Puerto por defecto: **8090**.

---

## Endpoints

### `GET /salud`

Health check. Responde si el servidor está vivo.

```bash
curl http://localhost:8090/salud
```

Respuesta:

```json
{"ok": true}
```

---

### `POST /recomendar`

Recibe el perfil del usuario (variables V1–V11) y devuelve el top 3 del motor de reglas.

**Body JSON requerido:**

```json
{
  "perfil": {
    "V1": "<categoría de rango de edad>",
    "V2": "<Masculino | Femenino>",
    "V3": "<situación laboral>",
    "V4": "<nivel de ingreso>",
    "V5": "<composición familiar>",
    "V6": "<tipo de vivienda>",
    "V7": "<Sí | No>",
    "V8": "<Carro | Moto | No tiene>",
    "V9": "<Sí | No>",
    "V10": "<Sí | No>",
    "V11": "<Sí | No>"
  },
  "producto_explicito": "vida"
}
```

`producto_explicito` es opcional. Si se envía, ese producto sube al rank 1
independientemente de su score (lógica del motor).

**Categorías válidas por variable:**

| Variable | Categorías |
|---|---|
| V1 — Rango de edad | `18-25 años`, `26-35 años`, `36-45 años`, `46-55 años`, `56-65 años`, `66+ años` |
| V2 — Género | `Masculino`, `Femenino` |
| V3 — Situación laboral | `Formal dependiente`, `Formal independiente / profesional`, `Informal / cuenta propia sin cotización` |
| V4 — Ingreso mensual | `Bajo (< $1.3M)`, `Medio ($1.3M - $4.6M)`, `Alto (> $4.6M)` |
| V5 — Composición familiar | `Soltero(a) sin hijos`, `Pareja sin hijos`, `Con hijos menores de edad`, `Monoparental con hijos`, `Multigeneracional / adulto mayor a cargo` |
| V6 — Tipo de vivienda | `Propia pagada`, `Propia financiada (hipoteca)`, `Arrendada` |
| V7 — Arrienda a terceros | `Sí`, `No` |
| V8 — Vehículo | `Carro`, `Moto`, `No tiene` |
| V9 — Mascota | `Sí`, `No` |
| V10 — Bicicleta/patineta | `Sí`, `No` |
| V11 — Jefatura femenina sin pareja | `Sí`, `No` |

**Ejemplo completo — Madre soltera, ingreso bajo:**

```bash
curl -X POST http://localhost:8090/recomendar \
  -H "Content-Type: application/json" \
  -d '{
    "perfil": {
      "V1": "26-35 años",
      "V2": "Femenino",
      "V3": "Formal dependiente",
      "V4": "Bajo (< $1.3M)",
      "V5": "Monoparental con hijos",
      "V6": "Arrendada",
      "V7": "No",
      "V8": "No tiene",
      "V9": "No",
      "V10": "No",
      "V11": "Sí"
    }
  }'
```

Respuesta:

```json
{
  "top_3": [
    {"key": "vida",      "nombre": "Vida",              "linea": "Familia",    "score": 19, "max_score": 31, "pct": 61.3, "modo_cierre": "asesoria", "rank": 1, "forced_explicit": false},
    {"key": "educacion", "nombre": "Educación",          "linea": "Familia",    "score": 18, "max_score": 25, "pct": 72.0, "modo_cierre": "asesoria", "rank": 2, "forced_explicit": false},
    {"key": "exequial",  "nombre": "Exequial familiar",  "linea": "Familia",    "score": 17, "max_score": 24, "pct": 70.8, "modo_cierre": "auto",     "rank": 3, "forced_explicit": false}
  ],
  "trazabilidad": "ok",
  "session_id": "<uuid>"
}
```

Si la DB de trazabilidad falla por cualquier razón, la respuesta igual llega pero con
`"trazabilidad": "error"` — el log es best-effort y nunca bloquea la recomendación.

---

## Códigos de respuesta

| Status | Cuándo |
|---|---|
| 200 | Recomendación exitosa |
| 400 | JSON inválido o variable / categoría desconocida |
| 404 | Ruta no registrada |
| 500 | Error interno del motor |

---

## Cómo exponerlo a Make (orquestación)

**Misma máquina del demo:**
Make apunta directamente a `http://localhost:8090/recomendar`. El nodo HTTP de Make
hace POST con el perfil armado por el flujo anterior.

**Desde otra máquina / red externa:**
Usar un túnel temporal sin instalar nada permanente:

```bash
# Opción A — cloudflared (un binario, sin cuenta)
cloudflared tunnel --url http://localhost:8090

# Opción B — ngrok
ngrok http 8090
```

Ambas opciones generan una URL HTTPS pública que se pega en el módulo HTTP de Make.
Este README no instala ni configura los túneles — solo los menciona como opciones.

---

## Descarte limpio

Si el endpoint titular del equipo llega a tiempo, este archivo se descarta sin ruido:
basta con no iniciar el proceso. No modifica nada del motor ni de la DB.

---

> Construido con Claude Sonnet 4.6 (agente delegado), esfuerzo medio, supervisado por Fable 5.

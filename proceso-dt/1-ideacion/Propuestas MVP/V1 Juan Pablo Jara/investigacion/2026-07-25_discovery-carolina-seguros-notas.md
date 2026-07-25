# Discovery · Proceso actual de venta de seguros en Colsubsidio

**Fecha:** 2026-07-25
**Fuente:** mentora de seguros de Colsubsidio, conversación presencial 25-jul
**Proyecto:** Hackathon Colsubsidio × 30X — Reto 02 · Equipo Scala Labs

---

## Hallazgo principal

Colsubsidio actúa como **canal de comercialización**, no como aseguradora directa.
El proceso real de cierre consiste en **remitir el lead a la aseguradora del convenio**
(MetLife u otras), que cotiza, valida y **recauda**. Colsubsidio no cobra al usuario
ni envía checkouts propios. La relación es: Colsubsidio capta el interés → entrega
el lead al asegurador → el asegurador cierra y cobra.

---

## Proceso actual ("antes")

- El usuario llena un formulario en la web de Colsubsidio (o llega por otro canal).
- **Una persona del equipo de seguros descarga el lead manualmente** del formulario.
- Esa persona **envía los leads por correo, una sola vez al día**, a la aseguradora del convenio correspondiente.
- La aseguradora recibe el archivo, revisa, cotiza y contacta al prospecto.
- **Contacto con el lead:** manual, por WhatsApp y teléfono — mensaje escrito a mano por el asesor.
- **Sin CRM**: el área de seguros opera en Excel. (Salesforce existe a nivel corporativo, pero no está adoptado en esta área.)
- Los asesores tienen metas mensuales de presupuesto e ingresos definidas con el intermediario.

---

## Números duros

| Indicador | Valor |
|---|---|
| Leads promedio/mes | ~1.200 |
| Tasa de conversión | ~15% |
| CAC actual | ~$40.000 COP |

---

## Mercado objetivo

- Colsubsidio vende seguros **tanto a afiliados como a no afiliados** — no hay restricción de audiencia.
- Afiliados tienen un pequeño beneficio diferencial, pero el producto es accesible para todos.

---

## Modelo de propensión — visión del área

Carolina explicitó que el reto busca:
- Un **modelo de propensión** que prediga qué lead tiene mayor probabilidad de convertir.
- Identificar el **canal correcto por segmento**: no es lo mismo comunicar a un adulto joven (posiblemente TikTok) que a un adulto mayor (canales tradicionales). El canal de contacto debe ajustarse al perfil del prospecto.

---

## Implicaciones para el MVP (sin alarma, encuadre positivo)

Nada en la arquitectura del prototipo se rompe con este hallazgo. El encuadre correcto:

- **En producción**, Amparito (el agente) entrega a la aseguradora un **lead validado,
  calificado y con consentimiento firmado en segundos** — versus el correo manual
  que sale una vez al día. La velocidad de remisión es la ganancia inmediata.
- El pago en chat ("el usuario paga directamente") es una **visión de segunda fase**,
  condicionada a que la aseguradora habilite su propia pasarela para el canal.

### Ajustes técnicos derivados

- Agregar campo `aseguradora_id` en la base de trazabilidad (a qué convenio se remite el lead).
- Agregar estado `remitido_aseguradora` en el flujo de seguimiento del lead.
- Ajustar los diálogos de cierre en el agente: dejar claro al usuario que la aseguradora
  del convenio lo contactará para cotización y pago — no Colsubsidio directamente.

---

*Artefacto generado con Claude Sonnet 4.6, esfuerzo medio, a partir de transcript de audio · sesión coordinada por Claude Fable 5*

# Diálogos del asistente — nota v25-jul

> **Cierre real del proceso (discovery 25-jul)**
>
> En producción, Colsubsidio **no vende el seguro directamente**: remite el lead a la aseguradora del convenio, que es quien cotiza en firme y recauda. El "cierre" del flujo desde el chat es entonces **la remisión** (con consentimiento del usuario y `aseguradora_id` registrado), no la emisión de póliza.
>
> Impacto en el copy y en el MD v3 de Caro:
> - El cierre del asistente debe leerse como *"te ponemos en contacto con {aseguradora}"*, no *"acabas de contratar…"*.
> - El botón/CTA final es "remitir mi caso" (o equivalente), no "contratar".
> - En el demo se mantiene la sesión dorada con label `compro` para no romper la pantalla del PR #10; producción usará `remitido_aseguradora`.
>
> Contexto en `proceso-dt/1-ideacion/Propuestas MVP/V1 Juan Pablo Jara/investigacion/2026-07-25_discovery-cierre-remision-aseguradora.md`.

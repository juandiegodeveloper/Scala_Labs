# Arquitectura Jarvis — Venta asistida de seguros

## Tesis del diseño
El volumen de ventas lo absorbe un agente LLM (**Jarvis**); los asesores humanos dejan de ser el canal por defecto y pasan a ser un recurso **especializado** para seguros complejos. Escalar ventas deja de significar "contratar más asesores".

## Flujo

### 1. Captación
Cuatro puntos de entrada al sistema: campañas, QR, redirección desde SOAT y referidos. Todos convergen en la misma interfaz conversacional.

### 2. Onboarding y ruteo
Jarvis aplica **11 preguntas estructuradas**. Un **script de Python** clasifica la respuesta en dos rutas: seguro *simple* o seguro *complejo*. Este componente es determinista y auditable a propósito: la decisión de negocio no queda a criterio del LLM.

### 3A. Ruta simple (flujo primario)
El mismo LLM que hizo el onboarding —sin traspaso, sin pérdida de contexto— recomienda productos apoyado en:
- **RAG** para conocimiento de producto y condiciones.
- **SQL** para tarifas, catálogo y datos de cliente.

Si el cliente acepta, se capturan datos complementarios, se envían al **motor de cotización** y se valida si ya es afiliado. Si no lo es, entra al **embudo de afiliación**.

### 3B. Ruta compleja
Jarvis mantiene la gestión, pero ofrece escalamiento a un **asesor humano**. Esta ruta existe por dos razones: hay productos que técnicamente requieren asesoría, y hay una preferencia cultural en Colombia por la atención humana en decisiones de alto compromiso.

### 4. Capa de aprendizaje
Cada conversación con asesor se registra y alimenta un **dataset etiquetado por outcome** (venta / no venta). Con él se entrenan modelos para identificar qué patrones de interacción humana correlacionan con conversión. El resultado retroalimenta dos puntos:
- El **router**, para clasificar mejor qué caso realmente necesita humano.
- **Jarvis**, para incorporar los patrones de argumentación que funcionan.

## Por qué importa
El sistema es un ciclo cerrado: cada intervención humana costosa genera datos que reducen la necesidad de futuras intervenciones humanas. El margen operativo mejora con el uso.

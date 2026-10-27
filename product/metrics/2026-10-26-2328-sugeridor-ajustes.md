---
spec: product/specs/2026-10-26-2239-sugeridor-ajustes.md
exposure-plan: product/exposure-plans/2026-10-26-2253-sugeridor-ajustes.md
level: 1 — La sugerencia con el porqué en la alerta
status: designed
---

# Métricas de: Asistente sugeridor de ajustes de inventario

## Audiencia objetivo

5 analistas de RM de aerolíneas low cost o regionales. No compran datos competitivos pagos. Aplican ajustes en el inventario sin aprobación. Ya reciben las alertas de monitor-alertas. Solo cuentan sus 2 o 3 rutas elegidas.

- **Fuente:** segmento de `product/overview.md` + audiencia del nivel 1 del plan de exposición.
- **Tamaño:** 5.
- **Stand-ins:** un analista que necesita aprobación para aplicar un ajuste no es del segmento (ejemplo: Maria Urioste en el ensayo de T1). Sus datos se leen aparte y no cuentan en el denominador.
- **Iniciador y participante:** no aplica. En el nivel 1, solo el analista usa la feature. Las personas de reemplazo entran en el nivel 3, y el jefe en el nivel 5.

## Frecuencia esperada

Entre 1 y 3 cambios con sugerencia por analista por semana, en 2 o 3 rutas. `assumption`.

- Base: el ensayo de T1 dio 18 cambios alertados para 5 analistas en 5 días hábiles, en todas sus rutas (`synthetic`) — product/tests/materials/t1-monitor-alertas/Resultados de la prueba de monitor-alertas (concierge)-ensayo.md. Diego cuenta varios cambios por mes por ruta (`synthetic`) — product/interviews/2026-10-25-2248-diego-paredes.md.
- Ninguna fuente `real` mide esta frecuencia. La corrida real de T1 (2026-11-16 a 2026-11-27) la puede medir.
- **Ventana de retención:** la semana.
- **Mínimo para la revisión:** cada analista necesita 3 sugerencias. Si un analista recibe menos de 3 en la semana, el nivel se extiende 1 semana para ese analista (máximo 2 semanas). El umbral 2 de 3 no cambia.

## Acquisition

- **Señal:** el analista abre el detalle de una sugerencia (la razón y el dato crudo).
- **Definición expandida:** cuenta si abre al menos 1 sugerencia durante el nivel. Las alertas sin sugerencia por falta de dato no cuentan como sugerencia.
- **Cálculo:** analistas que abren ≥1 sugerencia / 5, durante el nivel (1 semana, o 2 para quien se extiende).
- **Meta:** 100 % (5 de 5) · **Razón:** los 5 eligieron sus rutas y ya reciben la alerta. El avance pide que 4 de 5 expliquen la razón, entonces con 4 de 5 ya no hay margen.
- **Eventos:** `alerta_enviada` (analista_id, aerolinea_id, ruta, cambio_id, sugerencia_id, tipo_sugerencia: `abrir clase` | `cerrar clase` | `no tocar` | `sin sugerencia`, dato_faltante, canal, nivel, timestamp, hora_local) · `sugerencia_abierta` (analista_id, sugerencia_id, nivel, timestamp).
- **Riesgo de captura:** `sugerencia_abierta` solo existe si la alerta tiene un enlace al detalle. Si el canal es WhatsApp con todo el texto en el mensaje, no hay evento de apertura. La confirmación de lectura es una aproximación, y el análisis tiene que decirlo. Depende de la pregunta abierta 5 del plan (canal).

## Activation

- **Señal:** en la revisión corta del final del nivel, el analista explica con sus palabras la razón de la sugerencia.
- **Definición expandida:** el moderador elige 3 sugerencias que el analista recibió (si es posible, al menos 1 `no tocar`). Para cada una, el analista explica la razón sin leer el texto. El moderador anota el resultado en la planilla de la revisión.
- **Umbral de la señal:** explica bien 2 de 3 sugerencias o más. "Bien" significa las 3 cosas:
  1. nombra el cambio del competidor;
  2. nombra al menos 1 dato propio que usa la sugerencia (tarifa propia, clases abiertas, reservas);
  3. contesta "¿por qué esa cantidad de asientos?" (o "¿por qué no tocar?").

  **Razón:** la creencia #12 (`[feature: sugeridor-ajustes] [usability]`) y la frustración de Diego: "si me preguntás por qué ese número… no te sabría explicar bien" — product/interviews/2026-10-25-2248-diego-paredes.md. Si el analista no explica la razón, no podemos interpretar en el nivel 2 si la aplica o no. · **Excluye:** abrir la sugerencia sin explicarla, y leer las 3 frases en voz alta sin decirlas con sus palabras.
- **Cálculo:** analistas que explican bien ≥2 de 3 / 5.
- **Meta:** 80 % (4 de 5) · **Razón:** es el criterio de avance del nivel 1.
- **Eventos:** `sugerencia_abierta` · `dato_crudo_visto` (analista_id, sugerencia_id, timestamp) · planilla de la revisión, 1 fila por sugerencia revisada: `revision_explicacion` (analista_id, sugerencia_id, nombra_cambio sí/no, nombra_dato_propio sí/no, explica_cantidad sí/no, explico_bien sí/no, contradiccion sí/no, contradiccion_texto, moderador, fecha).

## Retention

- **Señal:** el analista abre la sugerencia en 2 días distintos del nivel o más.
- **Definición expandida:** cuenta solo un analista que recibió sugerencias en 2 días o más. Un analista con sugerencias en 1 solo día no cuenta como retenido ni como no retenido: se informa aparte. Con 1 sola ventana semanal en el nivel 1, esta lectura mide la vuelta dentro de la semana, no de una semana a otra.
- **Curva de retención:** 1 cohorte (los 5 empiezan el mismo día). Por cada día hábil con sugerencia, la proporción de analistas que abre la sugerencia ese día. Con 5 personas y 1 semana, la lectura es solo de dirección. La curva semanal por cohorte empieza en el nivel 2, cuando se revisa este archivo.
- **Cálculo:** analistas que abren sugerencias en ≥2 días distintos / 5.
- **Meta:** 80 % (4 de 5) · **Razón:** si el analista abre solo la primera sugerencia, la razón no le da valor para la próxima decisión, y medir `apliqué` en el nivel 2 pierde sentido.
- **Eventos:** `alerta_enviada` · `sugerencia_abierta` (con fecha y hora local).

## Satisfaction

- **Instrumento:** CSAT de 1 pregunta en el detalle de la sugerencia · **Pregunta:** "¿Qué tan satisfecho está con la sugerencia y su explicación?" (1 a 5), y un comentario opcional: "¿Qué le falta?" · **Cuándo aparece:** al cerrar el detalle de la 3.ª sugerencia abierta. Si el analista no llega a 3, el último día hábil del nivel. 1 vez por analista · **Corte:** 4 o 5.
- **Definición expandida:** cuenta el analista de la audiencia que contesta 4 o 5. Una persona que no contesta no cuenta como satisfecha.
- **Cálculo:** analistas con 4 o 5 / 5. La tasa de respuesta y la proporción entre quienes contestan se informan aparte.
- **Meta:** 60 % (3 de 5) · **Razón:** es el primer contacto, y la lógica todavía no tiene el resultado real de T2 (#1). La satisfacción no es un criterio de avance del nivel 1. Si queda por debajo, leemos los comentarios antes de mostrar el nivel 2.
- **Eventos:** `csat_mostrada` (analista_id, sugerencia_id, timestamp) · `csat_respondida` (analista_id, puntaje, comentario, timestamp).

## Métricas de negocio

none declared. `product/overview.md` no tiene sección de sponsor ni métricas de negocio. Tiene 2 creencias `[viability]` sin número: #2 (un precio que el segmento paga y que cubre el costo del dato) y #7 (el jefe o la dirección atribuyen pérdida de ingreso a la reacción tardía). En el nivel 1, la feature se mide solo para el usuario. El plan mide el costo del dato (#9) en el nivel 3, y el caso de retorno (#2) necesita un diseño aparte con grupo de control.

## Conciliación con el plan de exposición

- **Avanzar — 4 de 5 analistas explican bien la razón en 2 de 3 casos o más:** `activation`, meta 80 % (4 de 5).
- **Avanzar — ningún analista encuentra una razón que contradiga el dato crudo:** ninguna métrica AARS lo lee. Lo lee un control de calidad: `revision_explicacion.contradiccion` = 0 en todas las filas.
- **Parar — 2 o más analistas no pueden explicar la razón:** `activation` ≤ 60 % (3 de 5). Coherente con la meta: 4 de 5 avanza, 3 de 5 o menos para.
- **Parar — un analista encuentra contradicciones:** el mismo control de calidad, `contradiccion` > 0. En ese caso, cambiar la redacción o la lógica (A3) y repetir el nivel.
- **Condición para leer el nivel:** cada analista con 3 sugerencias o más. Si no, el nivel se extiende 1 semana para ese analista.
- `acquisition`, `retention` y `satisfaction` no leen ningún criterio del plan. Son diagnóstico: si la activación queda baja, dicen si el problema es llegar a la sugerencia, volver a ella o la experiencia.
- **Fuera de este nivel:** "vuelve a la planilla" y "consulta antes de decidir" (pregunta abierta 2 del plan) se definen al revisar este archivo para el nivel 2.

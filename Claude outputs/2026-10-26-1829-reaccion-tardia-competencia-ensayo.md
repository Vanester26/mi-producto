---
source: survey
status: ensayo
survey_design: product/surveys/2026-10-25-2014-reaccion-tardia-competencia.md
results: Notas/Ensayo/encuestas/respuestas_encuesta.csv
opportunity: 2026-10-02-2304-reaccion-tardia-competencia
n_total: 30
n_completas: 24
created: 2026-10-26
---

# Análisis de encuesta (ENSAYO): cómo siguen los analistas de RM a la competencia

> **Este análisis es un ensayo.** El CSV está en `Notas/Ensayo/`, tiene fechas posteriores a hoy (27-10 a 13-11) y no usa el cuestionario del diseño. Use este documento para practicar el análisis y para ajustar el instrumento. No use este documento como evidencia para las creencias del overview.

## 1. Denominador y límites

| | LinkedIn | Referido | Total |
|---|---|---|---|
| Respuestas | 19 | 11 | 30 |
| Descalificadas | 4 | 1 | 5 |
| Parciales | 1 | 0 | 1 |
| **Completas** | **14** | **10** | **24** |

- **Meta de n:** 30 calificados. Resultado: 24 completas. **La meta no se alcanzó.** Todos los resultados son direccionales.
- **Tasa de respuesta:** desconocida. El diseño pedía registrar cuántos mensajes de LinkedIn se enviaron. Ese dato no está.
- **Motivos de descalificación:** 2 jefes/gerentes (R03, R20), 2 pagan herramientas de monitoreo (R07, R24), 1 no aplicó ajustes en el último mes (R12).

### El CSV no corresponde al diseño

El CSV tiene 10 preguntas. El diseño tiene 4 de pantalla, 13 preguntas y 3 de opt-in. Consecuencias:

| Pregunta del CSV | Equivale a (diseño) | Problema |
|---|---|---|
| Q1 Rol | S1 | 3 respondentes con rol "Otro" (R11, R21, R27) completaron. El diseño los descalifica. |
| Q2 Herramientas pagas | S3 | Sin opción "No sé". |
| Q3 Ajuste último mes | R1 | Se usó como pantalla de la encuesta. En el diseño solo filtra candidatos a entrevista. |
| Q4 Tiempo diario | Q5 | Pregunta por "tiempo diario" y no por "el último día". Los tramos (1 h–2,5 h) no permiten leer el umbral de 1,5 h. |
| Q5 Mayor fricción | — | Mide la creencia #4. El diseño la dejó fuera de alcance a propósito. La opción "decisión" junta dos cosas: decidir y esperar aprobación. |
| Q6 Días hasta enterarse | Q6 | Pregunta general, no por un episodio concreto. |
| Q7 Confiabilidad de la tarifa pública (1–5) | — | Mide la percepción sobre la creencia #1. Las etiquetas de la escala no están en el CSV: este análisis supone 1 = nada confiable, 5 = muy confiable. |
| Q8 Otras fuentes | — | Una sola respuesta por persona. Parece que debía ser opción múltiple. |
| Q9–Q10 Opt-in y contacto | R2–R3 | Sin cambios. |

**Faltan del diseño:** S2 (tipo de aerolínea), S4, Q1 (rutas), Q2–Q3 (competidores por ruta), Q4 (workaround), Q7 (cómo se enteró), Q8 (% de rutas con demora), Q9 (gasto), Q10–Q10b (demos), Q11 (quién aprueba), Q12 (abierta), Q13 (país y flota).

**Límite grave:** sin S2, no sabemos si los respondentes trabajan en una low cost o regional. El segmento objetivo no está verificado.

### Canal y rol van juntos

| Rol | LinkedIn | Referido |
|---|---|---|
| Analista de RM / Pricing (en un equipo) | 12 | 1 |
| Única persona a cargo de RM | 0 | 8 |
| Otro rol | 2 | 1 |

LinkedIn trae analistas que trabajan en un equipo (perfil Mariana). Los referidos traen a la única persona de RM de su aerolínea (perfil Diego/Carmen). El diseño anticipó este sesgo. Por eso, **cada diferencia entre segmentos de este análisis es también una diferencia entre canales.** No es posible separar las dos con estos datos. El único analista que llegó por referido (R30) responde como los analistas de LinkedIn: esto sugiere que el rol pesa más que el canal, pero con n = 1.

### Calidad de las respuestas

- R10 completó en 41 s. La mediana es ~140 s. Marcar como dudosa. Si la quitamos, ninguna conclusión cambia.
- R25 (83 s) dice "más de 2,5 h al día" y también "nos enteramos el mismo día", fricción en la decisión y confiabilidad 1. No es imposible, pero conviene confirmarlo en entrevista.

## 2. Resultados por objetivo de aprendizaje

Segmentos: **Equipo** = analistas de RM en un equipo (n = 13). **Única** = única persona a cargo de RM (n = 8). **Otro** = rol mixto (n = 3, fuera del perfil del diseño).

### G1 — Tiempo y demora (creencia #6)

**Qué creíamos:** ≥1,5 h/día de recolección manual y ≥30% de rutas con ≥1 día de demora.

**Tiempo diario en recolectar datos de competidores**

| | Equipo (13) | Única (8) | Otro (3) | Total (24) |
|---|---|---|---|---|
| Menos de 30 min | 4 | 0 | 0 | 4 |
| 30 min a 1 h | 6 | 0 | 1 | 7 |
| 1 h a 2,5 h | 2 | 4 | 2 | 8 |
| Más de 2,5 h | 1 | 4 | 0 | 5 |

- Única: 8 de 8 dedican 1 h o más. 4 de 8 dedican más de 2,5 h.
- Equipo: 10 de 13 dedican menos de 1 h.
- El umbral de 1,5 h no se puede leer exacto. Rango posible en el total: entre 5 de 24 (seguro) y 13 de 24 (como máximo) llegan a 1,5 h.

**Días hasta enterarse de un cambio del competidor**

| | Equipo (13) | Única (8) | Otro (3) | Total (24) |
|---|---|---|---|---|
| El mismo día | 5 | 0 | 0 | 5 |
| 1 a 2 días | 7 | 0 | 2 | 9 |
| 3 a 5 días | 1 | 5 | 1 | 7 |
| Más de 5 días / por un cliente, agencia o caída de reservas | 0 | 3 | 0 | 3 |

- 19 de 24 se enteran con 1 día o más de demora.
- Única: 8 de 8 se enteran con 3 días o más. 3 de 8 se enteran por un síntoma (cliente, agencia, caída de reservas), no por revisión.
- Equipo: la demora típica es 1 a 2 días.
- **Límite:** el CSV mide la demora típica por persona. No mide la proporción de rutas con demora, que es el umbral de la creencia.

**Qué muestra:** la creencia se cumple en el segmento Única y no se cumple en el segmento Equipo en el eje tiempo. La demora de ≥1 día aparece en los dos, pero es mucho mayor en Única.

**Decisión que sigue:** la oportunidad tiene tamaño en el segmento "única persona de RM" (aerolíneas chicas). En el segmento "analista en equipo", el tiempo de recolección no alcanza el umbral. Recomendación: acotar el segmento de la oportunidad a Única y confirmarlo con datos reales del cuestionario completo (con S2 y Q13 para saber tipo y tamaño de aerolínea).

### G2 — Competidores por ruta (creencia #5)

**Sin datos.** El CSV no tiene Q2 ni Q3 del diseño. La decisión de alcance de cobertura queda abierta.

### G3 — Qué usan, cuánto gastan y quién aprueba (creencia #2)

**Sin datos de gasto, demos ni aprobador.** Solo hay datos parciales de fuentes complementarias (Q8 del CSV):

El total incluye los 3 respondentes de "Otro rol".

| Otra fuente además de la tarifa pública | Equipo (13) | Única (8) | Total (24) |
|---|---|---|---|
| Mi propia curva de reservas | 7 | 1 | 9 |
| Conocimiento histórico del competidor | 1 | 4 | 6 |
| Reportes de agencias o call center | 3 | 2 | 6 |
| Ninguna otra fuente | 1 | 1 | 2 |
| Mapa de asientos del competidor | 1 | 0 | 1 |

El segmento Equipo usa su curva de reservas. El segmento Única usa su memoria del competidor. Esto no reemplaza a G3: la decisión de precio y de a quién vender queda abierta.

### Fuera del diseño — fricción principal (creencia #4)

El diseño dejó la #4 para entrevistas. El CSV la preguntó igual. Leer solo como pista.

| Mayor fricción | Equipo (13) | Única (8) | Otro (3) | Total (24) |
|---|---|---|---|---|
| En la decisión (o esperar aprobación) | 10 | 0 | 1 | 11 |
| En la recolección | 2 | 3 | 0 | 5 |
| En las dos por igual | 1 | 4 | 1 | 6 |
| En la precisión al copiar o cargar | 0 | 1 | 1 | 2 |

- Equipo: 10 de 13 ponen la fricción en la decisión. Esto debilita la #4 para ese segmento.
- Única: 0 de 8 eligen solo la decisión. 7 de 8 eligen recolección, las dos o precisión.
- **Límite de redacción:** la opción "decisión" incluye "consultar/esperar aprobación de otros". En un equipo, esperar al jefe puede explicar esa respuesta. No sabemos si la fricción es analítica o de aprobación.

### Fuera del diseño — confiabilidad percibida de la tarifa pública (creencia #1)

Escala 1–5 (supuesto: 1 = nada confiable).

| | 1 | 2 | 3 | 4 | 5 | Mediana |
|---|---|---|---|---|---|---|
| Equipo (13) | 3 | 6 | 3 | 0 | 1 | 2 |
| Única (8) | 0 | 1 | 2 | 4 | 1 | 4 |
| Total (24) | 3 | 7 | 7 | 5 | 2 | 3 |

- Equipo confía poco en la tarifa pública para estimar ocupación. Única confía más.
- **Límite:** es una percepción. La creencia #1 pide comparar contra ocupación real observada. Una encuesta no puede confirmar ni contradecir la #1.

## 3. Insights priorizados

1. **[Alto] La oportunidad se concentra en la única persona de RM.** 8 de 8 dedican ≥1 h/día a recolectar y 8 de 8 se enteran con ≥3 días de demora. En analistas de equipo, 10 de 13 dedican <1 h. → Acotar el segmento de la oportunidad y del producto a aerolíneas donde una sola persona hace RM. Direccional (n = 8), y confundido con el canal de referidos.
2. **[Alto] En analistas de equipo, el problema parece ser la decisión, no la recolección.** 10 de 13 eligen "decisión". → Si el producto también apunta a este segmento, el valor está en la sugerencia de ajuste, no en la recolección. Confirmar en entrevista si es decisión analítica o espera de aprobación.
3. **[Medio] Un 3 de 8 en el segmento Única detecta el cambio por un síntoma** (cliente, agencia, caída de reservas). → Una alerta de cambio puede ser el primer valor visible para ese segmento, antes de la sugerencia.
4. **[Medio] El segmento que más necesita el producto es el que más confía en la tarifa pública** (mediana 4 vs. 2). → Riesgo: el segmento Única puede aceptar sugerencias sin cuestionarlas. Ese riesgo hace más urgente verificar la creencia #1 con datos reales de ocupación.
5. **[Alto, instrumento] El cuestionario aplicado no puede tomar la decisión del 13-11.** Faltan G2, G3 y el tipo de aerolínea. → Antes de la encuesta real: usar el cuestionario del diseño, un link por canal y registrar cuántos mensajes se enviaron.

## 4. Preguntas "por qué" para entrevistas

- ¿Por qué la única persona de RM tarda 3 a 5 días en enterarse? ¿Frecuencia de revisión, cantidad de rutas, otras tareas?
- En analistas de equipo, ¿la fricción de "decisión" es analítica o es esperar la aprobación del jefe?
- ¿Por qué los analistas de equipo confían poco en la tarifa pública? ¿Qué hace la curva de reservas que la tarifa no hace?
- ¿Por qué la única persona de RM confía más en la tarifa pública? ¿Tiene con qué compararla?
- R25: ¿cómo es posible más de 2,5 h/día de recolección y enterarse el mismo día?

## 5. Pool de reclutamiento

17 de 24 aceptan una conversación. 12 dejaron contacto (ver el CSV; los contactos no se copian aquí). Etiquetas contra las creencias #6 (tiempo/demora), #4 (recolectar vs. decidir) y #1 (confiabilidad). **Primero los que contradicen.**

**Contradicen (prioridad):**

| ID | Nombre | Segmento | Contradice | Nota |
|---|---|---|---|---|
| R25 | Kevin Paz | Equipo | #4, #1, #6 (demora) | Respuestas inconsistentes; confirmar |
| R19 | Tomás Aguilar | Equipo | #6 (tiempo y demora), #1 | 30–60 min, se entera el mismo día |
| R01 | Lucía Mamani | Equipo | #6 (tiempo), #4, #1 | |
| R08 | Andrea Villca | Equipo | #6 (tiempo), #4, #1 | |
| R29 | M. Fernanda Solís | Equipo | #6 (tiempo), #4, #1 | Confirma la demora (3–5 días) |
| R30 | Pablo Rivero | Equipo (referido) | #4 | Prefiere la tarde |
| R26 | Gladys Quispe | Única | #1 | Confirma #6 y #4 |

**Confirman:**

| ID | Nombre | Segmento | Confirma |
|---|---|---|---|
| R06 | Hernán Ortiz | Única | #6, #4, #1 |
| R02 | Rosa Benitez | Única | #6, #4 (las dos), #1 |
| R15 | Carla Ibañez | Única | #6, #4 (las dos) |
| R09 | Mirtha Gauto | Única | #6 (se entera por síntoma) |
| R21 | Daniela Ferreira | Otro rol | #6 — fuera del perfil del diseño |

**Aceptan pero sin contacto:** R05, R10, R13, R16, R23, R27. No es posible contactarlos salvo que la herramienta guarde el correo.

## 6. Contraste con las creencias del overview

Como es un ensayo, **no se anota nada en `product/overview.md`.** Con datos reales, esto se propondría:

- **#6** — *weakened* para analistas de equipo (tiempo); prometedora en la conversación para la única persona de RM. No *confirmed*: n = 8 y el umbral de % de rutas no se midió.
- **#4** — *weakened* para analistas de equipo. Sin cambio para la única persona de RM.
- **#1** — sin cambio. Una percepción no verifica la correlación con la ocupación real.
- **#2, #3, #5, #7** — sin datos.

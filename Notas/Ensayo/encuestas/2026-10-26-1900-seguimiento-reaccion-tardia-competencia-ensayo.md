---
opportunity: 2026-10-02-2304-reaccion-tardia-competencia
status: ensayo
parent_survey: product/surveys/2026-10-25-2014-reaccion-tardia-competencia.md
parent_analysis: Notas/Ensayo/2026-10-26-1829-reaccion-tardia-competencia-ensayo.md
created: 2026-10-26
---

# Encuesta de seguimiento (ENSAYO): completar los vacíos de la primera ola

- **Objetivos de aprendizaje:**
  - **G0 — Segmento.** Confirmar que el respondente trabaja en una aerolínea low cost, ultra low cost o regional, y conocer país y flota. Decide si las 12 respuestas pertenecen al segmento objetivo y permite el corte por tamaño (≤10 vs. >10 aviones).
  - **G1 — Umbrales de tiempo y demora.** Leer los umbrales de la creencia #6 con los tramos del diseño: ≥1,5 h en el último día y ≥30% de rutas con ≥1 día de demora. Decide si la oportunidad tiene tamaño en el segmento "única persona de RM".
  - **G2 — Competidores por ruta.** Cuántos competidores relevantes compara por ruta. Decide el alcance de cobertura (creencia #5: 1 a 3 alcanzan).
  - **G3 — Gasto, evaluaciones previas y quién aprueba.** Decide el rango de precio y a quién se le vende (creencia #2). **Límite:** "quién aprueba" queda visto desde el analista.
- **Respondentes:** los 12 respondentes de la primera ola que aceptaron una conversación y dejaron contacto. No hay pantalla: ya pasaron S1, S3 y R1 en la primera ola. G0 reemplaza a S2.
- **Duración estimada:** 10 preguntas, ~3 min.
- **Límite:** las 12 personas aceptaron conversar. Pueden estar más involucradas con el tema que el resto. Leer los resultados como complemento de la primera ola, no como muestra nueva.

## Texto de invitación

> Hola {nombre}. Gracias por responder nuestra encuesta sobre cómo sigue a la competencia. Nos faltaron algunas preguntas. ¿Nos ayuda con 3 minutos más? {link}. Seguimos interesados en la conversación de 30 minutos: le escribimos aparte para coordinar.

## Preguntas

Q1. ¿Qué tipo de aerolínea es la suya? [opción única]
   - Low cost o ultra low cost
   - Regional
   - De red / full service con hub y conexiones
   - Otro
   > Goal: G0 (reemplaza a S2; "De red" u "Otro" saca la respuesta del segmento en el análisis)

Q2. ¿En qué país opera principalmente su aerolínea, y cuántos aviones tiene aproximadamente? [país: lista · flota: 1–5 · 6–10 · 11–20 · 21–50 · Más de 50]
   > Goal: G0 (corte por tamaño)

Q3. ¿Cuántas rutas tiene hoy a su cargo? [opción única]
   - 1–5 · 6–10 · 11–20 · 21–30 · Más de 30
   > Goal: G1 (denominador) y corte por carga de trabajo

Q4. Piense en su último día laboral completo. ¿Cuánto tiempo dedicó a **juntar y pasar a planilla** datos de competidores? (sin contar el tiempo de decidir ajustes) [opción única]
   - Nada · Menos de 30 min · 30 a 59 min · 1 h a menos de 1,5 h · 1,5 h a menos de 2 h · 2 h a 3 h · Más de 3 h
   > Goal: G1 (umbral ≥1,5 h). Tramos del diseño, que sí separan 1,5 h.

Q5. En una semana normal, ¿en qué proporción de sus rutas se entera de los cambios del competidor **al día siguiente o después**? [opción única]
   - Ninguna · Menos del 10% · 10% a 29% · 30% a 49% · 50% o más · No sé
   > Goal: G1 (umbral ≥30% de rutas). Leer junto a la demora típica de la primera ola.

Q6. En una ruta típica suya, ¿contra cuántos competidores directos compara sus tarifas y horarios? [opción única]
   - Ninguno · 1 · 2 · 3 · 4 o más
   > Goal: G2

Q7. De sus rutas, ¿en cuántas hay más de 3 competidores que usted considera relevantes? [opción única]
   - Ninguna · Menos de una cuarta parte · Entre una cuarta parte y la mitad · Más de la mitad · Todas · No sé
   > Goal: G2

Q8. Hoy, ¿su aerolínea gasta algo por mes para obtener datos de competidores (APIs, proxies, servicios de scraping, suscripciones de datos)? [opción única]
   - No gastamos nada · Menos de USD 100 · USD 100–500 · USD 501–2.000 · Más de USD 2.000 · No sé
   > Goal: G3 (gasto actual como ancla de precio)

Q9. En los últimos 2 años, ¿su aerolínea pidió una demo o cotización de alguna herramienta paga de datos de competidores o de pricing? [opción única]
   - Sí, y no se contrató → mostrar Q9b
   - Sí, se contrató y después se dejó de usar → mostrar Q9b
   - No
   - No sé
   > Goal: G3

Q9b. ¿Cuál fue el motivo principal? [opción única]
   - El precio
   - Requería integración o trabajo de TI
   - No cubría nuestras rutas o competidores
   - No quedó claro el valor frente a lo que ya hacíamos
   - El equipo no la usó
   - No sé
   - Otro (¿cuál?)
   > Goal: G3

Q10. La última vez que su área contrató un software o suscripción, ¿quién lo aprobó? [opción única]
   - Jefe/a o gerente de Revenue Management
   - Gerente o director/a comercial
   - Gerente general o CEO
   - Finanzas o compras
   - Nunca contratamos software para el área
   - No sé
   > Goal: G3

## Distribución

| Canal | A quién llega | Alcance aprox. | Link |
|---|---|---|---|
| Correo o LinkedIn directo a los contactos de la primera ola | Los 12 con contacto: 5 "única persona de RM" (R02, R06, R09, R15, R26), 6 "analista en equipo" (R01, R08, R19, R25, R29, R30) y 1 "otro rol" (R21). Sobrerrepresenta a los más involucrados (aceptaron conversar). | 12 | Un link por respondente: `?rid=R01` … `?rid=R30` (campo oculto), para unir la respuesta con la primera ola |

Los contactos están en `Notas/Ensayo/encuestas/respuestas_encuesta.csv`. No se copian aquí.

- **Meta de n:** 12 de 12. Con n = 5 en "única" y n = 6 en "equipo", todo es direccional. El valor está en unir estas respuestas con las de la primera ola, persona por persona.
- **Recordatorio:** un solo recordatorio a los 3 días hábiles.
- **Primera revisión:** 2026-11-03
- **Cierre:** 2026-11-06 (antes de la primera revisión de la ola principal)

## Pasos fuera de la encuesta (no requieren respondentes)

1. Revisar en la herramienta de la primera ola las etiquetas de la escala de confianza (Q7 del CSV).
2. Revisar si la herramienta guardó correo o perfil de R05, R10, R13, R16, R23 y R27 (aceptaron conversar sin dejar contacto).
3. Contar los mensajes de LinkedIn enviados en la primera ola, para calcular la tasa de respuesta.

---
opportunity: 2026-10-02-2304-reaccion-tardia-competencia
status: draft
created: 2026-10-25
---

# Encuesta: cómo siguen los analistas de RM de low cost a la competencia

- **Objetivos de aprendizaje:**
  - **G1 — Tiempo y demora.** Cuántas horas por día dedica el analista a recolectar y comparar a mano, y en qué proporción de rutas se entera de un cambio del competidor con ≥1 día de demora. Decide si la oportunidad tiene el tamaño suficiente para seguir (creencia `[opportunity] [value]`: ≥1,5 h/día y ≥30% de rutas con ≥1 día de demora). Fecha: 2026-11-13.
  - **G2 — Competidores por ruta.** Contra cuántos competidores relevantes compara por ruta. Decide el alcance de cobertura de cualquier solución (creencia #5: 1 a 3 alcanzan).
  - **G3 — Qué usan, cuánto gastan y quién aprueba.** Workaround actual, gasto actual en datos del competidor, evaluaciones previas de herramientas pagas y quién aprobó la última compra de software del área. Decide el rango de precio viable y a quién se le vende (creencia #2). **Límite:** lo responden analistas; "quién aprueba" queda visto desde abajo y hay que confirmarlo con jefes de RM y dirección comercial en entrevistas.
- **Fuera de alcance a propósito:** la creencia #4 (recolectar vs. decidir) queda entera para las entrevistas. La pregunta abierta Q11 puede dar pistas, pero no se usa como veredicto.
- **Respondentes:** analistas de Revenue Management (incluye a quien es el "área de RM" completa en una aerolínea chica) de aerolíneas low cost, ultra low cost o regionales, que comparan ellos mismos contra la competencia y cuya aerolínea no compra datos competitivos pagos. Personas: Mariana Quiroga, Diego Paredes, Carmen Aguirre. Quedan fuera jefes de RM (Rodrigo), dirección comercial (Patricia) y aerolíneas de red con datos pagos (Andrés).
- **Duración estimada:** 4 de pantalla + 11 preguntas + 3 de opt-in, ~5–6 min.

## Pantalla

S1. ¿Cuál describe mejor su rol actual? [opción única]
   - Analista de Revenue Management o Pricing
   - Soy la única persona a cargo de Revenue Management en mi aerolínea
   - Jefe/a o gerente de Revenue Management
   - Otro rol comercial (ventas, distribución, marketing)
   - Otro
   → descalifica si: Jefe/a o gerente de RM, Otro rol comercial, Otro

S2. ¿Qué tipo de aerolínea es la suya? [opción única]
   - Low cost o ultra low cost
   - Regional
   - De red / full service con hub y conexiones
   - Otro
   → descalifica si: De red / full service, Otro

S3. ¿Su aerolínea paga hoy datos de tarifas de competidores? (ej.: Infare, MIDT, AirGain) [opción única]
   - Sí
   - No
   - No sé
   → descalifica si: Sí

S4. En el último mes, ¿revisó usted mismo/a tarifas, horarios o frecuencias de algún competidor en sus rutas? [opción única]
   - Sí
   - No
   → descalifica si: No

## Preguntas

Q1. ¿Cuántas rutas tiene hoy a su cargo? [opción única]
   - 1–5 · 6–10 · 11–20 · 21–30 · Más de 30
   > Goal: G1 (denominador para la proporción de rutas con demora) y corte por carga de trabajo

Q2. En una ruta típica suya, ¿contra cuántos competidores directos compara sus tarifas y horarios? [opción única]
   - Ninguno · 1 · 2 · 3 · 4 o más
   > Goal: G2

Q3. De sus rutas, ¿en cuántas hay más de 3 competidores que usted considera relevantes? [opción única]
   - Ninguna · Menos de una cuarta parte · Entre una cuarta parte y la mitad · Más de la mitad · Todas · No sé
   > Goal: G2 (dónde no alcanzan 1 a 3 competidores)

Q4. ¿Cómo obtiene hoy los datos de los competidores? Marque todas las que use. [opción múltiple]
   - Entro a mano a la web del competidor
   - Entro a mano a OTAs o metabuscadores (Google Flights, Despegar, etc.)
   - Un script o scraper propio o del equipo
   - Me lo pasa otra persona u otra área
   - Lo muestra nuestro sistema de reservas o de RM
   - Otro (¿cuál?)
   > Goal: G3 (workaround actual, la línea base contra la que compite cualquier solución)

Q5. Piense en su último día laboral completo. ¿Cuánto tiempo dedicó a **juntar y pasar a planilla** datos de competidores? (sin contar el tiempo de decidir ajustes) [opción única]
   - Nada · Menos de 30 min · 30 a 59 min · 1 h a menos de 1,5 h · 1,5 h a menos de 2 h · 2 h a 3 h · Más de 3 h
   > Goal: G1 (umbral ≥1,5 h/día). Se pregunta por un día concreto, no por "un día típico", para bajar la sobreestimación.

Q6. Piense en el último cambio de un competidor (tarifa, horario o frecuencia) que lo llevó a ajustar algo en el inventario. ¿Cuánto tiempo pasó entre que el competidor hizo el cambio y que usted se enteró? [opción única]
   - El mismo día · 1 día · 2 a 3 días · Más de 3 días · No sé cuándo lo hizo el competidor
   > Goal: G1 (demora en un episodio concreto)

Q7. ¿Cómo se enteró de ese cambio? [opción única]
   - En mi revisión habitual de esa ruta
   - Me avisó un script o alerta automática
   - Me lo comentó un colega, mi jefe u otra área
   - Por un cliente, el call center o una agencia
   - Por una caída en las reservas de la ruta
   - Otro
   > Goal: G1 (cuánta detección hoy es por casualidad o por síntoma, y no por revisión)

Q8. En una semana normal, ¿en qué proporción de sus rutas se entera de los cambios del competidor **al día siguiente o después**? [opción única]
   - Ninguna · Menos del 10% · 10% a 29% · 30% a 49% · 50% o más · No sé
   > Goal: G1 (umbral ≥30% de rutas). Es una estimación: leerla junto a Q6, no sola.

Q9. Hoy, ¿su aerolínea gasta algo por mes para obtener datos de competidores (APIs, proxies, servicios de scraping, suscripciones de datos)? [opción única]
   - No gastamos nada · Menos de USD 100 · USD 100–500 · USD 501–2.000 · Más de USD 2.000 · No sé
   > Goal: G3 (gasto actual como ancla de precio, en lugar de preguntar "¿pagaría…?")

Q10. En los últimos 2 años, ¿su aerolínea pidió una demo o cotización de alguna herramienta paga de datos de competidores o de pricing? [opción única]
   - Sí, y no se contrató → mostrar Q10b
   - Sí, se contrató y después se dejó de usar → mostrar Q10b
   - No
   - No sé
   > Goal: G3 (evaluaciones previas y por qué se cayeron)

Q10b. ¿Cuál fue el motivo principal? [opción única]
   - El precio
   - Requería integración o trabajo de TI
   - No cubría nuestras rutas o competidores
   - No quedó claro el valor frente a lo que ya hacíamos
   - El equipo no la usó
   - No sé
   - Otro (¿cuál?)
   > Goal: G3

Q11. La última vez que su área contrató un software o suscripción, ¿quién lo aprobó? [opción única]
   - Jefe/a o gerente de Revenue Management
   - Gerente o director/a comercial
   - Gerente general o CEO
   - Finanzas o compras
   - Nunca contratamos software para el área
   - No sé
   > Goal: G3 (quién firma, a partir de una compra real; visto desde el analista)

Q12. ¿Qué es lo más difícil de seguir lo que hace la competencia en sus rutas? [abierta, opcional]
   > Goal: G1 (qué explica el tiempo y la demora) y priorización de entrevistas. No se usa como veredicto sobre la #4.

Q13. ¿En qué país opera principalmente su aerolínea, y cuántos aviones tiene aproximadamente? [país: lista · flota: 1–5 · 6–10 · 11–20 · 21–50 · Más de 50]
   > Goal: corte por segmento (aerolínea chica tipo Carmen/Diego vs. mediana tipo Mariana)

## Pantalla + opt-in (reclutamiento para entrevistas)

R1. En el último mes, ¿aplicó usted mismo/a un ajuste en el inventario a raíz de un cambio de un competidor? [Sí / No]
   → no es candidato si: No

R2. Estamos conversando con analistas de RM para entender mejor este trabajo. ¿Aceptaría una conversación de 30 minutos sobre esto? No es una venta. [Sí / No]

R3. Si respondió que sí, ¿cómo podemos contactarle? (correo o LinkedIn) [abierta, opcional, se muestra solo si R2 = Sí]

**Pantalla final (todos):** "Gracias. Si conoce a otro/a analista de RM de una low cost o regional, este link es para compartirle: {link de referidos}."

## Distribución

| Canal | A quién llega | Alcance aprox. | Link |
|---|---|---|---|
| LinkedIn, mensaje directo por cargo | Analistas de RM/pricing de low cost y regionales de LatAm buscados por cargo y empresa. Sobrerrepresenta a los más senior y activos en LinkedIn (perfil Mariana); subrepresenta a los que casi no lo usan o tienen el rol mezclado con otras tareas (perfiles Diego y Carmen). Tasa de respuesta en frío baja. | unknown | `?canal=linkedin` |
| Referidos de respondentes | Colegas de RM de quienes ya respondieron. Llega a analistas poco visibles en LinkedIn, pero sesga hacia la red de los primeros respondentes (misma aerolínea, mismo país). | unknown | `?canal=referido` |

- **Meta de n:** 30 analistas calificados en total (que pasan S1–S4). Los cortes por tamaño de flota (≤10 vs. >10 aviones, Q13) y por país van a quedar por debajo de 30 por segmento: se leen como direccionales.
- **Riesgo de alcance:** con el alcance de ambos canales en `unknown`, no se puede verificar antes de publicar que la meta sea alcanzable. Referencia: con ~10–15% de respuesta a mensajes en frío y una parte descalificada por S2–S3, 30 calificados piden del orden de **250–300 mensajes** de LinkedIn. Si se envían bastantes menos, la meta probablemente no se alcanza. Registrar cuántos mensajes se mandaron para calcular la tasa de respuesta.
- **Sesgo conjunto:** ninguno de los dos canales llega bien a quien no está en LinkedIn ni conoce a un respondente. Si el n se queda corto, el siguiente canal a sumar es la base de clientes de KIU (vía account managers), con su propio link y anotando que sobrerrepresenta a clientes satisfechos.
- **Primera revisión:** 2026-11-06
- **Cierre:** 2026-11-12 (deja el 13-11 para la decisión de tamaño de la agenda de research)

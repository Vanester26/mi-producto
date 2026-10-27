---
opportunity: reaccion-tardia-competencia
solutions: product/solutions/2026-10-26-2022-reaccion-tardia-competencia.md
status: ready
---

# Solution tests for: Reacción tardía a movimientos del competidor

## Why test
Están en test A1 `monitor-alertas` y A2 `sugeridor-ajustes`. La evidencia del dolor es solo `synthetic` y `secondary`. Nadie reaccionó a ninguna de las dos soluciones. Para A1, no sabemos si quitar la recolección quita la demora, o si la demora está en decidir (#4). Para A2, no sabemos si los datos públicos contienen la señal de ocupación sobre la que se basa cada sugerencia (#1).

## T1. monitor-alertas: alerta manual diaria a 5 analistas
- **Test status:** ready
- **Belief under test:** #4 `[product]` `[value]` "El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste. Si el analista ya sabe rápido qué mirar y lo difícil es la decisión, un producto que recolecta y sugiere resuelve el problema equivocado."
- **Risk:** [value]
- **Test type:** concierge
- **What we do:**
  1. Cada analista elige 3 a 5 rutas y 1 o 2 competidores por ruta.
  2. Durante 5 días hábiles, el equipo revisa a mano esas rutas cada mañana: tarifa más baja a D-7, D-14 y D-30, horario y frecuencia.
  3. Antes de las 9:00 (hora local del analista), el equipo envía por WhatsApp un mensaje con los cambios desde el día anterior. Si no hay cambios, el mensaje lo dice.
  4. El analista contesta cada cambio con una de tres opciones: "ajusté", "no toco" o "lo miro después". Si contesta "lo miro después", el equipo pregunta otra vez a las 18:00.
  5. Al final de cada día, el equipo pregunta: "¿Revisó hoy a mano alguna de estas rutas?" (sí/no).
  6. Si el analista es cliente de KIU, el equipo verifica la hora de cada ajuste en el log del inventario.
- **With whom:** 5 analistas reales de RM de low cost o regionales sin datos competitivos pagos, que aplican ajustes sin aprobación. Recruitment: opt-in de la encuesta (R1 = Sí, R2 = Sí). Si no alcanza, clientes de KIU a través de los account managers. Este canal tiende a traer clientes satisfechos y se registra por participante. Al menos 2 de los 5 tienen un perfil como el de Diego o Carmen (aerolínea de ≤10 aviones).
- **Material needed:** un mensaje de alerta en español: ruta, competidor, qué cambió (antes → ahora) y fecha de salida afectada, sin ninguna sugerencia. Una lista de rutas y competidores por analista. Una planilla de recolección para el equipo, con la hora de cada captura. Una capture sheet por cambio alertado: hora de envío, respuesta, hora de respuesta, tipo de decisión, verificación en log (si existe) y la respuesta diaria sobre la revisión manual. Queda fuera a propósito: cualquier sugerencia, gráfico, dashboard o explicación de "qué hacer".
- **Material:** [product/tests/materials/t1-monitor-alertas/](materials/t1-monitor-alertas/)
- **Duration:** 5 días hábiles de corrida, más 1 semana de reclutamiento. Ventana objetivo: 2026-11-16 a 2026-11-27, después del cierre de la encuesta.
- **Signal and threshold:**
  - S1: proporción de cambios alertados con una decisión ("ajusté" o "no toco") el mismo día. Umbral: ≥70%.
  - S2: analistas que contestan "no" a la revisión manual en ≥3 de los 5 días. Umbral: ≥3 de 5.
  - Mínimo para leer el test: ≥15 cambios alertados en total y ≥4 analistas que terminan la semana. Si no se llega, se agrega 1 semana. Si igual no se llega, el resultado es `inconclusive`.
- **Decision rule:**
  - continue: si S1 ≥70% y S2 ≥3 de 5.
  - change: si S1 ≥70% y S2 <3 de 5 (la alerta sirve, pero no reemplaza la revisión: hay que probar la confianza en el dato y la cobertura). También si S1 está entre 40% y 69% (la alerta ayuda en parte: probar A1 junto con un criterio de reacción, A3).
  - discard: si S1 <40%. El cuello de botella es decidir, no recolectar. #4 queda weakened y A2 gana peso.
- **Expected provenance:** real
- **Next step if it passes:** un monitor automático real con 5 a 10 analistas durante 3 a 4 semanas. Prueba #8 (`[feature: monitor-alertas] [value]`) y #9 (`[feasibility]`, owner tech).

## T2. sugeridor-ajustes: ¿lo público predice la ocupación? (clave = aerolínea propia)
- **Test status:** ready
- **Belief under test:** #1 `[product]` `[value]` "El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario."
- **Risk:** [value]. Se prueba con una señal técnica, porque la creencia es sobre la calidad de una predicción.
- **Test type:** technical-test
- **Owner:** tech / datos
- **What we do:**
  1. Con el permiso escrito de una aerolínea cliente de KIU (low cost o regional, ≥30 vuelos/día), capturar cada día desde el 2026-10-28 su tarifa pública más baja para la salida a D-14, por ruta y vuelo, desde su web. Registrar también el horario y la frecuencia semanal de la ruta.
  2. Cuando cada vuelo ya voló, tomar su ocupación real del inventario (clave de respuestas).
  3. Clasificar cada vuelo: ocupación alta (≥80%) o baja (<80%).
  4. Antes de ver la ocupación, fijar las variables y el método: tarifa a D-14 vs. la mediana de la ruta, día de la semana, horario y frecuencia. Método: regresión logística simple.
  5. Entrenar con el primer 70% de los vuelos (por fecha de salida). Medir con el último 30% (hold-out).
  6. Antes de capturar nada, tech verifica si el inventario guarda el historial de clases abiertas o de tarifas. Si lo guarda, se usan 3 a 6 meses de historia y no hace falta esperar.
- **With whom:** sin usuarios. Datos de 1 aerolínea cliente, con su permiso. Vuelos con salida entre 2026-11-11 y 2026-11-28 (≥500 vuelos, ≥150 en hold-out).
- **Material needed:** un script de captura diaria de la tarifa pública a D-14, con fecha, hora, ruta, vuelo, tarifa y marca tarifaria. La extracción de la ocupación real por vuelo desde el inventario. Un documento de método, fijado antes de ver los resultados, con las variables, el corte de 80%, el modelo y la partición 70/30. Una capture sheet con el resultado: n, clase mayoritaria, precisión del hold-out y matriz de confusión. Queda fuera a propósito: datos del competidor, interfaz, sugerencias y modelos complejos.
- **Material:** [product/tests/materials/t2-sugeridor-ajustes/](materials/t2-sugeridor-ajustes/)
- **Duration:** captura del 2026-10-28 al 2026-11-14, vuelos hasta el 2026-11-28, análisis hasta el 2026-12-04.
- **Signal and threshold:**
  - Precisión en el hold-out. Umbral: ≥70% y ≥10 puntos sobre la clase mayoritaria.
  - Mínimo para leer el test: ≥150 vuelos en hold-out, con ≥20% en cada clase. Si no se llega, el resultado es `inconclusive`.
- **Decision rule:**
  - continue: si la precisión es ≥70% y está ≥10 puntos sobre la clase mayoritaria.
  - change: si está entre 5 y 9 puntos sobre la clase mayoritaria. La señal es débil: A2 pasa a sugerir por reglas explícitas (A3 dentro de software), sin inferir la ocupación.
  - discard: si está <5 puntos sobre la clase mayoritaria. Lo público no predice ni la ocupación propia. Se descarta la inferencia de ocupación de A2 y #1 queda weakened.
- **Expected provenance:** real
- **Next step if it passes:** el mismo test sobre el competidor, con las estadísticas mensuales por ruta y aerolínea de las autoridades aeronáuticas (DGAC, Aerocivil) como clave. Después, un `prototype-shown` con sugerencias a 5 analistas para probar #10 (`[feature: sugeridor-ajustes] [value]`).

## Results

### T1. monitor-alertas — ensayo (`synthetic`)
- **Qué se observó:** 18 cambios alertados a 5 analistas durante 5 días hábiles (fechas de la planilla: 2026-11-16 a 2026-11-20). 16 de 18 cambios tuvieron una decisión el mismo día. 4 de 5 analistas contestaron "no" a la revisión manual en 3 días o más. Datos: [Resultados de la prueba de monitor-alertas (concierge)-ensayo.md](materials/t1-monitor-alertas/Resultados%20de%20la%20prueba%20de%20monitor-alertas%20(concierge)-ensayo.md).
- **Con quién y cuántos:** 5 analistas en la planilla: 4 `segment member` y 1 `stand-in` (Maria Urioste). Ella no aplica ajustes sin aprobación, entonces no es del segmento. Solo con los 4 del segmento: 16 cambios, S1 = 15/16 (94%), S2 = 4 de 4. El mínimo para leer el test se cumple.
- **Procedencia:** `synthetic`. La planilla dice que los datos son de práctica/ensayo. Las fechas de la corrida son posteriores a este análisis (2026-10-26).
- **Resultado:** `passed` como ensayo (S1 89% ≥ 70%; S2 4 de 5 ≥ 3 de 5). No es evidencia sobre el segmento y no mueve la creencia #4.
- **Decisión:** ninguna sobre A1. La corrida real queda pendiente (ventana 2026-11-16 a 2026-11-27).
- **Qué corregir antes de la corrida real:**
  1. **Filtro de entrada.** Una participante entró sin cumplir "aplica ajustes sin aprobación". Verificar los criterios del segmento antes de la semana de corrida.
  2. **Decisión diferida.** "1B, igualamos mañana" (Ignacio Soto, D2) se registró como "no toco", pero el texto dice que va a ajustar mañana. Definir en el guion cómo se registra una decisión diferida. Con esa fila como "sin decisión", S1 del segmento es 14/16 (88%). El resultado no cambia.
  3. **Efecto de la repregunta de las 18:00.** La repregunta produjo 2 de las 15 decisiones del mismo día del segmento. Un monitor automático no tiene esa repregunta. En la corrida real, registrar esta cifra aparte. Sin la repregunta, S1 del segmento es 13/16 (81%).
  4. **Etiqueta del archivo.** La planilla de ensayo usa nombres de aerolíneas reales. Marcar el archivo como ensayo (en el nombre o en un campo de procedencia), para no leerlo después como evidencia real.
- **Correcciones aplicadas (2026-10-26):** (1) `mensaje-reclutamiento.md`: los criterios del segmento se verifican antes de confirmar a la persona; un `stand-in` no cuenta para los 5 ni para el mínimo. (2) `guion-concierge.md` y `capture-sheet.md`: nuevo valor `diferida`, que cuenta como `sin decisión` para S1. (3) Nueva columna `por_repregunta` y nueva cifra "S1 sin repregunta"; el umbral no cambia. (4) El archivo de resultados tiene un aviso de procedencia `synthetic` (ensayo), y la capture sheet tiene un campo de procedencia del archivo. El archivo de resultados ya tiene `-ensayo` en el nombre.

### T2. sugeridor-ajustes — ensayo (`synthetic`)
- **Qué se observó:** según la planilla, 576 vuelos de Z8 (Paranair, regional, 32 vuelos/día, 5 rutas desde ASU), con salidas del 2026-11-11 al 2026-11-28. 29 excluidos, 383 en entrenamiento y 164 en hold-out. Precisión del modelo en hold-out: 74,4% (122/164). Clase alta en hold-out: 43,9%. Datos: [Resultados de la prueba de sugeridor-ajustes (technical-test)-ensayo.md](materials/t2-sugeridor-ajustes/Resultados%20de%20la%20prueba%20de%20sugeridor-ajustes%20(technical-test)-ensayo.md).
- **Con quién y cuántos:** sin usuarios. Datos atribuidos a 1 aerolínea cliente.
- **Procedencia:** `synthetic`. Las fechas de captura, extracción y fijación del método son posteriores a este análisis (2026-10-26). El SHA-256 registrado para `metodo.md` es el hash de un archivo vacío.
- **Resultado:** `inconclusive` como ensayo. Los números informados pasarían el umbral, pero el test no corrió según el diseño:
  1. El hold-out informado (164) es mayor que el máximo posible con el corte 2026-11-23 (5 días × 32 = 160).
  2. La precisión de referencia no sigue el método §8: con la matriz es 56,1%, no 57,3% (diferencia +18,3, no +17,1).
  3. Hay 8 vuelos excluidos "sin captura a D-14", pero el registro diario no muestra días ni filas perdidas.
  4. La planilla dice al mismo tiempo "historial: 3 meses" y "captura diaria", y la cantidad de vuelos solo coincide con la captura diaria.
- **Decisión:** ninguna sobre A2. No mueve la creencia #1.
- **Qué corregir antes de la corrida real:**
  1. **Fijar el método de verdad.** Calcular el SHA-256 de `metodo.md` el día que se fija (hoy: `edd0ae350fe204aa91c841e988f2ffd34766229e7389f4f6f0619cd5ae0b6b70`, versión con el período de historial) y registrarlo antes de la primera extracción.
  2. **Una sola fuente de datos.** Tech confirma si el inventario guarda el historial. Si lo guarda, se usan 3–6 meses de historia y el período se escribe en la capture sheet. Si no, se usa solo la captura diaria.
  3. **Verificar la partición.** `analisis.py` imprime la cantidad de vuelos por fecha de salida, y el hold-out coincide con la fecha de corte.
  4. **Referencia según el método.** La precisión de referencia es la proporción de la clase mayoritaria (de entrenamiento) en el hold-out.
  5. **Explicar cada exclusión** con el día y el vuelo.
  6. **Notas sin conclusiones fuera del test.** Un `passed` vale para la aerolínea propia. El paso siguiente es el test sobre el competidor, no la integración.
- **Correcciones aplicadas (2026-10-26):** (1) `capture-sheet.md`: instrucción para calcular el hash, aviso sobre el hash de archivo vacío y el hash de la versión actual de `metodo.md`. `metodo.md` no cambió. (2) Fuente de datos: marcar una sola, con el período si es historial. (3) `analisis.py` imprime los vuelos por fecha de salida y calcula `control_particion`; si el control falla, el resultado es `inconclusive`. (4) La capture sheet pide copiar la referencia de `resultado.json` y tiene un control con la matriz. El cálculo de `analisis.py` ya seguía el método §8. (5) `analisis.py` escribe `excluidos.csv` con fecha, vuelo y motivo de cada exclusión. (6) La capture sheet tiene la regla "sin conclusiones fuera del test". El archivo de resultados ya tiene `-ensayo` en el nombre. Fuente de datos: historial del inventario. El cliente confirmó el 2026-10-26 que guarda 12 meses de log diario por clase y nivel tarifario. Se usan 6 meses: salidas del 2026-04-26 al 2026-10-25. No hace falta la captura diaria. Nuevo documento `historial-tarifas.md`. `metodo.md` §2, `analisis.py` y `extraccion-ocupacion.md` tienen el nuevo período. Nuevo hash de `metodo.md`: `edd0ae350fe204aa91c841e988f2ffd34766229e7389f4f6f0619cd5ae0b6b70`.

## Decision

Sin decisión sobre A1 ni sobre A2 todavía. Las corridas de T1 y T2 fueron ensayos (`synthetic`). Sirven para corregir los tests, no para decidir. Los resultados no favorecen a ninguna de las dos alternativas. Las corridas reales están pendientes: T1 con analistas del segmento (2026-11-16 a 2026-11-27) y T2 con datos reales de la aerolínea cliente, con 6 meses de historial del inventario (salidas del 2026-04-26 al 2026-10-25). T2 no espera la captura diaria.

---
feature: sugeridor-ajustes
opportunity: reaccion-tardia-competencia
solutions: product/solutions/2026-10-26-2022-reaccion-tardia-competencia.md
tests: product/tests/2026-10-26-2038-reaccion-tardia-competencia.md
status: draft
---

# Asistente sugeridor de ajustes de inventario

## Problema

Cuando el competidor cambia una tarifa, un horario o una frecuencia, el analista de RM no sabe si el cambio importa ni cuánto mover. Por eso espera a una compañera o al jefe, o iguala a las apuradas. La espera cuesta ventas, y la igualación rápida puede costar yield. Cada analista usa un criterio distinto, y nadie puede explicar después por qué se ajustó una ruta. Por qué ahora: el segmento descartó las herramientas de mercado por precio, y las herramientas de decisión con IA (Fetcherr, Airnguru) se venden a aerolíneas medianas y grandes.

> Evidencia: "Lo que no sé es si cien bolivianos de diferencia en un vuelo del martes me tienen que preocupar o no. No tengo un criterio claro, entonces a veces reacciono a todo y a veces me paralizo y no hago nada." — Diego Paredes, product/interviews/2026-10-25-2248-diego-paredes.md (`synthetic`)

> Evidencia: "Cuando por fin ve un cambio del competidor, ajusta rápido y casi siempre iguala, porque no tiene tiempo para pensarlo. Sospecha que algunas de esas igualaciones le costaron yield sin ganar pasajeros." — Carmen Aguirre, product/personas/carmen-aguirre.md (`synthetic`)

> Evidencia: "No puede auditar por qué un analista ajustó una ruta: la justificación vive en la cabeza de cada uno." — Rodrigo Salinas, product/personas/rodrigo-salinas.md (`synthetic`)

Toda la evidencia del dolor es `synthetic` o `secondary`. No hay evidencia `real` todavía.

## Para quién

- **Diego Paredes** (principal) — analista novato en una low cost chica. Sabe ver el precio del competidor, pero no sabe decidir. Consulta cada ajuste grande y no puede justificar sus números.
- **Carmen Aguirre** (principal) — es toda el área de RM en una low cost startup. No tiene tiempo para pensar cada cambio y casi siempre iguala. Necesita la sugerencia en el celular.
- **Rodrigo Salinas** (secundario) — jefe de RM. Quiere un criterio igual en todo el equipo y quiere ver por qué se ajustó cada ruta.
- **Mariana Quiroga** marca un límite: ignora toda sugerencia sin el dato crudo y sin el porqué. Por eso la explicación y el dato crudo son obligatorios.

## Recorrido del usuario

Recorrido de Diego Paredes. Los pasos 1 y 2 vienen de su entrevista (`synthetic`). Los pasos 3 a 6 agregan el producto en el punto de dolor.

1. **Disparador** — El competidor baja la tarifa más barata de Santa Cruz–Sucre para el fin de semana. Hoy Diego lo ve por casualidad, un martes a la noche en el celular, y no sabe desde cuándo está así.
2. **Hoy: la espera** — Al otro día, Diego anota el cambio y le pregunta a su compañera si hay que reaccionar. Abren una clase más barata a media mañana del miércoles. Si ella no está, Diego espera al jefe, a veces todo el día.
3. **La alerta con la sugerencia** — Antes de las 9:00, Diego recibe la alerta del cambio. La alerta tiene una sugerencia concreta: "Abrir clase X para el sábado y el domingo, N asientos", o "No tocar".
4. **El porqué y el dato crudo** — Diego abre la sugerencia. Ve la razón en 2 o 3 frases, la tarifa del competidor (antes → ahora), la fecha de la captura, su propia tarifa y las clases que tiene abiertas.
5. **La decisión** — Diego elige: aplicar, no tocar, o cambiar la sugerencia con una razón escrita. Él aplica el ajuste en el sistema de inventario. El producto no aplica nada.
6. **Resultado** — Diego decide el mismo martes por la mañana, sin esperar a la compañera ni al jefe. En la reunión semanal, le muestra al jefe la sugerencia, el dato y su decisión. **Aquí llega el valor:** Diego tiene un criterio que puede explicar.

## Historias de usuario críticas

### Ver la sugerencia con el porqué y el dato crudo
Como Diego Paredes, quiero ver una sugerencia concreta con su razón y el dato que la produce, para decidir sin consultar a mi compañera y poder justificar el ajuste ante mi jefe.

Criterios de aceptación:
- [ ] Cada cambio alertado muestra una sola sugerencia: `abrir clase`, `cerrar clase` o `no tocar`.
- [ ] Si la sugerencia es abrir o cerrar una clase, muestra la clase, las fechas de salida y la cantidad de asientos.
- [ ] La sugerencia muestra la razón en 3 frases o menos, en español, y nombra los datos que usa.
- [ ] La sugerencia muestra el dato crudo: tarifa del competidor antes y ahora, fecha y hora de la captura, tarifa propia y clases abiertas.
- [ ] Caso de borde: si falta un dato (por ejemplo, la captura del competidor falló), el producto no da una sugerencia y dice qué dato falta.

Vínculo: creencia #4 (decidir es lo difícil) y frustración de Diego "no tengo un criterio claro" — product/interviews/2026-10-25-2248-diego-paredes.md

### Decidir y registrar la decisión
Como Diego Paredes, quiero registrar si apliqué, no toqué o cambié la sugerencia, para que mi decisión y su razón queden escritas.

Criterios de aceptación:
- [ ] Cada sugerencia tiene 3 opciones: `apliqué`, `no toco` y `cambié`.
- [ ] Si la sugerencia es `no tocar`, `apliqué` significa que el analista no cambió nada.
- [ ] La opción `cambié` no se puede guardar sin una razón escrita.
- [ ] El producto guarda la fecha y la hora de cada decisión.
- [ ] El producto no cambia nada en el sistema de inventario.
- [ ] Caso de borde: una sugerencia sin decisión al final del día queda como `sin decisión` y aparece otra vez a la mañana siguiente.

Vínculo: creencia #10 `[feature: sugeridor-ajustes] [value]` — product/solutions/2026-10-26-2022-reaccion-tardia-competencia.md

### Cubrir todas las rutas cuando queda solo
Como Diego Paredes, quiero recibir cada mañana las sugerencias de todas mis rutas monitoreadas, para no dejar rutas chicas sin mirar cuando mi compañera está de licencia.

Criterios de aceptación:
- [ ] Antes de las 9:00 (hora local), el producto envía la lista de cambios con sus sugerencias para todas las rutas monitoreadas.
- [ ] Las rutas sin cambios aparecen en la lista como `sin cambios`.
- [ ] Cada ruta muestra 1 a 3 competidores.
- [ ] Caso de borde: si la captura de una ruta falla, la lista lo dice el mismo día y nombra la ruta.

Vínculo: frustración de Diego (Trinidad sin mirar casi 3 días) — product/interviews/2026-10-25-2248-diego-paredes.md; creencia #6.

### Recibir la sugerencia en el celular
Como Carmen Aguirre, quiero recibir la sugerencia en el celular, sin instalar nada, para decidir entre reuniones y no igualar a las apuradas.

Criterios de aceptación:
- [ ] La alerta llega por un canal que Carmen ya usa en el celular (mensaje o correo).
- [ ] La sugerencia, la razón y el dato crudo se leen completos en la pantalla de un celular.
- [ ] Carmen no instala ninguna aplicación y no necesita a TI.
- [ ] Todo el texto está en español.

Vínculo: preferencias de dispositivo de Carmen — product/personas/carmen-aguirre.md

### Ver por qué se ajustó una ruta
Como Rodrigo Salinas, quiero ver el historial de sugerencias y decisiones de cada ruta, para revisar el criterio del equipo sin pedir una explicación a cada analista.

Criterios de aceptación:
- [ ] Para cada ruta, el historial muestra la fecha, la sugerencia, la decisión, la razón (si hay) y el analista.
- [ ] El historial se puede filtrar por ruta y por analista.
- [ ] El historial muestra la proporción de sugerencias aplicadas, no tocadas y cambiadas.
- [ ] Caso de borde: una sugerencia `sin decisión` aparece en el historial como `sin decisión`.

Vínculo: frustración de Rodrigo "no puede auditar por qué un analista ajustó una ruta" — product/personas/rodrigo-salinas.md

## Hipótesis

Creemos que los analistas de RM de low cost sin datos competitivos pagos, como Diego y Carmen, van a aplicar la sugerencia, o a cambiarla con una razón escrita, en la mayoría de los cambios alertados, y van a dejar de consultar a la compañera o al jefe antes de cada ajuste, porque la sugerencia les da un criterio que pueden explicar.

Nos equivocamos si, en 3 a 4 semanas con 5 analistas del segmento, menos del 50% de las sugerencias tienen la decisión `apliqué` o `cambié` con razón, o si los analistas vuelven a su planilla para decidir en 3 o más de 5 días hábiles.

## Alternativas consideradas

Explorado en: product/solutions/2026-10-26-2022-reaccion-tardia-competencia.md
- A1 `monitor-alertas` — en prueba en paralelo: esta feature usa su mecanismo de alertas y le agrega la sugerencia.
- A3 `criterio-reaccion` — parked: es weak en Viable como producto. Vuelve como lógica de la sugerencia (reglas explícitas) si #1 falla.
- A4 `planilla-mejorada` — discarded: no ataca la demora ni las rutas sin mirar.
- Vista semanal por mercado para Rodrigo y Patricia — parked: su usuario no sufre la demora. Vuelve si la viabilidad (#7) pide un resumen para quien firma.

## Probado antes del spec

Probado en: product/tests/2026-10-26-2038-reaccion-tardia-competencia.md
- T2 sugeridor-ajustes — inconclusive (synthetic, rehearsal) · #1. La corrida real está pendiente, con 6 meses de historial del inventario. Un `passed` vale solo para la ocupación de la aerolínea propia, no para la del competidor.
- T1 monitor-alertas — passed (synthetic, rehearsal) · #4. Es un ensayo y no es evidencia sobre el segmento.
- #10 (la adopción de la sugerencia) — not tested (declared). El paso siguiente de T2, si pasa, es un `prototype-shown` con 5 analistas.

Este spec se escribió antes de la corrida real de T2, por decisión de Vanessa Ballester (2026-10-26). Hay que revisar el spec cuando llegue el resultado real.

## Supuestos

Referencias a `product/overview.md` (registro único de creencias):
- [product] [value] #1 El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario.
- [product] [value] #4 El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste. (Esta feature apuesta a lo contrario: que decidir también es difícil.)
- [product] [value] #5 Comparar contra 1 a 3 competidores en rutas específicas alcanza para decidir el ajuste.
- [product] [viability] #2 Existe un precio al que este segmento sí compra este producto, y ese precio cubre el costo del dato.
- [feature: monitor-alertas] [feasibility] #9 Es posible obtener tarifa, horario y frecuencia de 1 a 3 competidores en 20 rutas de forma sostenida, por menos de USD 500/mes.
- [feature: sugeridor-ajustes] [value] #10 El analista aplica la sugerencia, o la cambia con una razón escrita, en ≥50% de los casos, y no vuelve a su planilla.
- [feature: sugeridor-ajustes] [feasibility] #11 Para un cliente de KIU, el producto puede leer las clases abiertas y la disponibilidad propia del inventario sin un proyecto de integración de TI de la aerolínea.
- [feature: sugeridor-ajustes] [usability] #12 Un analista novato como Diego entiende la razón de la sugerencia y la puede explicar a su jefe sin ayuda.

---
opportunity: reaccion-tardia-competencia
status: testing-several
chosen: monitor-alertas, sugeridor-ajustes
tests:
---

# Solutions for: Reacción tardía a movimientos del competidor

## What the evidence says now
- Ninguna creencia se movió. No hay evidencia `real` ni `survey`. La encuesta (product/surveys/2026-10-25-2014-reaccion-tardia-competencia.md) está en borrador y cierra el 2026-11-12.
- La creencia #6 `[opportunity] [value]` (tiempo y demora) está abierta, no contradicha.
- La creencia #4 (recolectar vs. decidir) está en conflicto. El research secundario y la entrevista sintética con Diego indican que lo difícil es decidir. La persona Mariana indica que lo difícil es recolectar. Todo es `secondary` o `synthetic`.
- La creencia #1 (lo público predice la ocupación) tiene incertidumbre alta. No hay validación pública, y Diego y Mariana no confían en esa relación (`synthetic`).

## Baseline: what people do today
Los analistas copian a mano tarifas y horarios desde la web del competidor y las OTAs, a una planilla, a menudo desde el celular fuera de horario. Diego y Carmen usan un checklist heredado, sin horarios ni frecuencias. Mariana tiene un scraper en Python que se rompe sin aviso. Fuentes: product/personas/{mariana-quiroga, diego-paredes, carmen-aguirre}.md y product/interviews/2026-10-25-2248-diego-paredes.md, `synthetic`. La pregunta Q4 de la encuesta verifica esta línea base.

## Alternatives
### A1. Monitor con alertas de cambios (`monitor-alertas`)
Recolecta tarifa, horario y frecuencia de 1 a 3 competidores por ruta. Envía una alerta (celular o correo) cuando algo cambia. No sugiere ningún ajuste. Ataca la recolección y la demora. Para Mariana Quiroga, Carmen Aguirre y Diego Paredes (primary). Reemplaza la copia manual y el scraper casero.

### A2. Sugeridor de ajustes de inventario (`sugeridor-ajustes`)
Es A1 más una sugerencia concreta de ajuste por clase, con su explicación y el dato crudo visibles. Ataca la decisión. Para Diego Paredes y Carmen Aguirre (primary), y para Rodrigo Salinas (secondary), que quiere un criterio consistente en el equipo. Reemplaza la intuición y la práctica de copiar lo que hace la compañera.

### A3. Criterio de reacción escrito (`criterio-reaccion`)
Una guía por tipo de ruta: cuándo igualar, cuándo no tocar nada, cuántos asientos mover. Incluye un checklist nuevo con horarios y frecuencias. No es software. Ataca la decisión con un proceso. Para Diego, Carmen y Rodrigo. Reemplaza el checklist heredado.

### A4. Planilla mejorada (`planilla-mejorada`)
Una plantilla con links directos por ruta y fecha, comparación automática y control de tipeo. Hace menos doloroso el workaround actual. Para Diego y Carmen. Reemplaza la planilla heredada.

## Comparison
| Alternative          | Desirable                                                                                                                                                                              | Feasible                                                                                                                                                                                     | Viable                                                                                                                           | Riskiest belief                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| A1 monitor-alertas   | mixed: Mariana y Carmen pierden horas y días recolectando (synthetic, personas). Diego dice que recolectar no es lo difícil (synthetic, entrevista). pain evidenced, relief not tested | to check with tech. El dato crudo cuesta cientos de USD/mes, pero hay anti-bot, riesgo legal y vías que cierran (secondary, product/research/2026-10-03-0011-reaccion-tardia-competencia.md) | mixed: AirGain vende un monitor modular por ruta a low cost. Precio desconocido (secondary)                                      | #4 [product] [value]                                                                                                     |
| A2 sugeridor-ajustes | mixed: Diego y Carmen quieren un criterio (synthetic). Mariana ignora las sugerencias de caja negra (synthetic). pain evidenced, relief not tested                                     | to check with tech. La integración con inventario choca con la restricción "sin proyecto de TI" (brief)                                                                                      | mixed: el hueco "recomendación + aerolínea chica" parece vacío, pero Airnguru y Fetcherr ya venden decisión en LatAm (secondary) | #1 [product] [value]                                                                                                     |
| A3 criterio-reaccion | mixed: Diego y Carmen quieren saber cuándo igualar y cuándo no. Rodrigo quiere un criterio consistente (synthetic)                                                                     | mixed (assumption): alguien con experiencia real en RM tiene que escribirlo                                                                                                                  | weak (assumption): una guía no da ingreso por suscripción                                                                        | Los analistas aplican una guía escrita en la mayoría de los cambios que ven, en lugar de igualar o esperar por intuición |
| A4 planilla-mejorada | weak: reduce los errores de tipeo, pero no cubre las rutas que nadie mira durante días (synthetic)                                                                                     | strong (assumption): no usa datos externos                                                                                                                                                   | weak (assumption)                                                                                                                | La mayor parte del tiempo se pierde en copiar, no en buscar el dato                                                      |

## Decision
Vanessa Ballester eligió para probar A1 y A2 en paralelo (2026-10-26). Coincide con la recomendación. Las dos se separan en la creencia #4, y son las únicas con un camino de ingreso. No hay entrada en corrections.md.

## To test
- A1 — #4 "El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste.": si lo difícil es decidir, una alerta solo hace que el analista iguale más rápido, o que se paralice antes. Se diseña en /design-solution-tests.
- A2 — #1 "El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario.": si la relación es débil, cada sugerencia es ruido, y Mariana deja la herramienta. Se diseña en /design-solution-tests.

## Value proposition: monitor-alertas
- Pain relieved: 2 a 2,5 h por mañana de copia manual (Mariana). Rutas sin mirar durante 3 o 4 días (Diego, Carmen). Un scraper que falla sin aviso. Todo `synthetic`.
- Gain created: el analista se entera el mismo día de los cambios de tarifa, horario y frecuencia en todas sus rutas, también cuando queda solo.
- Replaces: la planilla manual, el checklist heredado y el scraper casero. Razón para cambiar: no se rompe sin aviso, avisa también los cambios de horario y frecuencia, y no requiere programar.
- Deliberately does not: sugerir ajustes, conectarse al sistema de inventario, cubrir más de 3 competidores por ruta, ni dar una vista agregada para la dirección.

## Value proposition: sugeridor-ajustes
- Pain relieved: no saber si una diferencia de precio importa ni cuánto mover (Diego). Igualar a las apuradas y perder yield (Carmen). Criterios distintos en cada analista (Rodrigo). Todo `synthetic`.
- Gain created: una sugerencia concreta (abrir o cerrar clase, cuántos asientos, o "no tocar") con el porqué y el dato crudo visibles, para justificarla frente al jefe.
- Replaces: copiar lo que hace la compañera, reaccionar a todo o a nada, y la consulta al jefe que tarda un día.
- Deliberately does not: aplicar el ajuste en forma automática, ser una caja negra sin el dato crudo, ni pedir un proyecto de integración de TI.

## Beliefs
- [opportunity: reaccion-tardia-competencia] [value] Los analistas de RM de low cost sin datos competitivos pagos dedican ≥1,5 h/día a recolectar y comparar a mano, y en ≥30% de sus rutas reaccionan a un cambio del competidor con ≥1 día de demora. (#6, referenciada)
- [product] [value] #4 El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste. (referenciada)
- [product] [value] #1 El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario. (referenciada)
- [feature: monitor-alertas] [value] Con alertas de cambios, el analista se entera el mismo día de ≥80% de los cambios del competidor en sus rutas monitoreadas, y deja de revisar a mano esas rutas. (registrada, #8)
- [feature: monitor-alertas] [feasibility] Es posible obtener tarifa, horario y frecuencia de 1 a 3 competidores en 20 rutas de forma sostenida, por menos de USD 500/mes, y detectar una falla de captura en menos de 24 h. (registrada, #9)
- [feature: sugeridor-ajustes] [value] El analista aplica la sugerencia, o la cambia con una razón escrita, en ≥50% de los casos, y no vuelve a su planilla. (registrada, #10)

## Discarded or parked
- A3 criterio-reaccion — parked: es weak en Viable como producto comercial. Vuelve como lógica de A2 si #1 falla: un sugeridor por reglas sin inferir la ocupación.
- A4 planilla-mejorada — discarded: no ataca la demora ni las rutas sin mirar, que son el centro de la oportunidad. Solo reduce los errores de tipeo.
- Vista semanal por mercado para Rodrigo y Patricia — parked: su usuario es otro (secondary y tertiary), no el que sufre la demora. Vuelve si la viabilidad (#7) pide un resumen para quien firma.

## Outcome

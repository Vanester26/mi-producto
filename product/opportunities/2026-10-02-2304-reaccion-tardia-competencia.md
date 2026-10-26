---
status: framed
segment: Equipos de Revenue Management de aerolíneas low cost que compiten rutas contra 1 a 3 competidores y no compran datos competitivos pagos (MIDT, QL2, Infare) — analistas que hacen la comparación a mano y el jefe de RM que prioriza mercados
personas: mariana-quiroga, diego-paredes, rodrigo-salinas, patricia-ocampo, andres-villaverde
---

# Opportunity: Reacción tardía a movimientos del competidor

Los analistas de RM de low cost sin datos competitivos pagos reaccionan con uno a tres días de demora a los cambios de tarifa, horario y frecuencia del competidor, porque recolectar y comparar a mano les consume horas por día y no alcanza para cubrir todas las rutas. Por qué ahora: el segmento ya evaluó y descartó las herramientas de mercado por precio, y sigue sin visibilidad competitiva estructurada.

## Segment and personas

- Mariana Quiroga (primary) — lo sufre: pierde 2–2,5 h cada mañana copiando tarifas y horarios de dos competidores; su scraper se rompe sin aviso y vuelve a lo manual.
- Diego Paredes (primary) — lo sufre: cuando queda solo, las rutas chicas quedan sin mirar hasta 3 días; errores de tipeo al copiar tarifas a mano.
- Rodrigo Salinas (secondary) — sufre la consecuencia: se entera 2–3 días tarde de cambios de frecuencia en rutas clave; no puede auditar por qué se ajustó una ruta.
- Patricia Ocampo (tertiary) — no lo sufre: no usa el inventario ni el producto. Responde la creencia de viabilidad: firma el presupuesto y exige retorno en el año.
- Andrés Villaverde (negative) — no lo sufre: ya lo resolvió con Infare, QL2 y MIDT. Marca el límite de alcance (cobertura de mercado completa, O&D de red).
- Missing: ninguna.

## Signals

| Signal | Provenance | Source |
|---|---|---|
| El analista pierde 2–2,5 h/día recolectando tarifas y horarios de 2 competidores, ruta por ruta | synthetic | product/personas/mariana-quiroga.md |
| Scraper casero que se rompe cuando el competidor cambia su web; falla sin aviso | synthetic | product/personas/mariana-quiroga.md |
| Rutas chicas sin revisar hasta 3 días cuando el equipo queda reducido | synthetic | product/personas/diego-paredes.md |
| Errores de tipeo al copiar tarifas a mano llevaron a bajar una tarifa sin necesidad | synthetic | product/personas/diego-paredes.md |
| El jefe de RM se entera 2–3 días tarde de un aumento de frecuencia del competidor | synthetic | product/personas/rodrigo-salinas.md |
| El segmento evaluó MIDT/QL2/Infare y los descartó por costo | unverified | product/overview.md (sin fuente nombrada) |
| La comparación hoy se hace a mano, todos los días, ruta por ruta | unverified | product/overview.md (sin fuente nombrada) |
| Hoy el tiempo de reacción es de días/horas | unverified | Input de la oportunidad (sin fuente nombrada) |

Todas las señales son `synthetic` o `unverified`: no hay evidencia `real`, `survey` ni `secondary` todavía.

## Business outcome

Revenue nuevo (modo commercial): ingreso por suscripción de aerolíneas low cost que hoy no compran datos competitivos porque MIDT, QL2 e Infare están fuera de su presupuesto.

## Constraints

- La aerolínea no puede asumir un proyecto de integración de TI (meses de TI, seguridad y compras). Si la solución se conecta o no al sistema de inventario sigue siendo una decisión de solución abierta, no un hecho.
- El costo para la aerolínea tiene que quedar por debajo del umbral que hizo descartar a Infare (referencia de Patricia: "más que un analista al año") — ver creencia #2 del overview.
- Fecha de decisión sobre esta oportunidad: 2026-12-15.

## Beliefs

Referencias a `product/overview.md` (registro único de creencias):

- [opportunity: reaccion-tardia-competencia] [value] Los analistas de RM de low cost sin datos competitivos pagos dedican ≥1,5 h/día a recolectar y comparar a mano, y en ≥30% de sus rutas reaccionan a un cambio del competidor con ≥1 día de demora.
- [opportunity: reaccion-tardia-competencia] [viability] El jefe de RM o la dirección comercial pueden atribuir pérdida de ingreso a episodios concretos de reacción tardía en el último trimestre, y la estiman por encima del costo anual de un analista.

Creencias ya registradas que esta oportunidad toca:

- #4 [product] [value] — el dolor principal es el tiempo de recolectar y comparar, no decidir el ajuste. Es la condición de borde de esta oportunidad: si cae, el problema es otro.
- #2 [product] [viability] — existe un precio que el segmento paga y que cubre el costo de obtener el dato del competidor; quién firma.
- #5 [product] [value] — 1 a 3 competidores por ruta alcanzan para decidir.
- #1 [product] [value] — la tarifa/horario/frecuencia pública predice la ocupación real. Afecta a cualquier solución que *sugiera* ajustes, no al problema.

## Research agenda

| Belief | Instrument | Decision it unlocks | By when |
|---|---|---|---|
| [value] tiempo y demora de reacción | 1) Datos propios, si existen: logs de ajustes del sistema de inventario cruzados con fechas de cambios públicos del competidor. 2) Encuesta a analistas de RM de low cost (horas/día, rutas cubiertas, demora típica), con bloque de opt-in. | Si la oportunidad tiene el tamaño suficiente para seguir | 2026-11-13 |
| #4 recolectar vs. decidir | Entrevistas a analistas reclutados entre los opt-in de la encuesta, priorizando respuestas que contradigan la #4 | Si el problema a atacar es la recolección, la decisión o ambas — cambia por completo el set de soluciones | 2026-12-11 |
| [viability] pérdida atribuible | Secondary (casos públicos, benchmarks de yield en low cost) + entrevistas a jefes de RM y dirección comercial pidiendo episodios concretos del último trimestre | Si hay un caso de retorno que la dirección comercial firme | 2026-12-11 |
| #2 precio / quién firma | Secondary (pricing de MIDT/QL2/Infare y alternativas) + preguntas de disposición a pagar en la encuesta | Rango de precio viable y comprador (jefe de RM vs. dirección comercial) | 2026-11-13 |
| #5 1–3 competidores alcanzan | Encuesta (cuántos competidores relevantes por ruta) + entrevistas | Alcance de cobertura de cualquier solución | 2026-12-11 |

Decisión final (perseguir / descartar / reformular): 2026-12-15.

## Candidate ideas (not evaluated)

- Monitoreo automatizado de tarifa, horario y frecuencia del competidor (del input original).
- Sugerencia de ajuste concreto de control tarifario en el lenguaje del analista (del input original; depende de la creencia #1).
- Línea base a comparar: el workaround actual — planilla manual + scraper casero (Mariana).

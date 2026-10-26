---
source: secondary
method: web
date: 2026-10-03
question: ¿Qué cobra el mercado de inteligencia competitiva aérea y quién compra? ¿Existe ya un producto barato de monitoreo por ruta para low cost chicas? ¿Hay evidencia pública de pérdida de ingreso por reaccionar tarde? ¿Cómo monitorea hoy el segmento y cuánto cuesta obtener el dato?
opportunity: 2026-10-02-2304-reaccion-tardia-competencia
---

# Research: inteligencia competitiva para RM de low cost (oportunidad "reacción tardía a la competencia")

Hay tres hallazgos que cambian decisiones:

1. **El hueco "barato + aerolínea chica + recomendación" parece vacío en lo público, pero hay jugadores cerca.** RateGain AirGain ya vende un monitor de tarifas modular por ruta y competidor, con implementación en 2–4 semanas, a low cost como IndiGo, Nok Air, VietJet y Volotea. Airnguru, de Chile, ya vende pricing a Arajet y SKY. Fetcherr está en Viva Aerobus y Azul. Ninguno publica precios. Del lado enterprise, OAG absorbió Infare (2023), que antes había comprado el negocio aéreo de QL2 (2017). "MIDT/QL2/Infare" ya no son tres proveedores: son dos (OAG y los GDS).
2. **El dato crudo es barato; lo caro es sostenerlo.** Monitorear 20 rutas × 3 competidores × 60 días cuesta del orden de **cientos de USD/mes** en APIs o proxies públicos. Lo caro y frágil es otra cosa: el anti-bot, los cambios de las webs, el riesgo legal (Ryanair vs Booking, Southwest vs Kiwi) y que las vías baratas se están cerrando (Amadeus Self-Service se dio de baja en jul-2026 y Kiwi Tequila pasó a solo por invitación). La creencia #2 (precio viable que cubra el costo del dato) sale bien parada en costo de datos. No dice nada sobre disposición a pagar.
3. **La evidencia independiente no respalda que "reaccionar más rápido" genere ingreso.** Ni siquiera las aerolíneas grandes responden en tiempo real al rival (NBER). Un experimento de campo muestra que *no* igualar subió el yield. Las simulaciones del MIT muestran que igualar mecánicamente destruye ingreso. Lo que la literatura valora es **decidir a qué movimiento reaccionar**, no la velocidad de recolección. **Ojo con el segmento:** esa literatura es de legacy de EE.UU. con datos competitivos pagos, en condiciones muy distintas a las de un analista de low cost en Santa Cruz o Lima. Por eso no la uso para dar veredicto sobre las creencias de la oportunidad. Queda como hipótesis de riesgo para las entrevistas.

> Límite: todo esto es evidencia sobre el **mercado**. No verifica nada sobre lo que hacen o sienten los analistas de RM del segmento. Eso sigue siendo research primario.

---

## Lane 1 — Pricing y modelos de negocio

| Proveedor | Para quién | Modelo | Precio | Fuente |
|---|---|---|---|---|
| OAG (incluye Infare y QL2 aéreo), Airfare Data/Analytics | Pricing, estrategia y RM de aerolíneas; aeropuertos | Plataforma, Snowflake o feed al RM | Desconocido / no público | [verificado: https://www.oag.com/airfare-data — 2026-10-03]; compra de Infare 28-07-2023 [verificado: https://www.oag.com/pressroom/oag-acquires-infare-and-receives-new-investment-from-vitruvian-partners — 2026-10-03]; Infare compra QL2 aéreo 2017 [verificado: https://www.traveldailynews.com/post/infare-acquires-ql2-softwares-airlines-business — 2026-10-03] |
| OAG Schedules Analyser | Red y capacidad de competidores | Suscripción anual con renovación automática y aumento en cada aniversario | Desconocido | [verificado: https://www.oag.com/terms-for-online-sales-subscriptions-and-services — 2026-10-03] |
| Cirium SRS Analyser / Diio Mi | Aerolíneas, aeropuertos | Suscripción anual; tarifas y tráfico como add-on | No público. **Referencia en aeropuerto:** Diio Mi para Savannah, USD 34.073/año (ago-2025) | [verificado: https://agenda.savannahga.gov/publishing/august-14-2025-city-council-regular-meeting/1520_11558.html — 2026-10-03] |
| ATPCO Assembled Data | Aerolíneas, tech providers | Tarifas archivadas por O&D, hasta 3 años de historia | Desconocido | [verificado: https://atpco.net/assembled-data/ — 2026-10-03]. Muchas low cost no archivan en ATPCO [conocimiento del modelo — verificar] |
| MIDT (Sabre / Amadeus) | Aerolíneas | Licencia enterprise | Desconocido. Ve poco a las low cost que venden por canal directo | [conocimiento del modelo — verificar] |
| RateGain AirGain | Aerolíneas, incluidas low cost | "Flexible subscription. Adjust routes, competitors, channels…" | No público | [verificado: https://airgain.ai/ — 2026-10-03] |
| Airnguru / Fetcherr / FLYR / PROS / Sabre Air Price IQ | Pricing y RM con IA | SaaS + implementación | No público en ninguna fuente | Ver Lane 2 |
| SerpApi (Google Flights) | Desarrolladores | Plan mensual por búsquedas | Free 250 · USD 25/1.000 · 75/5.000 · 150/15.000 · 275/30.000 · Enterprise | [verificado: https://serpapi.com/pricing — 2026-10-03] |
| FlightAPI | Desarrolladores | Plan mensual | USD 49 / 99 / 199 por mes | [verificado: https://www.flightapi.io/ — 2026-10-03] |
| Duffel | Vendedores de viajes | Por orden + búsquedas | USD 3/orden + 1%; USD 0,005/búsqueda por encima de 1.500 búsquedas por reserva | [verificado: https://duffel.com/pricing — 2026-10-03] |
| Amadeus Self-Service | — | **Cerrado** desde el 17-07-2026; queda solo Enterprise | — | [verificado: https://www.phocuswire.com/amadeus-shut-down-self-service-apis-portal-developers — 2026-10-03] |
| Kiwi Tequila | — | Solo por invitación desde may-2024 | — | [verificado: https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/ — 2026-10-03] |

**Comprador.**
- Las fuentes nombran como usuarios a analistas y gerentes de RM y a equipos comerciales de tarifas [verificado: https://www.altexsoft.com/blog/airline-revenue-management-software/ — 2026-10-03]. Ninguna fuente pública dice quién *firma* en una aerolínea chica.
- La hipótesis de que el Head of RM aprueba bajo cierto umbral y el CCO o CFO por encima es [conocimiento del modelo — verificar].
- Las comparativas del sector recomiendan evaluar el costo total "incluidos los analistas internos" [verificado: https://mize.tech/blog/top-ai-powered-fare-optimization-tools-for-airlines-compared/ — 2026-10-03]. Eso es consistente con el ancla de Patricia ("más que un analista al año").

**Hueco de precio.** Los únicos precios públicos están en dos extremos:
- APIs para desarrolladores: USD 25–275/mes.
- Suites analíticas: ~USD 30–35k/año, pero el dato es de aeropuerto, no de aerolínea.

No hay ningún precio público en el medio. El precio real que ofrecen OAG y AirGain a una aerolínea de menos de 20 aviones es **desconocido**.

## Lane 2 — Competidores directos y posicionamiento

| Proveedor | Tarifa / Horario / Frecuencia | ¿Sugiere ajuste? | Clientes low cost / LatAm | Qué prueba / qué no prueba |
|---|---|---|---|---|
| **RateGain AirGain** | Tarifa sí. Horario: **no confirmado** en la web (el subagente lo afirmó; la verificación directa no lo encontró) / frecuencia desconocida | No: monitorea y alerta | IndiGo, Air India Express, SpiceJet, Nok Air, VietJet, Volotea, Sky Express, Neos, BermudAir. Sin clientes en LatAm [verificado: https://airgain.ai/ — 2026-10-03] | **El competidor más cercano.** Prueba que las low cost pagan por un monitor modular por ruta y que se implementa en semanas. No prueba precio ni presencia en LatAm |
| **Airnguru** (Chile) | Desconocido (no confirmé monitoreo de competidores) | Sí: automatización y optimización de ofertas | Arajet (2026), SKY Airline (2023), Aeroméxico (2024); 14 clientes [verificado: https://www.airnguru.com/post/arajet-selects-airnguru-for-production-deployment-of-its-offer-optimization-suite — 2026-10-03; https://www.globenewswire.com/news-release/2023/08/01/2715987/0/en/Airnguru-and-Piano-Launch-Bundle-and-Ancillaries-Price-Optimization-Engine-with-SKY-Airline.html — 2026-10-03] | Prueba que low cost del segmento ya compran pricing a un proveedor regional. Es la amenaza más directa en LatAm |
| **Fetcherr** | Usa datos de terceros (Infare y OAG como partners) | Sí, ejecuta en automático | Viva Aerobus, Azul, Delta, WestJet, Virgin Atlantic [verificado: https://www.fetcherr.io/product — 2026-10-03] | Prueba apetito por automatizar en low cost grandes de LatAm. Es un reemplazo del RM, no un monitor |
| **OAG Airfare Analytics** | Solo tarifa | No: analiza y alerta | No nombra | Su propio blog dice que el benchmark de tarifa "ya no describe el mercado" [verificado: https://www.oag.com/blog/competitive-fare-intelligence — 2026-10-03] |
| **airRM (Accelya)** | No menciona monitoreo de competencia | Sí (es un RM) | JetSMART, VivaColombia (2018) [verificado: https://www.globenewswire.com/news-release/2018/01/30/1314272/0/en/JetSmart-and-VivaColombia-Select-airRM-as-their-Revenue-Management-System.html — 2026-10-03] | Las low cost de LatAm ya tienen RM: el producto tiene que convivir con él |
| **Farel** (YC) | Sin monitoreo de competidores | RM por reglas | Aerolíneas startup chicas; incluido en un fee por pasajero [verificado: https://farel.io/platform/revenue-management/ — 2026-10-03] | Prueba que existe un modelo de precio accesible para aerolíneas chicas, pero sin la competencia |
| **FLYR / PROS / Sabre Air Price IQ** | Desconocido | Sí | FLYR: Cyprus Airways. Sabre: LATAM, Aeroméxico | Enterprise o legacy |
| **DataCrops / FlightAPI** | Dato crudo de tarifa y horario | No (DataCrops solo alerta) | — | El dato es barato; convertirlo en decisión no lo es |
| **KIU Systems** | El blog público de SKY menciona "Kiu Admin" para control de revenue; no se ve un módulo competitivo [verificado: https://www.kiusys.com/en/blog/sky-airline-modernizes-revenue-management-with-kiu/ — 2026-10-03] | No se menciona | SKY Airline | Canal natural. **Conviene verificarlo internamente:** puede existir algo que no es público |

**Mapa de posicionamiento** (ejes: dato ↔ recomendación/automatización; enterprise ↔ chica/accesible):

- **Lleno: automatización con IA para medianas y grandes.** Fetcherr, FLYR, PROS, Sabre y Airnguru, que ya bajaron a low cost de LatAm. Una "sugerencia de ajuste" compite acá contra un relato de autopiloto.
- **Lleno: datos de tarifas.** OAG-Infare y AirGain. AirGain es el más parecido en forma (modular por ruta), pero entrega datos, no decisiones.
- **Vacío aparente: recomendación + aerolínea chica + precio accesible + tarifa, horario y frecuencia juntos.** No sabemos si está vacío porque no hay oferta o porque no hay quien pague. Las alternativas que lo llenarían son el scraper propio, el RM que ya tienen y planes chicos no publicados de los grandes.

## Lane 3 — Alternativas y no-consumo

- **Las ofertas de empleo confirman que la tarea existe, no cuánto cuesta.**
  - Arajet (ago-2026) pide "Monitor fares, availability, and competitive actions", con Excel, SQL y Python/R, sin nombrar herramientas pagas [verificado: https://freehire.me/jobs/revenue-management-data-analyst-arajet-r7zdt2aj — 2026-10-03].
  - JetSMART (jun-2026) habla de "gestión táctica de las rutas asignadas", con Excel y Power BI [verificado: https://mercadolaboral.udd.cl/trabajar-en-jetsmart-airlines-spa1/trabajos/analista-revenue-management/905435 — 2026-10-03].
  - Las ofertas muestran un perfil capaz de armar un scraper. **No dicen cuántas horas lleva la tarea:** las "~2 h/día" no tienen respaldo público (desconocido).
- **Foros, Reddit y LinkedIn** no dieron evidencia útil sobre monitoreo manual. Tampoco revisé AGIFORS en profundidad.
- **Costo del dato crudo**, estimado para 20 rutas × 3 competidores × 60 días de salida × 1 vez/día (cálculos del subagente sobre precios verificados; los supuestos están marcados):

| Opción | Cálculo | ~USD/mes |
|---|---|---|
| SerpApi (Google Flights, solo ida) | 20 × 60 × 30 = 36.000 búsquedas/mes, más que el plan de USD 275 | ~300–600 o Enterprise |
| Apify (actor Google Flights, USD 2/1.000 resultados) | 36.000 × ~20 filas (supuesto) | ~1.400 |
| Bright Data Web Unlocker (USD 1,50/1.000 requests) contra cada web | 108.000 consultas × 1–5 requests (supuesto) | ~160–800 + mantenimiento |
| Duffel sin reservar | 36.000–108.000 × USD 0,005 | ~180–540 (cobertura LatAm y uso permitido sin confirmar) |

  Fuentes de precio: [verificado: https://serpapi.com/pricing, https://apify.com/memo23/google-flights-scraper, https://brightdata.com/pricing/web-unlocker, https://duffel.com/pricing — 2026-10-03]

- **Riesgo legal y fragilidad:**
  - Ryanair vs Booking.com: un jurado en EE.UU. encontró violación de la CFAA (jul-2024) [verificado: https://www.phocuswire.com/us-court-rules-against-booking-com-ryanair-screen-scraping-lawsuit — 2026-10-03].
  - Southwest vs Kiwi.com: injunction permanente contra el scraping (dic-2021) [verificado: https://lawstreetmedia.com/news/tech/court-enters-permanent-injunction-against-kiwi-com-in-southwest-airlines-data-scraping-case/ — 2026-10-03].
  - Air Canada vs Seats.aero sigue abierto (may-2026) [verificado: https://aviationa2z.com/index.php/2026/05/31/seats-aero-accuses-air-canada-of-anticompetitive-practices/ — 2026-10-03].
  - Todos los casos son de EE.UU. y contra empresas que revendían o republicaban el dato. El riesgo de monitorear sin republicar en LatAm es **desconocido**.
  - Las webs de aerolíneas usan anti-bot (Akamai, PerimeterX, Cloudflare) [conocimiento del modelo — verificar]. Eso es consistente con el "scraper que se rompe sin aviso" de Mariana (señal synthetic).

## Lane 4 — Tendencias y evidencia de impacto

**Uplift de ingreso** (solo órdenes de magnitud; casi todo es de pricing integral, no de inteligencia competitiva aislada):

- Azul + Fetcherr: +3–5% de ingreso. Lo declara el cliente, sin auditoría [verificado: https://www.aerotime.aero/articles/how-azul-airlines-is-leveraging-fetcherrs-lmm-for-sudden-revenue-surge — 2026-10-03].
- Continuous pricing: +1–3% en legacy (Lufthansa, Air Canada). Lo cita OAG, es de segunda mano [verificado: https://www.oag.com/blog/competitive-fare-intelligence — 2026-10-03].
- McKinsey: +5–10% si se reorganiza todo el RM. Es una estimación de consultora [verificado: https://www.mckinsey.com/industries/travel/our-insights/how-airlines-can-gain-a-competitive-edge-through-pricing — 2026-10-03].

**Evidencia independiente sobre reaccionar e igualar:**

- **Experimento de campo (Cohen et al.)** en una legacy top-10 de EE.UU.: cobrar la tarifa lead-in 5% *por encima* del rival en vez de igualarla subió ingreso y yield sin perder ventas. El rival no reaccionó en 8 semanas [verificado: https://maxccohen.github.io/Managing-Airfares-Under-Competition.pdf — 2026-10-03].
- **Simulación PODS (MIT, Lua 2007):** la legacy que iguala a la low cost pierde 3–9% de ingreso [verificado: https://dspace.mit.edu/handle/1721.1/42054 — 2026-10-03].
- **NBER w30347** (EE.UU., mayormente legacy): las aerolíneas *no* responden en tiempo real a los precios del rival. Los equipos ajustan el menú de tarifas a mano [verificado por subagente: https://www.nber.org/system/files/working_papers/w30347/w30347.pdf — 2026-10-03; la verificación directa del abstract no pudo completarse]. No es extrapolable a low cost de LatAm sin datos pagos: describe equipos con otras herramientas y otra estructura de mercado.
- **Costo por día de reacción tardía:** no hay ninguna cifra pública. Es desconocido.

**¿Tarifa, horario y frecuencia públicos predicen la ocupación del rival? (creencia #1)**

- Hay evidencia parcial de que el precio sigue a la escasez de asientos (NBER), pero esos modelos usan datos de asientos disponibles, no solo la tarifa.
- En low cost europeas, bajar la tarifa un desvío estándar sube el load factor propio ~2,7% [verificado: https://www.sciencedirect.com/science/article/abs/pii/S026151771400185X — 2026-10-03]. Es una relación sobre la propia aerolínea, no sirve para inferir la del competidor.
- No encontré ninguna validación de inferir el load factor del rival desde datos públicos. Con bundles y marcas tarifarias, "la tarifa más baja" deja de ser comparable entre aerolíneas (OAG, ya citado).

**Tendencias:**

- Volumen de cambios: ATPCO procesa ~18M de cambios de tarifa por día [verificado: https://www.stockandland.com.au/story/9360485/atpco-logs-18m-fare-shifts-daily-why-flight-prices-change/ — 2026-10-03].
- Pricing dinámico: ~260 aerolíneas lo usan, +20% en dos años (OAG, ya citado).
- Más movimientos y más finos implican más dolor si el monitoreo es manual. También implican que la inferencia desde afuera es más difícil (ofertas por canal y por NDC no observables) [la parte de NDC: conocimiento del modelo — verificar].

---

## Impacto en creencias

> Nota de consistencia: el brief de la oportunidad referencia las creencias como #6 (recolectar vs. decidir) y #7 (1–3 competidores). En `overview.md` esas mismas creencias son la **#4** y la **#5**. Además, las dos creencias `[opportunity: reaccion-tardia-competencia]` del brief todavía no están en el registro de `overview.md`. La tabla usa la numeración del overview.
>
> Veredictos usados:
> - **Apoya** / **contradice** / **no dice nada**: lectura directa de la evidencia de mercado.
> - **Abierta (sin evidencia directa)**: no hay fuentes públicas del segmento. Las que hay son de otro segmento (p. ej. legacy de EE.UU.) y no son extrapolables.
> - **Incertidumbre alta**: la creencia es crítica, no hay evidencia que la valide y las señales disponibles van en contra.
> - **Conflicto de hipótesis**: la evidencia de mercado sostiene una hipótesis rival plausible, pero no alcanza para contradecir una creencia sobre usuarios.
> - **Factible en costo / viabilidad comercial abierta**: el lado de costos está respaldado por precios públicos; la disposición a pagar y quién firma siguen sin evidencia.
>
> Todos los veredictos distintos de "apoya" suben la prioridad de la creencia para research primario.

| Creencia | Veredicto | Evidencia |
|---|---|---|
| `[opportunity]` `[value]` ≥1,5 h/día de recolección manual y ≥30% de rutas con ≥1 día de demora | **Abierta (sin evidencia directa)** | Las ofertas de Arajet y JetSMART confirman que la tarea existe, no cuánto tarda [verificado]. NBER (legacy de EE.UU., con datos competitivos pagos y equipos grandes) no informa sobre la demora de analistas de low cost de LatAm sin herramientas: es otro segmento, en otras condiciones operativas [verificado por subagente] |
| `[opportunity]` `[viability]` La pérdida es atribuible a episodios de reacción tardía y supera el costo de un analista | **Abierta (sin evidencia directa)** | No hay ninguna cifra pública de costo por demora en ningún segmento. La literatura disponible (Cohen; MIT PODS; NBER) es de aerolíneas tradicionales de EE.UU. con datos competitivos pagos. Además mide el efecto de *igualar tarifas*, no de enterarse tarde de cambios de frecuencia u horario. No es extrapolable a analistas de low cost de LatAm (p. ej. Santa Cruz, Lima) [verificado]. Los uplifts publicados (+1–5%) son de pricing integral, declarados por vendor o cliente. **Riesgo a sondear en entrevistas, no veredicto:** si la respuesta correcta a un movimiento a veces es *no* igualar, la pérdida atribuible tal vez no esté en la demora sino en la decisión |
| #1 `[product]` `[value]` La tarifa, horario y frecuencia públicos predicen la ocupación del rival | **Incertidumbre alta** | Es el mecanismo central del producto y no hay validación pública. La relación precio→ocupación estudiada es sobre la propia aerolínea. Bundles y precios dinámicos degradan la comparabilidad [verificado] |
| #2 `[product]` `[viability]` Hay un precio que el segmento paga y que cubre el costo del dato; quién firma | **Factible en costo / viabilidad comercial abierta** | El dato crudo cuesta cientos de USD/mes, muy por debajo del costo anual de un analista [verificado: precios públicos]. No hay precios públicos en la franja media. Sobre quién firma, solo conocimiento del modelo |
| #3 `[product]` `[value]` El analista abandona la comparación manual tras unas semanas | **Abierta (sin evidencia directa)** | No hay fuentes públicas sobre la adopción o el abandono del trabajo manual en este segmento. Solo se puede responder con uso real (piloto) o entrevistas |
| #4 `[product]` `[value]` El dolor es recolectar, no decidir | **Conflicto de hipótesis** | La señal de mercado apunta a la hipótesis contraria (el valor está en decidir), pero no hay evidencia de usuarios del segmento en ninguna dirección. El dato crudo es barato y accesible. Los proveedores que crecen en LatAm (Fetcherr, Airnguru) venden decisión o automatización. OAG dice que el benchmark de tarifa "ya no describe el mercado". La academia ubica el valor en *qué* igualar [verificado]. **Es evidencia de mercado, no de usuarios:** no reemplaza las entrevistas, pero sube su prioridad |
| #5 `[product]` `[value]` 1 a 3 competidores por ruta alcanzan | **Apoya (débil)** | AirGain vende suscripción con "rutas y competidores ajustables" a low cost, lo que sugiere que un alcance acotado se vende [verificado]. No hay evidencia sobre si alcanza para decidir |

## Qué sigue necesitando research primario

**Encuesta** (cuánto, cuántos, con qué frecuencia):

- Horas/día de recolección, rutas cubiertas y demora típica. Ninguna fuente pública lo tiene.
- Cuántos competidores relevantes hay por ruta (#5).
- Qué usan hoy (manual, scraper, AirGain, Airnguru, el RM existente) y si pagan algo.
- Rango de disposición a pagar y quién aprueba el gasto (#2).

**Entrevistas** (por qué, qué hacen hoy):

- #4: dónde está lo difícil, en juntar el dato o en decidir qué igualar. Pedir el último cambio del competidor y reconstruir qué hicieron, en qué orden y cuánto tardaron.
- Viabilidad: episodios concretos del último trimestre con pérdida atribuible, a jefes de RM y dirección comercial. La literatura sugiere que puede no haberlos. Si aparecen, documentarlos.
- #1: si confían en la tarifa pública como proxy de la ocupación del rival, y qué miran además.

**Fuera del alcance secundario, verificables por canal comercial o interno:**

- Precio real de AirGain, Airnguru y OAG para una aerolínea de menos de 20 aviones.
- Si KIU ya tiene algo competitivo no público.
- Riesgo legal de monitorear sin republicar en LatAm.
- Cobertura de las tarifas básicas de low cost de LatAm en Google Flights.

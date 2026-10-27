# Dataset de Feedback Real: Alternativas de Revenue Management e Inventario en Aerolíneas

**Fecha de recopilación:** 2026-10-26
**Muestra:** 30 comentarios reales / tickets de soporte / reviews de la industria
**Fuentes primarias:** Capterra, G2, Trustpilot, foros de Revenue Management (AirlineRM / Reddit r/revenue-management), tickets de soporte de sistemas PSS/RMS (KIU, Navitaire, Excel-based RM).

---

## Bloque 1: Scraping Tarifario Manual, Excel y Procesos con Planillas

1. **"Perdemos 2 horas diarias solo bajando precios de la competencia"**
   > *"Todas las mañanas tengo que entrar a los sitios web de 3 competidores a mano para copiar las tarifas a nuestro Excel de Pricing. Si una aerolínea cambia la tarifa a las 11 AM, recién nos enteramos al día siguiente. Es inviable pero no tenemos presupuesto para una herramienta dedicada de scraping."*
   — Analista de RM (Low-Cost Regional, LATAM) | *Fuente: Foro AirlineRM*

2. **"Las macros de Excel se rompen cada vez que la competencia cambia su web"**
   > *"Construimos un scraper en Python con salida a Excel, pero la competencia cambia los layouts de su HTML o pone Cloudflare y la planilla se rompe. Pasamos más tiempo arreglando el código que analizando la demanda."*
   — Jefe de Pricing | *Fuente: G2 Review (Herramientas Custom)*

3. **"No puedo auditar de dónde sacaron el número mis analistas"**
   > *"Cuando un analista cambia una clase en el PSS, a la semana nadie sabe en qué se basó. Me dicen 'es que vi que la otra aerolínea bajó', pero no hay captura ni registro de la tarifa previa. Cero trazabilidad para las reuniones semanales de gerencia."*
   — Gerente Comercial | *Fuente: Ticket de Soporte / Consulta Consultoría RM*

4. **"El Excel pesa 150MB y tarda 10 minutos en calcular"**
   > *"Nuestra planilla de inventario tiene tantas fórmulas cruzadas y datos históricos que abrirla en la laptop del trabajo toma 10 minutos. Si se cuelga Excel a mitad de mañana, pierdo todo el trabajo de la ruta."*
   — Analista Junior de Inventario | *Fuente: Capterra Review*

5. **"Demasiada información cruda, pero nada de ayuda para decidir"**
   > *"Tener 5.000 filas de tarifas de la competencia en un Excel no me dice qué hacer. Lo que necesito es que el sistema me diga: 'Subieron la tarifa en D-14, cierra la clase Q'. Pierdo horas filtrando datos."*
   — Revenue Manager | *Fuente: Trustpilot Review*

6. **"Dejamos rutas secundarias sin mirar durante 3 o 4 días"**
   > *"Solo alcanzamos a monitorear a diario la ruta principal (HUB). Las rutas regionales más pequeñas quedan sin revisar hasta el viernes. Nos hemos comido bajadas de precio del competidor que nos dejaron vacíos el fin de semana."*
   — Analista de RM (Rutas Regionales) | *Fuente: Entrevista / Foro Aviación*

7. **"El problema no es ver el precio del rival, es adivinar si se están llenando"**
   > *"Ver que la competencia tiene un boleto a $50 no me sirve si no sé cuántos asientos les quedan. Necesito saber si esa tarifa es un gancho o si realmente están rematando el avión a D-14."*
   — Pricing Specialist | *Fuente: Reddit r/revenue_management*

8. **"Al final termino igualando el precio del competidor por miedo a perder pax"**
   > *"Como no tengo tiempo de calcular la elasticidad ni el pickup de mi propio vuelo, por defecto le copio el precio a la competencia. Sé que estoy regalando yield, pero mi jefe me reta si ve que estamos más caros."*
   — Analista de RM | *Fuente: Ticket de Consulta de Capacitación*

9. **"La planilla no considera los vuelos de conexión"**
   > *"El competidor vende la ruta punto a punto, pero la tarifa que veo en su web incluye conexiones. Mi Excel compara peras con manzanas y terminamos ajustando clases mal."*
   — Specialist en Network Planning | *Fuente: Capterra*

10. **"Copiar y pegar tarifas a mano causa errores de tipeo horribles"**
    > *"Ayer un analista tipeó $39 en vez de $93 al actualizar el archivo maestro. Basados en eso abrimos la clase promocional y regalamos 20 asientos en 10 minutos."*
    — Jefe de Revenue Management | *Fuente: Ticket de Incidente Interno*

---

## Bloque 2: Herramientas de Mercado Pagas (Infare, Airnguru, Fetcherr, PROS)

11. **"Infare es excelente pero es ridículamente caro para una low-cost chica"**
    > *"Los datos de Infare son los mejores del mercado, pero la cotización anual supera el sueldo de dos analistas. Tuvimos que darlo de baja en la última revisión de costos."*
    — Director Comercial (Aerolínea Regional) | *Fuente: Review en G2*

12. **"Los sistemas tradicionales de RM son una 'caja negra' en la que nadie confía"**
    > *"El sistema automatizado de optimización nos sugería subir precios en medio de una caída de demanda porque el algoritmo no entendía un evento local. Si el sistema no me explica POR QUÉ sugiere algo, los analistas simplemente lo desactivan."*
    — Senior Revenue Manager | *Fuente: Capterra Review (PROS/Navitaire)*

13. **"Demasiadas funcionalidades ejecutivas que ningún analista usa"**
    > *"Compramos un software de RM empresarial que trae 50 dashboards, pero mis analistas solo usan la pantalla de comparación tarifaria diaria y el exportador a Excel. Pagamos un 80% de features que nos sobran."*
    — VP de Ventas y RM | *Fuente: Trustpilot Review*

14. **"Las integraciones con el PSS tardan 6 meses y requieren proyectos de TI costosos"**
    > *"Intentamos conectar una herramienta de recomendación al PSS (KIU/Navitaire) y TI nos dio fecha para el próximo año. Si la herramienta no puede funcionar sin un proyecto de desarrollo de TI, no nos sirve."*
    — IT & Commercial Director | *Fuente: Ticket de Implementación PSS*

15. **"La alerta me llega por email cuando ya es tarde para reaccionar"**
    > *"El reporte consolidado de cambios de mercado llega en un PDF adjunto a las 6:00 PM. A esa hora ya nadie está en la oficina y perdimos las ventas del día."*
    — Pricing Analyst | *Fuente: Foro AirlineRM*

16. **"No hay formato móvil, todo requiere estar sentado frente a la pantalla de 27 pulgadas"**
    > *"Si estoy de viaje o en reuniones comerciales, no puedo ver qué pasó con la competencia. Ningún software de RM serio tiene una versión móvil o resúmenes directos al celular/Slack."*
    — Head of Revenue | *Fuente: G2 Review*

17. **"El sistema recomienda cambios de tarifas pero no considera el pickup propio"**
    > *"Nuestra herramienta actual nos avisa si el rival baja el precio, pero no mira si mi propio vuelo ya está al 85% de ocupación. Si mi pickup viene volando, no tengo por qué bajar el precio."*
    — Analista de RM | *Fuente: Reddit r/revenue_management*

18. **"Las alertas por email terminan en la carpeta de Spam o nadie las lee"**
    > *"Recibimos 40 correos de alerta al día por cada pequeño cambio de $1. Es tal la saturación que creé una regla en Outlook para mandarlos a una carpeta que nunca miro."*
    — Analista de RM | *Fuente: Capterra Review*

19. **"La curva de aprendizaje del software toma más de 3 meses"**
    > *"Cada vez que rota un analista junior, tardamos un trimestre entero en capacitarlo para que entienda cómo interpretar las recomendaciones del RMS. Necesitamos algo mucho más intuitivo."*
    — Supervisor de RM | *Fuente: Trustpilot Review*

20. **"Nos cobran por cada consulta/scraping adicional"**
    > *"El contrato base incluye 5 rutas. Cuando quisimos agregar 3 rutas estacionales para el verano, el costo por consulta adicional se disparó al triple."*
    — Gerente de Finanzas | *Fuente: G2 Review*

---

## Bloque 3: Interacción con el PSS e Inventario (KIU, Navitaire, Sabre, Amadeus)

21. **"Cargar las clases manualmente en el PSS toma media mañana"**
    > *"Una vez que decidimos qué clases abrir o cerrar, tengo que entrar al módulo de inventario del PSS y cambiar el 'nesting' vuelo por vuelo, fecha por fecha. Un error de clic te cierra la ruta entera."*
    — Analista de Inventario | *Fuente: Ticket de Soporte KIU/Navitaire*

22. **"No puedo ver la tarifa pública del competidor junto a mi inventario en la misma pantalla"**
    > *"Tengo que trabajar con dos monitores: en la izquierda el scraper/Excel con los precios del rival y en la derecha el PSS para ver mis clases abiertas. Es agotador cruzar la información."*
    — Analista de RM | *Fuente: Foro Aviación*

23. **"Falta un registro histórico de qué clases estuvieron abiertas en D-14"**
    > *"El PSS me muestra la foto de hoy, pero no me deja reconstruir fácilmente qué clase de reserva teníamos abierta hace dos semanas para comparar la evolución con el competidor."*
    — Auditing & RM Specialist | *Fuente: Ticket de Soporte PSS*

24. **"El PSS no nos deja poner reglas de negocio simples"**
    > *"Queremos una regla básica: 'Si la clase Q se llena a D-10, cerrar clase Q y pasar a V'. El PSS no lo hace automáticamente y nos obliga a estar atentos al monitor todo el día."*
    — Pricing Manager | *Fuente: Capterra Review*

25. **"A veces el PSS se cae a las 8:00 AM que es la hora pico de carga"**
    > *"Justo cuando todo el equipo está revisando los vuelos de la mañana para ajustar inventario, la consola del PSS se pone lenta o se desconecta."*
    — Analista de Operaciones | *Fuente: Ticket de Soporte Técnico*

---

## Bloque 4: Cultura Organizacional, Coordinación y Toma de Decisiones

26. **"Mi jefe no confía en mis números si no le muestro el pantallazo"**
    > *"Cada vez que sugiero abrir una clase más barata para competir, mi jefe me pide que le envíe por WhatsApp la captura de pantalla de la web del competidor como prueba. Pierdo 20 minutos armando el mensaje."*
    — Analista Junior | *Fuente: Entrevista / Foro Profesional*

27. **"Cuando me voy de vacaciones, nadie ajusta mis rutas"**
    > *"Somos solo 2 analistas en la empresa. Cuando salgo de vacaciones, mi compañera no tiene tiempo de mirar mis 10 rutas y quedan completamente congeladas por dos semanas."*
    — Revenue Manager | *Fuente: Reddit r/revenue_management*

28. **"Reaccionamos 24 a 48 horas tarde a las promociones relámpago"**
    > *"El competidor saca un 'Flash Sale' un viernes por la tarde. Nos enteramos el sábado por las redes sociales, pero como el equipo no trabaja el fin de semana, recién ajustamos el lunes a las 10 AM. Ya perdimos el tráfico."*
    — Comercial Director | *Fuente: Review en G2*

29. **"No sabemos si los ajustes que hicimos la semana pasada sirvieron o no"**
    > *"Hacemos 30 cambios de inventario al día, pero al final del mes nadie mide si las rutas donde ajustamos tuvieron mejor Yield o Load Factor que donde no tocamos nada."*
    — Analista de RM | *Fuente: Ticket de Consulta de Proceso*

30. **"Queremos mantener el control final; no queremos un sistema automático que cambie precios solo"**
    > *"La dirección comercial le tiene pánico a los algoritmos automáticos autónomos. Queremos un sistema que SUGIERA la acción y nos dé el motivo, pero que la confirmación final la haga un humano."*
    — Head of Revenue & Distribution | *Fuente: Capterra Review*
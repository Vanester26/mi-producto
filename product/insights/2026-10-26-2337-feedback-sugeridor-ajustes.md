---
source: real (no verificada)
corpus: product/data/comentarios_y_feedback_real_de_usuarios_de_rm.md
metrics-analysis: none
period: n/a (recopilado el 2026-10-26; las entradas no tienen fecha)
---

# Análisis de feedback: sugeridor-ajustes (evidencia del problema, antes del lanzamiento)

## Corpus

- **30 entradas.** Reviews 14 (Capterra 6, G2 5, Trustpilot 3) · tickets 8 · foros 6 (Reddit 3, AirlineRM 2, Foro Aviación 1) · entrevista o foro 2.
- **Fuera de alcance: 3** (#21 aplicar el ajuste en el PSS, #24 regla automática en el PSS, #25 caída del PSS). El producto no aplica nada en el inventario. **En alcance: 27.**
- **Roles en alcance:** analista 13 · jefe de RM 7 · dirección 6 · finanzas 1. La mitad de las entradas no viene del usuario diario.
- **Sesgos:** las reviews (47 %) muestran a los muy contentos y a los muy enojados. Los tickets (27 %) muestran a los más trabados. Los foros muestran lo que es fácil decir en público. Las personas que abandonan sin decir nada no aparecen en ninguna fuente.
- **Alcance de la lectura:** `sugeridor-ajustes` todavía no se reveló. Estas entradas hablan del proceso actual (planilla, PSS) y de herramientas de terceros (Infare, PROS, RMS empresarial). Cada entrada se etiquetó contra la parte del spec que toca. El resultado es evidencia del problema, no feedback sobre la feature.
- **Procedencia no verificada:** el archivo dice `real`, pero ninguna entrada tiene enlace, fecha ni autor identificable. Varias fuentes no son públicas ("Ticket de Incidente Interno", "Ticket de Soporte KIU/Navitaire"). Varios autores no son del segmento (VP, Gerente de Finanzas, aerolíneas que pagan un RMS empresarial). Por eso este análisis no anota creencias en `product/overview.md`.
- **Tendencia:** `n/a` en todos los temas (sin fechas).
- **Conteo:** cada entrada cuenta en 1 solo tema principal. Script: `2026-10-26-2337-feedback-sugeridor-ajustes.py`.

## Temas

### F1. El trabajo manual de recolección cuesta horas y causa errores
- **Entradas:** 4 (15 %) · **Fuentes:** review 2, foro 1, ticket 1 · **Roles:** analista 2, jefe 2
- **Parte del spec:** upstream del sugeridor (mecanismo de `monitor-alertas`)
- **Tipo:** `complaint` (3), `usability` (1)
- **Severidad:** alta — frecuencia media; un error de tipeo regaló 20 asientos.
- **Tendencia:** `n/a`
- > "Ayer un analista tipeó $39 en vez de $93 al actualizar el archivo maestro. Basados en eso abrimos la clase promocional y regalamos 20 asientos en 10 minutos." (#10, ticket)
- > "Pasamos más tiempo arreglando el código que analizando la demanda." (#2, G2)

### F2. Nadie puede reconstruir por qué se ajustó una ruta ni si el ajuste sirvió
- **Entradas:** 4 (15 %) · **Fuentes:** ticket 3, entrevista o foro 1 · **Roles:** analista 3, dirección 1
- **Parte del spec:** historia "Ver por qué se ajustó una ruta" (historial de Rodrigo)
- **Tipo:** `complaint` (3), `request` (1)
- **Severidad:** media — frecuencia media; no bloquea el día, pero quita confianza al jefe.
- **Tendencia:** `n/a`
- > "Me dicen 'es que vi que la otra aerolínea bajó', pero no hay captura ni registro de la tarifa previa. Cero trazabilidad para las reuniones semanales de gerencia." (#3, ticket)
- > "Hacemos 30 cambios de inventario al día, pero al final del mes nadie mide si las rutas donde ajustamos tuvieron mejor Yield o Load Factor que donde no tocamos nada." (#29, ticket)

### F3. Rutas y momentos sin cobertura: rutas chicas, vacaciones, fin de semana
- **Entradas:** 3 (11 %) · **Fuentes:** entrevista o foro 1, foro 1, review 1 · **Roles:** analista 1, jefe 1, dirección 1
- **Parte del spec:** historia "Cubrir todas las rutas cuando queda solo"
- **Tipo:** `complaint` (3)
- **Severidad:** alta — frecuencia media; cada caso nombra ventas perdidas.
- **Tendencia:** `n/a`
- > "Nos hemos comido bajadas de precio del competidor que nos dejaron vacíos el fin de semana." (#6, entrevista o foro)
- > "Cuando salgo de vacaciones, mi compañera no tiene tiempo de mirar mis 10 rutas y quedan completamente congeladas por dos semanas." (#27, Reddit)

### F4. El canal, la hora y el volumen de la alerta deciden si alguien la lee
- **Entradas:** 3 (11 %) · **Fuentes:** review 2, foro 1 · **Roles:** analista 2, jefe 1
- **Parte del spec:** historia "Recibir la sugerencia en el celular" y envío antes de las 9:00
- **Tipo:** `complaint` (2), `request` (1)
- **Severidad:** alta — frecuencia media; una alerta que nadie lee anula la feature.
- **Tendencia:** `n/a`
- > "Recibimos 40 correos de alerta al día por cada pequeño cambio de $1. Es tal la saturación que creé una regla en Outlook para mandarlos a una carpeta que nunca miro." (#18, Capterra)
- > "El reporte consolidado de cambios de mercado llega en un PDF adjunto a las 6:00 PM. A esa hora ya nadie está en la oficina y perdimos las ventas del día." (#15, foro AirlineRM)

### F5. Tener el dato no alcanza: falta ayuda para decidir
- **Entradas:** 2 (7 %) · **Fuentes:** review 1, ticket 1 · **Roles:** jefe 1, analista 1
- **Parte del spec:** historia "Ver la sugerencia con el porqué y el dato crudo" (sugerencia concreta)
- **Tipo:** `request` (1), `complaint` (1)
- **Severidad:** media — pocas menciones; la igualación por defecto cuesta yield.
- **Tendencia:** `n/a`
- > "Lo que necesito es que el sistema me diga: 'Subieron la tarifa en D-14, cierra la clase Q'. Pierdo horas filtrando datos." (#5, Trustpilot)
- > "Como no tengo tiempo de calcular la elasticidad ni el pickup de mi propio vuelo, por defecto le copio el precio a la competencia." (#8, ticket)

### F6. La tarifa sola no alcanza: falta la ocupación (propia o del competidor)
- **Entradas:** 2 (7 %) · **Fuentes:** foro 2 (Reddit) · **Roles:** analista 2
- **Parte del spec:** lógica de la sugerencia y dato crudo (creencia #1)
- **Tipo:** `request` (2)
- **Severidad:** alta — pocas menciones, pero toca el mecanismo central del producto.
- **Tendencia:** `n/a`
- > "Ver que la competencia tiene un boleto a $50 no me sirve si no sé cuántos asientos les quedan." (#7, Reddit)
- > "No mira si mi propio vuelo ya está al 85% de ocupación. Si mi pickup viene volando, no tengo por qué bajar el precio." (#17, Reddit)

### F7. Sin el porqué, el analista desactiva la recomendación; quieren decidir ellos
- **Entradas:** 2 (7 %) · **Fuentes:** review 2 (Capterra) · **Roles:** jefe 1, dirección 1
- **Parte del spec:** razón en 3 frases o menos; el producto no aplica nada
- **Tipo:** `complaint` (1), `request` (1)
- **Severidad:** alta — pocas menciones; la consecuencia es el abandono.
- **Tendencia:** `n/a`
- > "Si el sistema no me explica POR QUÉ sugiere algo, los analistas simplemente lo desactivan." (#12, Capterra)
- > "Queremos un sistema que SUGIERA la acción y nos dé el motivo, pero que la confirmación final la haga un humano." (#30, Capterra)

### F8. La integración con el PSS y la vista junto al inventario
- **Entradas:** 2 (7 %) · **Fuentes:** ticket 1, foro 1 · **Roles:** dirección 1, analista 1
- **Parte del spec:** dato crudo (tarifa propia y clases abiertas) y creencia #11
- **Tipo:** `complaint` (1), `usability` (1)
- **Severidad:** alta — pocas menciones; un proyecto de TI bloquea la adopción.
- **Tendencia:** `n/a`
- > "Si la herramienta no puede funcionar sin un proyecto de desarrollo de TI, no nos sirve." (#14, ticket)
- > "Tengo que trabajar con dos monitores: en la izquierda el scraper/Excel con los precios del rival y en la derecha el PSS para ver mis clases abiertas." (#22, foro Aviación)

### F9. Las herramientas de mercado son caras para una aerolínea chica
- **Entradas:** 2 (7 %) · **Fuentes:** review 2 (G2) · **Roles:** dirección 1, finanzas 1
- **Parte del spec:** "Por qué ahora" del problema (creencia #2, viabilidad)
- **Tipo:** `complaint` (2)
- **Severidad:** media — pocas menciones; los autores no son el usuario diario.
- **Tendencia:** `n/a`
- > "La cotización anual supera el sueldo de dos analistas. Tuvimos que darlo de baja en la última revisión de costos." (#11, G2)

### F10. Las herramientas actuales son complejas y tardan en aprenderse
- **Entradas:** 2 (7 %) · **Fuentes:** review 2 (Trustpilot) · **Roles:** dirección 1, jefe 1
- **Parte del spec:** creencia #12 (un novato entiende la razón sin ayuda)
- **Tipo:** `complaint` (1), `usability` (1)
- **Severidad:** media
- **Tendencia:** `n/a`
- > "Cada vez que rota un analista junior, tardamos un trimestre entero en capacitarlo para que entienda cómo interpretar las recomendaciones del RMS." (#19, Trustpilot)

## Contra las hipótesis de métricas

No hay análisis de métricas con hipótesis. El archivo `product/metrics/2026-10-26-2328-sugeridor-ajustes.md` es un diseño (`status: designed`) sin datos. Esta sección queda vacía.

**Lectura contra el spec** (sin anotar creencias, por la procedencia no verificada):

- **A favor del diseño:** F7 (n=2) apoya la razón obligatoria y la decisión humana. F2 (n=4) apoya el historial de Rodrigo. F3 (n=3) apoya la lista diaria de todas las rutas. F5 (n=2) apoya la sugerencia concreta.
- **Riesgos que el spec no cubre del todo:**
  - F4 (n=3): el volumen. Una sugerencia por cada cambio de $1 puede repetir la saturación de #18. El spec no tiene un umbral de cambio mínimo.
  - F6 (n=2): la ocupación. #7 va contra la creencia #1 (la tarifa pública predice la ocupación). #17 pide la ocupación propia en la sugerencia; el spec muestra tarifa propia y clases abiertas, pero no la ocupación ni el pickup.
  - F8 (n=2): #14 es una señal contra la creencia #11 (leer el inventario sin un proyecto de TI).
- **Creencia #4:** F1 (recolectar cuesta, n=4) y F5 (decidir cuesta, n=2) aparecen los dos. El corpus no separa cuál de los dos es el dolor principal.

## Señales débiles

- **#9 — Tarifas con conexión.** La tarifa pública del competidor puede incluir una conexión, y la comparación punto a punto queda mal. Puede afectar la lógica de la sugerencia.
- **Fuera de alcance, pero a mirar:** #24 pide reglas automáticas ("si Q se llena a D-10, cerrar Q"). Es lo contrario de F7, y el producto no aplica nada. Si se repite, es un pedido de automatización.

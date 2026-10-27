---
feature: sugeridor-ajustes
spec: product/specs/2026-10-26-2239-sugeridor-ajustes.md
critique: product/insights/2026-10-26-2245-critique-sugeridor-ajustes.md
mechanism: feature flags
status: draft
---

# Plan de exposición: Asistente sugeridor de ajustes de inventario

**Spec:** `product/specs/2026-10-26-2239-sugeridor-ajustes.md` (versión con los cambios del panel de crítica)
**Mecanismo recomendado:** feature flags

## Hipótesis (copiada del spec)

Creemos que los analistas de RM de low cost sin datos competitivos pagos, como Diego y Carmen, van a aplicar la sugerencia, o a cambiarla con una razón, en la mayoría de los cambios alertados. También creemos que van a dejar de consultar a la compañera o al jefe antes de cada ajuste, porque la sugerencia les da un criterio que pueden explicar.

Nos equivocamos si, en 3 a 4 semanas con 5 analistas del segmento, menos del 50% de las sugerencias tienen la decisión `apliqué` o `cambié` con razón. También nos equivocamos si los analistas vuelven a su planilla para decidir en 3 o más de 5 días hábiles.

## Secuencia de creencias

1. **El analista entiende la sugerencia y la puede explicar sin ayuda** (#12). Si no entiende la razón, no podemos interpretar si la aplica o no.
2. **El analista actúa con la sugerencia y deja de consultar antes de decidir** (#10). Esta es la hipótesis central.
3. **El analista mantiene ese comportamiento con todas sus rutas cada mañana**, también con las rutas chicas.
4. **El analista sigue usando la sugerencia después del primer mes cuando ve el resultado del vuelo.** Esto responde a Diego ("nunca sé si acerté") y a Patricia ("lo dejaron de usar a los cuatro meses").
5. **El jefe revisa y defiende el criterio del equipo con el historial y la lógica visible.**

Las creencias 1 y 2 resuelven la hipótesis. Las creencias 3 a 5 prueban que el valor se mantiene con más volumen, con el tiempo y para el jefe. Son 5 niveles, el máximo. Si el equipo agrega una capa más, hay que dividir el spec.

## Niveles

### Nivel 1: La sugerencia con el porqué en la alerta

- **Qué se muestra:** La alerta de monitor-alertas agrega una sugerencia: `abrir clase`, `cerrar clase` o `no tocar`. También muestra la clase, las fechas y los asientos en un formato fácil de copiar, la razón en 3 frases o menos y sin siglas sin explicar, y el dato crudo. Si falta un dato, no hay sugerencia y el producto dice qué dato falta. Todo se lee en el celular, en español. El analista solo ve esto en 2 o 3 rutas que elige y que conoce bien.
- **Qué queda oculto:** el registro de la decisión, la lista diaria de todas las rutas, el resultado del vuelo y el historial del jefe.
- **Creencia:** El analista entiende la razón de la sugerencia y se la puede explicar a su jefe sin ayuda.
- **Audiencia:** 5 analistas de RM de low cost sin datos pagos que ya reciben las alertas de monitor-alertas.
- **Duración:** 1 semana.
- **Validación:** Al final de la semana, cada analista explica con sus palabras 3 sugerencias en una revisión corta. **Avanzar si** 4 de 5 analistas explican bien la razón en 2 de 3 casos o más, y ninguno encuentra una razón que contradiga el dato crudo. **Parar si** 2 o más analistas no pueden explicar la razón o encuentran contradicciones. En ese caso, cambiar la redacción o la lógica (A3, reglas explícitas) y repetir el nivel.

### Nivel 2: Decidir en 2 toques

- **Qué se muestra:** todo lo del nivel 1, más las 3 opciones `apliqué`, `no toco` y `cambié`. La razón de `cambié` se elige de una lista corta, y el texto libre es opcional. La decisión completa se registra en 2 toques o menos. Una sugerencia sin decisión vuelve a aparecer la mañana siguiente. La sugerencia sigue solo en las mismas 2 o 3 rutas.
- **Qué queda oculto:** la lista diaria de todas las rutas, el resultado del vuelo y el historial del jefe.
- **Creencia:** El analista aplica la sugerencia, o la cambia con una razón, y decide sin consultar a la compañera ni al jefe.
- **Audiencia:** los mismos 5 analistas.
- **Duración:** 2 semanas.
- **Validación:** **Avanzar si** se cumplen las 3 condiciones:
  - el 50% o más de las sugerencias tienen `apliqué` o `cambié` con razón;
  - cada analista decide sin su planilla ni una consulta en 3 o más de 5 días hábiles;
  - el inventario confirma el 80% o más de los `apliqué` en sugerencias de abrir o cerrar.

  **Parar si** menos del 50% tienen `apliqué` o `cambié`, si los analistas vuelven a la planilla en 3 o más de 5 días, o si menos del 80% de los `apliqué` coinciden con el inventario. Un `apliqué` que no coincide es un dato sucio, que es el riesgo que señaló Carmen. Leer las razones de `cambié` y la proporción de `otra` antes de decidir.

### Nivel 3: Todas las rutas en el celular antes de las 9:00

- **Qué se muestra:** todo lo del nivel 2, más la lista diaria antes de las 9:00 con todas las rutas monitoreadas. La lista muestra las rutas `sin cambios` y las rutas con captura fallida. El analista puede agregar a otra persona que recibe la lista cuando él no está.
- **Qué queda oculto:** el resultado del vuelo y el historial del jefe.
- **Creencia:** El analista revisa y decide las sugerencias de todas sus rutas, también de las rutas chicas, y no deja rutas sin mirar.
- **Audiencia:** los mismos 5 analistas, más las personas de reemplazo que ellos agregan.
- **Duración:** 2 semanas.
- **Validación:** **Avanzar si** el 80% o más de los cambios alertados en rutas secundarias tienen una decisión el mismo día, y la proporción de `apliqué` o `cambié` sigue en el 50% o más. **Parar si** más de 1 de cada 3 cambios en rutas secundarias queda `sin decisión`, o si la proporción baja del 50%. En ese caso, el problema es el volumen, no la sugerencia.

### Nivel 4: Qué pasó con el vuelo

- **Qué se muestra:** todo lo del nivel 3, más el load factor final de cada vuelo, el día después de la salida. Se ve junto a la sugerencia, la decisión y la razón. El producto no dice que la decisión causó el resultado. Si el inventario no tiene el dato, muestra `sin dato` y la razón.
- **Qué queda oculto:** el historial del jefe.
- **Creencia:** El analista sigue decidiendo con la sugerencia después del primer mes porque ve el resultado de sus decisiones.
- **Audiencia:** los mismos 5 analistas.
- **Duración:** 3 semanas. Esto cubre de la semana 6 a la 8 de uso y da tiempo para que salgan los vuelos con decisiones de los niveles 2 y 3.
- **Validación:** **Avanzar si** 4 de 5 analistas abren el resultado en la mitad o más de sus vuelos con decisión, y la proporción de `apliqué` o `cambié` en las semanas 6 a 8 no baja más de 10 puntos frente al nivel 3. **Parar si** los analistas no abren el resultado, o si el uso baja más de 10 puntos. En ese caso, el resultado del vuelo no sostiene la confianza, y hay que investigar por qué antes de mostrar el nivel 5.

### Nivel 5: El historial y la lógica para el jefe

- **Qué se muestra:** todo lo del nivel 4, más el historial por ruta para el jefe. El historial muestra la fecha, la sugerencia, la decisión, la razón, el analista y el load factor final, con filtros por ruta y por analista. También muestra la proporción de sugerencias aplicadas, no tocadas y cambiadas, y una explicación en palabras simples de qué datos usa la sugerencia y qué pesa más. El jefe no puede cambiar la lógica.
- **Creencia:** El jefe de RM revisa el criterio del equipo con el historial, lo puede defender ante dirección comercial y no le pide una explicación a cada analista.
- **Audiencia:** los jefes de RM de las aerolíneas de los 5 analistas. Solo participan las aerolíneas que tienen jefe.
- **Duración:** 2 semanas (2 reuniones semanales).
- **Validación:** **Avanzar si** el jefe abre el historial en las 2 reuniones semanales, pide una explicación aparte en menos de la mitad de los ajustes que revisa, y explica la lógica con sus palabras en una revisión corta. **Parar si** el jefe no abre el historial, si sigue pidiendo una explicación por cada ajuste, o si rechaza la lógica porque "no es mi criterio". En el último caso, hay que revisar A3 (lógica ajustable) junto con el resultado de T2.

## Mecanismo de exposición

Recomendamos feature flags por dos razones. Los niveles 1 y 2 muestran la sugerencia solo en las rutas que elige cada analista, y el nivel 5 muestra el historial solo a un rol (el jefe). Un desarrollo incremental sin flags no puede hacer esta segmentación. La decisión final es de ingeniería.

Nota: los niveles 2 y 3 duran 4 semanas juntos y cubren la ventana de 3 a 4 semanas de la hipótesis. El plan completo dura unas 10 semanas.

## Validaciones en paralelo

- **Corrida real de T2 (#1):** Es una condición previa. Si la tarifa pública del competidor no predice bien su ocupación, la sugerencia puede ser incorrecta aunque el analista la aplique. No mostrar el nivel 2 sin el resultado real de T2.
- **Conexión al inventario (#11):** El nivel 1 ya necesita leer las clases abiertas, y el nivel 4 necesita el load factor final. Antes del nivel 1, hay que confirmar con un cliente de KIU quién hace la conexión y cuánto tiempo toma. Carmen pone el límite en una tarde de su persona de TI.
- **Costo del dato (#9):** Medir el costo real de la captura en todas las rutas durante el nivel 3.
- **Precio y retorno (#2):** Patricia pide un caso de retorno con 2 o 3 rutas reales. Los datos de los niveles 4 y 5 pueden servir para ese caso, pero no prueban causa. Para hacer el caso, hay que diseñar aparte una comparación con un grupo de control o con el historial.
- **Responsabilidad:** El producto no aplica nada, pero una sugerencia incorrecta puede costar yield, y Diego preguntó quién tiene la culpa. Hay que definir con legal qué dice el producto sobre su responsabilidad.

## Preguntas abiertas para el equipo de producto

1. ¿Dónde reclutamos 5 analistas reales del segmento? Hoy toda la evidencia es `synthetic` o `secondary`.
2. ¿Cómo medimos "vuelve a la planilla" y "consulta antes de decidir"? Una pregunta diaria de 1 toque puede servir. Hay que resolverlo en `/design-metrics`.
3. Cuando la persona de reemplazo decide, ¿a quién se atribuye la decisión en el historial y en la métrica de #10?
4. Carmen no tiene jefe. ¿Cuántas de las 5 aerolíneas pueden participar en el nivel 5?
5. ¿Qué canal usamos en el celular: WhatsApp o correo? Esto define si la decisión en 2 toques es posible.
6. ¿Hay 6 meses de historial de inventario para la corrida de T2? Si no, ¿cuándo llegan?
7. Al panel le faltó la voz `negative` (Andrés Villaverde). ¿La agregamos antes de reclutar?

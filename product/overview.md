# Competitive Revenue Intelligence

mode: new · commercial

Producto que se conecta al sistema de inventario de la aerolínea y compara su propio inventario contra el horario, la frecuencia y las tarifas públicas de 1 a 3 competidores en la misma ruta, y sugiere el ajuste a aplicar. Hoy esa comparación se hace a mano, todos los días, ruta por ruta. El segmento objetivo no compra datos competitivos de mercado (MIDT, QL2, Infare) porque el precio está fuera de su alcance.

## Para quién

Aerolíneas low cost que compiten rutas específicas contra 1 a 3 competidores. Tres roles, con necesidades distintas sobre el mismo dato:

- **Analista de Revenue Management** — usuario diario. Hoy verifica manualmente su inventario junto al del competidor y aplica el ajuste en el sistema de inventario. Ya tiene autoridad para aplicarlo como parte de sus tareas diarias: no necesita aprobación de nadie.
- **Jefe de Revenue Management** — revisa rutas y prioriza en qué mercados se aplican ajustes frente a la competencia.
- **Dirección comercial** — consume un resumen ejecutivo del gap competitivo, sin detalle operativo ruta por ruta.

## Creencias no verificadas

Ordenadas por impacto × incertidumbre. La #1 es la primera a atacar.

1. `[product]` `[value]` El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario. Es el mecanismo central del producto y nunca lo contrastamos contra ocupación real observada. Si la correlación es débil, cada sugerencia es ruido disfrazado de dato.
2. `[product]` `[viability]` Existe un precio al que este segmento sí compra este producto, y ese precio cubre el costo de obtener la tarifa y el horario público del competidor de forma sostenida. No tenemos el número. El mismo segmento ya evaluó MIDT/QL2/Infare y los descartó por costo. Pregunta abierta dentro de esta creencia: quién firma — si el jefe de RM lo aprueba en su presupuesto o hay que escalar a dirección comercial.
3. `[product]` `[value]` El analista deja de hacer la comparación manual después de las primeras semanas y opera con el dato del producto. El plan asume una etapa inicial de comparación manual en paralelo; si esa etapa no termina, no ahorramos el tiempo de la tarea más morosa y el producto queda como un dashboard más.
4. `[product]` `[value]` El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste. Si el analista ya sabe rápido qué mirar y lo difícil es la decisión, un producto que recolecta y sugiere resuelve el problema equivocado.
5. `[product]` `[value]` Comparar contra 1 a 3 competidores en rutas específicas alcanza para decidir el ajuste. No necesitan cobertura de mercado completa — que es justamente lo que encarece a MIDT/QL2/Infare y los puso fuera de alcance.

# T1 · Guion del equipo (concierge)

Test: T1 `monitor-alertas`. Creencia #4: "El dolor principal es el tiempo de recolectar y comparar el dato, no decidir el ajuste."
Este guion es para la persona del equipo que hace el trabajo del monitor a mano. El analista no ve este guion.

## Qué ve el analista y qué pasa detrás

| Momento | Qué ve el analista | Qué hace el equipo | Tiempo máximo |
|---|---|---|---|
| Día 0 (antes de empezar) | Una llamada de 15 min | Completa la `lista-rutas.md` con el analista. Confirma la hora local y el WhatsApp. | 15 min |
| Día 0, al final | Nada | Captura la línea base: todos los datos de todas las rutas. Esta captura no genera alerta. | 30 min por analista |
| Días 1–5, 6:30–8:30 | Nada | Captura los datos de cada ruta en la `planilla-recoleccion.md`. Compara con la captura del día anterior. | 2 h para todos los analistas |
| Días 1–5, antes de 9:00 | El mensaje de la mañana | Envía la alerta (mensaje 1) o el mensaje sin cambios (mensaje 2). | Antes de 9:00 hora local |
| Días 1–5, durante el día | Nada | Registra cada respuesta y su hora en la `capture-sheet.md`. | Registro en menos de 30 min |
| Días 1–5, 18:00 | La repregunta (si hubo C) y la pregunta del final del día | Envía el mensaje 3 (si aplica) y el mensaje 4. Registra las respuestas. | 18:00 hora local |
| Día 6 | Un mensaje de agradecimiento | Si el analista es cliente de KIU, verifica en el log del inventario la hora de cada "ajusté". | 1 h por analista |

## Pasos de la captura diaria

1. Abra la web del competidor de cada ruta. Use una ventana privada.
2. Busque la tarifa más baja disponible para las salidas a D-7, D-14 y D-30. Calcule D-n desde la fecha de captura.
3. Registre el horario de salida y la frecuencia semanal de la ruta.
4. Registre la hora exacta de cada captura.
5. Compare cada dato con la captura del día anterior para la **misma fecha de salida**.
6. Un dato diferente = un cambio. Escriba un ID al cambio: `{analista}-{día}-{n}`. Ejemplo: `A1-D2-03`.
7. Si la web no muestra el dato, registre `sin dato`. No alerte un cambio sin el dato de ayer y el dato de hoy.

## Cómo registrar la respuesta

| El analista escribe | `decisión_final` |
|---|---|
| A, o "ajusté", y el ajuste ya está hecho | `ajusté` |
| B, o "no toco", sin otra acción | `no toco` |
| C, o "lo miro después" | `sin decisión` (hasta la respuesta de las 18:00) |
| Una acción para otro día. Ejemplo: "1B, igualamos mañana" | `diferida` |

- Registre el texto del analista en `texto_original`. No cambie la letra que eligió.
- Si el texto dice que va a ajustar otro día, registre `diferida`, aunque la letra sea B.
- Para S1, una decisión `diferida` es igual a `sin decisión`. Si el ajuste se hace el mismo día de la alerta, cambie a `ajusté`.
- Si tiene una duda sobre una respuesta, pregunte al analista: `¿Ya hizo el ajuste hoy, o lo va a hacer otro día?`

## Repregunta de las 18:00

- Envíe la repregunta (mensaje 3) solo para los cambios con respuesta C.
- Si la decisión del mismo día llega por la repregunta, escriba `sí` en la columna `por_repregunta` de la capture sheet.
- La lectura informa S1 con la repregunta y S1 sin la repregunta. El umbral se aplica a S1 con la repregunta (sin cambios). S1 sin la repregunta muestra cuánto puede esperar un monitor automático, que no hace la repregunta.

## Reglas

- No envíe sugerencias. No diga qué conviene hacer. No conteste preguntas sobre qué hacer.
- Si el analista pregunta "¿qué harías vos?", conteste: `Para esta prueba no damos recomendaciones. Decida como lo hace siempre.`
- No cambie las rutas ni los competidores durante los 5 días.
- No envíe la alerta después de las 9:00. Si se atrasa, envíe igual y registre la hora real. Marque `atrasada` en la capture sheet.
- Use el mismo número de WhatsApp todos los días.

## Si falta material para leer el test

- Al final del día 5, cuente los cambios alertados y los analistas que terminaron la semana.
- Si hay menos de 15 cambios o menos de 4 analistas, agregue 1 semana con las mismas reglas.
- Si igual no llega, el resultado es `inconclusive`. No cambie el umbral.

## Cierre (día 6)

Envíe:

```
Terminamos la prueba. Muchas gracias por su tiempo, {nombre}.
Esto fue un servicio hecho a mano por nuestro equipo, no un producto.
Le vamos a contar lo que aprendimos.
```

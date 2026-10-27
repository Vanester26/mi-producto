# T1 · Mensajes de WhatsApp para el analista

Test: T1 `monitor-alertas` (concierge). Creencia #4.
Use estos textos sin cambios. No agregue sugerencias, gráficos ni explicaciones de "qué hacer".

## 1. Alerta de la mañana (con cambios)

Envíe antes de las 9:00, hora local del analista. Envíe un solo mensaje por día. Ponga un número a cada cambio.

```
Buenos días, {nombre}. Cambios del competidor desde ayer:

1) {ORIGEN}-{DESTINO} · {competidor}
   Qué cambió: {tarifa más baja | horario | frecuencia}
   Antes: {valor de ayer}  →  Ahora: {valor de hoy}
   Salida afectada: {DD/MM} ({D-7 | D-14 | D-30})

2) {ORIGEN}-{DESTINO} · {competidor}
   Qué cambió: ...
   Antes: ...  →  Ahora: ...
   Salida afectada: ...

Conteste cada número con una opción:
A = ajusté
B = no toco
C = lo miro después

Ejemplo: 1A 2C
```

Reglas para completar el mensaje:

- Tarifa: escriba la moneda y el valor. Ejemplo: `USD 89`.
- Horario: escriba la hora de salida y el número de vuelo. Ejemplo: `07:40 (XX123)`.
- Frecuencia: escriba los vuelos por semana. Ejemplo: `5 por semana`.
- Un cambio = una ruta + un competidor + un dato + una fecha de salida.
- No escriba "subió", "bajó", "conviene" ni "importante". Muestre solo el valor de antes y el valor de ahora.

## 2. Mensaje de la mañana (sin cambios)

```
Buenos días, {nombre}. Hoy no hay cambios del competidor en sus rutas desde ayer.
```

## 3. Repregunta de las 18:00

Envíe solo si el analista contestó C a uno o más cambios. Envíe a las 18:00, hora local del analista.

```
{nombre}, a la mañana marcó "lo miro después" en:
{n}) {ORIGEN}-{DESTINO} · {competidor} · {qué cambió}

¿Qué hizo? Conteste A (ajusté) o B (no toco).
Si todavía no decidió, conteste C.
```

## 4. Pregunta del final del día

Envíe todos los días a las 18:00, hora local del analista. Envíe también los días sin cambios.

```
Una última pregunta de hoy: ¿revisó a mano alguna de estas rutas?
{ORIGEN}-{DESTINO}, {ORIGEN}-{DESTINO}, ...

Conteste SÍ o NO.
```

## 5. Si el analista contesta con texto libre

- Si el texto dice claramente una de las tres opciones, registre esa opción. Copie el texto original en la capture sheet.
- Si no está claro, envíe una sola vez: `Gracias. Para el cambio {n}, ¿es A, B o C?`
- No pregunte por qué. No comente la decisión.

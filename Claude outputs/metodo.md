# T2 · Método (fijado antes de ver la ocupación)

Test: T2 `sugeridor-ajustes` (technical-test). Owner: tech / datos.
Creencia #1: "El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario."
Clave de respuestas: la ocupación real de la aerolínea propia (cliente de KIU, con permiso escrito).

**Fije este documento antes de la primera extracción de ocupación.** Escriba la fecha y el hash SHA-256 de este archivo en la capture sheet. No cambie este documento después. Si es necesario cambiarlo, registre el cambio y la razón en `product/corrections.md`.

## 1. Unidad

Un vuelo = una combinación de fecha de salida + número de vuelo + ruta. Solo vuelos operados por la aerolínea (sin códigos compartidos de otra aerolínea).

## 2. Datos de entrada

- `capturas.csv`: salida de `captura_tarifas.py`. Una fila por vuelo capturado a D-14.
- `ocupacion.csv`: salida de la extracción del inventario (ver `extraccion-ocupacion.md`).
- Vuelos con salida entre el 2026-11-11 y el 2026-11-28.

## 3. Clase (variable a predecir)

- `ocupacion` = pasajeros embarcados ÷ asientos de la configuración operada.
- **alta** si `ocupacion` ≥ 0,80. **baja** si `ocupacion` < 0,80.

## 4. Variables (4, y solo estas)

| Variable | Cálculo | Tipo |
|---|---|---|
| `tarifa_rel` | tarifa más baja del vuelo a D-14 ÷ mediana de esa tarifa en la misma ruta. La mediana se calcula **solo con los vuelos de entrenamiento**. Si la ruta no tiene vuelos de entrenamiento, use la mediana de todos los vuelos de entrenamiento. | numérica |
| `dia_semana` | día de la semana de la salida (lunes a domingo) | categórica |
| `franja` | hora de salida: madrugada 00:00–05:59 · mañana 06:00–11:59 · tarde 12:00–17:59 · noche 18:00–23:59 | categórica |
| `frecuencia` | vuelos distintos de la ruta con salida en la ventana de 7 días centrada en la salida (−3 a +3 días), contados en `capturas.csv`. Si la ventana tiene menos de 7 días con captura, escale: conteo ÷ días con captura × 7. | numérica |

La marca tarifaria se captura, pero **no** es una variable.

## 5. Exclusiones (aplicar antes de partir)

Excluya y cuente:

1. Vuelos cancelados.
2. Vuelos sin captura a D-14, o con estado `sin_dato` o `error`.
3. Vuelos con estado `agotado` (sin tarifa a la venta a D-14). Si estos son > 5 % del total, regístrelo en la capture sheet como riesgo para la lectura.
4. Vuelos sin ocupación en el inventario.
5. Filas con una moneda diferente a la moneda principal de la ruta.

## 6. Partición 70/30 por fecha

1. Ordene los vuelos por fecha de salida.
2. Calcule el porcentaje acumulado de vuelos por fecha.
3. La fecha de corte es la primera fecha donde el acumulado es ≥ 70 %. Esa fecha va a entrenamiento.
4. Todos los vuelos de una misma fecha van al mismo conjunto.
5. Hold-out = los vuelos con fecha posterior a la fecha de corte.

## 7. Modelo

- Regresión logística (scikit-learn `LogisticRegression`, `C=1.0`, `max_iter=1000`, sin ponderación de clases).
- `tarifa_rel` y `frecuencia`: estandarizadas con media y desvío de entrenamiento.
- `dia_semana` y `franja`: one-hot. Una categoría que no aparece en entrenamiento queda en cero.
- Umbral de probabilidad: 0,5.
- Sin búsqueda de hiperparámetros. Sin otros modelos.

## 8. Métrica

- **Precisión (accuracy)** en el hold-out = predicciones correctas ÷ vuelos del hold-out.
- **Clase mayoritaria** = la clase más frecuente en entrenamiento. Su precisión de referencia = la proporción de esa clase en el hold-out.
- **Diferencia** = precisión del modelo − precisión de referencia, en puntos porcentuales, con 1 decimal.

## 9. Mínimo para leer

- ≥ 150 vuelos en el hold-out.
- ≥ 20 % de vuelos en cada clase, en el hold-out.
- Si no se cumple: `inconclusive`.

## 10. Regla de decisión (del archivo de tests, sin cambios)

| Condición | Decisión |
|---|---|
| precisión ≥ 70 % **y** diferencia ≥ 10,0 | continue |
| diferencia entre 5,0 y 9,9 | change: A2 sugiere por reglas explícitas (A3 dentro de software), sin inferir ocupación |
| diferencia < 5,0 | discard: se descarta la inferencia de ocupación de A2. #1 queda weakened |

`analisis.py` calcula todo esto.

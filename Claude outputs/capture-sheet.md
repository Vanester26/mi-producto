# T2 · Capture sheet

Test: T2 `sugeridor-ajustes` (technical-test). Creencia #1. Owner: tech / datos.
Procedencia esperada: `real` (datos reales de 1 aerolínea cliente).

## 1. Antes de la captura

| Punto | Valor |
|---|---|
| Aerolínea (código) | |
| Tipo | low cost · regional |
| Vuelos por día (promedio en las rutas elegidas) | (≥ 30) |
| Permiso escrito: fecha y quién firma | |
| Rutas incluidas (`rutas.json`) | |
| ¿El inventario guarda historial de clases o tarifas? | sí · no |
| Si es sí: meses de historia usados | |
| Fuente de `capturas.csv` | captura diaria · historial del inventario |
| `metodo.md` fijado: fecha | |
| `metodo.md` fijado: SHA-256 | |

## 2. Registro diario de la captura

Una fila por día. Complete después de cada corrida.

| fecha_captura | fecha_salida (D-14) | hora de la corrida | filas | filas con `error` o `sin_dato` | vuelos `agotado` | nota |
|---|---|---|---|---|---|---|
| 2026-10-28 | 2026-11-11 | | | | | |
| … | … | | | | | |
| 2026-11-14 | 2026-11-28 | | | | | |

Si un día falla, corra otra vez el mismo día con `--fecha-captura`. No capture un día tarde: la tarifa ya no es la de D-14. Registre el día como perdido.

## 3. Extracción de la ocupación

| Punto | Valor |
|---|---|
| Fecha de extracción (después de 2026-11-28) | |
| Vuelos extraídos | |
| Vuelos con `embarcados` > `asientos` | |
| Quién extrajo | |

## 4. Resultado (copiar de `resultado.json`)

| Punto | Valor |
|---|---|
| Vuelos total (salidas 2026-11-11 a 2026-11-28) | |
| Excluidos: cancelados | |
| Excluidos: sin captura a D-14 | |
| Excluidos: agotados (y % del total; > 5 % = riesgo) | |
| Excluidos: sin ocupación | |
| Excluidos: otra moneda / sin tarifa | |
| Fecha de corte 70/30 | |
| n entrenamiento | |
| n hold-out (≥ 150) | |
| % clase alta en hold-out (20 %–80 %) | |
| Clase mayoritaria (entrenamiento) | |
| Precisión de referencia (%) | |
| Precisión del modelo en hold-out (%) | |
| Diferencia (puntos) | |
| Resultado | passed · failed · inconclusive |
| Decisión según la regla | continue · change · discard |

Matriz de confusión (hold-out):

| | predicho alta | predicho baja |
|---|---|---|
| **real alta** | | |
| **real baja** | | |

## 5. Notas para el análisis

- La clave es la ocupación de la aerolínea propia, no la del competidor. Un `passed` habilita el paso siguiente (competidor con DGAC/Aerocivil). No prueba #1 para el competidor.
- Registre aquí todo lo que no se hizo según `metodo.md`.

# T2 · Capture sheet

Test: T2 `sugeridor-ajustes` (technical-test). Creencia #1. Owner: tech / datos.
Procedencia esperada: `real` (datos reales de 1 aerolínea cliente).

**Procedencia de este archivo:** `real` · `ensayo` (marque una). Si es un ensayo, agregue `-ensayo` al nombre del archivo.

## 1. Antes de la captura

| Punto | Valor |
|---|---|
| Aerolínea (código) | |
| Tipo | low cost · regional |
| Vuelos por día (promedio en las rutas elegidas) | (≥ 30) |
| Permiso escrito: fecha y quién firma | |
| Rutas incluidas (`rutas.json`) | |
| ¿El inventario guarda historial de clases o tarifas? | sí: log diario de disponibilidad por clase y nivel tarifario, 12 meses (respuesta del cliente, 2026-10-26) |
| Si es sí: meses de historia usados | 6 |
| Fuente de `capturas.csv` (marque **una sola**) | historial del inventario |
| Si es historial: período de salidas usado (desde – hasta) | 2026-04-26 – 2026-10-25 |
| `metodo.md` fijado: fecha | |
| `metodo.md` fijado: SHA-256 | |

**Una sola fuente.** Si el inventario guarda el historial, use el historial y escriba el período. Con el historial, no complete la sección 2. Si no lo guarda, use solo la captura diaria y escriba "no aplica" en el período. No mezcle las dos fuentes.

**Hash del método.** Calcule el SHA-256 de `metodo.md` el día que lo fija, antes de la primera extracción. No copie un valor de otro archivo.

- Windows (PowerShell): `Get-FileHash metodo.md -Algorithm SHA256`
- Linux o Mac: `sha256sum metodo.md`

El hash `e3b0c442…b855` es el hash de un archivo vacío. Si obtiene ese valor, el archivo no se leyó bien. Hash de la versión actual de `metodo.md` (2026-10-26, período de 6 meses de historial): `edd0ae350fe204aa91c841e988f2ffd34766229e7389f4f6f0619cd5ae0b6b70`. Si el hash del día que fija el método es diferente, alguien cambió el archivo: registre el cambio en `product/corrections.md`.

## 2. Registro diario de la captura

**No aplica para T2:** la fuente es el historial del inventario (ver `historial-tarifas.md`). Use esta sección solo si vuelve a la captura diaria.

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
| Fecha de extracción (después de fijar `metodo.md`) | |
| Vuelos extraídos | |
| Vuelos con `embarcados` > `asientos` | |
| Quién extrajo | |

## 4. Resultado (copiar de `resultado.json`)

| Punto | Valor |
|---|---|
| Vuelos total (salidas 2026-04-26 a 2026-10-25) | |
| Excluidos: cancelados | |
| Excluidos: sin captura a D-14 | |
| Excluidos: agotados (y % del total; > 5 % = riesgo) | |
| Excluidos: sin ocupación | |
| Excluidos: otra moneda / sin tarifa | |
| Lista de excluidos (`excluidos.csv`): fecha de salida, vuelo y motivo de cada uno | adjunte |
| Fecha de corte 70/30 | |
| n entrenamiento | |
| n hold-out (≥ 150) | |
| Control de la partición (`control_particion` en `resultado.json`) | ok · error |
| % clase alta en hold-out (20 %–80 %) | |
| Clase mayoritaria (entrenamiento) | |
| Precisión de referencia (%) — copie el valor de `resultado.json`, no lo calcule a mano | |
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
- **Controles antes de escribir el resultado:**
  1. n hold-out ≤ (días de salida después de la fecha de corte) × vuelos por día. Ejemplo: con 5 días después del corte y 32 vuelos/día, el máximo es 5 × 32 = 160.
  2. La precisión de referencia = la proporción de la clase mayoritaria de entrenamiento en el hold-out. Con la matriz: si la mayoritaria es `baja`, referencia = (real baja) ÷ n hold-out.
  3. Cada vuelo "sin captura a D-14" tiene un día con filas perdidas o con `error` / `sin_dato` en la sección 2.
- **Sin conclusiones fuera del test.** Escriba solo el resultado y la decisión según la regla. Un `passed` vale para la ocupación de la aerolínea propia. El paso siguiente es el test sobre el competidor, no la integración ni el producto.

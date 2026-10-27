# T2 · Tarifa a D-14 desde el historial del inventario

Owner: tech / datos. Fuente: el log diario de disponibilidad por clase de reserva y nivel tarifario de la aerolínea cliente de KIU (12 meses de historia, respuesta del cliente del 2026-10-26).
Este documento reemplaza a `captura_tarifas.py` para T2. El script queda como alternativa si el historial no sirve.

## Qué construir

Un archivo `capturas.csv` con las mismas columnas que la salida de `captura_tarifas.py`. `analisis.py` lee este archivo sin cambios.

- Vuelos de las rutas de `rutas.json` con salida entre el **2026-04-26** y el **2026-10-25**.
- Una fila por vuelo (`fecha_salida` + `vuelo`).

## Cómo calcular la tarifa a D-14

Para cada vuelo:

1. Tome el estado del log del día D-14 (14 días antes de la salida). Use la misma hora para todos los vuelos: el estado a las **06:00**, hora local del origen. Si el log tiene solo un estado por día, use ese estado y escriba la regla en la capture sheet.
2. Busque las clases de reserva con disponibilidad > 0 en ese momento.
3. La tarifa a D-14 es la tarifa del nivel publicado **más bajo** entre esas clases.
4. Use la tarifa que ve el pasajero en la web de la aerolínea: el mismo canal, la misma moneda y el mismo tratamiento de impuestos y cargos. Si el log tiene solo la tarifa base, use la tarifa base en todos los vuelos y escriba esto en la capture sheet.

## Columnas

| Columna | Valor |
|---|---|
| `fecha_captura` | fecha de D-14 (AAAA-MM-DD) |
| `hora_captura` | hora del estado del log que usó (HH:MM) |
| `aerolinea` | código de la aerolínea |
| `ruta` | ORIGEN-DESTINO, códigos IATA |
| `vuelo` | mismo formato que `ocupacion.csv`. Ej. `XX123` |
| `fecha_salida` | AAAA-MM-DD |
| `hora_salida` | HH:MM, hora local del origen |
| `tarifa` | tarifa del paso 3. Vacía si `estado` no es `ok` |
| `moneda` | moneda de la tarifa |
| `marca_tarifaria` | marca o familia del nivel tarifario, si el log la tiene |
| `estado` | `ok` · `agotado` (ninguna clase con disponibilidad a D-14) · `sin_dato` (el log no tiene ese día o ese vuelo) |
| `fuente_url` | `historial-inventario` |

## Controles antes de entregar

- Un vuelo = una fila. Sin duplicados por `fecha_salida` + `vuelo`.
- Cuente las filas `sin_dato` por mes. Si un mes tiene > 5 % de filas `sin_dato`, escríbalo en la capture sheet.
- Revise 10 vuelos al azar: la tarifa del paso 3 tiene sentido frente a las tarifas publicadas de la ruta en esa fecha.
- **No lea la ocupación** para construir este archivo. La ocupación se extrae aparte (`extraccion-ocupacion.md`), después de fijar `metodo.md`.

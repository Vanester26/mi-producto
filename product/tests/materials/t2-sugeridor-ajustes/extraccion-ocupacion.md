# T2 · Extracción de la ocupación real (clave de respuestas)

Owner: tech / datos. Fuente: el inventario de la aerolínea cliente de KIU, con su permiso escrito.

## Antes de empezar (paso 6 del test)

Verifique esto **antes del 2026-10-28**:

1. ¿El inventario guarda el historial de clases abiertas o de tarifas por vuelo y por día? `sí / no`
2. Si es sí: ¿cuántos meses de historia hay? ¿Se puede leer la tarifa más baja a la venta a D-14 para cada vuelo?

Si las dos respuestas son sí, use 3 a 6 meses de historia. No espere la captura. Registre la decisión en la capture sheet. El método no cambia: solo cambia la fuente de `capturas.csv` y el rango de fechas.

**Respuesta del cliente (2026-10-26):** el inventario guarda el log diario de disponibilidad por clase y nivel tarifario, con 12 meses de historia. Se usan 6 meses: salidas del 2026-04-26 al 2026-10-25.

## Cuándo extraer

- Extraiga **después** de fijar `metodo.md` (fecha y hash en la capture sheet).
- Todos los vuelos del período ya volaron. Extraiga solo **después** de registrar la fecha y el hash de `metodo.md` en la capture sheet.
- Nadie del equipo de análisis mira la ocupación de esos vuelos antes de esa fecha.

## Qué extraer

Todos los vuelos de las rutas de `rutas.json` con salida entre el 2026-04-26 y el 2026-10-25.

Archivo `ocupacion.csv`, UTF-8, separador coma:

| Columna | Qué contiene |
|---|---|
| `fecha_salida` | AAAA-MM-DD, hora local del origen |
| `ruta` | ORIGEN-DESTINO, códigos IATA |
| `vuelo` | número de vuelo con el código de la aerolínea, sin espacios. Ej. `XX123` |
| `estado_vuelo` | `operado` · `cancelado` |
| `asientos` | asientos de la configuración **operada** (no la planificada) |
| `embarcados` | pasajeros embarcados, sin infantes sin asiento |

`analisis.py` calcula `ocupacion = embarcados ÷ asientos`.

## Controles

- Un vuelo = una fila. Sin filas duplicadas por `fecha_salida` + `vuelo`.
- `asientos` > 0 en todos los vuelos operados.
- `embarcados` ≤ `asientos` (si no, registre el vuelo en la capture sheet).
- El formato de `vuelo` es igual al formato de `capturas.csv`.

## Datos que no se extraen

No extraiga nombres, PNR ni datos de pasajeros. Solo los conteos por vuelo.

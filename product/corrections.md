# Correcciones

Registro vivo de lo que el humano corrigió de lo que propuso la IA. Cada `/review-evidence` agrega una entrada fechada al final.

## 2026-10-25

- Primera revisión de evidencia (`/review-evidence`). Sin correcciones esta semana.

## 2026-10-26

- T2 (`sugeridor-ajustes`, product/tests/2026-10-26-2038-reaccion-tardia-competencia.md): Vanessa Ballester sacó la variable "cambio de tarifa en los 7 días anteriores" del método. Razón: la captura solo toma la salida a D-14, así que no hay tarifa a D-21 para calcularla. Agregar la captura a D-21 dejaba ~99 vuelos en el hold-out, menos que el mínimo de 150. El cambio se hizo antes de capturar datos. El umbral y la regla de decisión no cambian.
- T2 (`sugeridor-ajustes`, product/tests/2026-10-26-2038-reaccion-tardia-competencia.md): Vanessa Ballester decidió omitir el paso 6 (tech verifica si el inventario guarda el historial). T2 usa solo la captura diaria desde el 2026-10-28. Razón: la captura diaria entrega el resultado el 2026-12-04, antes de la decisión sobre la oportunidad (2026-12-15). El método, el umbral y la regla de decisión no cambian.
- T2 (`sugeridor-ajustes`): la entrada anterior ya no aplica. El cliente contestó el 2026-10-26: el inventario guarda 12 meses de log diario de disponibilidad por clase y nivel tarifario. Vanessa Ballester eligió usar 6 meses de historial (salidas del 2026-04-26 al 2026-10-25) en lugar de la captura diaria. `metodo.md` §2 cambió (fuente y período) antes de fijar el método y antes de extraer la ocupación. Las variables, el modelo, el umbral y la regla de decisión no cambian.

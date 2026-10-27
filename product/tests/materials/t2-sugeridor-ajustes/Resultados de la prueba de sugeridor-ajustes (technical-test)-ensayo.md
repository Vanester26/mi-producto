# **Resultados de la prueba de sugeridor-ajustes (technical-test)**

> **Procedencia: `synthetic` (ensayo).** Este archivo no es evidencia real. Los datos son de práctica. No lo use para mover creencias. Análisis: `product/tests/2026-10-26-2038-reaccion-tardia-competencia.md`.


Registro completo y resultado de la prueba técnica T2 `sugeridor-ajustes` (evaluación de la Creencia \#1: "El precio, el horario y la frecuencia públicos del competidor predicen su ocupación real lo suficientemente bien como para basar en eso una recomendación de ajuste de inventario").Los datos corresponden al período de captura a D-14 (2026-10-28 al 2026-11-14) y salidas operadas (2026-11-11 al 2026-11-28) de la aerolínea cliente de KIU System Solution.

# **1\. Antes de la captura (Ficha técnica)**

| Punto | Valor |
| :---- | :---- |
| Aerolínea (código) | Z8 (Paranair) |
| Tipo | regional |
| Vuelos por día (promedio en rutas elegidas) | 32 |
| Permiso escrito: fecha y quién firma | 2026-10-20 · Gerencia Operativa |
| Rutas incluidas (`rutas.json`) | ASU-CDB, ASU-EZE, ASU-MVD, ASU-IAG, ASU-VVI |
| ¿El inventario guarda historial de clases o tarifas? | sí |
| Meses de historia usados | 3 meses |
| Fuente de `capturas.csv` | captura diaria via `captura_tarifas.py` |
| `metodo.md` fijado: fecha | 2026-10-27 |
| `metodo.md` fijado: SHA-256 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

# **2\. Registro diario de la captura (D-14)**

| Fecha Captura | Fecha Salida (D-14) | Hora Corrida | Filas | Filas con error / sin\_dato | Vuelos agotado | Nota |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-10-28 | 2026-11-11 | 06:00 | 32 | 0 | 1 | Captura limpia |
| 2026-10-29 | 2026-11-12 | 06:05 | 32 | 0 | 0 | Ok |
| 2026-10-30 | 2026-11-13 | 06:00 | 32 | 1 | 0 | Re-intentado a las 06:15 |
| 2026-10-31 | 2026-11-14 | 06:00 | 32 | 0 | 1 | Ok |
| 2026-11-01 | 2026-11-15 | 06:02 | 32 | 0 | 0 | Ok |
| 2026-11-02 | 2026-11-16 | 06:00 | 32 | 0 | 2 | Ok |
| 2026-11-03 | 2026-11-17 | 06:01 | 32 | 0 | 0 | Ok |
| 2026-11-04 | 2026-11-18 | 06:00 | 32 | 0 | 1 | Ok |
| 2026-11-05 | 2026-11-19 | 06:00 | 32 | 0 | 0 | Ok |
| 2026-11-06 | 2026-11-20 | 06:00 | 32 | 0 | 1 | Ok |
| 2026-11-07 | 2026-11-21 | 06:03 | 32 | 0 | 0 | Ok |
| 2026-11-08 | 2026-11-22 | 06:00 | 32 | 0 | 0 | Ok |
| 2026-11-09 | 2026-11-23 | 06:00 | 32 | 0 | 1 | Ok |
| 2026-11-10 | 2026-11-24 | 06:00 | 32 | 0 | 0 | Ok |
| 2026-11-11 | 2026-11-25 | 06:00 | 32 | 0 | 1 | Ok |
| 2026-11-12 | 2026-11-26 | 06:00 | 32 | 0 | 0 | Ok |
| 2026-11-13 | 2026-11-27 | 06:00 | 32 | 0 | 0 | Ok |
| 2026-11-14 | 2026-11-28 | 06:00 | 32 | 0 | 1 | Cierre de captura |

# **3\. Extracción de la ocupación**

| Punto | Valor |
| :---- | :---- |
| Fecha de extracción | 2026-11-30 |
| Vuelos extraídos | 576 |
| Vuelos con embarcados \> asientos | 0 |
| Quién extrajo | Equipo de Datos / PSS KIU |

# **4\. Resultado (Salida de `analisis.py` / `resultado.json`)**

| Punto | Valor |
| :---- | :---- |
| Vuelos total (salidas 2026-11-11 a 2026-11-28) | 576 |
| Excluidos: cancelados | 12 |
| Excluidos: sin captura a D-14 | 8 |
| Excluidos: agotados | 9 (1.56 % del total) |
| Excluidos: sin ocupación | 0 |
| Excluidos: otra moneda / sin tarifa | 0 |
| Fecha de corte 70/30 | 2026-11-23 |
| n entrenamiento | 383 |
| n hold-out | 164 (Cumple ≥ 150\) |
| % clase alta en hold-out | 43.9 % (Cumple 20 % – 80 %) |
| Clase mayoritaria (entrenamiento) | baja |
| Precisión de referencia (%) | 57.3 % |
| Precisión del modelo en hold-out (%) | 74.4 % |
| **Diferencia (puntos)** | **\+17.1 puntos** |
| **Resultado** | **`passed`** |
| **Decisión según la regla** | **`continue`** |

## **Matriz de confusión (hold-out)**

|  | Predicho Alta | Predicho Baja |
| :---- | :---- | :---- |
| **Real Alta** | 58 | 14 |
| **Real Baja** | 28 | 64 |

# **5\. Notas para el análisis**

1. **Veredicto Técnico (`passed` / `continue`):** El modelo de regresión logística alcanzó una precisión del **74.4 %** frente al **57.3 %** de la clase mayoritaria de referencia, logrando una mejora de **\+17.1 puntos porcentuales** (cumpliendo holgadamente el requisito de \$\\ge 70%\$ de precisión y \$\\ge 10.0\$ puntos de diferencia).  
2. **Evaluación de la Creencia \#1:** La tarifa pública a D-14 combinada con la frecuencia y variables temporales demuestra poder predictivo sobre la ocupación real del vuelo.  
3. **Continuidad del Producto:** Este resultado autoriza mantener el enfoque de recomendación directa de ajustes de inventario para A2 (`sugeridor-ajustes`), pasando a la fase de integración con datos competitivos.


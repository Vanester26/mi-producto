# **Resultados de la prueba de monitor-alertas (concierge)**

> **Procedencia: `synthetic` (ensayo).** Este archivo no es evidencia real. Los datos son de práctica. No lo use para mover creencias. Análisis: `product/tests/2026-10-26-2038-reaccion-tardia-competencia.md`.


*Hojas de registro completas de la prueba de `monitor-alertas`: 5 analistas de RM, 18 cambios alertados, durante una semana (5 días hábiles). Se usan con `/analyze-solution-tests`.*

*En el caso del proyecto, estos resultados son de práctica/ensayo para descubrir patrones de adopción y respuesta.*

*Las fechas corresponden a la semana de prueba (día 1 a día 5 hábiles: 16 al 20 de noviembre de 2026).*

# **Quiénes participaron**

| Analista | Aerolínea | Tipo | Flota | Perfil ≤10 aviones | Datos competitivos pagos | Aplica ajustes sin aprobación | Canal de reclutamiento | Procedencia | Cliente KIU / Log disponible | Días completados | Terminó la semana |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Ignacio Soto | FlyBondi (Argentina) | low cost | 12 | no | no | sí | encuesta opt-in | segment member | sí | 5 | sí |
| Rene Avila | Paranair (Paraguay) | regional | 4 | sí | no | sí | account manager KIU | segment member | sí | 5 | sí |
| Richard Rodriguez | Rutaca Airlines (Venezuela) | regional | 6 | sí | no | sí | account manager KIU | segment member | sí | 5 | sí |
| Maria Urioste | Star Perú (Perú) | regional | 8 | sí | no | no | encuesta opt-in | stand-in | no | 5 | sí |
| Cristian Troche | JetSMART (Chile) | low cost | 18 | no | no | sí | encuesta opt-in | segment member | no | 5 | sí |

# **Definiciones**

* **Mismo día:** La decisión (`ajusté` o `no toco`) fue tomada y registrada en la misma fecha del envío de la alerta.  
* **Respuesta 1:** Primera respuesta enviada por el analista tras la alerta matutina (A \= ajusté, B \= no toco, C \= lo miro después).  
* **Respuesta 18h:** Estado reportado tras la repregunta del final del día (18:00 hs).  
* **Verificación log:** Cotejo realizado en el PSS (KIU) de la hora exacta de carga del ajuste contra la respuesta del analista.

# **Registro, una fila por cambio alertado (Hoja 2 \- S1)**

| ID Cambio | Analista | Fecha Envío | Hora Envío | Atrasada | Respuesta 1 | Hora Resp 1 | Respuesta 18h | Hora Resp 18h | Decisión Final | Fecha Decisión | Mismo Día | Verificación Log | Hora Ajuste Log | Texto Original |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Ignacio Soto-D1-01 | Ignacio Soto | 2026-11-16 | 08:30 | no | A | 09:15 | no aplica | — | ajusté | 2026-11-16 | sí | coincide | 09:22 | 1A |
| Ignacio Soto-D2-01 | Ignacio Soto | 2026-11-17 | 08:25 | no | B | 08:50 | no aplica | — | no toco | 2026-11-17 | sí | no hay log | — | 1B, igualamos mañana |
| Ignacio Soto-D3-01 | Ignacio Soto | 2026-11-18 | 08:35 | no | C | 09:40 | A | 18:10 | ajusté | 2026-11-18 | sí | coincide | 17:45 | 1A |
| Ignacio Soto-D4-01 | Ignacio Soto | 2026-11-19 | 08:20 | no | A | 08:45 | no aplica | — | ajusté | 2026-11-19 | sí | coincide | 09:02 | 1A cerramos Q |
| Ignacio Soto-D5-01 | Ignacio Soto | 2026-11-20 | 08:30 | no | B | 09:10 | no aplica | — | no toco | 2026-11-20 | sí | no hay log | — | 1B |
| Rene Avila-D1-01 | Rene Avila | 2026-11-16 | 08:40 | no | A | 09:30 | no aplica | — | ajusté | 2026-11-16 | sí | coincide | 09:45 | 1A |
| Rene Avila-D2-01 | Rene Avila | 2026-11-17 | 08:45 | no | C | 10:15 | B | 18:20 | no toco | 2026-11-17 | sí | no hay log | — | 1B |
| Rene Avila-D3-01 | Rene Avila | 2026-11-18 | 08:40 | no | A | 09:05 | no aplica | — | ajusté | 2026-11-18 | sí | coincide | 09:18 | 1A |
| Rene Avila-D4-01 | Rene Avila | 2026-11-19 | 08:50 | no | A | 09:20 | no aplica | — | ajusté | 2026-11-19 | sí | coincide | 09:35 | 1A |
| Richard Rodriguez-D1-01 | Richard Rodriguez | 2026-11-16 | 08:55 | no | B | 11:00 | no aplica | — | no toco | 2026-11-16 | sí | no hay log | — | 1B no tocamos tarifa |
| Richard Rodriguez-D2-01 | Richard Rodriguez | 2026-11-17 | 08:50 | no | C | 09:50 | C | 18:15 | sin decisión | 2026-11-18 | no | no hay log | — | 1C no llegué a verlo |
| Richard Rodriguez-D3-01 | Richard Rodriguez | 2026-11-18 | 08:45 | no | A | 09:10 | no aplica | — | ajusté | 2026-11-18 | sí | coincide | 09:28 | 1A |
| Richard Rodriguez-D5-01 | Richard Rodriguez | 2026-11-20 | 08:50 | no | A | 09:35 | no aplica | — | ajusté | 2026-11-20 | sí | coincide | 09:50 | 1A |
| Maria Urioste-D2-01 | Maria Urioste | 2026-11-17 | 09:10 | sí | C | 11:30 | B | 18:30 | no toco | 2026-11-17 | sí | no hay log | — | 1B |
| Maria Urioste-D4-01 | Maria Urioste | 2026-11-19 | 08:55 | no | C | 10:40 | C | 18:25 | sin decisión | 2026-11-20 | no | no hay log | — | 1C esperando aprobación |
| Cristian Troche-D1-01 | Cristian Troche | 2026-11-16 | 08:30 | no | A | 08:55 | no aplica | — | ajusté | 2026-11-16 | sí | no hay log | — | 1A |
| Cristian Troche-D3-01 | Cristian Troche | 2026-11-18 | 08:35 | no | A | 09:05 | no aplica | — | ajusté | 2026-11-18 | sí | no hay log | — | 1A |
| Cristian Troche-D5-01 | Cristian Troche | 2026-11-20 | 08:40 | no | B | 09:15 | no aplica | — | no toco | 2026-11-20 | sí | no hay log | — | 1B |

# **Revisión manual por día (Hoja 3 \- S2)**

| Analista | Día | Fecha | ¿Revisó a mano? | Hora Respuesta | Texto Original |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Ignacio Soto | 1 | 2026-11-16 | NO | 18:05 | NO |
| Ignacio Soto | 2 | 2026-11-17 | NO | 18:10 | NO |
| Ignacio Soto | 3 | 2026-11-18 | NO | 18:02 | NO |
| Ignacio Soto | 4 | 2026-11-19 | NO | 18:15 | NO |
| Ignacio Soto | 5 | 2026-11-20 | NO | 18:00 | NO |
| Rene Avila | 1 | 2026-11-16 | NO | 18:08 | NO |
| Rene Avila | 2 | 2026-11-17 | NO | 18:20 | NO |
| Rene Avila | 3 | 2026-11-18 | NO | 18:04 | NO |
| Rene Avila | 4 | 2026-11-19 | SÍ | 18:12 | SÍ, miré el horario de la tarde |
| Rene Avila | 5 | 2026-11-20 | NO | 18:06 | NO |
| Richard Rodriguez | 1 | 2026-11-16 | NO | 18:15 | NO |
| Richard Rodriguez | 2 | 2026-11-17 | SÍ | 18:22 | SÍ, entré a la web por la duda |
| Richard Rodriguez | 3 | 2026-11-18 | NO | 18:10 | NO |
| Richard Rodriguez | 4 | 2026-11-19 | NO | 18:05 | NO |
| Richard Rodriguez | 5 | 2026-11-20 | NO | 18:11 | NO |
| Maria Urioste | 1 | 2026-11-16 | SÍ | 18:30 | SÍ |
| Maria Urioste | 2 | 2026-11-17 | SÍ | 18:35 | SÍ |
| Maria Urioste | 3 | 2026-11-18 | SÍ | 18:18 | SÍ |
| Maria Urioste | 4 | 2026-11-19 | SÍ | 18:28 | SÍ |
| Maria Urioste | 5 | 2026-11-20 | NO | 18:14 | NO |
| Cristian Troche | 1 | 2026-11-16 | NO | 18:02 | NO |
| Cristian Troche | 2 | 2026-11-17 | NO | 18:09 | NO |
| Cristian Troche | 3 | 2026-11-18 | NO | 18:15 | NO |
| Cristian Troche | 4 | 2026-11-19 | SÍ | 18:21 | SÍ, chequeé una tarifa |
| Cristian Troche | 5 | 2026-11-20 | NO | 18:05 | NO |

# **Consolidado y Lectura de Métricas**

| Métrica / Criterio | Valor Obtenido | Requisito / Umbral | Estado |
| :---- | :---- | :---- | :---- |
| Total de cambios alertados | 18 | ≥ 15 | Cumplido |
| Analistas que completaron la semana | 5 | ≥ 4 | Cumplido |
| Cambios con decisión el mismo día | 16 | — | — |
| **S1 (Decisión el mismo día)** | **88.8 %** (16/18) | **≥ 70 %** | **PASSED** |
| Analistas con NO en ≥ 3 días de revisión | 4 (Ignacio Soto, Rene Avila, Richard Rodriguez, Cristian Troche) | — | — |
| **S2 (Reducción de revisión manual)** | **4 de 5** | **≥ 3 de 5** | **PASSED** |
| Semana extra agregada | No | — | No requerida |
| **Veredicto Final** | **PASSED (continue)** | — | **Creencia \#4 Confirmada** |

# **Notas dejadas por los analistas**

* **Ignacio Soto, D1:** "Cargué el ajuste apenas me llegó la alerta a las 09:15 hs. Me ahorró entrar a las 3 páginas de la competencia."  
* **Ignacio Soto, D4:** "Cerramos la clase Q en la ruta BUE-MDZ. La notificación directa al celular acelera todo."  
* **Rene Avila, D4:** "Entré a revisar manualmente solo para confirmar el horario del vuelo de la tarde de la competencia."  
* **Richard Rodriguez, D2:** "Tuve un día complicado de reuniones y no llegué a ver el ajuste a tiempo."  
* **Maria Urioste, D4:** "Tengo que pedirle autorización a mi jefe antes de tocar la tarifa en el sistema, por eso marqué 'lo miro después'."  
* **Cristian Troche, D3:** "Confirmado el ajuste. No necesitamos volver a abrir la web a mano cuando nos llega el reporte consolidado a la mañana."


# T1 · Capture sheet

Test: T1 `monitor-alertas` (concierge). Creencia #4.
Esta planilla da los datos para leer S1, S2 y el mínimo del test. Complete las tres hojas.

**Procedencia de este archivo:** `real` · `ensayo` (marque una). Si es un ensayo, agregue `-ensayo` al nombre del archivo. No use nombres reales de aerolíneas ni de personas en un ensayo.

## Hoja 1 · Participantes

Una fila por analista.

| Columna | Qué escribir |
|---|---|
| analista | ID (A1, A2, …) |
| aerolínea | Nombre |
| tipo | `low cost` · `regional` |
| flota | Cantidad de aviones |
| perfil ≤10 aviones | `sí` · `no` (Diego o Carmen) |
| datos competitivos pagos | `no` · `sí` (si es sí, no es del segmento) |
| aplica ajustes sin aprobación | `sí` · `no` (si es no, no es del segmento) |
| canal de reclutamiento | `encuesta opt-in` · `account manager KIU` |
| procedencia | `segment member` · `stand-in` |
| cliente KIU / log disponible | `sí` · `no` |
| días completados | 0 a 5 (o a 10 si se agrega 1 semana) |
| terminó la semana | `sí` · `no` |

| analista | aerolínea | tipo | flota | perfil ≤10 aviones | datos competitivos pagos | aplica ajustes sin aprobación | canal de reclutamiento | procedencia | cliente KIU / log disponible | días completados | terminó la semana |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

## Hoja 2 · Cambios alertados (S1)

Una fila por cambio alertado.

| Columna | Qué escribir |
|---|---|
| id_cambio | Igual que en la planilla de recolección |
| analista | ID |
| fecha_envío | AAAA-MM-DD, hora local del analista |
| hora_envío | HH:MM |
| atrasada | `sí` si se envió después de las 9:00 |
| respuesta_1 | `A` · `B` · `C` · `sin respuesta` |
| hora_respuesta_1 | HH:MM |
| respuesta_18h | `A` · `B` · `C` · `sin respuesta` · `no aplica` |
| hora_respuesta_18h | HH:MM |
| decisión_final | `ajusté` · `no toco` · `diferida` · `sin decisión` (ver "Cómo registrar la respuesta" en el guion) |
| por_repregunta | `sí` si la decisión del mismo día llegó por la repregunta de las 18:00. Si no, `no` |
| fecha_decisión | AAAA-MM-DD |
| mismo_día | `sí` si decisión_final es `ajusté` o `no toco` y fecha_decisión = fecha_envío |
| verificación_log | `coincide` · `no coincide` · `no hay log` (solo para "ajusté") |
| hora_ajuste_log | HH:MM (si hay log) |
| texto_original | El texto que escribió el analista |

| id_cambio | analista | fecha_envío | hora_envío | atrasada | respuesta_1 | hora_respuesta_1 | respuesta_18h | hora_respuesta_18h | decisión_final | por_repregunta | fecha_decisión | mismo_día | verificación_log | hora_ajuste_log | texto_original |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | |

## Hoja 3 · Revisión manual por día (S2)

Una fila por analista y por día. Complete también los días sin cambios.

| analista | día (1–5) | fecha | ¿revisó a mano? (`SÍ` · `NO` · `sin respuesta`) | hora_respuesta | texto_original |
|---|---|---|---|---|---|
| | | | | | |

## Lectura (no cambie los umbrales)

1. **Mínimo para leer.** Total de cambios alertados (filas de la hoja 2) ≥ 15. Analistas con "terminó la semana" = `sí` ≥ 4. Si no llega, agregue 1 semana. Si igual no llega: `inconclusive`.
2. **S1** = cambios con mismo_día = `sí` ÷ total de cambios alertados. Umbral: ≥ 70 %.
3. **S2** = cantidad de analistas con `NO` en ≥ 3 de los 5 días (hoja 3). Umbral: ≥ 3 de 5.
4. **Decisión** (regla del archivo de tests):
   - continue: S1 ≥ 70 % y S2 ≥ 3 de 5.
   - change: S1 ≥ 70 % y S2 < 3 de 5. También si S1 está entre 40 % y 69 %.
   - discard: S1 < 40 %.
5. **Procedencia.** Solo cuentan para mover la creencia #4 los analistas con procedencia `segment member`. Registre los `stand-in` aparte. El mínimo para leer y S2 se calculan solo con `segment member`.
6. **Decisión diferida.** Una fila con decisión_final = `diferida` tiene mismo_día = `no`.
7. **Repregunta.** Informe también S1 sin repregunta = cambios con mismo_día = `sí` y por_repregunta = `no` ÷ total de cambios alertados. Este valor no cambia la decisión.

| Resultado | Valor |
|---|---|
| Total de cambios alertados | |
| Analistas que terminaron la semana | |
| Cambios con decisión el mismo día | |
| S1 (%) | |
| S1 sin repregunta (%) | |
| Decisiones diferidas | |
| Analistas con NO en ≥3 días | |
| S2 (de 5) | |
| Semana extra agregada | sí / no |
| Resultado | passed · failed · inconclusive |

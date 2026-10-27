"""T2 · Cálculo de la métrica según metodo.md (sugeridor-ajustes).

Uso:
  pip install pandas scikit-learn
  python analisis.py --capturas capturas.csv --ocupacion ocupacion.csv

Escribe resultado.json y excluidos.csv, y muestra el resultado. No cambie el método aquí:
este script aplica metodo.md tal como está fijado.
"""

import argparse
import json
from datetime import timedelta

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

DESDE, HASTA = "2026-04-26", "2026-10-25"  # período de metodo.md §2
CORTE_OCUPACION = 0.80
DIAS = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
FRANJAS = ["madrugada", "manana", "tarde", "noche"]


def franja(hhmm):
    h = int(str(hhmm).split(":")[0])
    return FRANJAS[0] if h < 6 else FRANJAS[1] if h < 12 else FRANJAS[2] if h < 18 else FRANJAS[3]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capturas", required=True)
    ap.add_argument("--ocupacion", required=True)
    ap.add_argument("--salida", default="resultado.json")
    a = ap.parse_args()

    cap = pd.read_csv(a.capturas, dtype=str)
    occ = pd.read_csv(a.ocupacion, dtype=str)
    excl = {}
    excluidos = []  # una fila por vuelo excluido: fecha_salida, vuelo, motivo

    cap = cap[(cap.fecha_salida >= DESDE) & (cap.fecha_salida <= HASTA)]
    occ = occ[(occ.fecha_salida >= DESDE) & (occ.fecha_salida <= HASTA)]
    # Si un vuelo se capturó más de una vez para la misma salida, usar la primera captura.
    cap = cap[cap.vuelo.fillna("") != ""].sort_values(["fecha_captura", "hora_captura"])
    cap = cap.drop_duplicates(["fecha_salida", "vuelo"], keep="first")

    # Frecuencia (antes de exclusiones de tarifa: cuenta vuelos publicados).
    cap["fs"] = pd.to_datetime(cap.fecha_salida)
    dias_con_captura = set(cap.fs)
    def frecuencia(row):
        ventana = [row.fs + timedelta(days=k) for k in range(-3, 4)]
        con = [d for d in ventana if d in dias_con_captura]
        # Una fila = un vuelo distinto (fecha_salida + vuelo), ya sin duplicados.
        n = ((cap.ruta == row.ruta) & (cap.fs.isin(con))).sum()
        return n / len(con) * 7 if con else np.nan
    cap["frecuencia"] = cap.apply(frecuencia, axis=1)

    occ = occ.drop_duplicates(["fecha_salida", "vuelo"])
    df = occ.merge(cap, on=["fecha_salida", "vuelo"], how="left", suffixes=("", "_cap"))
    total = len(df)

    def quitar(mask, nombre):
        nonlocal df
        excl[nombre] = int(mask.sum())
        for _, r in df[mask].iterrows():
            excluidos.append({"fecha_salida": r.fecha_salida, "vuelo": r.vuelo, "motivo": nombre})
        df = df[~mask]

    quitar(df.estado_vuelo != "operado", "cancelados")
    quitar(df.estado.isna() | df.estado.isin(["sin_dato", "error"]), "sin_captura_d14")
    n_agot = int((df.estado == "agotado").sum())
    quitar(df.estado == "agotado", "agotados")
    df = df.assign(asientos=pd.to_numeric(df.asientos, errors="coerce"),
                   embarcados=pd.to_numeric(df.embarcados, errors="coerce"),
                   tarifa=pd.to_numeric(df.tarifa, errors="coerce"))
    quitar(df.asientos.isna() | (df.asientos <= 0) | df.embarcados.isna(), "sin_ocupacion")
    moneda_ppal = df.groupby("ruta").moneda.agg(lambda s: s.mode().iat[0])
    quitar(df.moneda != df.ruta.map(moneda_ppal), "otra_moneda")
    quitar(df.tarifa.isna(), "sin_tarifa")

    df = df.copy()
    df["alta"] = (df.embarcados / df.asientos >= CORTE_OCUPACION).astype(int)
    df["dia_semana"] = pd.to_datetime(df.fecha_salida).dt.dayofweek.map(dict(enumerate(DIAS)))
    df["franja"] = df.hora_salida.map(franja)

    # Partición 70/30 por fecha.
    por_fecha = df.groupby("fecha_salida").size().sort_index()
    acum = por_fecha.cumsum() / por_fecha.sum()
    corte = acum[acum >= 0.70].index[0]
    tr, ho = df[df.fecha_salida <= corte].copy(), df[df.fecha_salida > corte].copy()

    # Control de la partición: el hold-out tiene que ser igual a los vuelos con salida después del corte.
    print("Vuelos por fecha de salida (después de exclusiones):")
    for f, n in por_fecha.items():
        print(f"  {f}  {n:4d}  {'entrenamiento' if f <= corte else 'hold-out'}")
    esperado_ho = int(por_fecha[por_fecha.index > corte].sum())
    control_particion = "ok" if (len(ho) == esperado_ho and len(tr) + len(ho) == len(df)) else "error"
    print(f"Fecha de corte: {corte} · hold-out esperado: {esperado_ho} · hold-out real: {len(ho)} · control: {control_particion}")
    pd.DataFrame(excluidos, columns=["fecha_salida", "vuelo", "motivo"]).to_csv("excluidos.csv", index=False)

    # tarifa_rel con mediana de entrenamiento.
    med_ruta = tr.groupby("ruta").tarifa.median()
    med_global = tr.tarifa.median()
    for d in (tr, ho):
        d["tarifa_rel"] = d.tarifa / d.ruta.map(med_ruta).fillna(med_global)

    def X(d):
        num = d[["tarifa_rel", "frecuencia"]].astype(float)
        num = (num - tr[["tarifa_rel", "frecuencia"]].astype(float).mean()) / \
              tr[["tarifa_rel", "frecuencia"]].astype(float).std(ddof=0).replace(0, 1)
        dias = pd.get_dummies(pd.Categorical(d.dia_semana, categories=DIAS), prefix="d")
        fr = pd.get_dummies(pd.Categorical(d.franja, categories=FRANJAS), prefix="f")
        return np.hstack([num.values, dias.values, fr.values]).astype(float)

    n_ho = len(ho)
    pct_alta_ho = ho.alta.mean() if n_ho else float("nan")
    leible = n_ho >= 150 and 0.20 <= pct_alta_ho <= 0.80

    modelo = LogisticRegression(C=1.0, max_iter=1000).fit(X(tr), tr.alta)
    pred = modelo.predict(X(ho))
    acc = float((pred == ho.alta.values).mean())
    # metodo.md §8: clase mayoritaria de entrenamiento; referencia = su proporción en el hold-out.
    mayoritaria = int(tr.alta.mean() >= 0.5)
    ref = float((ho.alta.values == mayoritaria).mean())
    dif = round((acc - ref) * 100, 1)
    cm = pd.crosstab(pd.Series(ho.alta.values, name="real"),
                     pd.Series(pred, name="predicho")).reindex(index=[1, 0], columns=[1, 0], fill_value=0)

    if control_particion != "ok":
        resultado, decision = "inconclusive", "sin decisión (error en la partición)"
    elif not leible:
        resultado, decision = "inconclusive", "sin decisión (no cumple el mínimo)"
    elif acc >= 0.70 and dif >= 10.0:
        resultado, decision = "passed", "continue"
    elif 5.0 <= dif < 10.0:
        resultado, decision = "failed", "change"
    elif dif < 5.0:
        resultado, decision = "failed", "discard"
    else:
        resultado, decision = "fuera de la regla", "decidir en /analyze-solution-tests y registrar en corrections.md"

    out = {
        "vuelos_total": total, "exclusiones": excl,
        "agotados_pct": round(n_agot / total * 100, 1) if total else None,
        "fecha_corte": corte, "n_entrenamiento": len(tr), "n_holdout": n_ho,
        "vuelos_por_fecha": {str(k): int(v) for k, v in por_fecha.items()},
        "control_particion": control_particion,
        "pct_alta_holdout": round(pct_alta_ho * 100, 1),
        "clase_mayoritaria_entrenamiento": "alta" if mayoritaria else "baja",
        "precision_referencia_pct": round(ref * 100, 1),
        "precision_modelo_pct": round(acc * 100, 1),
        "diferencia_puntos": dif,
        "matriz_confusion": {"real_alta": {"pred_alta": int(cm.iat[0, 0]), "pred_baja": int(cm.iat[0, 1])},
                             "real_baja": {"pred_alta": int(cm.iat[1, 0]), "pred_baja": int(cm.iat[1, 1])}},
        "minimo_cumplido": bool(leible), "resultado": resultado, "decision": decision,
    }
    with open(a.salida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

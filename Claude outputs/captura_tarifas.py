"""T2 · Captura diaria de la tarifa pública a D-14 (sugeridor-ajustes).

Owner: tech / datos. Usar solo con el permiso escrito de la aerolínea.

Qué hace:
  Una vez por día, para cada ruta de rutas.json, busca en la web pública de
  la aerolínea los vuelos con salida en D-14 (hoy + 14 días). Para cada vuelo
  registra la tarifa más baja a la venta, su marca tarifaria y la hora de
  salida. Agrega las filas a capturas.csv.

Cuándo correrlo:
  Todos los días del 2026-10-28 al 2026-11-14, a la misma hora (ej. 06:00 hora
  local, ±1 h). Use cron o el Programador de tareas.

Uso:
  pip install playwright && playwright install chromium
  python captura_tarifas.py --config rutas.json
  python captura_tarifas.py --config rutas.json --fecha-captura 2026-10-28   # repetir un día

Pendiente para tech:
  Complete la función `extraer_vuelos` para la web de la aerolínea. Es la
  única parte que depende del sitio. No cambie las columnas de salida.

Formato de rutas.json:
  {
    "aerolinea": "XX",
    "zona_horaria": "America/La_Paz",
    "url_busqueda": "https://www.ejemplo-aerolinea.com/...",
    "salida_csv": "capturas.csv",
    "rutas": [{"origen": "VVI", "destino": "LPB"}, ...]
  }
"""

import argparse
import csv
import json
import os
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from playwright.sync_api import sync_playwright

D_N = 14
COLUMNAS = [
    "fecha_captura", "hora_captura", "aerolinea", "ruta", "vuelo",
    "fecha_salida", "hora_salida", "tarifa", "moneda", "marca_tarifaria",
    "estado", "fuente_url",
]
# estado: ok | agotado | sin_dato | error


def extraer_vuelos(page, url_busqueda, origen, destino, fecha_salida):
    """Busca un solo tramo de ida, 1 adulto, en la fecha dada.

    Devuelve una lista con un dict por vuelo:
      {"vuelo": "XX123", "hora_salida": "07:40",
       "tarifa": 89.0 o None, "moneda": "USD",
       "marca_tarifaria": "LIGHT", "estado": "ok" | "agotado",
       "url": url de la página leída}

    Reglas:
      - Un dict por vuelo operado por la aerolínea (sin códigos compartidos).
      - `tarifa` = la tarifa más baja a la venta para ese vuelo, con tasas,
        tal como la ve un pasajero.
      - Si el vuelo aparece pero no tiene tarifa a la venta: estado "agotado",
        tarifa None.
      - Si la página no muestra vuelos para la ruta y la fecha: devuelva [].
    """
    raise NotImplementedError("Completar para la web de la aerolínea.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--fecha-captura", help="AAAA-MM-DD; por defecto, hoy")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)
    tz = ZoneInfo(cfg["zona_horaria"])
    hoy = (date.fromisoformat(args.fecha_captura) if args.fecha_captura
           else datetime.now(tz).date())
    fecha_salida = hoy + timedelta(days=D_N)
    salida = cfg.get("salida_csv", "capturas.csv")
    nuevo = not os.path.exists(salida)

    filas = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for r in cfg["rutas"]:
            ruta = f'{r["origen"]}-{r["destino"]}'
            hora = datetime.now(tz).strftime("%H:%M")
            base = {"fecha_captura": hoy.isoformat(), "hora_captura": hora,
                    "aerolinea": cfg["aerolinea"], "ruta": ruta,
                    "fecha_salida": fecha_salida.isoformat()}
            try:
                vuelos = extraer_vuelos(page, cfg["url_busqueda"], r["origen"],
                                        r["destino"], fecha_salida)
            except NotImplementedError:
                raise
            except Exception as e:  # registrar y seguir con la próxima ruta
                filas.append({**base, "vuelo": "", "hora_salida": "",
                              "tarifa": "", "moneda": "", "marca_tarifaria": "",
                              "estado": "error", "fuente_url": repr(e)[:200]})
                continue
            if not vuelos:
                filas.append({**base, "vuelo": "", "hora_salida": "",
                              "tarifa": "", "moneda": "", "marca_tarifaria": "",
                              "estado": "sin_dato", "fuente_url": cfg["url_busqueda"]})
                continue
            for v in vuelos:
                filas.append({**base, "vuelo": v["vuelo"].replace(" ", ""),
                              "hora_salida": v["hora_salida"],
                              "tarifa": "" if v["tarifa"] is None else v["tarifa"],
                              "moneda": v.get("moneda", ""),
                              "marca_tarifaria": v.get("marca_tarifaria", ""),
                              "estado": v["estado"], "fuente_url": v.get("url", "")})
        browser.close()

    with open(salida, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS)
        if nuevo:
            w.writeheader()
        w.writerows(filas)

    errores = sum(1 for x in filas if x["estado"] in ("error", "sin_dato"))
    print(f"{hoy} · salida {fecha_salida} · {len(filas)} filas · {errores} con error o sin dato")


if __name__ == "__main__":
    main()

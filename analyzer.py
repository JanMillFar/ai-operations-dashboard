import pandas as pd

def analizar_riesgo(df):

    incidencias = df[df["Estado"] == "Retrasado"]

    total_pedidos = len(df)
    total_incidencias = len(incidencias)

    if total_incidencias >= 3:
        riesgo = "ALTO"
    elif total_incidencias >= 1:
        riesgo = "MEDIO"
    else:
        riesgo = "BAJO"

    return {
        "incidencias": incidencias,
        "total_pedidos": total_pedidos,
        "total_incidencias": total_incidencias,
        "riesgo": riesgo
    }
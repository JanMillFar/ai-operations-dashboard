import pandas as pd

from analyzer import analizar_riesgo
from recommendations import generar_recomendacion

# Leer CSV
df = pd.read_csv("data/pedidos.csv")

print("=== PEDIDOS ===")
print(df)

# Analizar riesgo
resultado = analizar_riesgo(df)

incidencias = resultado["incidencias"]
riesgo = resultado["riesgo"]

print("\n=== INCIDENCIAS ===")
print(incidencias)

print("\n=== RESUMEN OPERATIVO ===")
print(f"Total pedidos: {resultado['total_pedidos']}")
print(f"Pedidos retrasados: {resultado['total_incidencias']}")
print(f"RIESGO OPERATIVO: {riesgo}")

# Prioridades altas
prioridad_alta = incidencias[incidencias["Prioridad"] == "Alta"]

print("\n=== PRIORIDADES ALTAS ===")
print(prioridad_alta[["Pedido", "Producto", "Proveedor"]])

# Recomendación
recomendacion = generar_recomendacion(riesgo)

print("\n=== RECOMENDACION AUTOMATICA ===")
print(recomendacion)
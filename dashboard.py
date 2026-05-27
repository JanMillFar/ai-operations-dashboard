import pandas as pd
import matplotlib.pyplot as plt

# Llegir dades
df = pd.read_csv("data/pedidos.csv")

# KPIs
total_pedidos = len(df)
retrasados = len(df[df["Estado"] == "Retrasado"])
ok = len(df[df["Estado"] == "OK"])

# Comptar proveïdors amb incidències
proveedores_criticos = (
    df[df["Estado"] == "Retrasado"]["Proveedor"]
    .value_counts()
)

# Mostrar KPIs
print("=== DASHBOARD OPERATIVO ===")
print(f"Total pedidos: {total_pedidos}")
print(f"Pedidos OK: {ok}")
print(f"Pedidos retrasados: {retrasados}")

# Crear gràfic
plt.figure(figsize=(8, 5))

proveedores_criticos.plot(kind="bar")

# Títol i etiquetes
plt.title("Proveedores con incidencias")
plt.xlabel("Proveedor")
plt.ylabel("Cantidad de incidencias")

# Ajustar layout
plt.tight_layout()

# Mostrar
plt.show()
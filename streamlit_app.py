import streamlit as st
import pandas as pd

# from ai_report import generar_informe_ia

# Configuració pàgina
st.set_page_config(
    page_title="AI Operations Dashboard",
    layout="wide"
)

# Títol
st.title("AI Operations Dashboard")

st.markdown(
    "Monitorización logística y operacional en tiempo real."
)

# SIDEBAR
st.sidebar.header("Configuración")

# Upload CSV
uploaded_file = st.sidebar.file_uploader(
    "Subir archivo CSV",
    type=["csv"]
)

# Llegir dades
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

else:
    df = pd.read_csv("data/pedidos.csv")

# Filtres
st.sidebar.header("Filtros")

estado_filtro = st.sidebar.multiselect(
    "Estado",
    options=df["Estado"].unique(),
    default=df["Estado"].unique()
)

proveedor_filtro = st.sidebar.multiselect(
    "Proveedor",
    options=df["Proveedor"].unique(),
    default=df["Proveedor"].unique()
)

# Aplicar filtres
df_filtrado = df[
    (df["Estado"].isin(estado_filtro)) &
    (df["Proveedor"].isin(proveedor_filtro))
]

# KPIs
total_pedidos = len(df_filtrado)
retrasados = len(
    df_filtrado[df_filtrado["Estado"] == "Retrasado"]
)
ok = len(
    df_filtrado[df_filtrado["Estado"] == "OK"]
)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total pedidos", total_pedidos)
col2.metric("Pedidos OK", ok)
col3.metric("Pedidos retrasados", retrasados)

# Taula principal
st.subheader("Pedidos")

st.dataframe(df_filtrado)

# Incidències
incidencias = df_filtrado[
    df_filtrado["Estado"] == "Retrasado"
]

st.subheader("Incidencias críticas")

st.dataframe(incidencias)

# Gràfic
st.subheader("Proveedores con incidencias")

st.bar_chart(
    incidencias["Proveedor"].value_counts()
)

# Risc operacional
st.subheader("Riesgo operacional")

if retrasados >= 3:
    st.error("🔴 RIESGO OPERATIVO ALTO")

elif retrasados >= 1:
    st.warning("🟠 RIESGO OPERATIVO MEDIO")

else:
    st.success("🟢 RIESGO OPERATIVO BAJO")

# Recomanació automàtica
st.subheader("Recomendación automática")

if retrasados >= 3:
    st.write(
        "Revisar proveedores críticos y priorizar entregas urgentes."
    )

elif retrasados >= 1:
    st.write(
        "Monitorizar incidencias y revisar tiempos de entrega."
    )

else:
    st.write(
        "Operativa estable."
    )

# # INFORME IA
# st.subheader("Informe IA")
#
# if st.button("Generar informe IA"):
#
#     incidencias_texto = incidencias.to_string(index=False)
#
#     with st.spinner("Generando informe IA..."):
#
#         informe = generar_informe_ia(incidencias_texto)
#
#     st.success("Informe generado.")
#
#     st.write(informe)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ai_report import generar_informe_ia
from pdf_report import generar_pdf

# CONFIGURACIÓN PÁGINA
st.set_page_config(
    page_title="AI Operations Dashboard",
    page_icon="📊",
    layout="wide"
)

# HEADER
st.title("📊 AI Operations Dashboard")

st.markdown("""
Real-time operational monitoring platform with risk analysis,
incident tracking and AI-powered operational insights.
""")

st.divider()

# CARGAR DATOS
df = pd.read_csv("data/pedidos_criticos.csv")

# SIDEBAR
st.sidebar.header("Filters")

proveedor = st.sidebar.selectbox(
    "Select Supplier",
    ["All"] + list(df["Proveedor"].unique())
)

estado = st.sidebar.selectbox(
    "Select Status",
    ["All"] + list(df["Estado"].unique())
)

# FILTROS
if proveedor != "All":
    df = df[df["Proveedor"] == proveedor]

if estado != "All":
    df = df[df["Estado"] == estado]

# INCIDENCIAS
incidencias = df[df["Estado"] == "Retrasado"]

# KPI CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📦 Total Orders",
        value=len(df)
    )

with col2:
    st.metric(
        label="⚠️ Delayed Orders",
        value=len(incidencias)
    )

with col3:

    riesgo = "HIGH" if len(incidencias) >= 3 else "MEDIUM"

    st.metric(
        label="🚨 Operational Risk",
        value=riesgo
    )

st.divider()

# TABLA PRINCIPAL
st.subheader("📋 Orders Overview")

st.dataframe(df)

# TABLA INCIDENCIAS
st.subheader("⚠️ Delayed Orders")

st.dataframe(incidencias)

# GRÁFICO
st.subheader("📊 Incidents by Supplier")

grafico = incidencias["Proveedor"].value_counts()

if not grafico.empty:

    fig, ax = plt.subplots()

    grafico.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Supplier")
    ax.set_ylabel("Incidents")

    st.pyplot(fig)

else:

    st.info("No incident data available for selected filters.")

# RECOMENDACIÓN AUTOMÁTICA
st.subheader("🤖 Automated Recommendation")

if len(incidencias) >= 3:

    st.warning(
        "High operational risk detected. Review critical suppliers and prioritize urgent deliveries."
    )

else:

    st.success(
        "Operational flow stable."
    )

# UPLOAD CSV
st.subheader("📂 Upload CSV")

uploaded_file = st.file_uploader(
    "Upload operational dataset",
    type=["csv"]
)

if uploaded_file is not None:

    nuevo_df = pd.read_csv(uploaded_file)

    st.write("Uploaded dataset:")

    st.dataframe(nuevo_df)

# IA REPORT
st.subheader("🧠 AI Executive Analysis")

if st.button("Generate AI Report"):

    incidencias_texto = incidencias.to_string()

    with st.spinner("Generating AI operational analysis..."):

        informe = generar_informe_ia(incidencias_texto)

    st.success("AI report generated successfully.")

    st.markdown(informe)

    # GENERAR PDF
    pdf_path = generar_pdf(informe)

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📥 Download Executive PDF Report",
            data=pdf_file,
            file_name="executive_report.pdf",
            mime="application/pdf"
        )
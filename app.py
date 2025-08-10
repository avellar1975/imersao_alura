import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


# --- Carregamento dos dados ---
df = pd.read_parquet("https://github.com/avellar1975/imersao_alura/blob/main/notebooks/dados_normalizados.parquet?raw=true")


# --- Configuração da página ---
st.set_page_config(
    page_title="Dashboard Econômico",
    page_icon="📊",
    layout="wide"  # largura total
)

# --- Sidebar para filtros ---
st.sidebar.header("Filtros")

anos_unicos = sorted(df["Ano"].unique())
anos_selecionados = st.sidebar.multiselect(
    "Selecione os Anos", 
    options=anos_unicos,
    default=anos_unicos
)

indicadores = ["IPCA", "PIB", "Desocupacao"]
indicadores_selecionados = st.sidebar.multiselect(
    "Selecione os Indicadores",
    options=indicadores,
    default=indicadores
)

# --- Filtra DataFrame ---
df_filtrado = df[df["Ano"].isin(anos_selecionados)].copy()

# --- Garante que a coluna de datas tenha um nome ---
df_filtrado = df_filtrado.reset_index().rename(columns={"index": "Data"})

# --- Transforma para formato longo ---
df_long = df_filtrado.melt(
    id_vars=["Data", "Ano"], 
    value_vars=indicadores_selecionados,
    var_name="Indicador", 
    value_name="Valor"
)

# --- Título ---
st.title("📊 Dashboard de Indicadores Econômicos")
st.subheader("Comparação por Ano e Indicador")

# --- Gráfico Interativo ---
fig = px.line(
    df_long,
    x="Data",
    y="Valor",
    color="Indicador",
    hover_data={"Ano": True},
    markers=True,
    height=600
)

fig.update_layout(
    autosize=True,
    height=600,
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# --- Estatísticas ---
st.write("Estatísticas Descritivas (dados filtrados):")
st.write(df_long.groupby("Indicador")["Valor"].describe())

# --- Dados filtrados ---
with st.expander("Ver dados filtrados"):
    st.dataframe(df_long)
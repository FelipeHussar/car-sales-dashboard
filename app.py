import pandas as pd
import plotly.express as px
import streamlit as st

# Título do app
st.header("Dashboard de Carros Usados - EUA")

# Carregar os dados
df = pd.read_csv('vehicles.csv')

# Botão para histograma
if st.button("Mostrar histograma (odômetro)"):
    st.write("Distribuição da quilometragem dos veículos")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão
if st.button("Mostrar dispersão (odômetro × preço)"):
    st.write("Relação entre quilometragem e preço")
    fig2 = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

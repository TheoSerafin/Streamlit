import pandas as pd
import streamlit as st
import plotly.express as px

#ler arquivo
tabela = pd.read_excel("C:\Users\theo_\Downloads\Teste.xlsx")

#plotar gráficos
graf_barra = px.bar(tabela, x="Produto", y="Valor", color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra, use_container_width=True)

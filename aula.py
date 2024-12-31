import pandas as pd
import streamlit as st
import plotly.express as px

tabela = pd.read_excel(r"C:\Users\theo_\Downloads\Traços.xlsx")
graf_barra = px.bar(tabela, x="Produtos", y="Valor", color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra, use_container_width=True)
print(tabela)

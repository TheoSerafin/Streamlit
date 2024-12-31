import pandas as pd
import streamlit as st
import plotly.express as px

tabela = {
    "Produtos":("Tablet","Computador","Celular"),
    "Valor":(1500,2000,3000)
}

graf_barra = px.bar(tabela, x="Produtos", y="Valor", color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra, use_container_width=True)
print(tabela)
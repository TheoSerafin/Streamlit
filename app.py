import streamlit as st
import pandas as pd
import plotly.express as px

tabela = {
    'Data': ['01/12','02/12'],
    'Valor': [10,20]
}
tabela_df = pd.DataFrame(tabela)
graf_barra = px.bar(tabela, x="Data", y="Valor", color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra, use_container_width=True)
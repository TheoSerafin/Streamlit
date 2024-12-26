import streamlit as st
import pandas as pd

tabela = {
    'Data': ['01/12','02/12'],
    'Valor': [10,20]
}
tabela_df = pd.DataFrame(tabela)
st.bar_chart(tabela_df,x='Data',y='Valor')
import plotly.express as px
import streamlit as st
import pandas as pd

# Carregar a tabela do arquivo Excel
tabela = pd.read_excel(r"C:\Users\theo_\Downloads\adm.xlsx")
# Criar o gráfico de barras
graf_barra = px.bar(tabela, x="Dias", y="Total", color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra, use_container_width=True)

# Somar os valores de cada tipo de despesa
gastos = tabela[["Transporte", "RU", "Lanche", "Debito", "Material", "Remédio"]].sum()

# Criar um DataFrame para os gastos
gastos_df = pd.DataFrame({'Tipo de Gasto': gastos.index, 'Valores': gastos.values})

# Criar o gráfico de pizza geral
graf_pizza = px.pie(gastos_df, names='Tipo de Gasto', values='Valores', title='Distribuição dos Tipos de Gasto')

# Criar o gráfico de Saldo Disponível
saldo = px.pie(tabela, names="Dinheiro", values="Valor", title="Saldo Disponível")

# Plotar os gráficos de pizza em colunas
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(graf_pizza, use_container_width=True)
with col2:
    st.plotly_chart(saldo, use_container_width=True)

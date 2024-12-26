import plotly.express as px
import streamlit as st
import pandas as pd

#criando a tabela
tabela = pd.read_excel(r"C:\Users\theo_\Downloads\NovaPlanilha.xlsx")

#plotando o gráfico de barra
graf_barra = px.bar(tabela,x = tabela["Dias"],y = tabela['Total'],color_discrete_sequence=['#ff6100'])
st.plotly_chart(graf_barra)

#criando o gráfico de pizza geral
gastos = tabela[["Transporte", "RU","Lanche","Debito","Material","Remédio"]].sum()
gastos_df = pd.DataFrame({'Tipo de Gasto': gastos.index, 'Valores': gastos.values})
graf_pizza = px.pie(gastos_df, names='Tipo de Gasto', values='Valores', title='Distribuição dos Tipos de Gasto')


#criando o gráfico de Saldo Disponivel
saldo = px.pie(tabela, names="Dinheiro", values="Valor",title="Saldo Disponivel")

#plotando os gráficos de pizza
col1 ,col2 = st.columns(2,border=True,gap="small")
with col1:
    st.plotly_chart(graf_pizza, use_container_width=True)
with col2:
    st.plotly_chart(saldo, use_container_width=True)
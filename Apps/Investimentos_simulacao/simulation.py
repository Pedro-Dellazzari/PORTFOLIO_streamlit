#Importando as bibliotecas
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

#API
import finnhub

#Configurando API
finnhub_client = finnhub.Client(api_key="sandbox_c7i9ij2ad3if83qggk30")

#Lendo os dados
bolsa = pd.read_excel("Apps/Investimentos_simulacao/info.xlsx",sheet_name="bolsa")

cripto = pd.read_excel("Apps/Investimentos_simulacao/info.xlsx",sheet_name="moedas")

#Função pegar dados
def bolsa_line_chart(symbol, price, data_user):

    try:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}.SA&apikey=F7V1K3CSSAL8YCM2".format(symbol)

        response = requests.get(url)
        data = response.json()

        datas = []
        fechamento = []

        for date in data['Time Series (Daily)']:
            datas.append(date)
            fechamento.append(data['Time Series (Daily)'][date]['4. close'])

        st.subheader(bolsa[bolsa["symbol"] == symbol]['acao'].iloc[0])
    except:

        url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={}&market=BRL&apikey=F7V1K3CSSAL8YCM2".format(symbol)

        response = requests.get(url)
        data = response.json()

        datas = []
        fechamento = []

        for date in data['Time Series (Digital Currency Daily)']:
            datas.append(date)
            fechamento.append(data['Time Series (Digital Currency Daily)'][date]['4a. close (BRL)'])

        st.subheader(cripto[cripto["symbol"] == symbol]['acao'].iloc[0])

    #Criando o dataframe
    dataset = pd.DataFrame()
    dataset['data'] = datas
    dataset['valor'] = fechamento

    #valor da data do usuário
    before_price = dataset[dataset['data'] == str(data_user)]['valor'].iloc[0]
    now_price = dataset['valor'].iloc[0]

    valor_gasto = price * float(before_price)
    valor_atual = price * float(now_price)

    perda_lucro = ((valor_atual - valor_gasto)/valor_gasto) * 100

    #Colocando o nome


    #Criando a linha
    st.write("Se você tivesse aplicado {} em {} você teria um total de {:.2f}% de lucro/perda".format(price, data_user,perda_lucro))

    st.write("Valor da ação na data: {}".format(before_price))
    st.write("Valor gasto: {}".format(valor_gasto))

    st.write("Valor da ação hoje: {}".format(now_price))
    st.write("Valor atual: {}".format(valor_atual))

    #Construindo os gráficos
    dataset['data'] = pd.to_datetime(dataset['data'])
    dataset['valor'] = dataset['valor'].astype(float)

    if perda_lucro < 0:
        color = 'red'
    else:
        color = 'green'

    bar_stock_price = px.line(dataset, x='data',y='valor',title="Valor por Data", template='ggplot2')
    bar_stock_price.update_traces(line_color=color)
    bar_stock_price.add_annotation(x=pd.to_datetime(data_user), y=before_price, text='Investimento', align='right', arrowhead=2, yshift=10)
    bar_stock_price.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(bar_stock_price)



#Criando a função para o multiapp
def app():

    st.subheader("Simulação de investimentos")

    #Descrição do projeto
    st.markdown("Esse projeto tem como objetivo realizar uma simulação do seu investimento em Ações ou Criptomoedas")
    st.markdown("Lembrando que esse aplicativo não apresenta nenhuma dica ou informação de como investir seu dinheiro. Apenas realiza o cálculo :)")
    st.markdown("Para investir seu dinheiro fale com um profissional")
    st.write("ESCOLHA UMA DATA SEM SER FINAL DE SEMANA\nCOLOQUE UM VALOR MAIOR QUE ZERO NA QUANTIDADE")

    acoe = st.checkbox("Bolsa de Ações - BR")
    cripto_choice = st.checkbox("Bolsa de Criptomoedas - BRL")


    col1, col2, col3 = st.columns(3)

    data_user = col1.date_input("Data do investimento")
    price_user = col2.number_input("Quantidades")

    if acoe:
        escolha = col3.selectbox("Investimento", options=bolsa['symbol'])
    elif cripto_choice:
        escolha = col3.selectbox("Investimento", options=cripto['symbol'])

    button = st.button("Ver investimento")

    if button:
        bolsa_line_chart(escolha, price_user, data_user)




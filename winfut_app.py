import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="WINFUT - Análise de Tendência", layout="wide")
st.title("📈 Analisador de Tendência - WINFUT")

st.markdown("Faça upload de um arquivo CSV com os candles do WINFUT para iniciar a análise.")

arquivo = st.file_uploader("📂 Enviar arquivo CSV", type=['csv'])

if arquivo:
    df = pd.read_csv(arquivo)
    df.columns = [col.lower() for col in df.columns]
    df = df.rename(columns={
        'abertura': 'open', 'máxima': 'high', 'minima': 'low', 'mínima': 'low', 'fechamento': 'close',
        'data': 'date', 'hora': 'time'
    })
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df.set_index('datetime', inplace=True)

    # Cálculo das médias
    df['MME20'] = df['close'].ewm(span=20).mean()
    df['MME200'] = df['close'].ewm(span=200).mean()

    # Exibir gráfico
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['open'], high=df['high'], low=df['low'], close=df['close'],
        name='Candles'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MME20'], line=dict(color='blue'), name='MME20'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MME200'], line=dict(color='orange'), name='MME200'))
    fig.update_layout(xaxis_rangeslider_visible=False)

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Aguardando envio de arquivo.")

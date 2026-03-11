import streamlit as st
from dados import carregar_dados
from agente import FinBuddy
from openai import OpenAI

# Carregar dados
transacoes, historico, perfil, produtos = carregar_dados()

# Inicializar LLM
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Inicializar agente
agente = FinBuddy(transacoes, historico, perfil, produtos, llm_client)

st.title("FinBuddy - Agente Financeiro Inteligente")
st.write("Controle seus gastos e receba alertas personalizados!")

entrada = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    resposta = agente.gerar_resposta(entrada)
    st.write(resposta)

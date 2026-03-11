import pandas as pd
import json

def carregar_dados():
    transacoes = pd.read_csv("../data/transacoes.csv")
    historico = pd.read_csv("../data/historico_atendimento.csv")
    
    with open("../data/perfil_investidor.json", "r") as f:
        perfil = json.load(f)
    
    with open("../data/produtos_financeiros.json", "r") as f:
        produtos = json.load(f)
    
    return transacoes, historico, perfil, produtos

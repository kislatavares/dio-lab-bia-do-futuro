from openai import OpenAI  # ou cliente do LLM que você usar

class FinBuddy:
    def __init__(self, transacoes, historico, perfil, produtos, llm_client):
        self.transacoes = transacoes
        self.historico = historico
        self.perfil = perfil
        self.produtos = produtos
        self.llm = llm_client

    def gerar_resposta(self, mensagem_usuario):
        system_prompt = """Você é FinBuddy, um agente financeiro inteligente.
        Sempre use os dados disponíveis; não invente informações; seja amigável."""
        
        contexto = f"""
        Perfil do cliente: {self.perfil['nome']} ({self.perfil['perfil']})
        Últimas transações: {self.transacoes.tail(5).to_dict(orient='records')}
        Pergunta: {mensagem_usuario}
        """
        
        prompt_completo = system_prompt + contexto
        
        resposta = self.llm.completions.create(
            model="text-davinci-003",
            prompt=prompt_completo,
            max_tokens=200
        )
        return resposta.choices[0].text.strip()

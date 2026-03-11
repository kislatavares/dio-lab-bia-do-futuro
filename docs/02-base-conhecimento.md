# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais foram enriquecidos com novas categorias de gastos (como transporte, lazer, assinaturas), limites de orçamento fictícios para cada categoria e exemplos de transações em diferentes meses. Também foram adicionados perfis de clientes simulados para testar respostas personalizadas do agente.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início de cada sessão do agente. Eles são lidos e transformados em dicionários ou dataframes, que ficam disponíveis para consulta dinâmica sempre que o usuário faz uma pergunta sobre gastos, alertas ou relatórios.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são consultados dinamicamente pelo agente. O system prompt define as regras gerais de interação, mas o histórico de transações, perfis e categorias são enviados ao modelo conforme a necessidade, garantindo respostas precisas sem sobrecarregar o prompt com informações irrelevantes.
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Limite mensal: Alimentação R$ 1.000 | Transporte R$ 600 | Lazer R$ 400

Últimas transações:
- 01/11: Supermercado - R$ 450 (Alimentação)
- 03/11: Streaming - R$ 55 (Lazer)
- 05/11: Posto de Gasolina - R$ 200 (Transporte)
- 06/11: Restaurante - R$ 120 (Alimentação)

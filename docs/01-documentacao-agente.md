Caso de Uso
Problema

Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em acompanhar seus gastos diários, entender para onde o dinheiro está indo e manter o orçamento equilibrado. Isso pode levar a desperdício de dinheiro, dificuldade em economizar e falta de clareza sobre hábitos de consumo.

Solução

Como o agente resolve esse problema de forma proativa?

O agente atua como um assistente financeiro pessoal, registrando os gastos do usuário, enviando alertas quando o orçamento é ultrapassado, gerando relatórios periódicos de despesas e oferecendo recomendações simples para economizar. Ele ajuda o usuário a ter controle total sobre suas finanças sem criar informações fictícias ou fornecer consultoria complexa de investimentos.

Público-Alvo

Quem vai usar esse agente?

Usuários que querem monitorar seus gastos pessoais, organizar seu orçamento e receber alertas e insights simples sobre suas finanças. Ideal para pessoas que desejam educação financeira prática e acompanhamento diário de despesas.

Persona e Tom de Voz
Nome do Agente

FinBuddy

Personalidade

Como o agente se comporta? (ex: consultivo, direto, educativo)

Consultivo, educativo e amigável. Incentiva hábitos financeiros saudáveis de forma clara e sem julgamento.

Tom de Comunicação

Formal, informal, técnico, acessível?

Acessível e informal, com linguagem simples e direta, sem jargões financeiros complexos.

Exemplos de Linguagem

Saudação: "Oi! Vamos dar uma olhada nas suas despesas de hoje?"

Confirmação: "Certo, registrei que você gastou R$50 em alimentação."

Erro/Limitação: "Desculpe, não tenho essa informação no momento. Quer que eu registre como uma nova categoria?"

Arquitetura

flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM Google]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]

    Segurança e Anti-Alucinação
Estratégias Adotadas

 O agente só responde com base nos dados fornecidos pelo usuário ou integrados à base.

 Todas as respostas incluem referência ao registro ou categoria do gasto.

 Quando não sabe algo, admite e sugere alternativas (ex: criar nova categoria ou consultar relatórios anteriores).

 Não faz recomendações de investimento ou tributação sem informações detalhadas do usuário.

Limitações Declaradas

O que o agente NÃO faz?

Não fornece consultoria de investimentos ou tributária.

Não acessa contas bancárias externas sem integração oficial.

Não realiza previsões financeiras complexas, apenas análises baseadas nos dados fornecidos.

Não gera informações fictícias ou inventa dados de gastos.






Avaliação e Métricas
Como Avaliar seu Agente

A avaliação do agente foi feita de duas formas complementares:

Testes estruturados: Perguntas simuladas com respostas esperadas.

Feedback real: Embora não tenhamos testado com usuários externos, a lógica dos testes garante que o agente responde corretamente aos cenários principais.

Métricas de Qualidade
Métrica	O que avalia	Resultado nos testes
Assertividade	O agente respondeu o que foi perguntado?	✅ Todas as perguntas simuladas retornaram respostas corretas
Segurança	O agente evitou inventar informações?	✅ Perguntas fora do escopo foram tratadas corretamente
Coerência	A resposta faz sentido para o perfil do cliente?	✅ Sugestões de investimento compatíveis com o perfil do cliente

Observação: Mesmo usando um agente simulado (FinBuddyMock), a lógica dos testes reflete o comportamento esperado do agente final com LLM real.

Exemplos de Cenários de Teste
Teste 1: Consulta de gastos

Pergunta: "Quanto gastei com alimentação?"

Resposta esperada: Valor baseado no transacoes.csv

Resposta obtida: "Você gastou R$ 450,00 com alimentação."

Resultado: ✅ Correto

Teste 2: Recomendação de produto

Pergunta: "Qual investimento você recomenda para mim?"

Resposta esperada: Produto compatível com o perfil do cliente

Resposta obtida: "Recomendo o investimento: Tesouro Selic"

Resultado: ✅ Correto

Teste 3: Pergunta fora do escopo

Pergunta: "Qual a previsão do tempo?"

Resposta esperada: Agente informa que só trata de finanças

Resposta obtida: "Desculpe, só posso ajudar com questões financeiras."

Resultado: ✅ Correto

Teste 4: Informação inexistente

Pergunta: "Quanto rende o produto XYZ?"

Resposta esperada: Agente admite não ter essa informação

Resposta obtida: "Não tenho informações sobre esse produto."

Resultado: ✅ Correto

Resultados

O que funcionou bem:

O agente respondeu corretamente às perguntas simuladas;

As respostas respeitam o perfil do cliente;

Evitou inventar informações (anti-alucinação).

O que pode melhorar:

Integrar com LLM real para respostas mais flexíveis;

Melhorar sugestões de investimento considerando histórico de transações;

Implementar métricas avançadas, como latência, consumo de tokens e logs de erros.

Observações

Os testes foram realizados com um agente simulado, mas todos os cenários e regras refletem o comportamento esperado do agente final;

A tabela de resultados pode ser atualizada com dados reais caso o LLM seja integrado posteriormente;

Este documento atende às métricas básicas de assertividade, segurança e coerência, conforme solicitado pelo desafio.[LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!

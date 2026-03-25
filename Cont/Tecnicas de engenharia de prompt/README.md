# Tecnicas de Engenharia de Prompt

Este README resume apenas esta aula e organiza os principais pontos do tema em formato de guia de estudo.

## Objetivo da aula

Entender como sair da percepcao de "magica" da IA e enxergar os mecanismos praticos usados para orientar LLMs com mais controle, previsibilidade e qualidade.

## Visao geral

A aula mostra que ferramentas como ChatGPT sao a camada visivel de uma base maior formada por LLMs. Em vez de tratar esses sistemas como caixas magicas, o foco e entender seus limites e como desenvolvedores guiam seu comportamento por meio de contexto, prompts, APIs e ajustes de execucao.

## Conceitos-chave

- LLMs geram texto prevendo a proxima palavra com base em grandes volumes de dados, nao "pensando" como um humano.
- Esses modelos podem refletir vieses, alucinar fatos e falhar quando o contexto fornecido e fraco ou inadequado.
- Engenharia de contexto define o que o modelo sabe em cada interacao, incluindo instrucoes, historico, documentos externos e ferramentas.
- Engenharia de prompt define como o modelo deve agir sobre esse contexto, transformando um problema real em um comando claro e direcionado.
- Um assistente especializado pode ser construido com uma base de conhecimento derivada de transcricoes, fragmentacao do conteudo, embeddings e recuperacao de trechos relevantes antes da geracao da resposta.
- Na pratica, desenvolvedores normalmente usam APIs de modelos prontos e ajustam hiperparametros como `temperature` e `max_tokens` para equilibrar criatividade, objetividade e custo.
- A qualidade da resposta depende diretamente da qualidade do contexto e da clareza do prompt: se a entrada for ruim, a saida tambem tende a ser ruim.

## Aplicacoes praticas

- Delimitar o escopo da tarefa antes de pedir qualquer resposta ao modelo.
- Fornecer contexto relevante, regras e materiais de apoio em vez de depender apenas do conhecimento generico da IA.
- Escrever prompts com objetivo, restricoes, formato de saida e criterio de qualidade.
- Usar configuracoes mais deterministicas para tarefas factuais e respostas mais criativas apenas quando isso fizer sentido.
- Em conteudos especializados, conectar o modelo a uma base de conhecimento confiavel em vez de deixar a resposta aberta.

## Referencias

- Video de apoio: [Da Magia a Engenharia de IA](https://youtu.be/Nz7_QQjvRXs)
- O video acima foi gerado no NotebookLM a partir do material da aula e foi usado aqui como referencia contextual.

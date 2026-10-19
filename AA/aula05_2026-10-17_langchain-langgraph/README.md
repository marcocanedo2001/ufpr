# AA Aula 05 de 17 de outubro de 2026

Professor Vinícius. Tema da seção no Moodle: LangChain e LangGraph. Laboratório de preparação para o projeto de classificação de avaliações.

## Começar

Siga [o ambiente Conda da disciplina](../CONDA_SETUP.md). A sequência mantém três camadas: entender o problema, acompanhar o funcionamento e praticar no notebook.

| Ordem | Notebook | Resultado de aprendizagem |
| --- | --- | --- |
| 1 | notebook/01_ambiente_api.ipynb | Verificar kernel, interpretar JSON e validar entradas |
| 2 | notebook/02_prompt_chain.ipynb | Acompanhar template, modelo simulado e parser |
| 3 | notebook/03_projeto_avaliacoes.ipynb | Planejar e implementar sua própria chain de classificação |
| 4 | notebook/04_langgraph.ipynb | Executar e explicar um grafo com validação e duas rotas |

Os notebooks são exercícios autorais, não cópias dos Colabs do professor. Nenhuma célula faz uma chamada paga ou baixa pesos automaticamente. O notebook 03 deixa a implementação avaliada para você desenvolver; não é uma entrega pronta.

## Entrega confirmada

[Moodle Entrega do Projeto](https://moodle.c3sl.ufpr.br/mod/assign/view.php?id=66424): inserir apenas o link do repositório, até **31/10/2026 às 23h59**, horário exibido no Moodle, consultado em 19/10. A seção informa presença 70% e projeto **ou** questionário 30%. O esqueleto solicita uma chain para indicar se as avaliações obtidas da API são positivas ou negativas, usando os componentes LangChain trabalhados em aula.

Não há obrigação explícita de LangGraph no texto consultado. O notebook 04 é aprofundamento. A preparação não iniciou questionário nem enviou atividade.

## Materiais e organização

- `material/FONTES.md`: slides, Colabs e projetos oficiais com status de acesso.
- `notebook/`: percurso guiado de estudo.
- `src/`: validação de dados e exercício de grafo, sem solução do classificador.
- `data/avaliacoes_sinteticas.json`: amostra pequena, identificada como sintética.
- `tests/`: verificações offline dos contratos e do grafo.
- `anotacoes/ROTEIRO_ESTUDO.md`: etapas e conferência antes da entrega.

Arquivos originais do Moodle devem permanecer para uso pessoal. A pasta `material/originais/` está ignorada no Git para que PDFs e notebooks do professor não sejam publicados inadvertidamente.

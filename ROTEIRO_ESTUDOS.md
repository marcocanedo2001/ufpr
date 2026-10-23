# Roteiro de estudos e laboratórios

Atualização de 19/10/2026. As disciplinas já organizadas são PYAI, FLLM, CONT, DSLLM, AA e PROD. Os índices de aula de cada pasta continuam como referência. Esta atualização prepara as duas aulas recentes e relaciona seus pré-requisitos, sem inventar materiais das demais aulas.

## Prioridade de entrega

| Sequência | Onde estudar | Prática correspondente |
| --- | --- | --- |
| 1 | AA aula05 slides Aula 01 e Aula 02 | Ler antes da implementação, especialmente Aula 02 p. 46 |
| 2 | AA notebook 01 | JSON, descrição das avaliações e tratamento de falhas |
| 3 | AA notebook 02 | Prompt, modelo, parser e chain |
| 4 | AA notebooks 05 e 06 | CSV e janela de conversa; templates, placeholder e Pydantic |
| 5 | AA notebook 03 | Implementar sua chain de classificação e preparar o repositório |
| 6 | AA notebook 04 | LangGraph como aprofundamento, depois da chain |
| 7 | DSLLM aula08 | Multimodal: imagem, vídeo, áudio, ferramentas e evidências |

Entrega AA: link do repositório no Moodle, até 31/10/2026 às 23h59, conforme atividade consultada. Enunciado confirmado nos PDFs: prompt, model e parser em uma chain; escolha de modelo local ou provedor; commit no GitHub. Chains de resposta aos comentários são desafio adicional.

## Pastas e ambientes

- AA/CONDA_SETUP.md e AA/environment.yml: ambiente `aa`, kernel Python (AA).
- AA/aula05_2026-10-17_langchain-langgraph/: material, notebook, anotacoes, src, tests e data.
- DSLLM/aula08_2026-10-16_audio-imagem-videos/environment.yml: ambiente `dsllm-multimodal`, separado do dsllm existente.
- DSLLM/aula08_2026-10-16_audio-imagem-videos/: material, notebook, anotacoes e data, com status real dos requisitos externos.

## Pré-requisitos nas outras matérias

| Disciplina | Rever quando houver dificuldade |
| --- | --- |
| PYAI | Listas, dicionários, funções, CSV, módulos e exceções |
| FLLM | Representação, classificação, matriz de confusão e limitações do modelo |
| CONT | Mensagens, prompt, contexto e recuperação de evidências |
| PROD | Organização do repositório e instruções para outra pessoa executar |

## Disponibilidade real

AA: dois PDFs recebidos e lidos, seis notebooks autorais e três projetos oficiais obtidos para consulta pessoal. Os Colabs continuam como links, sem cópia ipynb confirmada. Modelos Ollama não foram baixados. O uso remoto de Groq exige configuração própria.

DSLLM aula08: slides HTML e notebook original recebidos. O projeto completo com `lectures/04-multimodal-toolkit`, sobretudo `media/yellowstone_burn_recovery.mp4`, não está disponível. BreastMNIST, EuroSAT, Whisper tiny, embeddings e modelos Ollama exigem downloads para execução completa. Não crie uma pasta vazia como se fosse o projeto completo.

A instalação no seu Windows e a execução real com modelos não foram feitas. Configurações e práticas offline foram preparadas para facilitar essa etapa. Os originais ficam fora do Git público e dentro do pacote pessoal de laboratório.

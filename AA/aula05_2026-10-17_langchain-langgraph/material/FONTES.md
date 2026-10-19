# Fontes da aula e status de obtenção

Conferência em 19/10/2026 na seção LangChain & LangGraph, Aula I de 17/10/2026, Moodle UFPR.

| Material | Link oficial | Cópia local |
| --- | --- | --- |
| Slide 01 LangChain do Zero à Prática | https://moodle.c3sl.ufpr.br/mod/resource/view.php?id=66421 | Cópia pessoal recebida e lida em 19/10; material/originais/ (ignorado no Git) |
| Slide 02 LangChain Analisando Questões Operacionais | https://moodle.c3sl.ufpr.br/mod/resource/view.php?id=66422 | Cópia pessoal recebida e lida em 19/10; material/originais/ (ignorado no Git) |
| Colab conversacional simples | https://colab.research.google.com/drive/16Z7KMgQ-lwgH9iwgIsisWoe3sWD7yp9g?usp=sharing | Link oficial, não executado |
| Colab conversacional local | https://colab.research.google.com/drive/1ifILhSNPRt6TWVewNULmLroQ03jVnauR?usp=sharing | Link oficial, não executado |
| Colab modelos de prompt | https://colab.research.google.com/drive/1eeBcvzyqI8juV-2X91-fODe3zMVtd5dc?usp=sharing | Link oficial, não executado |

Projetos oficiais:
- https://github.com/fulbergarciaufpr/GenAI-LangChain-PrimeiroAgente
- https://github.com/fulbergarciaufpr/GenAI-LangChain-LLMLocal
- https://github.com/fulbergarciaufpr/GenAI-LangChain-AgenteAvaliador

O esqueleto do avaliador foi relido na fonte pública e usado para identificar a tarefa. O restante do percurso é complemento de estudo. Os PDFs recebidos têm 40 e 46 páginas. LangGraph é citado na página 8 da primeira apresentação, sem implementação nos dois conjuntos de slides. Isso não permite concluir tudo o que foi dito oralmente.

As cópias recebidas estão disponíveis localmente em `material/originais/` para leitura offline, sem publicação no repositório público.

Documentação oficial de apoio:
- https://docs.langchain.com/oss/python/langgraph/graph-api
- https://docs.langchain.com/oss/python/langgraph/workflows-agents
- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/oss/python/langgraph/interrupts

## Escopo confirmado nos PDFs

- Aula 01 p. 40: persistir histórico em CSV, carregar antes da conversa, atualizar a cada interação e limitar a janela. O slide pede remover vírgulas; compare esse procedimento com CSV que preserve o texto.
- Aula 02 pp. 14–15: quatro turnos completos correspondem a nove mensagens contando system. A retomada usa uma janela inicial diferente da formulação da atividade anterior; registre a interpretação adotada.
- Aula 02 pp. 17–36: PromptTemplate, ChatPromptTemplate, placeholder e esquema com Pydantic.
- Aula 02 pp. 37–45: chain prompt, model e parser. RunnableLambda fica explicitamente para a aula seguinte.
- Aula 02 p. 46: chain para classificar avaliações; modelo local ou provedor; commit em repositório próprio. Chains para responder aos comentários são desafio adicional.

Aula 02 traz “ChatPrompt” em um trecho sem definir a classe; nos exercícios use ChatPromptTemplate, conforme a importação real. Solicitar JSON não aplica sozinho um modelo Pydantic. “Confiança” declarada pelo modelo não equivale a probabilidade calibrada. Modelo local continua tendo contexto e recursos finitos.

Os três repositórios oficiais foram clonados em material/projetos-originais/ para consulta pessoal. Essa pasta está ignorada no Git público. Os arquivos Colab não foram exportados.

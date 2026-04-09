# Tecnicas de Engenharia de Prompt

Material de apoio da aula `Engenharia de Contexto`, da Especializacao em Inteligencia Artificial Generativa, com foco em como projetar contexto, prompts e aplicacoes com LLMs de forma mais controlada, util e reprodutivel.

## Visao geral da aula

A apresentacao parte de uma ideia central: LLMs nao devem ser tratados como "magica", mas como sistemas estatisticos que respondem com base no contexto disponivel e na forma como a tarefa e formulada.

Os principais blocos da aula sao:

- fundamentos sobre LLMs e como eles funcionam
- diferenca entre engenharia de contexto e engenharia de prompt
- uso de APIs e hiperparametros de inferencia
- frameworks para acessar modelos e construir aplicacoes
- desenho de aplicacoes com RAG
- avaliacao de aplicacoes baseadas em LLMs
- tecnicas praticas de prompt engineering

## O que sao LLMs

Segundo a aula, LLMs sao modelos treinados para prever o proximo token em uma sequencia de texto. Eles nao "pensam" como humanos; operam por padroes estatisticos aprendidos em grandes volumes de dados.

Pontos centrais:

- um LLM recebe texto de entrada e retorna texto de saida
- tokens sao representacoes numericas de partes do texto
- embeddings sao representacoes vetoriais que aproximam significados semelhantes
- transformers usam mecanismos como self-attention para misturar contexto e prever a proxima palavra

A aula tambem reforca algumas implicacoes praticas desse funcionamento:

- o modelo tende a produzir respostas "medias", parecidas com o que aparece com frequencia na internet
- LLMs podem refletir vieses, desinformacao e inconsistencias dos dados de treino
- o modelo nao possui crencas, senso de verdade ou memoria humana real
- respostas devem sempre ser verificadas, principalmente em tarefas de maior risco

## Engenharia de Contexto x Engenharia de Prompt

### Engenharia de Contexto

Engenharia de contexto e a pratica de projetar, estruturar e controlar o fluxo de informacoes fornecidas ao modelo.

Na aula, ela aparece como aquilo que define:

- o que o modelo sabe naquele momento
- a qualidade, coerencia e custo da resposta
- o nivel de ambiguidade e a chance de alucinacao

Em termos simples:

- contexto = dados, documentos, historico, instrucoes e fontes acessiveis ao modelo

### Engenharia de Prompt

Engenharia de prompt e o conjunto de estrategias usadas para dizer ao modelo como agir sobre esse contexto.

Na aula, isso envolve:

- traduzir um problema real para uma forma textual adequada ao modelo
- induzir comportamentos desejados
- especificar formato, estilo, criterios e restricoes da saida

Em termos simples:

- prompt = a forma de controle sobre o uso do contexto

### Relacao entre os dois

A apresentacao resume essa relacao assim:

- contexto fornece a materia-prima
- prompt define a forma de processamento
- qualidade da saida depende dos dois

Principios destacados:

- `garbage in, garbage out`
- mais contexto nao significa necessariamente resposta melhor
- relevancia importa mais do que quantidade
- contexto e prompt devem ter responsabilidades separadas

## Exemplo conceitual da aula: assistente com RAG

Um dos exemplos centrais da apresentacao e um assistente virtual para um curso de inferencia estatistica, construido a partir de videos das aulas.

Arquitetura resumida:

1. transcricao dos videos
2. segmentacao em chunks
3. geracao de embeddings
4. armazenamento em vector store
5. retriever para busca semantica
6. LLM para gerar a resposta
7. prompt para controlar comportamento e formato
8. memoria para historico da conversa
9. classificador para filtrar perguntas fora do escopo

Comportamentos desejados no exemplo:

- responder apenas com base no conteudo das aulas
- responder em portugues
- incluir links e timestamps quando apropriado
- reduzir alucinacao por meio de grounding

Esse exemplo e usado para mostrar que qualidade em GenAI depende menos de "um prompt genial" e mais de uma boa arquitetura de contexto.

## Uso de APIs para trabalhar com LLMs

A aula tambem apresenta APIs como a ponte pratica entre aplicacoes e modelos prontos.

Ideia central:

- a aplicacao envia uma requisicao
- o modelo processa a entrada
- a API retorna a resposta

Por que usar APIs:

- integracao mais simples com aplicacoes
- escalabilidade sem manter infraestrutura propria
- acesso a modelos atualizados com frequencia
- aceleracao de prototipagem e desenvolvimento

Para comecar, a aula destaca que normalmente voce precisa de:

- um fornecedor de API
- uma chave valida
- um modelo escolhido
- ambiente de desenvolvimento configurado
- leitura da documentacao da API

## Hiperparametros discutidos na aula

Os hiperparametros controlam o comportamento da inferencia sem alterar os pesos do modelo.

Parametros enfatizados:

- `temperature`: controla aleatoriedade
- `top_p`: controla amostragem por nucleo
- `max_tokens`: limita tamanho da resposta
- `stop`: define pontos de parada
- `n`: gera multiplas respostas
- `logit_bias`: favorece ou evita tokens
- `seed`: ajuda na reprodutibilidade, quando suportado
- `stream`: devolve tokens em tempo real

Regras praticas apresentadas:

- tarefas factuais e estruturadas tendem a usar menor temperatura
- tarefas criativas aceitam maior exploracao
- custo, latencia e comprimento da resposta devem ser controlados explicitamente
- na pratica, os melhores valores dependem da aplicacao e precisam ser testados

## Escolha de fornecedores e frameworks

A apresentacao distingue duas camadas:

### Frameworks para acessar modelos

Foco em usar o LLM como ferramenta dentro da linguagem de programacao.

Exemplos citados na aula:

- `chatlas`
- `llm`
- `ellmer`
- `tidychatmodels`

Vantagens:

- interface unificada entre fornecedores
- menos codigo para tarefas comuns
- troca mais facil de provedor
- maior produtividade em prototipos

### Frameworks para construir aplicacoes

Foco em desenvolver sistemas mais completos com fluxos, dados externos, RAG e agentes.

Exemplos citados:

- `LangChain`
- `LangGraph`
- `LlamaIndex`
- `AutoGen`
- `PydanticAI`

Esses frameworks aparecem na aula como suporte para:

- integracao com documentos, bancos e APIs
- orquestracao de fluxos complexos
- personalizacao e escalabilidade
- aplicacoes com RAG e agentes

## Como pensar uma aplicacao com LLM

A aula trata uma aplicacao de LLM como uma camada de traducao entre dois dominios:

- o problema do usuario
- o dominio do modelo

Isso significa que o sistema precisa:

1. entender o problema real do usuario
2. converter esse problema para uma entrada adequada ao modelo
3. receber a saida do modelo
4. transformar essa saida em algo util para o usuario

Um principio importante da apresentacao:

- bons prompts se parecem com documentos familiares ao conjunto de treino, como markdown, Q&A, codigo, artigo ou exercicio resolvido

## Avaliacao de aplicacoes com LLMs

A aula deixa claro que avaliacao nao e opcional, porque LLMs sao probabilisticos e sensiveis a pequenas mudancas de contexto e prompt.

### Avaliacao offline

Usada antes do deploy, com dados simulados ou historicos.

Indicadores citados:

- acuracia ou correcao
- relevancia
- taxa de alucinacao
- conformidade com formato
- consistencia
- latencia

Abordagens mencionadas:

- testes com dataset
- `LLM-as-a-judge`
- testes funcionais

### Avaliacao online

Usada em producao, com usuarios reais.

Dimensoes discutidas:

- engajamento
- qualidade percebida
- eficiencia
- confiabilidade

A mensagem da aula e direta: sistemas com LLM nunca estao "prontos"; precisam de monitoramento e adaptacao continua.

## Tecnicas de prompt engineering apresentadas

Na parte final, a apresentacao trabalha tecnicas para sair do prompt generico e construir instrucoes mais uteis.

### Ideias gerais

- clareza, especificidade e contexto melhoram a resposta
- prompt "bom o suficiente" costuma ser melhor estrategia do que buscar perfeicao teorica
- estrutura, exemplos e restricoes ajudam o modelo a produzir saidas mais confiaveis

### Estruturas e estrategias abordadas

- prompt basico
- prompt estruturado
- single-turn prompt
- multi-turn prompt
- conversation chains
- prompt templates
- zero-shot prompting
- few-shot learning
- in-context learning
- multi-step reasoning
- multi-task prompting

### Boas praticas destacadas

- usar instrucoes claras
- manter formato consistente
- evitar informacao desnecessaria
- escolher exemplos relevantes, diversos e nao ambiguos
- incluir edge cases quando fizer sentido
- avaliar com conjunto de teste apropriado e metricas adequadas

## Arquivos deste projeto

Este workspace contem exemplos praticos da aula:

- [Script1.py](/home/marco/mba_genai/Cont/Tecnicas de engenharia de prompt/Script1.py): chamadas diretas a API da OpenAI via `requests`
- [Script2.py](/home/marco/mba_genai/Cont/Tecnicas de engenharia de prompt/Script2.py): exemplos com `chatlas` e `LangChain`
- [Script1.ipynb](/home/marco/mba_genai/Cont/Tecnicas de engenharia de prompt/Script1.ipynb): versao em notebook do script 1
- [Script2.ipynb](/home/marco/mba_genai/Cont/Tecnicas de engenharia de prompt/Script2.ipynb): versao em notebook do script 2
- `Engenharia_Contexto_Aula1.pdf`: apresentacao base da aula

## Ambiente local

Este projeto usa um ambiente Conda chamado `cont01`.

### Criar ou atualizar o ambiente

```bash
conda env create -f environment.yml
conda env update -f environment.yml --prune
```

### Configurar a chave da OpenAI

1. Copie `.env.example` para `.env`
2. Preencha `OPENAI_API_KEY` no arquivo `.env`

Os scripts e notebooks carregam automaticamente o `.env` da raiz do projeto. Se a variavel `OPENAI_API_KEY` ja estiver exportada no shell, ela tambem sera usada.

### Validar a configuracao

```bash
conda env list | rg cont01
python -c "import requests, dotenv, openai, chatlas, shiny, langchain_openai, langchain_core; print('ok')"
```

Ao entrar nesta pasta pelo terminal em `zsh`, o ambiente `cont01` deve ser ativado automaticamente. No VS Code/Cursor, o interpretador Python do workspace tambem deve apontar para esse ambiente.

## Referencias

- Apresentacao: `Engenharia_Contexto_Aula1.pdf`
- Video de apoio: [Da Magia a Engenharia de IA](https://youtu.be/Nz7_QQjvRXs)
- Leituras e referencias mencionadas na aula:
  - Anthropic Academy
  - documentacao oficial dos fornecedores
  - *Prompt Engineering for LLMs*
  - *Getting started with AI: Good enough prompting*

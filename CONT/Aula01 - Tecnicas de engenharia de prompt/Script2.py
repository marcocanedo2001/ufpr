## Engenharia de Contexto: Aula 1 ----------------------------------------------
## Prof. Wagner Hugo Bonat · Especialização GenAI/UFPR -------------------------

# No terminal rode para instalar o chatlas
# pip install -U chatlas
# pip install openai
# pip install shiny

# Importando
import os
from pathlib import Path
from dotenv import load_dotenv

## Carregando variáveis da raiz do projeto, sem depender de caminho fixo
env_path = Path(__file__).resolve().parent / ".env"

## Carregando as variáveis de ambiente
load_dotenv(env_path)


## Exemplo básico de uso do chatlas
import chatlas as ctl
from chatlas import ChatOpenAI
from chatlas import token_usage

## Cria o chat
chat = ChatOpenAI(
  model = "gpt-4o",
  system_prompt = """Você é um especialista em visualização de dados. \
  Deve oferecer ajuda sempre baseada na gramática dos gráficos. \
  Não responda nada fora do contexto de visualização de dados."""
)


## Outra opção é usar direto no terminal (também não gosto)
chat.console() # Para sair digite ESC

## Chamada estilo programação
resposta = chat.chat("Qual gráfico devo usar para mostrar relações?")
print(str(resposta))

## Outras opções de chamada
resposta = chat.chat("Qual gráfico devo usar para mostrar relações?", echo = "none") # Não imprime a saida
print(str(resposta))

resposta = chat.chat("Qual gráfico devo usar para mostrar relações?", echo = "all") # Imprime tudo
print(str(resposta))

## stream se refere a ir imprimindo a resposta em real time. Não curto muito mas da pra fazer
response = chat.stream("O que é um diagrama de dispersão?")
for chunk in response:
    print(chunk, end="")

## Verificando quantos tokens foram usados
token_usage()

################################################################################
## Usando o LangChain ##########################################################
################################################################################

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

system_prompt = "Você é um assistente de perguntas e respostas."

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
])

## Exemplo 1: Controle de criatividade (temperature)
llm_deterministico = ChatOpenAI(
  model = "gpt-4o",
  temperature=0
)

llm_criativo = ChatOpenAI(
    model="gpt-4o",
    temperature=0.9
)

chain_det = prompt | llm_deterministico
chain_criativo = prompt | llm_criativo

pergunta = "Quem é Wagner Hugo Bonat?"

print("Determinístico:")
print(chain_det.invoke({"input": pergunta}).content)

print("\nCriativo:")
print(chain_criativo.invoke({"input": pergunta}).content)

## Exemplo 2 - Controle de tamanho
llm_curto = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=50
)

llm_longo = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=300
)

chain_curto = prompt | llm_curto
chain_longo = prompt | llm_longo

print("Resposta curta:")
print(chain_curto.invoke({"input": pergunta}).content)

print("\nResposta longa:")
print(chain_longo.invoke({"input": pergunta}).content)


## Exemplo 3 - Penalização de repetição
llm_sem_penalidade = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    frequency_penalty=0
)

llm_com_penalidade = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    frequency_penalty=1.0
)

chain1 = prompt | llm_sem_penalidade
chain2 = prompt | llm_com_penalidade

pergunta = "Liste vantagens de usar modelos estatísticos"

print("Sem penalidade:")
print(chain1.invoke({"input": pergunta}).content)

print("\nCom penalidade:")
print(chain2.invoke({"input": pergunta}).content)

## Exemplo 4 - Controle de diversidade (top_p)
llm_conservador = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    top_p=0.5
)

llm_diverso = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    top_p=1.0
)

chain1 = prompt | llm_conservador
chain2 = prompt | llm_diverso

pergunta = "Dê exemplos de aplicações de regressão"

print("Menos diversidade:")
print(chain1.invoke({"input": pergunta}).content)

print("\nMais diversidade:")
print(chain2.invoke({"input": pergunta}).content)

## Tente com outros modelos.


## Fim do Script 2 ------------------------------------------------------------

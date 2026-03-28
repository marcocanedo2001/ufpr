## Engenharia de contexto · Aula 1 ---------------------------------------------
## Prof. Wagner Hugo Bonat · GenAI/UFPR ----------------------------------------

# Método padrão usando requisição httr agnóstico de SDK (Software Development Kit)

## No terminal rode (apenas se você não tiver instalado as bibliotecas)
## pip install os requests python-dotenv 

## Setando o ambiente 
import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

## Carregando variáveis da raiz do projeto, sem depender de caminho fixo
env_path = Path(__file__).resolve().parent / ".env"

## Carregando as variáveis de ambiente
load_dotenv(env_path)

## Pegando a api key
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key não encontrada")

################################################################################
## Usando a API antiga da OPENAI chamada de completions ########################
################################################################################

## URL do endpoint da API (vai estar na documentação da API)
url = 'https://api.openai.com/v1/chat/completions'

## Header da solicitação (note aqui é que entra a sua chave da api)

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

## Escolha do modelo
## Prompt
## Hiperparâmetros (max_tokens e temperature)
## Solicitação
## Extrair a resposta

## Primeiro modelo realmente comercial da OpenAI

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'system', 'content': 'Você é um especialista em Inteligência Artificial Generativa.'},
        {'role': 'user', 'content': 'Explique o que são LLMs e como ganhar dinheiro com eles.'}
    ],
    'max_tokens': 500,
    'temperature': 0.7
}

## Finalmente! Chamamos a API (request)
response = requests.post(url, headers=headers, data=json.dumps(data))

## Inspecionando o objeto de saida
print("=== Status da Resposta ===")
print(f"Status Code       : {response.status_code}")  # Código de status HTTP (Se tudo deu certo é 200)
print(f"Motivo            : {response.reason}")       # Motivo textual do status (ex: 'OK', 'Bad Request') 
print(f"Sucesso?          : {response.ok}")           # Retorna True se o status for 200–399

print("\n=== Cabeçalhos da Resposta ===")
for key, value in response.headers.items():
    print(f"{key}: {value}")                          # Cabeçalhos HTTP da resposta

print("\n=== Corpo da Resposta ===")
print(f"Texto (raw)       : {response.text[:200]}...")  # Resposta em texto puro (limitado a 200 caracteres)
print(f"JSON (parsed)     : {response.json()}")         # Converte o corpo da resposta em JSON (se aplicável)

print("\n=== Informações da Solicitação (Request) ===")
print(f"Método HTTP       : {response.request.method}")    # Método HTTP usado (GET, POST, etc.)
print(f"URL               : {response.request.url}")       # URL da solicitação
print(f"Cabeçalhos Enviados: {response.request.headers}") # Cabeçalhos HTTP enviados
print(f"Payload Enviado   : {response.request.body}")     # Corpo da solicitação enviado

print("\n=== Tempo de Resposta ===")
print(f"Tempo de resposta : {response.elapsed}")           # Tempo de resposta (delta de tempo)

print("\n=== Cookies (se houver) ===")
print(f"Cookies recebidos : {response.cookies}")           # Cookies retornados pela API

print("\n=== Histórico de Redirecionamento ===")
print(f"Histórico de Redirects: {response.history}")  

## Resposta final
resposta = response.json()
resposta['choices'][0]['message']['content'] ## 
print(resposta['choices'][0]['message']['content'] )

################################################################################
## Refazendo a chamada usando a nova API da OpenAI - responses #################
################################################################################

## Endereço da API
url = "https://api.openai.com/v1/responses"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

## A questão do system prompt deixou de ser tão importante!
## Chamada minima
data = {
    "model": "gpt-3.5-turbo",
    "input": "Você é um especialista em Inteligência Artificial Generativa.\nExplique o que são LLMs e como ganhar dinheiro com eles."
}

response = requests.post(url, headers=headers, json=data)
resposta = response.json()

texto = resposta["output"][0]["content"][0]["text"]
print(texto)

## Efeito das gerações de modelos
data = {
    "model": "gpt-4.1",
    "input": "Você é um especialista em Inteligência Artificial Generativa.\nExplique o que são LLMs e como ganhar dinheiro com eles."
}

response = requests.post(url, headers=headers, json=data)
resposta_2 = response.json()

texto_2 = resposta_2["output"][0]["content"][0]["text"]
print(texto_2)

## Mais moderno
## GPT 5.4 foi lançado em março/2026
data = {
    "model": "gpt-5.4",
    "input": "Você é um especialista em Inteligência Artificial Generativa.\nExplique o que são LLMs e como ganhar dinheiro com eles."
}

response = requests.post(url, headers=headers, json=data) ## Note o tempo para a resposta (latência)
resposta_3 = response.json()

texto_3 = resposta_3["output"][0]["content"][0]["text"]
print(texto_3)

## Evolução em termos de resposta, formato, qualidade, tamanho e latência.
## Modelos bem antigos como o GPT-2 DAVINCI que eram apenas de completar (sem instrução e chat)
## não estão mais disponíveis via API.

## FIM -------------------------------------------------------------------------

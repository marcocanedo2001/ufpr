import datetime
from typing_extensions import Annotated

import requests
from fastapi import Body, FastAPI, HTTPException, Path, Query

# Cria a aplicacao FastAPI que sera exposta pelo servidor.
app = FastAPI()

# Armazena pessoas em memoria apenas para fins didaticos.
# A chave do dicionario e o CPF e o valor e outro dicionario com os dados da pessoa.
dict_pessoas = {}


# Endpoint simples para testar se a API esta respondendo.
@app.get("/saudacao")
def saudacao():
    # Retorna uma mensagem estatica em formato JSON.
    return {"message": "Olá, mundo!"}


# Endpoint para mostrar a data e hora atuais do servidor.
@app.get("/hora_atual")
def hora_atual():
    # Converte o horario atual para texto para facilitar a exibicao no JSON.
    return {"hora": str(datetime.datetime.now())}


# Endpoint que orquestra duas APIs do Open-Meteo para buscar o clima por cidade.
@app.get("/clima/{cidade}")
def consultar_clima(
    cidade: Annotated[
        str,
        Path(
            title="Cidade",
            description="Nome da cidade usada para consultar clima no Open-Meteo",
            min_length=2,
        ),
    ],
):
    # Define a URL da API de geocoding usada para descobrir latitude e longitude.
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    # Monta os parametros da busca limitando a resposta a uma unica cidade.
    geo_params = {"name": cidade, "count": 1, "language": "pt", "format": "json"}

    try:
        # Faz a primeira chamada externa para obter as coordenadas da cidade.
        geo_response = requests.get(geo_url, params=geo_params, timeout=10)
        geo_response.raise_for_status()
    except requests.RequestException as exc:
        # Retorna erro de integracao caso a API externa falhe.
        raise HTTPException(
            status_code=502,
            detail="Falha ao consultar o servico de geocoding",
        ) from exc

    # Converte a resposta da API para dicionario Python.
    geo_data = geo_response.json()

    # Valida se a cidade foi encontrada antes de continuar a orquestracao.
    if not geo_data.get("results"):
        raise HTTPException(status_code=400, detail="Cidade nao encontrada")

    # Extrai os principais dados da cidade retornados pelo geocoding.
    cidade_encontrada = geo_data["results"][0]
    latitude = cidade_encontrada["latitude"]
    longitude = cidade_encontrada["longitude"]

    # Define a URL da API de previsao e clima atual do Open-Meteo.
    weather_url = "https://api.open-meteo.com/v1/forecast"

    # Monta os parametros para pedir somente o clima atual nas coordenadas encontradas.
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    try:
        # Faz a segunda chamada externa usando as coordenadas da primeira resposta.
        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_response.raise_for_status()
    except requests.RequestException as exc:
        # Retorna erro de integracao caso a API de clima falhe.
        raise HTTPException(
            status_code=502,
            detail="Falha ao consultar o servico de clima",
        ) from exc

    # Converte a resposta de clima para dicionario Python.
    weather_data = weather_response.json()

    # Garante que o bloco de clima atual foi retornado pela API.
    if "current_weather" not in weather_data:
        raise HTTPException(status_code=502, detail="Resposta de clima invalida")

    # Retorna um payload consolidado com cidade, coordenadas e clima atual.
    return {
        "cidade_pesquisada": cidade,
        "cidade_encontrada": cidade_encontrada["name"],
        "pais": cidade_encontrada.get("country"),
        "latitude": latitude,
        "longitude": longitude,
        "clima_atual": weather_data["current_weather"],
    }


# Endpoint que valida um CPF recebido como parametro de caminho.
@app.get("/verificar-cpf/{cpf_teste}")
def verificar_cpf(
    cpf_teste: Annotated[
        int,
        Path(
            title="CPF",
            description="O CPF a ser testado",
            ge=1,
            le=99999999999,
        ),
    ],
):
    # Inicializa os acumuladores usados para calcular os digitos verificadores.
    somatorio_valida_ultimo = 0
    somatorio_valida_penultimo = 0

    # Separa os dois ultimos digitos do CPF para validacao posterior.
    ultimo = cpf_teste % 10
    cpf_teste //= 10
    penultimo = cpf_teste % 10
    cpf_teste //= 10

    # Inicia a soma do ultimo digito com o penultimo, como pede a regra do CPF.
    somatorio_valida_ultimo = penultimo * 2

    # Percorre os digitos restantes e monta os somatorios dos dois verificadores.
    for i in range(2, 12):
        modulo = cpf_teste % 10
        cpf_teste //= 10
        somatorio_valida_penultimo += modulo * i
        somatorio_valida_ultimo += modulo * (i + 1)

    # Valida o penultimo digito verificador.
    modulo = somatorio_valida_penultimo % 11
    if modulo < 2:
        if penultimo != 0:
            return {"cpf_valido": False}
    else:
        if penultimo != 11 - modulo:
            return {"cpf_valido": False}

    # Valida o ultimo digito verificador.
    modulo = somatorio_valida_ultimo % 11
    if modulo < 2:
        if ultimo != 0:
            return {"cpf_valido": False}
    else:
        if ultimo != 11 - modulo:
            return {"cpf_valido": False}

    # Se todas as validacoes passaram, o CPF e considerado valido.
    return {"cpf_valido": True}


# Endpoint POST para cadastrar uma pessoa.
@app.post("/adicionar-pessoa")
def adicionar_pessoa(
    cpf: Annotated[
        int,
        Body(
            embed=True,
            description="CPF da pessoa que sera cadastrada",
            ge=1,
            le=99999999999,
        ),
    ],
    nome: Annotated[
        str,
        Body(
            embed=True,
            description="Nome da pessoa que sera cadastrada",
            min_length=1,
        ),
    ],
):
    # Evita sobrescrever uma pessoa que ja existe.
    if cpf in dict_pessoas:
        raise HTTPException(status_code=409, detail="CPF ja cadastrado")

    # Salva a pessoa no dicionario em memoria.
    dict_pessoas[cpf] = {"cpf": cpf, "nome": nome}

    # Retorna os dados cadastrados.
    return {"mensagem": "Pessoa cadastrada com sucesso", "pessoa": dict_pessoas[cpf]}


# Endpoint GET para consultar o nome de uma pessoa pelo CPF.
@app.get("/nome-pessoa/{cpf}")
def nome_pessoa(
    cpf: Annotated[
        int,
        Path(
            title="CPF",
            description="CPF da pessoa que sera consultada",
            ge=1,
            le=99999999999,
        ),
    ],
):
    # Retorna erro 404 caso a pessoa nao exista no cadastro.
    if cpf not in dict_pessoas:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada")

    # Retorna somente o nome para manter o exemplo simples.
    return {"nome": dict_pessoas[cpf]["nome"]}


# Endpoint PUT para substituir completamente os dados de uma pessoa existente.
@app.put("/pessoa/{cpf}")
def atualizar_pessoa_put(
    cpf: Annotated[
        int,
        Path(
            title="CPF",
            description="CPF da pessoa que sera atualizada por PUT",
            ge=1,
            le=99999999999,
        ),
    ],
    nome: Annotated[
        str,
        Body(
            embed=True,
            description="Novo nome completo da pessoa",
            min_length=1,
        ),
    ],
):
    # Garante que o PUT seja aplicado apenas em uma pessoa ja existente.
    if cpf not in dict_pessoas:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada")

    # O PUT substitui o recurso inteiro neste exemplo simples.
    dict_pessoas[cpf] = {"cpf": cpf, "nome": nome}

    # Retorna o recurso completo apos a substituicao.
    return {"mensagem": "Pessoa atualizada com PUT", "pessoa": dict_pessoas[cpf]}


# Endpoint PATCH para alterar parcialmente os dados de uma pessoa.
@app.patch("/pessoa/{cpf}")
def atualizar_pessoa_patch(
    cpf: Annotated[
        int,
        Path(
            title="CPF",
            description="CPF da pessoa que sera atualizada por PATCH",
            ge=1,
            le=99999999999,
        ),
    ],
    nome: Annotated[
        str,
        Body(
            embed=True,
            description="Novo nome parcial ou completo da pessoa",
            min_length=1,
        ),
    ],
):
    # Confirma que a pessoa existe antes de aplicar a alteracao parcial.
    if cpf not in dict_pessoas:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada")

    # O PATCH altera apenas o campo informado na requisicao.
    dict_pessoas[cpf]["nome"] = nome

    # Retorna o estado atualizado do recurso.
    return {"mensagem": "Pessoa atualizada com PATCH", "pessoa": dict_pessoas[cpf]}


# Endpoint DELETE para remover uma pessoa do cadastro.
@app.delete("/pessoa/{cpf}")
def remover_pessoa(
    cpf: Annotated[
        int,
        Path(
            title="CPF",
            description="CPF da pessoa que sera removida",
            ge=1,
            le=99999999999,
        ),
    ],
):
    # Verifica se a pessoa realmente existe antes de tentar remover.
    if cpf not in dict_pessoas:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada")

    # Remove a pessoa do dicionario e guarda os dados removidos para retorno.
    pessoa_removida = dict_pessoas.pop(cpf)

    # Informa que a exclusao foi concluida com sucesso.
    return {"mensagem": "Pessoa removida com sucesso", "pessoa": pessoa_removida}


# Endpoint assíncrono simples para demonstrar o uso de async def no FastAPI.
@app.get("/teste_async")
async def teste(
    id: Annotated[
        int,
        Query(
            title="Identificador",
            description="Identificador numerico enviado para o teste assincrono",
            ge=1,
        ),
    ],
):
    # Retorna uma mensagem de teste concatenando o identificador recebido.
    return "Teste " + str(id)

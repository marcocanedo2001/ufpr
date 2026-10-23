"""Classificação das avaliações da API com Ollama e validação por item."""

import json

import httpx
import requests
from ollama import ResponseError
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

URL_AVALIACOES = "https://apis.codante.io/api/reviews-api/reviews"
MODELO = "qwen2.5:3b"

SYSTEM_MESSAGE = """Classifique o sentimento da experiência geral do cliente.
Aplique as regras nesta ordem:
1. Considere apenas os aspectos mencionados; cada aspecto distinto conta uma vez.
2. Se houver um único aspecto, siga o sentimento dele.
3. Se houver vários aspectos, siga a maioria dos aspectos positivos ou negativos.
4. Apenas em empate, siga o sentimento do produto; se produto não for mencionado, siga o atendimento.
5. Se o empate continuar sem resolução, responda negativo.

Responda exatamente positivo ou negativo: uma palavra no masculino e em minúsculas.
Não inclua prefixos, explicações, aspas ou pontuação na resposta.

Exemplo 1:
Comentário: O suporte foi atencioso e resolveu minha dúvida.
Resposta: positivo

Exemplo 2:
Comentário: O aparelho não funciona, embora a equipe tenha sido gentil.
Resposta: negativo

Classifique o próximo comentário seguindo as mesmas regras.
Sua resposta deve conter somente positivo ou negativo."""


def construir_chain(modelo=None):
    """Cria a sequência; não consulta API nem executa classificação."""
    if modelo is None:
        modelo = ChatOllama(
            model=MODELO,
            temperature=0,
            base_url="http://localhost:11434",
            client_kwargs={"trust_env": False, "timeout": 120},
        )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_MESSAGE),
        ("human", "Comentario: {comentario}"),
    ])
    return prompt | modelo | StrOutputParser()


def buscar_avaliacoes():
    """Consulta somente a página retornada pela URL do esqueleto."""
    resposta = requests.get(URL_AVALIACOES, timeout=20)
    resposta.raise_for_status()
    payload = resposta.json()
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError("Esperada uma lista no campo data")
    # A descrição é validada individualmente para não perder os outros itens.
    return payload["data"]


def validar_rotulo(saida):
    if not isinstance(saida, str):
        raise ValueError("Saída precisa ser texto")
    rotulo = saida.strip().lower()
    if rotulo not in {"positivo", "negativo"}:
        raise ValueError("Rótulo fora do contrato")
    return rotulo


def processar_avaliacoes(avaliacoes, chain):
    resultados = []
    for indice, item in enumerate(avaliacoes):
        registro = {
            "id": item.get("id", indice) if isinstance(item, dict) else indice,
            "texto": item.get("description") if isinstance(item, dict) else None,
            "esperado": item.get("esperado") if isinstance(item, dict) else None,
            "saida_bruta": None,
            "previsto": None,
            "erro": None,
        }
        # Sem ID de origem, a posição é usada como identificador substituto.
        try:
            if not isinstance(item, dict):
                raise ValueError("Avaliação precisa ser um objeto")
            texto = registro["texto"]
            if not isinstance(texto, str) or not texto.strip():
                raise ValueError("Descrição precisa ser texto não vazio")
            registro["saida_bruta"] = chain.invoke({"comentario": texto})
            registro["previsto"] = validar_rotulo(registro["saida_bruta"])
        except (ValueError, httpx.HTTPError, ResponseError) as exc:
            registro["erro"] = f"{type(exc).__name__}: {exc}"
        resultados.append(registro)
    return resultados


def main():
    try:
        avaliacoes = buscar_avaliacoes()
    except (requests.RequestException, ValueError) as exc:
        print(f"Coleta não concluída: {type(exc).__name__}: {exc}")
        return 1

    print(f"Modelo: {MODELO}")
    print(f"Avaliações recebidas na página: {len(avaliacoes)}")
    resultados = processar_avaliacoes(avaliacoes, construir_chain())
    for registro in resultados:
        print(json.dumps(registro, ensure_ascii=False))
    falhas = sum(item["erro"] is not None for item in resultados)
    print(f"Processadas: {len(resultados)} | Com falha: {falhas}")
    print("Sem rótulos humanos revisados da API, não se calcula acurácia.")
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())

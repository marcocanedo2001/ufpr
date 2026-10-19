"""Contratos do laboratório; não implementa o classificador avaliado."""
import requests

def extrair_avaliacoes(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ValueError("Esperada uma lista no campo data")
    saida = []
    for i, item in enumerate(payload["data"]):
        if not isinstance(item, dict):
            raise ValueError(f"Item {i} não é um objeto")
        texto = item.get("description")
        if not isinstance(texto, str) or not texto.strip():
            raise ValueError(f"Descrição inválida no item {i}")
        saida.append({"id": item.get("id", i), "texto": texto})
    return saida

def buscar_avaliacoes():
    resposta = requests.get(
        "https://apis.codante.io/api/reviews-api/reviews", timeout=20
    )
    resposta.raise_for_status()
    return extrair_avaliacoes(resposta.json())

def validar_rotulo(saida):
    if not isinstance(saida, str):
        raise ValueError("Saída precisa ser texto")
    rotulo = saida.strip().lower()
    if rotulo not in {"positivo", "negativo"}:
        raise ValueError("Rótulo fora do contrato")
    return rotulo

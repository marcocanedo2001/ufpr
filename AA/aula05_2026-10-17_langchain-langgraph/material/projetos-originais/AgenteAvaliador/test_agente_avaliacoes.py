"""Testes locais; --modelo-real habilita a avaliação com o Ollama."""

import json
import sys
import unittest
from unittest.mock import patch

import requests
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from agente_avaliacoes import (
    buscar_avaliacoes, construir_chain, processar_avaliacoes, validar_rotulo,
)


class Contratos(unittest.TestCase):
    def test_padronizacao_e_rejeicao(self):
        self.assertEqual(validar_rotulo(" POSITIVO "), "positivo")
        for valor in ("talvez", "sentimento: positivo", "positiva", None):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                validar_rotulo(valor)

    def test_preservacao_e_continuidade(self):
        chain = construir_chain(FakeListChatModel(responses=["talvez", "positivo"]))
        itens = [
            {"id": 1, "description": " "},
            {"id": 2, "description": "Bom, MAS caro!"},
            {"id": 3, "description": "Entrega excelente."},
        ]
        registros = processar_avaliacoes(itens, chain)
        self.assertEqual(len(registros), 3)
        self.assertIsNotNone(registros[0]["erro"])
        self.assertEqual(registros[1]["texto"], itens[1]["description"])
        self.assertEqual(registros[1]["id"], 2)
        self.assertEqual(registros[1]["saida_bruta"], "talvez")
        self.assertIsNone(registros[1]["previsto"])
        self.assertEqual(registros[2]["previsto"], "positivo")
        self.assertIsNone(registros[2]["erro"])

    def test_timeout_nao_e_lista_vazia(self):
        with patch("agente_avaliacoes.requests.get", side_effect=requests.Timeout("teste")):
            with self.assertRaises(requests.Timeout):
                buscar_avaliacoes()

    def test_contrato_api_e_status_http(self):
        with patch("agente_avaliacoes.requests.get") as get:
            get.return_value.json.return_value = {"data": "inválido"}
            with self.assertRaises(ValueError):
                buscar_avaliacoes()
            get.return_value.raise_for_status.assert_called_once()
            self.assertEqual(get.call_args.kwargs["timeout"], 20)
        with patch("agente_avaliacoes.requests.get") as get:
            get.return_value.raise_for_status.side_effect = requests.HTTPError("503")
            with self.assertRaises(requests.HTTPError):
                buscar_avaliacoes()


def testar_modelo_real():
    # Rótulos definidos antes desta execução; não são uma referência humana independente.
    frases = [
        ("O produto é excelente.", "positivo"),
        ("O produto é ótimo, o atendimento foi péssimo e a entrega atrasou.", "negativo"),
        ("O produto veio quebrado, mas o atendimento foi excelente.", "negativo"),
        ("A entrega foi rápida, mas a embalagem veio danificada.", "negativo"),
        ("entrega excelente.", "positivo"),
        ("O produto é bom e o atendimento foi excelente.", "positivo"),
        ("Não tive nenhum problema com o equipamento.", "positivo"),
        ("Não compraria novamente: a bateria parou no primeiro dia.", "negativo"),
        ("O equipamento funciona perfeitamente, mas a entrega demorou demais.", "positivo"),
        ("O atendente foi grosseiro, embora a entrega tenha sido rápida.", "negativo"),
    ]
    itens = [{"id": i, "description": texto, "esperado": esperado}
             for i, (texto, esperado) in enumerate(frases, 1)]
    resultados = processar_avaliacoes(itens, construir_chain())
    for item in resultados:
        print(json.dumps(item, ensure_ascii=False))
    acertos = sum(r["previsto"] == r["esperado"] for r in resultados)
    falhas = sum(r["erro"] is not None for r in resultados)
    print(f"Acertos: {acertos}/{len(resultados)} | Falhas de processamento: {falhas}")
    print("Casos 1–6: desenvolvimento; casos 7–10: complementares. Amostra exploratória.")
    return 0 if acertos == len(resultados) else 1


if __name__ == "__main__":
    if "--modelo-real" in sys.argv:
        raise SystemExit(testar_modelo_real())
    unittest.main()

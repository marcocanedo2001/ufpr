import unittest
from src.dados import extrair_avaliacoes, validar_rotulo

class Contratos(unittest.TestCase):
    def test_preserva_texto_e_id(self):
        item = {"id": 5, "description": "Muito bom, MAS caro!"}
        self.assertEqual(extrair_avaliacoes({"data": [item]}),
                         [{"id": 5, "texto": item["description"]}])
    def test_rejeita_estrutura_ou_descricao_invalida(self):
        for obj in [{}, {"data": {}}, {"data": [None]},
                    {"data": [{"description": " "}]}]:
            with self.subTest(obj=obj), self.assertRaises(ValueError):
                extrair_avaliacoes(obj)
    def test_rotulos(self):
        self.assertEqual(validar_rotulo(" Positivo "), "positivo")
        for valor in ["talvez", "não é positivo", None]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                validar_rotulo(valor)

if __name__ == "__main__":
    unittest.main()

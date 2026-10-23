import unittest
from src.grafo_estudo import app

class Grafo(unittest.TestCase):
    def test_caminho_valido(self):
        r=app.invoke({"texto":"Bom", "simulada":"Positivo"})
        self.assertEqual(r["sentimento"], "positivo")
    def test_vazio_nao_chama_etapa_seguinte(self):
        r=app.invoke({"texto":" ", "simulada":"positivo"})
        self.assertEqual(r["erro"], "entrada inválida")
        self.assertNotIn("bruta", r)
    def test_saida_invalida(self):
        r=app.invoke({"texto":"Bom", "simulada":"talvez"})
        self.assertEqual(r["erro"], "saída inválida")

if __name__ == "__main__":
    unittest.main()

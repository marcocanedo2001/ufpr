import unittest
import tempfile
from pathlib import Path
from src.historico import janela, salvar_csv, carregar_csv

class Historico(unittest.TestCase):
    def setUp(self):
        self.msgs=[("system", "Contexto")]
        for i in range(5):self.msgs += [("human", f"Pergunta {i}"), ("assistant", f"Resposta {i}")]
    def test_janelas_preservam_pares(self):
        for n in [2,4]:
            r=janela(self.msgs,n)
            self.assertEqual(len(r),1+2*n)
            self.assertEqual(r[0],self.msgs[0])
            self.assertEqual(r[1:],self.msgs[-2*n:])
    def test_rejeita_turno_incompleto(self):
        with self.assertRaises(ValueError):janela(self.msgs[:-1])
    def test_csv_preserva_e_compara_simplificacao(self):
        msgs=[("system","Contexto"),("human",'Bom, mas "caro".\nChegou hoje'),("assistant","Entendi")]
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"historico.csv"
            salvar_csv(p,msgs)
            self.assertEqual(carregar_csv(p),msgs)
            salvar_csv(p,msgs,remover_virgulas=True)
            self.assertEqual(carregar_csv(p)[1][1],msgs[1][1].replace(",",""))

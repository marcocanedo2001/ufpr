from __future__ import annotations

import unittest

from identificador_idioma.comparacao import comparar_perfis
from identificador_idioma.frequencia import calcular_frequencia


class TestCalcularFrequencia(unittest.TestCase):
    def test_retorna_alfabeto_completo_quando_texto_vazio(self) -> None:
        resultado = calcular_frequencia("")

        self.assertEqual(len(resultado), 26)
        self.assertTrue(all(valor == 0.0 for valor in resultado.values()))

    def test_calcula_percentuais_corretamente(self) -> None:
        resultado = calcular_frequencia("aaabbc")

        self.assertAlmostEqual(resultado["a"], 50.0)
        self.assertAlmostEqual(resultado["b"], 33.33333333333333)
        self.assertAlmostEqual(resultado["c"], 16.666666666666664)
        self.assertAlmostEqual(sum(resultado.values()), 100.0)

    def test_lanca_erro_para_tipo_invalido(self) -> None:
        with self.assertRaises(TypeError):
            calcular_frequencia(None)  # type: ignore[arg-type]


class TestCompararPerfis(unittest.TestCase):
    def test_retorna_idioma_mais_similar(self) -> None:
        freq_texto = {"a": 50.0, "b": 30.0, "c": 20.0}
        perfis = {
            "Idioma_A": {"a": 50.0, "b": 30.0, "c": 20.0},
            "Idioma_B": {"a": 10.0, "b": 10.0, "c": 80.0},
            "Idioma_C": {"a": 40.0, "b": 35.0, "c": 25.0},
        }

        idioma, similaridade, ranking = comparar_perfis(freq_texto, perfis)

        self.assertEqual(idioma, "Idioma_A")
        self.assertAlmostEqual(similaridade, 1.0)
        self.assertGreater(ranking["Idioma_A"], ranking["Idioma_C"])
        self.assertGreater(ranking["Idioma_C"], ranking["Idioma_B"])

    def test_trata_letras_ausentes_no_perfil_como_zero(self) -> None:
        freq_texto = {"a": 100.0, "b": 0.0}
        perfis = {
            "Idioma_A": {"a": 100.0},
            "Idioma_B": {"a": 0.0, "b": 100.0},
        }

        idioma, similaridade, ranking = comparar_perfis(freq_texto, perfis)

        self.assertEqual(idioma, "Idioma_A")
        self.assertAlmostEqual(similaridade, 1.0)
        self.assertGreater(ranking["Idioma_A"], ranking["Idioma_B"])

    def test_lanca_erro_quando_nao_ha_perfis(self) -> None:
        with self.assertRaises(ValueError):
            comparar_perfis({"a": 100.0}, {})


if __name__ == "__main__":
    unittest.main()

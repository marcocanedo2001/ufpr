from __future__ import annotations

import unittest

from identificador_idioma.limpeza import _remover_acentos, limpar_texto


class TestRemoverAcentos(unittest.TestCase):
    def test_remove_acentos_do_texto(self) -> None:
        self.assertEqual(_remover_acentos("ação útil"), "acao util")


class TestLimparTexto(unittest.TestCase):
    def test_remove_html_acentos_e_caracteres_nao_alfabeticos(self) -> None:
        texto = "<html><body>Olá, Mundo! ÁÉÍ 123</body></html>"

        self.assertEqual(limpar_texto(texto), "olamundoaei")

    def test_remove_tags_script_e_style_ignorando_caixa(self) -> None:
        texto = "<SCRIPT>alert(1)</SCRIPT><Style>p{color:red}</Style><p>Texto útil</p>"

        self.assertEqual(limpar_texto(texto), "textoutil")

    def test_decodifica_entidades_html(self) -> None:
        texto = "Jo&atilde;o &amp; Maria"

        self.assertEqual(limpar_texto(texto), "joaomaria")

    def test_permte_manter_acentos_ate_filtro_final(self) -> None:
        texto = "ação"

        self.assertEqual(limpar_texto(texto, remover_acentos=False), "ao")

    def test_lanca_erro_para_tipo_invalido(self) -> None:
        with self.assertRaises(TypeError):
            limpar_texto(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()

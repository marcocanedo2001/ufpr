from __future__ import annotations

import argparse

from .comparacao import comparar_perfis
from .download import baixar_texto
from .frequencia import calcular_frequencia
from .limpeza import limpar_texto
from .perfis import carregar_perfis_csv

DEFAULT_LANGS = "Portuguese,German,Finnish"


def build_parser() -> argparse.ArgumentParser:
    """Define interface de linha de comando do projeto."""
    parser = argparse.ArgumentParser(
        prog="identificador_idioma",
        description="Identifica idioma com base na frequência de letras.",
    )
    parser.add_argument("--url", required=True, help="URL da página a ser analisada.")
    parser.add_argument(
        "--csv",
        default="letter_frequency.csv",
        help="Caminho do CSV de frequências.",
    )
    parser.add_argument(
        "--langs",
        default=DEFAULT_LANGS,
        help="Idiomas separados por vírgula.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=15,
        help="Timeout da requisição em segundos.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=3,
        help="Quantidade de idiomas exibidos no ranking.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """TODO: orquestrar o fluxo ponta a ponta.

    Fluxo esperado:
    1. Fazer parse dos argumentos.
    2. Converter `--langs` em lista.
    3. Chamar `baixar_texto`.
    4. Chamar `limpar_texto`.
    5. Chamar `calcular_frequencia`.
    6. Chamar `carregar_perfis_csv`.
    7. Chamar `comparar_perfis`.
    8. Exibir: "O texto está em [idioma] com grau de similaridade X".
    9. Exibir ranking resumido com `--top`.
    10. Tratar erros com mensagens amigáveis e código de saída != 0.
    """
    parser = build_parser()
    _ = parser.parse_args(argv)

    raise NotImplementedError("TODO: implementar fluxo principal da CLI")

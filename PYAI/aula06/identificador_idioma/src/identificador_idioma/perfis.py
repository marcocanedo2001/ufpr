from __future__ import annotations


def carregar_perfis_csv(caminho_csv: str, idiomas: list[str]) -> dict[str, dict[str, float]]:
    """TODO: carregar perfis de idioma a partir do CSV `letter_frequency.csv`.

    O que implementar:
    1. Abrir o CSV com delimitador `;`.
    2. Ler cabeçalho e mapear nomes de idiomas para colunas.
    3. Validar se todos os idiomas solicitados existem no arquivo.
    4. Ler somente linhas de letras a-z.
    5. Limpar valores removendo `%` e `*`.
    6. Converter valores para float e montar:
       `{'Portuguese': {'a': 14.634, ...}, ...}`
    """
    raise NotImplementedError("TODO: implementar carregamento de perfis CSV")

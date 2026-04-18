from __future__ import annotations


def _remover_acentos(texto: str) -> str:
    """TODO: remover acentos com `unicodedata`.

    Sugestão:
    - normalizar com `unicodedata.normalize('NFD', texto)`
    - remover caracteres de marca diacrítica (categoria `Mn`)
    """
    raise NotImplementedError("TODO: implementar remoção de acentos")


def limpar_texto(texto_bruto: str, remover_acentos: bool = True) -> str:
    """TODO: limpar texto bruto mantendo somente letras a-z.

    O que implementar:
    1. Decodificar entidades HTML (`html.unescape`).
    2. Remover tags HTML (regex simples), incluindo script/style.
    3. Converter para minúsculas.
    4. Se `remover_acentos=True`, chamar `_remover_acentos`.
    5. Remover tudo que não for [a-z].
    6. Retornar string limpa para cálculo de frequência.
    """
    raise NotImplementedError("TODO: implementar limpeza de texto")

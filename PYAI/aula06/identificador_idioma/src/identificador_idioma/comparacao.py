from __future__ import annotations


def comparar_perfis(
    freq_texto: dict[str, float], perfis: dict[str, dict[str, float]]
) -> tuple[str, float, dict[str, float]]:
    """TODO: comparar o perfil do texto com os perfis de idioma.

    O que implementar:
    1. Calcular distância euclidiana entre `freq_texto` e cada perfil.
    2. Converter distância em similaridade (ex.: `1 / (1 + distancia)`).
    3. Encontrar o idioma com maior similaridade.
    4. Retornar:
       - idioma mais provável
       - similaridade do melhor idioma
       - ranking completo de similaridades por idioma
    """
    raise NotImplementedError("TODO: implementar comparação de perfis")

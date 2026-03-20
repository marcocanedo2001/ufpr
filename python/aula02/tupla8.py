"""
8. ORDENAÇÃO PERSONALIZADA
   Crie uma função `ordenar_pessoas` que recebe uma lista de tuplas no formato
   (nome, idade, altura) e retorna uma nova lista ordenada de acordo com um critério
   especificado por parâmetro:
   - Critério 1: ordenar por nome
   - Critério 2: ordenar por idade (crescente)
   - Critério 3: ordenar por altura (decrescente)
   - Critério 4: ordenar por idade e depois por altura

   Utilize a função sorted() com parâmetro key personalizado.
"""


def ordenar_pessoas(pessoas, criterio):
    if criterio == 1:
        return sorted(pessoas, key=lambda x: x[0])  # Ordenar por nome
    elif criterio == 2:
        return sorted(pessoas, key=lambda x: x[1])  # Ordenar por idade (crescente)
    elif criterio == 3:
        return sorted(
            pessoas, key=lambda x: x[2], reverse=True
        )  # Ordenar por altura (decrescente)
    elif criterio == 4:
        return sorted(
            pessoas, key=lambda x: (x[1], -x[2])
        )  # Ordenar por idade e depois por altura
    else:
        raise ValueError(
            "Critério inválido. Use 1 para nome, 2 para idade, 3 para altura ou 4 para idade e altura."
        )


# Exemplo de uso
pessoas = [("Alice", 30, 1.65), ("Bob", 25, 1.80), ("Charlie", 30, 1.70)]
print(ordenar_pessoas(pessoas, 1))  # Ordenar por nome
print(ordenar_pessoas(pessoas, 2))  # Ordenar por idade
print(ordenar_pessoas(pessoas, 3))  # Ordenar por altura
print(ordenar_pessoas(pessoas, 4))  # Ordenar por idade e depois por altura

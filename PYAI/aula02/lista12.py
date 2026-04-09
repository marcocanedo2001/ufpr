"""
12. COMBINAÇÕES E PERMUTAÇÕES
    Escreva uma função recursiva que receba uma lista de elementos (sem repetição)
    e retorne uma lista contendo todas as permutações possíveis desses elementos.

    Exemplo: Entrada = [1, 2, 3]
    Saída = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""


def permutacoes(lista):
    if len(lista) == 0:
        return [[]]

    resultado = []
    for i in range(len(lista)):
        elemento = lista[i]
        restante = lista[:i] + lista[i + 1 :]
        for p in permutacoes(restante):
            resultado.append([elemento] + p)

    return resultado


# Exemplo de uso
entrada = [1, 2, 3]
saida = permutacoes(entrada)
print(saida)

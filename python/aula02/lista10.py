"""
10. PESQUISA EM LISTA ORDENADA
    Implemente uma função chamada pesquisa_binaria
    que receba uma lista ordenada
    e um valor alvo. A função deve retornar a posição do
    valor na lista ou -1 se não existir.
    Não utilize funções prontas como index() ou in.
"""


def pesquisa_binaria(lista, valor_alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor_alvo:
            return meio
        elif lista[meio] < valor_alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# Exemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
valor_alvo = 7
posicao = pesquisa_binaria(lista_ordenada, valor_alvo)
if posicao != -1:
    print(f"Valor {valor_alvo} encontrado na posição {posicao}.")
else:
    print(f"Valor {valor_alvo} não encontrado na lista.")

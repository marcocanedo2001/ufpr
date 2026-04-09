"""
ISTA DE EXERCÍCIOS - PYTHON (TEMA: TUPLAS E FUNÇÕES)
======================================================

NÍVEL 1 - INICIANTE
-------------------

1. OPERAÇÕES BÁSICAS COM TUPLAS
   Crie uma função chamada `analisar_tupla` que recebe uma tupla de números inteiros
   e retorna uma nova tupla contendo:
   - O menor valor
   - O maior valor
   - A soma de todos os valores
   - A quantidade de elementos

   Exemplo:
   entrada = (5, 2, 8, 1, 9, 3)
   saída = (1, 9, 28, 6)
não utilize funções prontas como min(), max(),
sum() ou len() para resolver este exercício.
"""


def analisar_tupla(tupla):
    if not tupla:
        return None  # Retorna None para tuplas vazias

    menor = tupla[0]
    maior = tupla[0]
    soma = 0
    quantidade = 0

    for numero in tupla:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero
        quantidade += 1

    return (menor, maior, soma, quantidade)


# Exemplo de uso
entrada = (5, 2, 8, 1, 9, 3)
saida = analisar_tupla(entrada)
print(saida)  # Saída: (1, 9, 28, 6)

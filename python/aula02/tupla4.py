"""
4. PAR OU IMPAR
   Desenvolva uma funcao chamada `classificar_numeros` que recebe uma lista de numeros
   e retorna duas tuplas: uma com os numeros pares e outra com os numeros impares.

   Exemplo:
   entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   saida = (2, 4, 6, 8, 10) e (1, 3, 5, 7, 9)
"""


def classificar_numeros(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return tuple(pares), tuple(impares)


# Exemplo de uso
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = classificar_numeros(entrada)
print("Numeros pares:", pares)
print("Numeros impares:", impares)

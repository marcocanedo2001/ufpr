"""
2. CONTADOR DE VOGAIS
   Escreva uma função chamada `contar_vogais` que recebe uma string como parâmetro
   e retorna uma tupla com a contagem de cada vogal (a, e, i, o, u) presente na string,
   considerando maiúsculas e minúsculas.

   Exemplo:
   entrada = "Python é uma linguagem incrível"
   saída = (4, 2, 3, 2, 1)  # (a, e, i, o, u)
"""


def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contagem = [0] * 5  # Inicializa a contagem para cada vogal

    for char in texto:
        if char in vogais:
            index = vogais.index(char) % 5  # Obtém o índice da vogal (0-4)
            contagem[index] += 1  # Incrementa a contagem da vogal correspondente

    return tuple(contagem)  # Retorna a contagem como uma tupla


# Exemplo de uso
entrada = "Python é uma linguagem incrível"
saida = contar_vogais(entrada)
print(saida)  # Saída: (4, 2, 3, 2, 1)

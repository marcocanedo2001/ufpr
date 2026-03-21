import numpy as np


def sequencia_fib(qtde_valores):
    # Cria um array com o tamanho desejado para armazenar a sequencia.
    resposta = np.empty(qtde_valores, dtype=int)
    a = 0
    b = 1
    idx = 0

    while idx < qtde_valores:
        resposta[idx] = a
        # Atualiza os dois ultimos valores da sequencia.
        aux = b
        b = a + b
        a = aux
        idx += 1

    return resposta


def enesimo_fib(n):
    a = 0
    b = 1

    while n > 0:
        # Avanca uma posicao na sequencia a cada iteracao.
        aux = b
        b = a + b
        a = aux
        n -= 1

    return a


def estimar_prop_aurea(n_fibonacci):
    a = 0
    b = 1

    while n_fibonacci > 0:
        # Calcula termos consecutivos para estimar a razao aurea.
        aux = b
        b = a + b
        a = aux
        n_fibonacci -= 1

    return b / a

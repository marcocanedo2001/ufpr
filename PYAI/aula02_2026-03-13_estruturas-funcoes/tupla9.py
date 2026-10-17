"""
9. PROCESSAMENTO DE MATRIZES
   Implemente funções para manipular matrizes representadas
     como tuplas de tuplas
   (imutáveis, como se fossem matrizes reais):

   - `criar_matriz(linhas, colunas, valor_inicial=0)`:
   retorna uma matriz com dimensões especificadas
   - `somar_matrizes(m1, m2)`: retorna a soma de duas matrizes (tupla de tuplas)
   - `multiplicar_matrizes(m1, m2)`: retorna o produto de duas matrizes (se possível)
   - `transpor_matriz(m)`: retorna a matriz transposta
   - `diagonal_principal(m)`: retorna uma tupla com os elementos da diagonal principal
   - `traco(m)`: retorna a soma dos elementos da diagonal principal (se matriz quadrada)
   - `menor_elemento(m)`: retorna uma tupla (valor, linha, coluna) do menor elemento

   Lembre-se: como são tuplas, você precisará
   criar novas estruturas em vez de modificar as existentes.
"""


def criar_matriz(linhas, colunas, valor_inicial=0):
    """Cria uma matriz (tupla de tuplas) com as dimensões
    especificadas e valor inicial."""
    return tuple(tuple(valor_inicial for _ in range(colunas)) for _ in range(linhas))


def somar_matrizes(m1, m2):
    """Retorna a soma de duas matrizes (tupla de tuplas)."""
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões.")
    return tuple(
        tuple(m1[i][j] + m2[i][j] for j in range(len(m1[0]))) for i in range(len(m1))
    )


def multiplicar_matrizes(m1, m2):
    """Retorna o produto de duas matrizes (se possível)."""
    if len(m1[0]) != len(m2):
        raise ValueError(
            "O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda."
        )
    return tuple(
        tuple(
            sum(m1[i][k] * m2[k][j] for k in range(len(m1[0])))
            for j in range(len(m2[0]))
        )
        for i in range(len(m1))
    )


def transpor_matriz(m):
    """Retorna a matriz transposta."""
    return tuple(tuple(m[j][i] for j in range(len(m))) for i in range(len(m[0])))


def diagonal_principal(m):
    """Retorna uma tupla com os elementos da diagonal principal."""
    return tuple(m[i][i] for i in range(min(len(m), len(m[0]))))


def traco(m):
    """Retorna a soma dos elementos da diagonal principal (se matriz quadrada)."""
    if len(m) != len(m[0]):
        raise ValueError("A matriz deve ser quadrada para calcular o traço.")
    return sum(m[i][i] for i in range(len(m)))


def menor_elemento(m):
    """Retorna uma tupla (valor, linha, coluna) do menor elemento."""
    menor = m[0][0]
    posicao = (0, 0)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] < menor:
                menor = m[i][j]
                posicao = (i, j)
    return (menor, posicao[0], posicao[1])


# Exemplo de uso:
if __name__ == "__main__":
    m1 = criar_matriz(2, 3, 1)
    m2 = criar_matriz(2, 3, 2)
    print("Matriz 1:", m1)
    print("Matriz 2:", m2)
    print("Soma:", somar_matrizes(m1, m2))

    m3 = criar_matriz(3, 2, 3)
    print("Matriz 3:", m3)
    print("Produto (m1 x m3):", multiplicar_matrizes(m1, m3))

    print("Transposta de m1:", transpor_matriz(m1))

    m4 = criar_matriz(3, 3, 4)
    print("Matriz 4:", m4)
    print("Diagonal principal de m4:", diagonal_principal(m4))
    print("Traço de m4:", traco(m4))

    m5 = criar_matriz(2, 2, 5)
    print("Matriz 5:", m5)
    print("Menor elemento de m5:", menor_elemento(m5))

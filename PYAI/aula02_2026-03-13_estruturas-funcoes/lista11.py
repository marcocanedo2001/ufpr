"""
11. LISTA ESPIRAL
    Crie um programa que gere uma matriz quadrada de tamanho N
    (fornecido pelo usuário) preenchida com números em ordem
    crescente no formato espiral, começando do canto
    superior esquerdo e girando no sentido horário.

    Exemplo para N=4:
    1   2   3   4
    12 13  14   5
    11 16  15   6
    10  9   8   7
"""


def gerar_matriz_espiral(n):
    matriz = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while num <= n * n:
        # Preencher a linha superior
        for i in range(left, right + 1):
            matriz[top][i] = num
            num += 1
        top += 1

        # Preencher a coluna direita
        for i in range(top, bottom + 1):
            matriz[i][right] = num
            num += 1
        right -= 1

        # Preencher a linha inferior
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matriz[bottom][i] = num
                num += 1
            bottom -= 1

        # Preencher a coluna esquerda
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = num
                num += 1
            left += 1

    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print("\t".join(map(str, linha)))


def main():
    n = int(input("Digite o tamanho da matriz quadrada (N): "))
    matriz_espiral = gerar_matriz_espiral(n)
    imprimir_matriz(matriz_espiral)


if __name__ == "__main__":
    main()

"""
7. LISTAS DENTRO DE LISTAS
   Faça um programa que crie uma matriz 3x3 (3 linhas e 3 colunas) preenchida com números
   fornecidos pelo usuário. No final, exiba a matriz na tela e mostre:
   - A soma de todos os elementos
   - A soma da primeira linha
   - A soma da diagonal principal
"""

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)

# Exibir a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Antes estava errado porque soma_total, soma_primeira_linha e soma_diagonal_principal
# eram usados com += sem terem sido inicializados.
soma_total = 0
soma_primeira_linha = 0
soma_diagonal_principal = 0

# Antes a soma total nem chegava a funcionar por causa do NameError.
# Agora somamos todos os elementos percorrendo cada linha e cada número.
for linha in matriz:
    for numero in linha:
        soma_total += numero

# Antes estava errado porque linha[0] soma a primeira coluna, não a primeira linha.
for numero in matriz[0]:
    soma_primeira_linha += numero

# Antes a diagonal era recalculada várias vezes dentro de dois laços desnecessários.
# O correto é somar apenas os elementos [0][0], [1][1] e [2][2].
for i in range(3):
    soma_diagonal_principal += matriz[i][i]

print(f"Soma de todos os elementos: {soma_total}")
print(f"Soma da primeira linha: {soma_primeira_linha}")
print(f"Soma da diagonal principal: {soma_diagonal_principal}")

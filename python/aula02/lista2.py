"""
2. MAIOR E MENOR VALOR
   Crie um programa que leia 7 números inteiros, armazene-os em uma lista e mostre 
   o maior e o menor valor digitados, juntamente com suas respectivas posições
"""
lista = []

for i in range(7):
    numero = int(input(f"Digite o {i + 1}o numero inteiro: "))
    lista.append(numero)

maior = lista[0]
menor = lista[0]
posicao_maior = 0
posicao_menor = 0

for i in range(1, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicao_maior = i
    if lista[i] < menor:
        menor = lista[i]
        posicao_menor = i

print("Lista:", lista)
print("Maior valor:", maior, "- posicao:", posicao_maior)
print("Menor valor:", menor, "- posicao:", posicao_menor)

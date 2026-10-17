"""1. SOMA DOS ELEMENTOS
   Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário 
   e exiba a soma de todos os elementos
"""
lista = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}o numero inteiro: "))
    lista.append(numero)

soma = 0

for numero in lista:
    soma = soma + numero

print("Lista:", lista)
print("Soma dos elementos:", soma)

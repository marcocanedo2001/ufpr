"""
6. REMOVENDO DUPLICATAS
   Desenvolva um programa que receba uma lista de numeros inteiros (pode ter valores repetidos)
   e crie uma nova lista apenas com os valores unicos, mantendo a ordem de primeira aparicao.
"""

lista = []
lista_unica = []

numero = int(input("Digite um numero inteiro ou -1 para parar: "))

while numero != -1:
    lista.append(numero)
    numero = int(input("Digite um numero inteiro ou -1 para parar: "))

for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero)

print("Lista original:", lista)
print("Lista sem duplicatas:", lista_unica)

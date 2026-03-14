"""
3. CONTAGEM DE PARES
   Faça um programa que gere uma lista com 10 números aleatórios entre 1 e 100
   e mostre quantos deles são pares
"""

import random

lista = []
quantidade_pares = 0

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)

    if numero % 2 == 0:
        quantidade_pares = quantidade_pares + 1

print("Lista gerada:", lista)
print("Quantidade de numeros pares:", quantidade_pares)

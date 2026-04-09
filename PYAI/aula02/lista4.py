"""
4. INVERTENDO A LISTA
   Escreva um programa que leia 6 palavras e as armazene em uma lista.
   Em seguida, exiba a lista na ordem inversa sem usar o método reverse()
   ou fatiamento [::-1].
"""

lista = []

for i in range(6):
    palavra = input(f"Digite a {i + 1}a palavra: ")
    lista.append(palavra)

print("Lista na ordem inversa:")

for i in range(5, -1, -1):
    print(lista[i])

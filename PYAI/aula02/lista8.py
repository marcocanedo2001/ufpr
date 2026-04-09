"""
8. INTERCALANDO LISTAS
   Escreva um programa que leia duas listas de 5 elementos
   cada e gere uma terceira lista
   com os elementos intercalados
   (primeiro da lista A, primeiro da lista B,
   segundo da lista A, etc.)
"""

listaA = []
listaB = []
listaC = []
print("Digite os elementos da lista A:")
for i in range(5):
    elemento = input(f"Elemento {i + 1}: ")
    listaA.append(elemento)

print("Digite os elementos da lista B:")
for i in range(5):
    elemento = input(f"Elemento {i + 1}: ")
    listaB.append(elemento)

# Intercalar os elementos das listas A e B
for i in range(5):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print("Lista intercalada:")
print(listaC)

"""1. SOMA DOS ELEMENTOS
   Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário 
   e exiba a soma de todos os elementos
"""
lista=[]
i=0
item = input("inclua os objetos da lista ou sair para teminar: ")
while item != "sair":
    lista.append(item)
    i=1+1
    item = input("inclua os objetos da lista ou sair para teminar: " )
for i in lista:
    print(i)
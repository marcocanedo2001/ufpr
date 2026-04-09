"""
1. AGENDA TELEFONICA SIMPLES
   Crie um dicionario vazio e adicione 5 contatos com nome como chave e telefone como valor.
   Depois, permita que o usuario:
   - Consulte o telefone de um contato pelo nome
   - Exiba todos os contatos cadastrados
   - Verifique se um contato especifico existe na agenda
"""

agenda = {}

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}o contato: ")
    telefone = input(f"Digite o telefone de {nome}: ")
    agenda[nome] = telefone

nome_consulta = input("Digite o nome do contato para consultar o telefone: ")

if nome_consulta in agenda:
    print()
    print("Resultado da consulta:")
    print("Telefone de", nome_consulta + ":", agenda[nome_consulta])
else:
    print()
    print("Resultado da consulta:")
    print("Contato nao encontrado.")

print()
print("Contatos cadastrados:")

for nome in agenda:
    print(nome, "-", agenda[nome])

nome_verificar = input("Digite um nome para verificar se existe na agenda: ")

if nome_verificar in agenda:
    print()
    print("O contato", nome_verificar, "existe na agenda.")
else:
    print()
    print("O contato", nome_verificar, "nao existe na agenda.")

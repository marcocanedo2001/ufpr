"""
6. AGRUPANDO POR IDADE
   Recebe nome e idade de varias pessoas ate digitar "fim".
   Depois agrupa os nomes por idade em um dicionario.
"""

pessoas_por_idade = {}

nome = input("Digite o nome da pessoa ou fim para parar: ")

while nome.lower() != "fim":
    idade = int(input("Digite a idade de " + nome + ": "))

    if idade in pessoas_por_idade:
        pessoas_por_idade[idade].append(nome)
    else:
        pessoas_por_idade[idade] = [nome]

    nome = input("Digite o nome da pessoa ou fim para parar: ")

print("Pessoas agrupadas por idade:")

for idade in pessoas_por_idade:
    print(idade, "-", pessoas_por_idade[idade])

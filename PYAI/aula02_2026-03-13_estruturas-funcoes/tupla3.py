"""
3. CADASTRO DE PESSOAS
   Crie uma função `cadastrar_pessoa` que recebe nome, idade e
     cidade como parâmetros
   e retorna uma tupla com essas informações. Depois, faça um
   programa principal que:
   - Cadastre 3 pessoas usando a função
   - Armazene as tuplas em uma lista
   - Exiba os dados de todas as pessoas cadastradas
"""


def cadastrar_pessoa(nome, idade, cidade):
    return (nome, idade, cidade)


# Programa principal
pessoas = []
pessoas.append(cadastrar_pessoa("Alice", 30, "São Paulo"))
pessoas.append(cadastrar_pessoa("Bob", 25, "Rio de Janeiro"))
pessoas.append(cadastrar_pessoa("Charlie", 35, "Belo Horizonte"))

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Cidade: {pessoa[2]}")

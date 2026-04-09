"""
13. SISTEMA DE GERENCIAMENTO DE ESTOQUE
    Desenvolva um sistema simples de estoque utilizando listas. O sistema deve:
    - Armazenar produtos com código, nome, quantidade e preço
    - Permitir cadastrar, consultar, atualizar e excluir produtos
    - Gerar relatório de produtos com estoque baixo (menos de 5 unidades)
    - Calcular o valor total do estoque
    - Permitir buscar produtos por nome ou código
    - Implementar um menu interativo para o usuário
    - desenvolver usando principalmente listas e não utilizar classes
    - não usar dicionários
"""

# Lista para armazenar os produtos
estoque = []


# Função para cadastrar um produto
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    produto = [codigo, nome, quantidade, preco]
    estoque.append(produto)
    print("Produto cadastrado com sucesso!")


# Função para consultar um produto
def consultar_produto():
    codigo = input("Digite o código do produto para consulta: ")
    for produto in estoque:
        if produto[0] == codigo:
            print(
                f"Código: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}"
            )
            return
    print("Produto não encontrado.")


# Função para atualizar um produto
def atualizar_produto():
    codigo = input("Digite o código do produto para atualização: ")
    for produto in estoque:
        if produto[0] == codigo:
            nome = input("Digite o novo nome do produto: ")
            quantidade = int(input("Digite a nova quantidade do produto: "))
            preco = float(input("Digite o novo preço do produto: "))
            produto[1] = nome
            produto[2] = quantidade
            produto[3] = preco
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")


# Função para excluir um produto
def excluir_produto():
    codigo = input("Digite o código do produto para exclusão: ")
    for i, produto in enumerate(estoque):
        if produto[0] == codigo:
            del estoque[i]
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")


# Função para gerar relatório de produtos com estoque baixo
def relatorio_estoque_baixo():
    print("Produtos com estoque baixo (menos de 5 unidades):")
    for produto in estoque:
        if produto[2] < 5:
            print(
                f"Código: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}"
            )


# Função para calcular o valor total do estoque
def calcular_valor_total_estoque():
    valor_total = 0
    for produto in estoque:
        valor_total += produto[2] * produto[3]
    print(f"Valor total do estoque: R${valor_total:.2f}")


# Função para buscar produtos por nome ou código
def buscar_produto():
    criterio = input("Digite o nome ou código do produto para busca: ")
    for produto in estoque:
        if produto[0] == criterio or produto[1].lower() == criterio.lower():
            print(
                f"Código: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}"
            )
            return
    print("Produto não encontrado.")


# Função para exibir o menu interativo
def menu():
    while True:
        print("\nMenu de Gerenciamento de Estoque")
        print("1. Cadastrar Produto")
        print("2. Consultar Produto")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Relatório de Estoque Baixo")
        print("6. Calcular Valor Total do Estoque")
        print("7. Buscar Produto por Nome ou Código")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_produto()
        elif escolha == "2":
            consultar_produto()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            excluir_produto()
        elif escolha == "5":
            relatorio_estoque_baixo()
        elif escolha == "6":
            calcular_valor_total_estoque()
        elif escolha == "7":
            buscar_produto()
        elif escolha == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
menu()

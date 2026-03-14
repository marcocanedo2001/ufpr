"""
5. ESTOQUE DE PRODUTOS
   Uma loja mantem um dicionario com produtos e suas quantidades em estoque.
   O programa recebe uma venda, verifica o estoque, atualiza e alerta se ficar abaixo de 5.
"""

estoque = {"arroz": 50, "feijao": 30, "macarrao": 20, "oleo": 15}

print("Estoque atual:")
for produto in estoque:
    print(produto, "-", estoque[produto])

produto_venda = input("Digite o produto vendido: ")
produto_venda = produto_venda.lower()
quantidade_venda = int(input("Digite a quantidade vendida: "))

if produto_venda in estoque:
    if quantidade_venda <= estoque[produto_venda]:
        estoque[produto_venda] = estoque[produto_venda] - quantidade_venda
        print("Venda realizada com sucesso.")
        print("Novo estoque de", produto_venda + ":", estoque[produto_venda])

        if estoque[produto_venda] < 5:
            print("Alerta: estoque abaixo de 5 unidades.")
    else:
        print("Estoque insuficiente.")
else:
    print("Produto nao encontrado.")

"""
9. ANÁLISE DE VENDAS
   Uma loja registra suas vendas diárias em uma lista. Cada venda é representada por uma
   sublista contendo [nome_produto, quantidade, preco_unitario].
   Crie um programa que:
   - Calcule o faturamento total
   - Encontre o produto mais vendido (em quantidade)
   - Crie uma lista apenas com os produtos que tiveram faturamento acima de R$100,00
   - Mostre a média de preço dos produtos vendidos
"""

vendas_diarias = []
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome_produto.lower() == "sair":
        break
    quantidade = int(input("Digite a quantidade vendida: "))
    preco_unitario = float(input("Digite o preço unitário: "))

    vendas_diarias.append([nome_produto, quantidade, preco_unitario])
# Calcular o faturamento total
faturamento_total = 0
for _, quantidade, preco_unitario in vendas_diarias:
    faturamento_total += quantidade * preco_unitario
print(f"Faturamento total: R${faturamento_total:.2f}")
# Encontrar o produto mais vendido (em quantidade)
produto_mais_vendido = ""
maior_quantidade = 0
for nome, quantidade, _ in vendas_diarias:
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        produto_mais_vendido = nome
print(f"Produto mais vendido: {produto_mais_vendido}")
# Criar uma lista apenas com os produtos que tiveram faturamento acima de R$100,00
produtos_acima_100 = []
for nome, quantidade, preco_unitario in vendas_diarias:
    faturamento = quantidade * preco_unitario
    if faturamento > 100:
        produtos_acima_100.append(nome)
print("Produtos com faturamento acima de R$100,00:", produtos_acima_100)
# Mostrar a média de preço dos produtos vendidos
total_preco = 0
total_produtos = 0
for _, quantidade, preco_unitario in vendas_diarias:
    total_preco += preco_unitario * quantidade
    total_produtos += quantidade
media_preco = total_preco / total_produtos if total_produtos > 0 else 0
print(f"Média de preço dos produtos vendidos: R${media_preco:.2f}")

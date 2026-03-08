"""
O programa deve calcular o Índice de Massa Corpórea (IMC) do usuário, que é dado por
peso/(altura*altura) e exibir o valor de IMC na tela.
"""

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

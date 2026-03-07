"""Calcula o IMC a partir de peso e altura informados pelo usuário."""
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

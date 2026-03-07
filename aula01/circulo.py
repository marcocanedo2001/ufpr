"""Calcula perímetro e área de um círculo com base no raio informado."""
import math

raio = float(input("Digite o raio do círculo: "))
perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2
print(f"Perímetro do círculo: {perimetro:.2f}")
print(f"Área do círculo: {area:.2f}")

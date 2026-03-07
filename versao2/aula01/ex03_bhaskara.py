"""Resolve equações do segundo grau assumindo raízes reais."""
import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = b ** 2 - 4 * a * c
if delta == 0:
    raiz1 = -b / (2 * a)
    raiz2 = raiz1
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

if abs(raiz1) < 1e-12:
    raiz1 = 0.0
if abs(raiz2) < 1e-12:
    raiz2 = 0.0

print(f"Raiz 1: {raiz1:g}")
print(f"Raiz 2: {raiz2:g}")

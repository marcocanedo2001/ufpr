"""
7. CONVERSOR DE UNIDADES
   Implemente um conversor de unidades usando funções que retornam tuplas.
   Cada função de conversão deve retornar uma tupla com o valor convertido e a unidade de destino.

   Funções a implementar:
   - `celsius_para_fahrenheit(c)`: retorna (temperatura, "F")
   - `fahrenheit_para_celsius(f)`: retorna (temperatura, "C")
   - `km_para_milhas(km)`: retorna (distância, "milhas")
   - `milhas_para_km(milhas)`: retorna (distância, "km")
   - `kg_para_libras(kg)`: retorna (peso, "lb")
   - `libras_para_kg(lb)`: retorna (peso, "kg")

   Crie um menu interativo para o usuário escolher as conversões
"""


# implementação da função celsius_para_fahrenheit
def celsius_para_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return (f, "F")


# implementação da função fahrenheit_para_celsius
def fahrenheit_para_celsius(f):
    c = (f - 32) * 5 / 9
    return (c, "C")


# implementação da função km_para_milhas
def km_para_milhas(km):
    milhas = km * 0.621371
    return (milhas, "milhas")


# implementação da função milhas_para_km
def milhas_para_km(milhas):
    km = milhas / 0.621371
    return (km, "km")


# implementação da função kg_para_libras
def kg_para_libras(kg):
    lb = kg * 2.20462
    return (lb, "lb")


# implementação da função libras_para_kg
def libras_para_kg(lb):
    kg = lb / 2.20462
    return (kg, "kg")


# menu interativo para o usuário escolher as conversões
def menu():
    while True:
        print("Escolha a conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Km para Milhas")
        print("4. Milhas para Km")
        print("5. Kg para Libras")
        print("6. Libras para Kg")
        print("7. Sair")

        escolha = input("Digite o número da conversão desejada: ")

        if escolha == "1":
            c = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(c)
            print(f"{c}°C é igual a {resultado[0]}°{resultado[1]}")

        elif escolha == "2":
            f = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(f)
            print(f"{f}°F é igual a {resultado[0]}°{resultado[1]}")

        elif escolha == "3":
            km = float(input("Digite a distância em Km: "))
            resultado = km_para_milhas(km)
            print(f"{km} Km é igual a {resultado[0]} {resultado[1]}")

        elif escolha == "4":
            milhas = float(input("Digite a distância em Milhas: "))
            resultado = milhas_para_km(milhas)
            print(f"{milhas} Milhas é igual a {resultado[0]} {resultado[1]}")

        elif escolha == "5":
            kg = float(input("Digite o peso em Kg: "))
            resultado = kg_para_libras(kg)
            print(f"{kg} Kg é igual a {resultado[0]} {resultado[1]}")

        elif escolha == "6":
            lb = float(input("Digite o peso em Libras: "))
            resultado = libras_para_kg(lb)
            print(f"{lb} Libras é igual a {resultado[0]} {resultado[1]}")

        elif escolha == "7":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# chamada do menu
menu()

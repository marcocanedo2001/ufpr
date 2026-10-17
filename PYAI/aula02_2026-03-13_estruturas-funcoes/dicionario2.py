"""
2. CONTAGEM DE CARACTERES
   Escreva um programa que receba uma palavra ou frase do usuario e crie um dicionario
   onde cada chave e uma letra e cada valor e o numero de vezes que essa letra aparece.
   Considere apenas letras (ignore espacos e diferencas entre maiusculas/minusculas).
"""

texto = input("Digite uma palavra ou frase: ")
texto = texto.lower()

contagem = {}

for caractere in texto:
    if caractere != " ":
        if caractere in contagem:
            contagem[caractere] = contagem[caractere] + 1
        else:
            contagem[caractere] = 1

print("Contagem de letras:")

for letra in contagem:
    print(letra, "-", contagem[letra])

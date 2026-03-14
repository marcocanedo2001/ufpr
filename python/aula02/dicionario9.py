"""
9. SISTEMA DE VOTACAO
   Gerencia cadastro de candidatos, votos validos, brancos e nulos.
"""

candidatos = {}
votos = {}
votos_brancos = 0
votos_nulos = 0
total_votos = 0

quantidade_candidatos = int(input("Digite a quantidade de candidatos: "))

for i in range(quantidade_candidatos):
    nome = input(f"Digite o nome do {i + 1}o candidato: ")
    numero = int(input(f"Digite o numero de {nome}: "))
    candidatos[numero] = nome
    votos[numero] = 0

print("Digite os votos. Use -1 para encerrar a votacao.")
numero_voto = int(input("Digite o numero do voto: "))

while numero_voto != -1:
    total_votos = total_votos + 1

    if numero_voto == 0:
        votos_brancos = votos_brancos + 1
    elif numero_voto in candidatos:
        votos[numero_voto] = votos[numero_voto] + 1
    else:
        votos_nulos = votos_nulos + 1

    numero_voto = int(input("Digite o numero do voto: "))

print("Resultado da votacao:")

for numero in candidatos:
    print(candidatos[numero], "-", votos[numero], "votos")

votos_validos = 0
vencedor = ""
maior_voto = -1

for numero in votos:
    votos_validos = votos_validos + votos[numero]

    if votos[numero] > maior_voto:
        maior_voto = votos[numero]
        vencedor = candidatos[numero]

if total_votos > 0:
    percentual_validos = (votos_validos / total_votos) * 100
else:
    percentual_validos = 0

print("Percentual de votos validos:", percentual_validos, "%")
print("Candidato vencedor:", vencedor)
print("Votos em branco:", votos_brancos)
print("Votos nulos:", votos_nulos)

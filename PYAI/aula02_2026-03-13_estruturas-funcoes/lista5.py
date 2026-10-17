"""
5. MEDIA E ACIMA
   Crie um programa que leia as notas de uma turma (quantidade indefinida).
   O programa deve parar quando o usuario digitar -1.
   Calcule a media da turma e mostre quantos alunos obtiveram nota acima dessa media.
"""

lista_notas = []
soma = 0

nota = float(input("Digite a nota do aluno ou -1 para parar: "))

while nota != -1:
    lista_notas.append(nota)
    soma = soma + nota
    nota = float(input("Digite a nota do aluno ou -1 para parar: "))

if len(lista_notas) > 0:
    media = soma / len(lista_notas)
    acima_media = 0

    for nota in lista_notas:
        if nota > media:
            acima_media = acima_media + 1

    print("Media da turma:", media)
    print("Quantidade de alunos acima da media:", acima_media)
else:
    print("Nenhuma nota foi digitada.")

"""
7. NOTAS POR DISCIPLINA
   Guarda 3 notas por disciplina, calcula media por disciplina, media geral
   e mostra quais disciplinas ficaram acima da media geral.
"""

notas = {}
soma_geral = 0
quantidade_notas = 0

for i in range(3):
    disciplina = input(f"Digite o nome da {i + 1}a disciplina: ")
    lista_notas = []

    for j in range(3):
        nota = float(input(f"Digite a {j + 1}a nota de {disciplina}: "))
        lista_notas.append(nota)
        soma_geral = soma_geral + nota
        quantidade_notas = quantidade_notas + 1

    notas[disciplina] = lista_notas

media_geral = soma_geral / quantidade_notas

print("Media por disciplina:")

for disciplina in notas:
    media_disciplina = sum(notas[disciplina]) / 3
    print(disciplina, "-", media_disciplina)

print("Media geral do aluno:", media_geral)
print("Disciplinas acima da media geral:")

for disciplina in notas:
    media_disciplina = sum(notas[disciplina]) / 3
    if media_disciplina > media_geral:
        print(disciplina)

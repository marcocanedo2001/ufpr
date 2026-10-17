"""
3. NOTAS DOS ALUNOS
   Crie um dicionario com nomes de 4 alunos e suas respectivas notas (valor inteiro de 0 a 10).
   Depois, calcule e mostre:
   - A media da turma
   - O aluno com a maior nota
   - Quantos alunos foram aprovados (nota >= 7)
"""

notas = {}
soma = 0
aprovados = 0

for i in range(4):
    nome = input(f"Digite o nome do {i + 1}o aluno: ")
    nota = int(input(f"Digite a nota de {nome}: "))
    notas[nome] = nota
    soma = soma + nota

media = soma / 4

nomes = list(notas.keys())
melhor_aluno = nomes[0]
maior_nota = notas[melhor_aluno]

for nome in notas:
    if notas[nome] > maior_nota:
        maior_nota = notas[nome]
        melhor_aluno = nome

    if notas[nome] >= 7:
        aprovados = aprovados + 1

print("Media da turma:", media)
print("Aluno com a maior nota:", melhor_aluno)
print("Maior nota:", maior_nota)
print("Quantidade de aprovados:", aprovados)

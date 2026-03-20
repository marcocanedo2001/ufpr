"""
6. ESTATÍSTICAS DE TURMA
   Uma turma tem vários alunos. Cada aluno é representado por uma tupla contendo:
   (nome, nota1, nota2, nota3)

   Escreva funções para:
   - `media_aluno(aluno)`: calcula a média de um aluno
   - `melhor_aluno(turma)`: retorna o nome e a média do aluno com melhor desempenho
   - `aprovados(turma)`: retorna uma lista de tuplas apenas dos alunos aprovados (média >= 7)
   - `estatisticas_gerais(turma)`: retorna uma tupla com (média_da_turma, desvio_padrão, maior_nota, menor_nota)

   Utilize a turma: [("Ana", 8.5, 7.0, 9.0), ("Carlos", 6.0, 5.5, 7.5), ("Mariana", 9.0, 9.5, 8.0)]
"""


def media_aluno(aluno):
    nome, nota1, nota2, nota3 = aluno
    media = (nota1 + nota2 + nota3) / 3
    return media


def melhor_aluno(turma):
    melhor = None
    melhor_media = -1
    for aluno in turma:
        media = media_aluno(aluno)
        if media > melhor_media:
            melhor_media = media
            melhor = aluno[0]
    return melhor, melhor_media


def aprovados(turma):
    aprovados_list = []
    for aluno in turma:
        if media_aluno(aluno) >= 7:
            aprovados_list.append(aluno)
    return aprovados_list


def estatisticas_gerais(turma):
    medias = [media_aluno(aluno) for aluno in turma]
    media_da_turma = sum(medias) / len(medias)
    desvio_padrão = (
        sum((x - media_da_turma) ** 2 for x in medias) / len(medias)
    ) ** 0.5
    maior_nota = max(medias)
    menor_nota = min(medias)
    return media_da_turma, desvio_padrão, maior_nota, menor_nota


# Exemplo de uso
turma = [("Ana", 8.5, 7.0, 9.0), ("Carlos", 6.0, 5.5, 7.5), ("Mariana", 9.0, 9.5, 8.0)]

print("Média de cada aluno:")
for aluno in turma:
    print(f"{aluno[0]}: {media_aluno(aluno):.2f}")

print("\nMelhor aluno:")
nome, media = melhor_aluno(turma)
print(f"{nome}: {media:.2f}")

print("\nAlunos aprovados:")
for aluno in aprovados(turma):
    print(f"{aluno[0]}: {media_aluno(aluno):.2f}")

print("\nEstatísticas gerais:")
media_turma, desvio_padrao, maior_nota, menor_nota = estatisticas_gerais(turma)
print(f"Média da turma: {media_turma:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")

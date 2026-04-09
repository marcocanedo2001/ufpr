"""
13. SISTEMA DE RECOMENDACAO
    Sistema simples baseado em conteudo usando dicionarios, sem funcoes.
"""

usuarios = {
    "joao": {
        "filmes": ["Matrix", "Interestelar"],
        "livros": ["1984", "Duna"],
        "avaliacoes": {"Matrix": 5, "1984": 4}
    },
    "maria": {
        "filmes": ["Matrix", "Senhor dos Aneis"],
        "musicas": ["Bohemian Rhapsody"],
        "avaliacoes": {"Matrix": 4, "Senhor dos Aneis": 5}
    },
    "ana": {
        "filmes": ["Interestelar"],
        "livros": ["Duna", "O Hobbit"],
        "musicas": ["Imagine"],
        "avaliacoes": {"Interestelar": 5, "O Hobbit": 4}
    }
}

itens = {
    "Matrix": {"tipo": "filme", "genero": "Ficcao Cientifica", "ano": 1999},
    "Interestelar": {"tipo": "filme", "genero": "Ficcao Cientifica", "ano": 2014},
    "Senhor dos Aneis": {"tipo": "filme", "genero": "Fantasia", "ano": 2001},
    "1984": {"tipo": "livro", "genero": "Distopia", "autor": "George Orwell"},
    "Duna": {"tipo": "livro", "genero": "Ficcao Cientifica", "autor": "Frank Herbert"},
    "O Hobbit": {"tipo": "livro", "genero": "Fantasia", "autor": "J. R. R. Tolkien"},
    "Bohemian Rhapsody": {"tipo": "musica", "genero": "Rock", "ano": 1975},
    "Imagine": {"tipo": "musica", "genero": "Rock", "ano": 1971}
}

# Registrar avaliacao
usuarios["joao"]["avaliacoes"]["Interestelar"] = 5

# Itens consumidos por Joao
itens_joao = set()
for tipo_item in usuarios["joao"]:
    if tipo_item != "avaliacoes":
        for nome_item in usuarios["joao"][tipo_item]:
            itens_joao.add(nome_item)

# Itens consumidos por Maria
itens_maria = set()
for tipo_item in usuarios["maria"]:
    if tipo_item != "avaliacoes":
        for nome_item in usuarios["maria"][tipo_item]:
            itens_maria.add(nome_item)

# Similaridade entre Joao e Maria
intersecao = itens_joao.intersection(itens_maria)
uniao = itens_joao.union(itens_maria)

if len(uniao) > 0:
    similaridade_joao_maria = len(intersecao) / len(uniao)
else:
    similaridade_joao_maria = 0

# Itens consumidos por Ana
itens_ana = set()
for tipo_item in usuarios["ana"]:
    if tipo_item != "avaliacoes":
        for nome_item in usuarios["ana"][tipo_item]:
            itens_ana.add(nome_item)

# Similaridade entre Joao e Ana
intersecao = itens_joao.intersection(itens_ana)
uniao = itens_joao.union(itens_ana)

if len(uniao) > 0:
    similaridade_joao_ana = len(intersecao) / len(uniao)
else:
    similaridade_joao_ana = 0

# Recomendacoes para Joao
recomendacoes = {}

for outro_usuario in usuarios:
    if outro_usuario != "joao":
        itens_outro = set()

        for tipo_item in usuarios[outro_usuario]:
            if tipo_item != "avaliacoes":
                for nome_item in usuarios[outro_usuario][tipo_item]:
                    itens_outro.add(nome_item)

        intersecao = itens_joao.intersection(itens_outro)
        uniao = itens_joao.union(itens_outro)

        if len(uniao) > 0:
            similaridade = len(intersecao) / len(uniao)
        else:
            similaridade = 0

        if similaridade > 0:
            for nome_item in itens_outro:
                if nome_item not in itens_joao:
                    pontos = similaridade

                    if nome_item in usuarios[outro_usuario]["avaliacoes"]:
                        pontos = pontos + (usuarios[outro_usuario]["avaliacoes"][nome_item] / 5)

                    if nome_item in recomendacoes:
                        recomendacoes[nome_item] = recomendacoes[nome_item] + pontos
                    else:
                        recomendacoes[nome_item] = pontos

lista_recomendacoes = list(recomendacoes.items())
lista_recomendacoes.sort(key=lambda dado: dado[1], reverse=True)

# Itens similares a Matrix
similares_matrix = []
item_base = "Matrix"

for nome_item in itens:
    if nome_item != item_base:
        pontos = 0

        for caracteristica in itens[item_base]:
            if caracteristica in itens[nome_item] and itens[nome_item][caracteristica] == itens[item_base][caracteristica]:
                pontos = pontos + 1

        if pontos > 0:
            similares_matrix.append((nome_item, pontos))

similares_matrix.sort(key=lambda dado: dado[1], reverse=True)

print("Similaridade entre joao e maria:", similaridade_joao_maria)
print("Similaridade entre joao e ana:", similaridade_joao_ana)
print("Recomendacoes para joao:", lista_recomendacoes)
print("Itens similares a Matrix:", similares_matrix)

"""
8. MESCLANDO DICIONARIOS
   Desenvolva uma funcao chamada mesclar_dicionarios que receba dois dicionarios
   e retorne um novo dicionario combinando as chaves de ambos.
"""

def mesclar_dicionarios(d1, d2):
    novo_dicionario = {}

    for chave in d1:
        novo_dicionario[chave] = d1[chave]

    for chave in d2:
        if chave in novo_dicionario:
            novo_dicionario[chave] = novo_dicionario[chave] + d2[chave]
        else:
            novo_dicionario[chave] = d2[chave]

    return novo_dicionario


d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}

resultado = mesclar_dicionarios(d1, d2)

print("Dicionario 1:", d1)
print("Dicionario 2:", d2)
print("Dicionario mesclado:", resultado)

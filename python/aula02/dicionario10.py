"""
10. ANALISE DE TEXTOS
    Le uma string longa e gera estatisticas usando dicionarios.
"""

texto = input("Digite um texto: ")
texto = texto.lower()

for caractere in ",.!?;:":
    texto = texto.replace(caractere, "")

palavras = texto.split()
frequencia_palavras = {}
frequencia_letras = {}
palavras_por_tamanho = {}
soma_tamanho = 0

for palavra in palavras:
    soma_tamanho = soma_tamanho + len(palavra)

    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] = frequencia_palavras[palavra] + 1
    else:
        frequencia_palavras[palavra] = 1

    tamanho = len(palavra)
    if tamanho in palavras_por_tamanho:
        palavras_por_tamanho[tamanho].append(palavra)
    else:
        palavras_por_tamanho[tamanho] = [palavra]

    for letra in palavra:
        if letra in frequencia_letras:
            frequencia_letras[letra] = frequencia_letras[letra] + 1
        else:
            frequencia_letras[letra] = 1

lista_frequencia = list(frequencia_palavras.items())
lista_frequencia.sort(key=lambda item: item[1], reverse=True)
top_10 = lista_frequencia[:10]

if len(palavras) > 0:
    tamanho_medio = soma_tamanho / len(palavras)
else:
    tamanho_medio = 0

print("Top 10 palavras mais frequentes:")
for palavra, quantidade in top_10:
    print(palavra, "-", quantidade)

print("Numero total de palavras:", len(palavras))
print("Numero de palavras unicas:", len(frequencia_palavras))
print("Tamanho medio das palavras:", tamanho_medio)
print("Frequencia de letras:", frequencia_letras)
print("Palavras agrupadas por tamanho:", palavras_por_tamanho)

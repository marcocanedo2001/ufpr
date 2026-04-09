""" "
10. ANÁLISE DE TEXTOS AVANÇADA
    Desenvolva funções para análise de textos utilizando tuplas como estruturas de retorno:

    - `estatisticas_texto(texto)`: retorna uma tupla com (total_palavras, total_caracteres, total_linhas, palavras_unicas)
    - `palavras_frequentes(texto, n=5)`: retorna uma tupla com as n palavras mais frequentes e suas contagens
    - `indices_por_palavra(texto, palavra)`: retorna uma tupla com os índices (posições) onde a palavra aparece
    - `analisar_frase(frase)`: retorna uma tupla aninhada com (palavras, numero_palavras, tamanho_medio, palindromos)

    Teste com um parágrafo ou arquivo de texto fornecido pelo usuário.

"""


def estatisticas_texto(texto):
    palavras = texto.split()
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    total_linhas = texto.count("\n") + 1
    palavras_unicas = len(set(palavras))

    return (total_palavras, total_caracteres, total_linhas, palavras_unicas)


def palavras_frequentes(texto, n=5):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    palavras_ordenadas = sorted(
        frequencia.items(), key=lambda item: item[1], reverse=True
    )
    return tuple(palavras_ordenadas[:n])


def indices_por_palavra(texto, palavra):
    palavras = texto.split()
    indices = [i for i, p in enumerate(palavras) if p == palavra]
    return tuple(indices)


def analisar_frase(frase):
    palavras = frase.split()
    numero_palavras = len(palavras)
    tamanho_medio = (
        sum(len(p) for p in palavras) / numero_palavras if numero_palavras > 0 else 0
    )
    palindromos = [p for p in palavras if p == p[::-1]]

    return (palavras, numero_palavras, tamanho_medio, palindromos)


# Testando as funções com um parágrafo fornecido pelo usuário
if __name__ == "__main__":
    texto = input("Digite um parágrafo de texto para análise: ")

    estatisticas = estatisticas_texto(texto)
    print(f"Estatísticas do texto: {estatisticas}")

    frequentes = palavras_frequentes(texto)
    print(f"Palavras mais frequentes: {frequentes}")

    palavra_busca = input("Digite uma palavra para encontrar seus índices: ")
    indices = indices_por_palavra(texto, palavra_busca)
    print(f"Índices da palavra '{palavra_busca}': {indices}")

    frase = input("Digite uma frase para análise: ")
    analise_frase = analisar_frase(frase)
    print(f"Análise da frase: {analise_frase}")

"""
4. DICIONARIO DE TRADUCAO
   Faca um mini-dicionario Portugues-Ingles com pelo menos 10 palavras.
   O programa deve permitir que o usuario digite uma palavra em portugues
   e mostre sua traducao para ingles (ou mensagem de nao encontrado).
"""

dicionario = {
    "casa": "house",
    "livro": "book",
    "carro": "car",
    "gato": "cat",
    "cachorro": "dog",
    "escola": "school",
    "janela": "window",
    "porta": "door",
    "mesa": "table",
    "cadeira": "chair"
}

palavra = input("Digite uma palavra em portugues: ")
palavra = palavra.lower()

if palavra in dicionario:
    print("Traducao em ingles:", dicionario[palavra])
else:
    print("Palavra nao encontrada no dicionario.")

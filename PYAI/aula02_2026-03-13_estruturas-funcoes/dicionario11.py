"""
11. SISTEMA DE BIBLIOTECA
    Usa dicionarios aninhados para cadastrar, emprestar, devolver e buscar livros.
"""

from datetime import datetime, timedelta


def cadastrar_livro(biblioteca, isbn, titulo, autor, ano, genero):
    biblioteca[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "status": "disponivel",
        "emprestado_para": "",
        "data_emprestimo": "",
        "total_emprestimos": 0
    }


def emprestar_livro(biblioteca, isbn, pessoa, data_emprestimo):
    if isbn in biblioteca and biblioteca[isbn]["status"] == "disponivel":
        biblioteca[isbn]["status"] = "emprestado"
        biblioteca[isbn]["emprestado_para"] = pessoa
        biblioteca[isbn]["data_emprestimo"] = data_emprestimo
        biblioteca[isbn]["total_emprestimos"] = biblioteca[isbn]["total_emprestimos"] + 1
        return True
    return False


def devolver_livro(biblioteca, isbn):
    if isbn in biblioteca and biblioteca[isbn]["status"] == "emprestado":
        biblioteca[isbn]["status"] = "disponivel"
        biblioteca[isbn]["emprestado_para"] = ""
        biblioteca[isbn]["data_emprestimo"] = ""
        return True
    return False


def buscar_por_autor(biblioteca, autor):
    encontrados = []
    for isbn in biblioteca:
        if biblioteca[isbn]["autor"].lower() == autor.lower():
            encontrados.append(biblioteca[isbn]["titulo"])
    return encontrados


def buscar_por_genero(biblioteca, genero):
    encontrados = []
    for isbn in biblioteca:
        if biblioteca[isbn]["genero"].lower() == genero.lower():
            encontrados.append(biblioteca[isbn]["titulo"])
    return encontrados


def buscar_por_ano(biblioteca, ano):
    encontrados = []
    for isbn in biblioteca:
        if biblioteca[isbn]["ano"] == ano:
            encontrados.append(biblioteca[isbn]["titulo"])
    return encontrados


def listar_atrasados(biblioteca, data_atual):
    atrasados = []
    data_atual_obj = datetime.strptime(data_atual, "%Y-%m-%d")

    for isbn in biblioteca:
        livro = biblioteca[isbn]
        if livro["status"] == "emprestado":
            data_emprestimo_obj = datetime.strptime(livro["data_emprestimo"], "%Y-%m-%d")
            prazo = data_emprestimo_obj + timedelta(days=14)

            if data_atual_obj > prazo:
                atrasados.append(livro["titulo"])

    return atrasados


def relatorio_mais_emprestados(biblioteca):
    lista = []

    for isbn in biblioteca:
        livro = biblioteca[isbn]
        lista.append((livro["titulo"], livro["total_emprestimos"]))

    lista.sort(key=lambda item: item[1], reverse=True)
    return lista


biblioteca = {}

cadastrar_livro(biblioteca, "111", "Dom Casmurro", "Machado de Assis", 1899, "Romance")
cadastrar_livro(biblioteca, "222", "1984", "George Orwell", 1949, "Distopia")
cadastrar_livro(biblioteca, "333", "O Hobbit", "J. R. R. Tolkien", 1937, "Fantasia")

emprestar_livro(biblioteca, "111", "Ana", "2026-02-20")
emprestar_livro(biblioteca, "222", "Bruno", "2026-03-10")
devolver_livro(biblioteca, "222")
emprestar_livro(biblioteca, "222", "Carla", "2026-03-12")

print("Busca por autor:", buscar_por_autor(biblioteca, "Machado de Assis"))
print("Busca por genero:", buscar_por_genero(biblioteca, "Fantasia"))
print("Busca por ano:", buscar_por_ano(biblioteca, 1949))
print("Livros atrasados:", listar_atrasados(biblioteca, "2026-03-13"))
print("Relatorio de livros mais emprestados:", relatorio_mais_emprestados(biblioteca))

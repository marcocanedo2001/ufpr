"""
Programa de teste para lista7.py.
Executa o script com entradas conhecidas e valida as somas exibidas.
"""

from pathlib import Path
import subprocess
import sys


ARQUIVO_LISTA7 = Path(__file__).with_name("lista7.py")


def executar_lista7(entradas):
    dados_entrada = "\n".join(str(numero) for numero in entradas) + "\n"

    resultado = subprocess.run(
        [sys.executable, str(ARQUIVO_LISTA7)],
        input=dados_entrada,
        capture_output=True,
        text=True,
        check=False,
    )

    return resultado.returncode, resultado.stdout, resultado.stderr


def validar_teste(nome_teste, entradas, soma_total, soma_primeira_linha, soma_diagonal):
    codigo, saida, erro = executar_lista7(entradas)

    if codigo != 0:
        print(f"{nome_teste}: FALHOU")
        print("O programa terminou com erro.")
        print(erro)
        return False

    verificacoes = [
        f"Soma de todos os elementos: {soma_total}",
        f"Soma da primeira linha: {soma_primeira_linha}",
        f"Soma da diagonal principal: {soma_diagonal}",
    ]

    for verificacao in verificacoes:
        if verificacao not in saida:
            print(f"{nome_teste}: FALHOU")
            print(f"Saida esperada nao encontrada: {verificacao}")
            print("Saida completa:")
            print(saida)
            return False

    print(f"{nome_teste}: OK")
    return True


def main():
    testes = [
        {
            "nome": "Teste 1 - matriz de 1 a 9",
            "entradas": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "soma_total": 45,
            "soma_primeira_linha": 6,
            "soma_diagonal": 15,
        },
        {
            "nome": "Teste 2 - todos os valores 2",
            "entradas": [2, 2, 2, 2, 2, 2, 2, 2, 2],
            "soma_total": 18,
            "soma_primeira_linha": 6,
            "soma_diagonal": 6,
        },
        {
            "nome": "Teste 3 - valores negativos e positivos",
            "entradas": [0, -1, 5, 10, 3, -2, 4, 8, 1],
            "soma_total": 28,
            "soma_primeira_linha": 4,
            "soma_diagonal": 4,
        },
    ]

    todos_ok = True

    for teste in testes:
        ok = validar_teste(
            teste["nome"],
            teste["entradas"],
            teste["soma_total"],
            teste["soma_primeira_linha"],
            teste["soma_diagonal"],
        )
        if not ok:
            todos_ok = False

    if todos_ok:
        print("Todos os testes passaram.")
    else:
        print("Alguns testes falharam.")
        sys.exit(1)


if __name__ == "__main__":
    main()

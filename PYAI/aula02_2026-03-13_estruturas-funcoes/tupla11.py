"""
11. SISTEMA DE FUNCIONARIOS COM TUPLAS
    Modele um sistema de funcionarios onde cada funcionario eh representado por
    uma tupla:

    (id, nome, cargo, salario, data_admissao)

    Implemente funcoes para:

    - cadastrar_funcionario(funcionarios, id, nome, cargo, salario, data)
    - buscar_por_cargo(funcionarios, cargo)
    - aumento_salarial(funcionarios, percentual, cargo=None)
    - media_salarial(funcionarios, cargo=None)
    - funcionario_mais_antigo(funcionarios)
    - folha_pagamento(funcionarios)

    A ideia eh trabalhar com tuplas de forma imutavel e usar funcoes de alta
    ordem quando fizer sentido.
"""

from datetime import datetime
from functools import reduce


def _normalizar_funcionarios(funcionarios):
    """Garante que a estrutura manipulada internamente seja uma tupla."""
    return tuple(funcionarios)


def cadastrar_funcionario(funcionarios, id, nome, cargo, salario, data):
    """Retorna uma nova tupla com o funcionario cadastrado."""
    funcionarios = _normalizar_funcionarios(funcionarios)
    novo_funcionario = (id, nome, cargo, salario, data)
    return funcionarios + (novo_funcionario,)


def buscar_por_cargo(funcionarios, cargo):
    """Retorna uma tupla com todos os funcionarios de um determinado cargo."""
    funcionarios = _normalizar_funcionarios(funcionarios)

    # filter mantem apenas os funcionarios que atendem ao criterio de cargo.
    filtrados = filter(lambda funcionario: funcionario[2].lower() == cargo.lower(), funcionarios)
    return tuple(filtrados)


def aumento_salarial(funcionarios, percentual, cargo=None):
    """Retorna uma nova tupla com os salarios atualizados."""
    funcionarios = _normalizar_funcionarios(funcionarios)
    fator = 1 + (percentual / 100)

    def aplicar_aumento(funcionario):
        id_funcionario, nome, cargo_funcionario, salario, data = funcionario

        if cargo is None or cargo_funcionario.lower() == cargo.lower():
            salario = round(salario * fator, 2)

        # map cria uma nova sequencia sem alterar a tupla original.
        return (id_funcionario, nome, cargo_funcionario, salario, data)

    return tuple(map(aplicar_aumento, funcionarios))


def media_salarial(funcionarios, cargo=None):
    """Retorna a media salarial geral ou filtrada por cargo."""
    funcionarios = _normalizar_funcionarios(funcionarios)

    if cargo is not None:
        funcionarios = buscar_por_cargo(funcionarios, cargo)

    if len(funcionarios) == 0:
        return 0.0

    # reduce consolida os salarios para permitir calcular total e media.
    total_salarios = reduce(lambda acumulado, funcionario: acumulado + funcionario[3], funcionarios, 0)
    return round(total_salarios / len(funcionarios), 2)


def funcionario_mais_antigo(funcionarios):
    """Retorna o funcionario com a data de admissao mais antiga."""
    funcionarios = _normalizar_funcionarios(funcionarios)

    if len(funcionarios) == 0:
        return None

    return min(
        funcionarios,
        key=lambda funcionario: datetime.strptime(funcionario[4], "%Y-%m-%d"),
    )


def folha_pagamento(funcionarios):
    """Retorna o total gasto com salarios."""
    funcionarios = _normalizar_funcionarios(funcionarios)

    if len(funcionarios) == 0:
        return 0.0

    # reduce soma os salarios para obter o gasto total da folha.
    return round(reduce(lambda acumulado, funcionario: acumulado + funcionario[3], funcionarios, 0.0), 2)


def _formatar_funcionario(funcionario):
    """Formata um funcionario em uma linha legivel para exibicao."""
    id_funcionario, nome, cargo, salario, data = funcionario
    return (
        f"ID: {id_funcionario} | Nome: {nome} | Cargo: {cargo} | "
        f"Salario: R$ {salario:.2f} | Admissao: {data}"
    )


def _imprimir_funcionarios(titulo, funcionarios):
    """Exibe uma tupla de funcionarios em formato de lista legivel."""
    print(titulo)

    if len(funcionarios) == 0:
        print("  (nenhum funcionario)")
        print()
        return

    for funcionario in funcionarios:
        print(f"  - {_formatar_funcionario(funcionario)}")

    print()


if __name__ == "__main__":
    funcionarios = (
        (1, "Ana Souza", "Analista", 4500.0, "2021-03-10"),
        (2, "Bruno Lima", "Gerente", 8200.0, "2019-07-01"),
        (3, "Carla Mendes", "Analista", 4700.0, "2020-11-15"),
        (4, "Diego Alves", "Desenvolvedor", 6000.0, "2018-02-20"),
    )

    print("=== SISTEMA DE FUNCIONARIOS ===\n")
    _imprimir_funcionarios("Funcionarios originais:", funcionarios)

    funcionarios_com_novo = cadastrar_funcionario(
        funcionarios, 5, "Eva Costa", "Analista", 4900.0, "2024-01-08"
    )
    _imprimir_funcionarios("Apos novo cadastro:", funcionarios_com_novo)

    _imprimir_funcionarios("Funcionarios do cargo Analista:", buscar_por_cargo(funcionarios, "Analista"))
    _imprimir_funcionarios("Aumento geral de 10%:", aumento_salarial(funcionarios, 10))
    _imprimir_funcionarios(
        "Aumento de 8% para o cargo Analista:", aumento_salarial(funcionarios, 8, "Analista")
    )

    print("Media salarial geral: R$ {:.2f}".format(media_salarial(funcionarios)))
    print("Media salarial do cargo Analista: R$ {:.2f}".format(media_salarial(funcionarios, "Analista")))
    print("Funcionario mais antigo:", _formatar_funcionario(funcionario_mais_antigo(funcionarios)))
    print("Folha de pagamento: R$ {:.2f}".format(folha_pagamento(funcionarios)))

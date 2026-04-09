"""
12. EXPRESSOES MATEMATICAS (DESAFIO)
    Crie um sistema para avaliar expressoes matematicas simples representadas
    como tuplas.

    Uma expressao e representada por uma tupla aninhada no formato:
    (operador, operando1, operando2)

    Onde operador e uma string ('+', '-', '*', '/', '^') e operandos podem
    ser numeros ou outras expressoes (tuplas).

    Funcoes:
    - avaliar(expressao, variaveis=None)
    - to_string(expressao)
    - simplificar(expressao)
    - derivar(expressao, var)
"""


OPERADORES = {"+", "-", "*", "/", "^"}
PRECEDENCIA = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def _eh_expressao(expressao):
    # Uma expressao valida tem exatamente 3 itens:
    # (operador, operando_esquerdo, operando_direito).
    return (
        isinstance(expressao, tuple)
        and len(expressao) == 3
        and isinstance(expressao[0], str)
        and expressao[0] in OPERADORES
    )


def _eh_numero(valor):
    # Neste exercicio, tratamos inteiros e floats como numeros validos.
    return isinstance(valor, (int, float))


def _eh_variavel(valor):
    # Qualquer string que nao seja operador representa uma variavel simbolica.
    return isinstance(valor, str) and valor not in OPERADORES


def avaliar(expressao, variaveis=None):
    """Avalia uma expressao recursivamente.

    Se `variaveis` for informado, nomes simbolicos sao procurados nesse mapa.
    """
    if variaveis is None:
        variaveis = {}

    # Caso base 1: numero ja esta avaliado.
    if _eh_numero(expressao):
        return expressao

    # Caso base 2: se for uma variavel, buscamos seu valor no dicionario.
    if _eh_variavel(expressao):
        if expressao not in variaveis:
            raise KeyError(f"Variavel '{expressao}' nao informada.")
        return variaveis[expressao]

    # Se nao for numero, variavel ou tupla valida, a expressao esta incorreta.
    if not _eh_expressao(expressao):
        raise TypeError("Expressao invalida.")

    operador, esquerdo, direito = expressao
    # A avaliacao e recursiva: primeiro resolvemos os operandos internos.
    a = avaliar(esquerdo, variaveis)
    b = avaliar(direito, variaveis)

    # Depois aplicamos o operador correspondente.
    if operador == "+":
        return a + b
    if operador == "-":
        return a - b
    if operador == "*":
        return a * b
    if operador == "/":
        return a / b
    if operador == "^":
        return a**b

    raise ValueError(f"Operador desconhecido: {operador}")


def _prec(operador):
    return PRECEDENCIA[operador] if operador in PRECEDENCIA else 99


def _formatar_operando(operando, operador_pai, lado):
    # Se o operando nao for uma subexpressao, ele pode ser mostrado direto.
    if not _eh_expressao(operando):
        return to_string(operando)

    operador_filho = operando[0]
    texto = to_string(operando)

    # Se o filho tiver precedencia menor, usamos parenteses para evitar ambiguidade.
    if _prec(operador_filho) < _prec(operador_pai):
        return f"({texto})"

    # Subtracao exige mais cuidado no lado direito.
    if operador_pai == "-" and lado == "direito" and operador_filho in {"+", "-"}:
        return f"({texto})"

    # Somas aninhadas ficam mais didaticas quando agrupadas visualmente.
    if operador_pai == "+" and operador_filho in {"+", "-"}:
        return f"({texto})"

    # Divisao sempre mostra o lado direito entre parenteses quando ele e uma expressao.
    if operador_pai == "/" and lado == "direito":
        return f"({texto})"

    # Potencia associativa a direita: x ^ (y ^ z).
    if operador_pai == "^" and lado == "direito" and operador_filho == "^":
        return f"({texto})"

    return texto


def to_string(expressao):
    """Converte a expressao para uma string infixa legivel."""
    if _eh_numero(expressao):
        # Evita imprimir 5.0 quando o valor e inteiro na pratica.
        if isinstance(expressao, float) and expressao.is_integer():
            return str(int(expressao))
        return str(expressao)

    if _eh_variavel(expressao):
        return expressao

    if not _eh_expressao(expressao):
        raise TypeError("Expressao invalida.")

    operador, esquerdo, direito = expressao
    esquerda = _formatar_operando(esquerdo, operador, "esquerdo")
    direita = _formatar_operando(direito, operador, "direito")
    return f"{esquerda} {operador} {direita}"


def simplificar(expressao):
    """Simplifica expressoes com operandos constantes e identidades basicas."""
    # Termos atomicos ja estao no formato mais simples possivel.
    if _eh_numero(expressao) or _eh_variavel(expressao):
        return expressao

    if not _eh_expressao(expressao):
        raise TypeError("Expressao invalida.")

    # Simplificamos primeiro os filhos para depois tentar reduzir o pai.
    operador, esquerdo, direito = expressao
    esquerdo = simplificar(esquerdo)
    direito = simplificar(direito)

    # Se os dois lados virarem numeros, calculamos o valor final diretamente.
    if _eh_numero(esquerdo) and _eh_numero(direito):
        return avaliar((operador, esquerdo, direito))

    if operador == "+":
        # Agrupa constantes para deixar a saida mais limpa:
        # (x + 3) + 2 -> (x + 5)
        if _eh_expressao(esquerdo) and esquerdo[0] == "+" and _eh_numero(esquerdo[2]) and _eh_numero(direito):
            return simplificar(("+", esquerdo[0:2] + (esquerdo[2] + direito,)))
        if _eh_expressao(direito) and direito[0] == "+" and _eh_numero(direito[2]) and _eh_numero(esquerdo):
            return simplificar(("+", direito[0:2] + (direito[2] + esquerdo,)))
        # Elemento neutro da soma.
        if esquerdo == 0:
            return direito
        if direito == 0:
            return esquerdo

    elif operador == "-":
        # Subtrair zero nao muda o valor; subtrair algo igual zera a expressao.
        if direito == 0:
            return esquerdo
        if esquerdo == direito:
            return 0

    elif operador == "*":
        # Elemento absorvente e elemento neutro da multiplicacao.
        if esquerdo == 0 or direito == 0:
            return 0
        if esquerdo == 1:
            return direito
        if direito == 1:
            return esquerdo

    elif operador == "/":
        # Dividir por 1 nao altera a expressao; zero dividido por qualquer coisa continua zero.
        if esquerdo == 0:
            return 0
        if direito == 1:
            return esquerdo

    elif operador == "^":
        # Regras mais comuns para potencia.
        if direito == 0:
            return 1
        if direito == 1:
            return esquerdo
        if esquerdo == 0:
            return 0
        if esquerdo == 1:
            return 1

    return (operador, esquerdo, direito)


def derivar(expressao, var):
    """Deriva simbolicamente a expressao em relacao a `var`."""
    # Derivada de constante = 0.
    if _eh_numero(expressao):
        return 0

    # Derivada de uma variavel:
    # 1 se ela for a variavel de derivacao, 0 caso contrario.
    if _eh_variavel(expressao):
        return 1 if expressao == var else 0

    if not _eh_expressao(expressao):
        raise TypeError("Expressao invalida.")

    operador, esquerdo, direito = expressao

    if operador == "+":
        # (u + v)' = u' + v'
        return simplificar(("+", derivar(esquerdo, var), derivar(direito, var)))

    if operador == "-":
        # (u - v)' = u' - v'
        return simplificar(("-", derivar(esquerdo, var), derivar(direito, var)))

    if operador == "*":
        # Regra do produto:
        # (u * v)' = u' * v + u * v'
        regra = (
            "+",
            ("*", derivar(esquerdo, var), direito),
            ("*", esquerdo, derivar(direito, var)),
        )
        return simplificar(regra)

    if operador == "/":
        # Regra do quociente:
        # (u / v)' = (u' * v - u * v') / v^2
        numerador = (
            "-",
            ("*", derivar(esquerdo, var), direito),
            ("*", esquerdo, derivar(direito, var)),
        )
        denominador = ("^", direito, 2)
        return simplificar(("/", numerador, denominador))

    if operador == "^":
        if _eh_numero(direito):
            # Regra da potencia com expoente constante:
            # (u^n)' = n * u^(n-1) * u'
            regra = (
                "*",
                ("*", direito, ("^", esquerdo, direito - 1)),
                derivar(esquerdo, var),
            )
            return simplificar(regra)

        # Regra geral: d(u^v) = u^v * (v' * ln(u) + v * u'/u)
        # A funcao ln nao faz parte do sistema, entao limitamos a regra
        # ao caso mais comum com expoente constante.
        raise NotImplementedError(
            "Derivada de potencias com expoente nao constante nao suportada."
        )

    raise ValueError(f"Operador desconhecido: {operador}")


def _imprimir_titulo(titulo):
    print(titulo)
    print("-" * len(titulo))


def _imprimir_bloco(rotulo, expressao, variaveis=None, derivada_de=None):
    # Pequena rotina para deixar a demonstracao no __main__ padronizada.
    print(f"{rotulo}:")
    print(f"  Estrutura   : {expressao}")
    print(f"  Leitura     : {to_string(expressao)}")
    print(f"  Simplificada : {to_string(simplificar(expressao))}")

    if variaveis is not None:
        print(f"  Avaliacao   : {avaliar(expressao, variaveis)}")

    if derivada_de is not None:
        derivada = simplificar(derivar(expressao, derivada_de))
        print(f"  Derivada    : {to_string(derivada)}")

    print()


if __name__ == "__main__":
    expr = ("*", ("+", 3, 4), ("-", 10, 2))
    expr_var = ("*", ("+", "x", 3), ("-", "x", 1))

    _imprimir_titulo("EXPRESSOES MATEMATICAS COM TUPLAS")

    _imprimir_bloco("1) Exemplo numerico", expr)
    _imprimir_bloco("2) Exemplo com variavel", expr_var, variaveis={"x": 5}, derivada_de="x")
    _imprimir_bloco("3) Potencia simples", ("^", "x", 2), derivada_de="x")

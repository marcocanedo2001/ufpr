# Classe para representar uma pessoa
class Pessoa:
    def __init__(self, nome=None, cpf=-1):
        self.__nome = nome
        if cpf != -1 and self.__validar_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError("CPF inválido")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("Alterando nome de {} para {}".format(self.__nome, nome))
        self.__nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if self.__validar_cpf(cpf) and cpf != -1:
            self._cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def __validar_cpf(self, cpf_teste):
        somatorio_valida_ultimo = 0
        somatorio_valida_penultimo = 0
        ultimo = cpf_teste % 10
        cpf_teste //= 10
        penultimo = cpf_teste % 10
        cpf_teste //= 10
        somatorio_valida_ultimo = penultimo * 2

        for i in range(2, 12):
            modulo = cpf_teste % 10
            cpf_teste //= 10
            somatorio_valida_penultimo += modulo * i
            somatorio_valida_ultimo += modulo * (i + 1)

        modulo = somatorio_valida_penultimo % 11
        if modulo < 2:
            if penultimo != 0:
                return False  # CPF inválido
        else:
            if penultimo != 11 - modulo:
                return False  # CPF inválido

        modulo = somatorio_valida_ultimo % 11
        if modulo < 2:
            if ultimo != 0:
                return False  # CPF inválido
        else:
            if ultimo != 11 - modulo:
                return False  # CPF inválido

        return True  # CPF válido

    def __eq__(self, other):
        return self._cpf == other.cpf

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self._cpf == other.cpf

    def __lt__(self, other):
        return self._cpf < other.cpf

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        return self._cpf > other.cpf

    def __le__(self, other):
        return not self.__gt__(other)

    def __str__(self) -> str:
        verificador = self._cpf % 100
        atual = self._cpf // 100
        terc = atual % 1000
        atual = atual // 1000
        seg = atual % 1000
        prim = atual // 1000
        return f"{self.nome} {prim:03d}.{seg:03d}.{terc:03d}-{verificador:02d}"

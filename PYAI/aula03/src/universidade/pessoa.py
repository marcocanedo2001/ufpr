# Classe para representar uma pessoa
class Pessoa:
    def __init__(self,nome=None,cpf=-1):
        self.__nome = nome
        if cpf != -1 and self.__validar_cpf(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = -1 # CPF inválido ou não fornecido

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("Alterando nome de {} para {}".format(self.__nome, nome))
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if self.__validar_cpf(cpf) and cpf != -1:
            self.__cpf = cpf
        else:
            print("CPF inválido: {}".format(cpf))
            self.__cpf = -1  # CPF inválido

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

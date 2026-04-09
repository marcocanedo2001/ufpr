from .professor import Professor


class ProfessorSubstituto(Professor):
    def __init__(self, nome, cpf, valor_hora=60, carga_horaria=40):
        super().__init__(nome, cpf, valor_hora, carga_horaria)
        self.__anos_trabalho = 0

    @property
    def anos_trabalho(self):
        return self.__anos_trabalho

    @anos_trabalho.setter
    def anos_trabalho(self, anos_trabalho):
        self.__anos_trabalho = anos_trabalho

    def _calcular_bonus(self):
        return self.__anos_trabalho * 300

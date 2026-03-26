from .professor import Professor


class ProfessorAdjunto(Professor):
    def __init__(self, nome, cpf, valor_hora=60, carga_horaria=40):
        super().__init__(nome, cpf, valor_hora, carga_horaria)
        self.__qtde_proj_pesquisa = 0

    @property
    def qtde_proj_pesquisa(self):
        return self.__qtde_proj_pesquisa

    @qtde_proj_pesquisa.setter
    def qtde_proj_pesquisa(self, qtde_proj_pesquisa):
        self.__qtde_proj_pesquisa = qtde_proj_pesquisa

    def _calcular_bonus(self):
        return self.qtde_proj_pesquisa * 1000

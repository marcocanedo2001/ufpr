from abc import ABC, abstractmethod
from typing import cast
from .pessoa import Pessoa


class Professor(ABC, Pessoa):
    def __init__(self, nome, cpf, valor_hora=60, carga_horaria=40):
        super().__init__(nome, cpf)
        self.__valor_hora = valor_hora
        self.__carga_horaria = carga_horaria

    @abstractmethod
    def _calcular_bonus(self):
        pass

    @property
    def salario(self):
        # Carga semanal * custo * 4,5 semanas no mês + Bônus
        return self.__carga_horaria * self.__valor_hora * 4.5 + self._calcular_bonus()

    def __str__(self) -> str:
        return f"{super().__str__()} R${self.salario},00"

from universidade.pessoa import Pessoa

from universidade.pessoa import Pessoa
from universidade.professor_adjunto import ProfessorAdjunto

lista = []
lista.append(Pessoa("João da Silva", 77777777777))
lista.append(ProfessorAdjunto("Maria", 11111111111))
lista.append(ProfessorAdjunto("Pedro", 55555555555))
lista.append(Pessoa("Camila", 88888888888))
lista.sort()
for p in lista:
    print(p)

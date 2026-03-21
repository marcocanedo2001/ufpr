from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

p1 = Pessoa("João")
d1 = Disciplina("Matemática", 60, p1)
d2 = Disciplina("História", 80)

d1.adicionar_conteudo_ministrado("Conteúdo 1", 1)
d1.adicionar_conteudo_ministrado("Conteúdo 2", 2)
d2.adicionar_conteudo_ministrado("Revolução Francesa", 3)

print(conteudo1.proxy_id)


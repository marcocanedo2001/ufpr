from universidade.conteudo_ministrado import ConteudoMinistrado
from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

p1 = Pessoa("João",11111111111) 
d1 = Disciplina("Orientação a Objetos", 60, p1) 

d1.adicionar_conteudo_ministrado("Getters e Setters", 1) 
d1.adicionar_conteudo_ministrado("Classes", 2) 
d1.adicionar_conteudo_ministrado("Modificadores de Acesso", 1)
 
d1.exibir_informacoes()

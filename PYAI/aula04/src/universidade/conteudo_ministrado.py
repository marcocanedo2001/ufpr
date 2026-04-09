class ConteudoMinistrado:
    PROXY_ID = 0

    def __init__(self, descricao, carga_horaria):
        self.__descricao = descricao
        self.__carga_horaria = carga_horaria
        self.__id = ConteudoMinistrado.PROXY_ID
        ConteudoMinistrado.PROXY_ID += 1

    @property
    def descricao(self):
        return self.__descricao

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def id(self):
        return self.__id


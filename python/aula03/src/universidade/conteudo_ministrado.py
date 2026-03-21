class ConteudoMinistrado:
    PROXY_ID = 0
    def __init__(self, descricao, carga_horaria):
        self.__descricao = descricao
        self.__carga_horaria = carga_horaria
        #incrementar o id automaticamente a cada nova instância criada
        ConteudoMinistrado.PROXY_ID += 1
        self.__proxy_id = ConteudoMinistrado.PROXY_ID

    @property
    def descricao(self):
        return self.__descricao

    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @property
    def proxyid(self):
        return self.__proxy_id

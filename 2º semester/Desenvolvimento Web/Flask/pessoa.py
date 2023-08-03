class Pessoa:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula= matricula
    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
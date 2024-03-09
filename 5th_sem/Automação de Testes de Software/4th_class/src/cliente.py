class Cliente:

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha
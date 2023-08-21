class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos públicos
        self.nome = nome
        self.idade = idade
        # atributos privado 
        self.__cpf = cpf 
        self.__rg = rg

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self,cpf):
        if self.__validar_cpf(cpf):
            self.__cpf = cpf

    def get_rg(self):
        return self.__rg
    
    def set_rg(self,rg):
        self.__rg = rg 

    def __validar_cpf(self, cpf):
        if type(cpf) == str and len(cpf) == 11:
            return True
        else:
            print("CPF inválido")
            return False

pessoa1 = Pessoa('João', 26,"11111111111", "333333333")

pessoa1.nome = "Paulo"
pessoa1.idade = 26
pessoa1.set_cpf('3333333333')
print("Nome", pessoa1.nome)
print("CPF", pessoa1.get_cpf())


#   while i < len(self.socios):
#                   if self.socios[i].nome in lista_expulsos:
#                       ...
#                   else:
#                       i += 1
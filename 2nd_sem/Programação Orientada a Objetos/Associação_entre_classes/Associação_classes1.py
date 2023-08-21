class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def exibir_dados(self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        self.endereco.exibir_dados()


class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua 
        self.numero = numero 
        self.cep = cep
    
    def exibir_dados(self):
        print('Rua: ',self.rua)
        print('Número: ',self.numero)
        print('CEP: ',self.cep)

endereco1 = Endereco('Rua Silva', 123, '878765-999')

pessoa1 = Pessoa('Paulo', 30, endereco1)

pessoa1.exibir_dados()

pessoa1.endereco.exibir_dados()
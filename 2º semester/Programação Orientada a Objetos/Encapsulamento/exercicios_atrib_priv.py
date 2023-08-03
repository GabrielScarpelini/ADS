'''Exercicio 1
Altere a classe Funcionario do programa abaixo:
Transforme os seus atributos em atributos privados.
Crie os métodos get e set para todos os atributos.
Faça as alterações necessárias para que o programa principal funcione corretamente,
após as alterações feitas na classe.
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario


func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.salario = 2000.0              # Altera salário
print("Nome:", func1.nome)
print("CPF:", func1.cpf)
print("Salário:", func1.salario)'''

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome - nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario


func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)              # Altera salário
print("Nome:", func1.get_nome())
print("CPF:", func1.get_cpf())
print("Salário:", func1.get_salario())

'''Exercício 02

Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os objetos na lista de filmes
Percorrer a lista de filmes e imprimir no terminal os dados de todos os filmes cadastrados
'''

class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, genero):
        self.__genero = genero

filmes = []
for x in range(3):
    filme = Filme(input('Digite o nome do filme:'), input('Digite o genêro:'))
    filmes.append(filme)

''' ow pode fazer
for x in range(3):
    titulo = input()
    genero = input()
    filme1 = Filme(titulo, genero)
    filmes.append(filme1)'''

for x in filmes:
    print(f'O título do filme é {x.get_titulo()}, e o gênero é {x.get_genero()}')

'''Exercício 03

Implemente as classes ContaBancaria e Cliente, conforme o diagrama de classes abaixo.



Classe Cliente
Atributos::
nome: nome do cliente (público)
cpf: cpf do cliente (privado)
senha: senha do cliente (privado)
Métodos:
get_senha: retorna a senha do cliente


Classe ContaBancaria
Atributos:
numero: numero da conta (público) 
cliente: objeto Cliente associado à conta (público)
saldo: saldo da conta (privado). Deve ser inicializado com zero.
Métodos:
get_saldo: retorna o saldo da conta.
depositar: recebe como parâmetros de entrada um valor e uma senha. Acrescenta esse valor
ao saldo da conta apenas se a senha for igual à senha do cliente.
sacar: recebe como parâmetros de entrada um valor e uma senha. Subtrai
esse valor do saldo da conta, apenas se a senha for igual à senha do cliente.
cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150
'''

class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

class ContaBancaria:
    def __init__ (self, numero, cliente):
        self.numero = numero 
        self.cliente = cliente
        self.__saldo = 0
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor, senha):
        if self.cliente.get_senha() == senha:
            self.__saldo += valor
        else:
            print('Depósito não realizado, Senha informada está incorreta')
    
    def sacar(self, valor, senha):
        if self.cliente.get_senha() == senha:
            if self.__saldo < valor:
                print('Valor indisponível')
            else:
                self.__saldo -= valor
        else:
            print('Saque não realizado, Senha informada está incorreta')

cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "122")              # senha inválida
print(conta.get_saldo())            # Imprime 150



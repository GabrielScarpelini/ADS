'''Exercício 01

Nome da classe:
Carro

Atributos:
marca
modelo
placa

Métodos:
__init__(self, marca, modelo, placa): Método construtor
exibir_dados(self): Deve exibir os valores dos atributos do carro

No programa principal:
Crie dois objetos da classe Carro
Utilize o método exibir_dados para
exibir no terminal os atributos dos carros.'''


class Carro:

    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibe_dados(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa: {self.placa}')


veiculo1 = Carro('Volkswagen', 'Golf GTI', 'EWD-2022')
veiculo2 = Carro('Volvo', 'XC60', 'EPK-1563')

veiculo1.exibe_dados()
veiculo2.exibe_dados()


'''Exercício 02

Nome da classe:
Funcionario

Atributos:
nome
sobrenome
salario

Métodos:
__init__(self, nome, sobrenome, salario): Método construtor.
Deve fazer uma validação do salário e, se o salário informado
for negativo, deve definí-lo como zero.
aumentar_salario(self): Aumentar o salário do funcionário em 10%.


No programa principal:
Crie dois objetos da classe Funcionario
Utilize o método aumentar_salario para atualizar os salários dos funcionários.
'''


class Funcionario:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        if self.salario < 0:
            self.salario = 0
        else:
            self.salario = salario

    def aumentar_salario(self):
        self.salario += self.salario * 0.10

emp1 = Funcionario('Gabriel', 'Scarpelini', -2000)
emp2 = Funcionario('Miguel', 'Da Silva', 1500)
emp1.aumentar_salario()
emp2.aumentar_salario()

'''Exercício 03

Nome da Classe:
ContaBancaria

Atributos:
numero
titular
senha
saldo (deve ser inicializado no construtor com o valor zero)

Métodos:
__init__(self, numero, titular, senha):
Método construtor.
depositar(self, valor, senha): Deve verificar se a senha informada está
correta.Se estiver, deve realizar a operação de deposito e atualizar o saldo da
conta. Caso contrário deve exibir uma mensagem de senha incorreta.
sacar(self, valor, senha): Deve verificar se a senha informada está correta.
Se estiver, deve realizar a operação de saque e atualizar o saldo da conta.
Caso contrário deve exibir uma mensagem de senha incorreta.


No programa principal:
Crie um objeto da classe ContaBancaria
Realize operações de depósito e saque utilizando os métodos
implementados na clase.'''


class ContaBancaria:

    # saldo não entra pois ele foi um valor pré definido no escopo
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):
        if senha == self.senha:
            self.saldo += valor
        else:
            print('Senha Incorreta')

    def sacar(self, valor, senha):
        if senha == self.senha:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('Senha incorreta')


pessoa1 = ContaBancaria(1234, 'Gabriel', 123456)

pessoa1.depositar(500, 123456)
pessoa1.sacar(450, 123456)

print(pessoa1.saldo)

'''Exercício 04 

Nome da Classe:
Aluno

Atributos:
ra
nome
turma
notas: lista de notas do aluno. Deve ser inicializada no construtor como uma lista vazia.

Métodos:
__init__(self, ra, nome, turma): Método construtor. 
inserir_nota(self, nota): Deve verificar se a nota informada é valida (de 0 à 10). 
Se for válida, deve inserir a nota na lista de notas do aluno. 
Caso contrário deve exibir uma mensagem de nota inválida.
calcular_media(self): Calcula e retorna a média aritmética das notas do alunos.

No programa principal:
Crie três objeto da classe Aluno
Insira algumas notas para cada aluno.
Insira os objetos em uma lista.
Percorra a lista de alunos e exiba a média de cada alu
'''


class Alunos:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.nota = []      # por notas for algo pedido para nós criarmos ela não entra nos parâmetros

    def inserir_nota(self, nota):
        if nota < 0 or nota > 10:
            print('Nota invalida')
        else:
            self.nota.append(nota)

    def calcular_media(self):
        return sum(self.nota)/len(self.nota)
    

aluno1 = Alunos(2102341, 'Gabriel', 'ADS 2A')
aluno2 = Alunos(2000000, 'Lago', 'ADS 2A')
aluno3 = Alunos(1999999, 'Daniel', 'ADS 2A')

aluno1.inserir_nota(20)
aluno1.inserir_nota(10)
aluno1.inserir_nota(9)
aluno1.inserir_nota(6)

aluno2.inserir_nota(50)
aluno2.inserir_nota(6)
aluno2.inserir_nota(9)
aluno2.inserir_nota(8)

aluno3.inserir_nota(-2)
aluno3.inserir_nota(1)
aluno3.inserir_nota(9)
aluno3.inserir_nota(9)
print(aluno1.nota)
print(aluno2.nota)
print(aluno3.nota)

lista = [aluno1, aluno2, aluno3]


for x in lista:
    print(f'{x.nome} {x.calcular_media():.2f}')


'''Exercício 05


Nome da Classe:
Carro

Atributos:
quantidade_combustivel (quantidade de litros de combustível no tanque do carro):
a  quantidade inicial deve ser zero.

Métodos:
adicionar_combustivel(self, litros): recebe uma quantidade de litros de 
combustível para abastecer o tanque.
obter_combustivel(self): retorna a quantidade atual de combustível.
andar(self, distancia): recebe uma distância em km e simula o ato de dirigir o 
veículo por essa distância, reduzindo o nível de combustível no tanque de gasolina. 
Considere que o veiculo consome 0.20 litros de combustivel por quilômetro percorrido.'''


class Carro:
    def __init__(self):  # como aqui o tanque nós atribuímos, não precisa colocar nada ao lado de self
        self.quanidade_combustivel = 0

    def adicionar_combustivel(self, litros):
        self.quanidade_combustivel += litros

    def obter_combustivel(self):
        return self.quanidade_combustivel

    def andar(self, distancia):
        if self.quanidade_combustivel - distancia* 0.2 >= 0:
            self.quanidade_combustivel -= distancia * 0.2
        else:
            return print('Você ficará sem gasolina')

meu_carro = Carro()
meu_carro.adicionar_combustivel(20)				    # Adiciona 20 litros
meu_carro.andar(150)						        # Andar 80 quilômetros
print('Litros de combustível no tanque:', meu_carro.obter_combustivel())
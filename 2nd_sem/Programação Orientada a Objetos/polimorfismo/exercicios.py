from abc import ABC, abstractmethod 

'''Exercício 01'

Implemente o diagrama abaixo utilizando polimorfismo para calcular as operações matemáticas.
 
A classe Operacao deve ser abstrata. O método calcular da classe Operação também deve ser abstrato.

As classes herdeiras devem implementar o método calcular. Esse método deve realizar a operação correspondente e retornar o resultado.

Observe que as classes não possuem atributos, portanto não precisam ter construtores.


Utilize o trecho de programa abaixo para testar suas classes
# Programa Principal

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50'''

class Operacao(ABC):
    @abstractmethod
    def calcular(self, x, y):
        pass

class Soma(Operacao):
    def calcular(self, x, y):
        return x + y

class Subtracao(Operacao):
    def calcular(self, x, y):
        return x - y

class Multiplicacao(Operacao):
    def calcular(self, x, y):
        return x * y

class Divisao(Operacao):
    def calcular(self, x, y):
        return x / y 

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50'''

print('----------------------------------------------')

'''Exercício 02
Crie uma hierarquia de classes conforme o diagrama abaixo. 
Os atributos em comum devem ficar na classe Animal.
Os métodos emitir_som devem imprimir uma mensagem simulando a emissão do som do animal correspondente.
A classe Veterinario deve conter o método examinar(), que recebe como entrada um objeto que representa um animal e, quando o animal for examinado, esse animal deve emitir o seu som.
No programa principal, crie objetos dos 3 tipos de animais e execute o método que emite o som de cada um.


Utilize o trecho de programa abaixo para testar suas classes
dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato

'''

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class Veterinario:
    def examinar(self, animal):
       return animal.emitir_som()


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print('auuuu au au au au')

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print('miau miau miau')

class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print('iiihihihihih')

dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato

print('----------------------------------------------')

'''Exercício 03

Crie uma hierarquia de classes para representar os diferentes tipos de funcionários de um escritório que tem os seguintes cargos: gerente, assistente e vendedor. 
Escreva uma superclasse abstrata chamada Funcionario que define o método abstrato calcular_salario().
Essa classe também deve ter os seguintes atributos: nome, matricula e salario_base.
A classe Funcionario deverá ser herdada pelas outras classes que são: Gerente, Assistente e Vendedor. 
Em cada classe-filha deve-se sobrescrever o método calcular_salario(). Este método deve calcular e retornar o salário de cada funcionário, da seguinte forma: 
O assistente recebe o salário_base.
O gerente recebe duas vezes o salário_base.
O vendedor recebe o salário_base mais uma comissão de 10%. 
Implemente um programa principal que cria um objeto de cada tipo (gerente, assistente e vendedor) e os armazena em uma lista.
Percorra essa lista e imprima o salário de cada funcionário.'''

class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 2

class Assistente(Funcionario):
    def calcular_salario(self):
        return self.salario_base 

class Vendedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.10

emp1 = Vendedor('Igor', 1111, 2500)
emp2 = Gerente('Iago', 1112, 5000)
emp3 = Assistente('Daniel', 1113, 2000)

lista = [emp1, emp2, emp3]

for x in lista:
    print(f'Olá {x.nome} seu salario é {x.calcular_salario()}')

print('----------------------------------------------')

'''Exercício 04

Um banco trabalha com três tipos de contas:
conta corrente
conta especial
conta poupança
Em todas as contas é necessário armazenar o número da conta, o nome do correntista e o saldo.
Para a conta especial é necessário armazenar também o valor do limite.
As operações possíveis são: depósito, saque e impressão do saldo. Essas operações devem ser definidas numa classe abstrata denominada Conta.
A operação de depósito e saldo são iguais para os três tipos de conta.
A operação de saque só é diferente na conta especial, pois esta admite que o saldo fique negativo até o limite estabelecido.
Nas demais contas o saque não pode ser realizado se não houver saldo suficiente.
Implemente uma hierarquia de classes que atenda a descrição acima.
'''




class Conta(ABC):
    def __init__(self, num_conta, nome, saldo):
        self.num_conta = num_conta
        self.nome = nome 
        self.saldo = saldo 
    
    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def impressao(self):
        pass

class Corrente(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insulficiente')
        else:
            self.saldo -= valor
            print(f'seu saldo atual é {self.saldo}')
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def impressao(self):
        print(f'seu saldo é {self.saldo}')

class Espcial(Conta):
    def __init__(self, num_conta, nome, saldo, limite):
        super().__init__(num_conta, nome, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            print('Você não tem limite suficiente para realizar a operação')
        else:
            self.saldo -= valor
            print(f'seu saldo é {self.saldo}')
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def impressao(self):
        print(f'seu saldo é {self.saldo}')

class Poupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insulficiente')
        else:
            self.saldo -= valor
            print(f'seu saldo atual é {self.saldo}')
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def impressao(self):
        print(f'seu saldo é {self.saldo}')

pessoa1 = Poupanca(1111, 'Igor', 0)
pessoa2 = Espcial(6666, 'Lago', 0, -10000)
pessoa3 = Corrente(5656, 'Daniel', 0)

pessoa1.sacar(200)
pessoa1.depositar(100)
pessoa1.impressao()
pessoa1.sacar(2200)

pessoa2.depositar(200)
pessoa2.impressao()
pessoa2.sacar(10201)

pessoa3.depositar(200)
pessoa3.impressao()
pessoa3.sacar(2200)







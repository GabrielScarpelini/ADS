'''Exercício 01

A associação entre classes ocorre quando uma classe possui atributos que são objetos de
Outra classe. De acordo com esse conceito, observe o diagrama de classes abaixo, que
representa uma associação onde uma Pessoa possui um Carro.


Implemente as classes Pessoa e Carro.

Classe Pessoa:
Atributos:
nome: nome da pessoa
idade: idade da pessoa
carro: objeto da classe Carro (valor inicial definido no construtor como None)
Métodos:
comprar_carro: recebe um objeto Carro e atribui esse objeto ao atributo carro.

Classe Carro:
Atributos:
marca: marca do carro
modelo: modelo do carro
placa: placa do carro
ano: ano de fabricação do carro
Métodos: 
Não possui


Você pode utilizar o trecho de programa abaixo para testar as suas classes:

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime: João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime :Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime: AAA-1111'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None
    
    def comprar_carro(self,carro):
        self.carro = carro
    
class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime: João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime :Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime: AAA-1111


'''Exercício 02

Observe o diagrama de classes abaixo, que representa uma associação onde um
Pedido possui uma lista de Produtos.



Implemente as classes Produto e Pedido.

Classe Pedido:
Atributos:
produtos: Lista de objetos do classe Produto (inicializar no construtor como uma lista vazia)
Métodos:
adicionar_produto: recebe um objeto Produto e o adiciona na lista de produtos.
calcular_valor: deve retornar o valor total do pedido (soma dos preços de todos os produtos do pedido)

Classe Produto:
Atributos:
nome: nome do produto
preco: preço do produto
quantidade: quantidade de itens do produto
Métodos: 
Não possui


Você pode utilizar o programa abaixo para testar as suas classes:'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome 
        self.preco = preco 
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_valor(self):
        soma = 0 
        for prod in self.produtos:
            soma += prod.preco * prod.quantidade
        return soma


            
       

cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())	    # imprime 20.90



'''Exercicio 3 
Implemente o diagrama de classes abaixo.

Classe Paciente
Atributos:
nome
cpf
idade
Métodos:
não possui

Classe Medico
Atributos:
nome
crm
especializacao
Métodos:
não possui

Classe Exame
Atributos:
medico: objeto da classe Medico
paciente: objeto da classe Paciente
descricao
resultado
Métodos:
imprimir_exame(): exibe um relatório com os dados do exame (inclusive os dados do médico e do paciente)

Você pode utilizar o programa a seguir para testar as suas classes:

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)
# paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)
'''

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
         self.medico = medico
         self.paciente = paciente
         self.descricao = descricao
         self.resultado = resultado

    def imprimir_exame(self):
        print("Nome do médico ", self.medico.nome)
        print("CRM do médico ", self.medico.crm)
        print("Especialidade ", self.medico.especializacao)
        print("Nome do paciênte ", self.paciente.nome)
        print("CPF do paciênte ", self.paciente.cpf)
        print("Idade do paciênte ", self.paciente.idade)
        print("Descrição do exame ", self.descricao)
        print("Resultado ", self.resultado )
        

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()

'''Exercício 04


Implemente o diagrama de classes abaixo.


Classe Emprego
Atributos:
cargo
area
salario
bonus: percentual de bonificação
Métodos:
não possui


Classe Pessoa
Atributos:
nome
fone
email
emprego: objeto do tipo Emprego
dependentes: lista de objetos do tipo Pessoa. Inicializar como uma lista vazia.
	Métodos:
calcular_salario: retorna o valor do salário do funcionário, de acordo com o percentual de
bonificação e quantidade de dependentes. Por exemplo, se o bônus for de 2%, e o funcionário tiver 3
dependentes, ele receberá 6% de acréscimo sobre o salário.

Você pode utilizar o programa a seguir para testar as suas classes:

emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())                # imprime 1100.0'''

class Emprego:
    def __init__(self,cargo, area, salario, bonus): # atributos 
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus

class Pessoa:
    def __init__(self, nome, fone, email, emprego): # atributos 
        self.nome = nome 
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = [] 

    def calcular_salario(self):#solução do prof
        porcentagem = len(self.dependentes) * self.emprego.bonus 
        aumento = self.emprego.salario * porcentagem / 100
        return self.emprego.salario + aumento

emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999","paulo@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())                # imprime 1100.0
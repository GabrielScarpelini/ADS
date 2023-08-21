class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.__placa = placa

    def get_placa(self):
        return self.__placa

    def teste(self):
        print('teste')
    
    def exibir(self):
        print('---------------------')
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.get_placa())


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, partida):
        super().__init__(marca, modelo, placa)
        self.partida = partida

    def exibir(self):
        super().exibir()
        print('Partida Elétrica: ', self.partida)


class Carro(Veiculo):                  # classe Carro herda da classe Veiculo
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas           # atributo específico do Carro

    def exibir(self):
        super().exibir()
        print('Portas: ', self.portas)

    def teste(self):
        print('lago lindo')

# Programa Principal
carro1 = Carro("Ford", "Ka", "AAA-1234", 4)
carro1.exibir()
carro1.teste()

moto1 = Moto('BMW', 'S1000RR', 'EWD-1950', 'Sim')
moto1.exibir()



class ExcecaoSenhaInvalida(Exception):

    pass


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.__saldo = 0
        self.cliente = cliente

    def get_saldo(self, senha):
        if self.cliente.get_senha() == senha:
            return self.__saldo

        else:
            raise ExcecaoSenhaInvalida

    def depositar(self, valor, senha):
        if self.cliente.get_senha() == senha:
            self.__saldo += valor

        else:
            raise ExcecaoSenhaInvalida

    def sacar(self, valor, senha):
        if self.cliente.get_senha() == senha:
            self.__saldo -= valor

        else:
            raise ExcecaoSenhaInvalida 
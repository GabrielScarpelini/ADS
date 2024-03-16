from pytest import fixture
from src.conta_bancaria import ContaBancaria
from src.cliente import Cliente

@fixture
def cliente():
    return Cliente('Jose da Silva', '123456789-00', '1234')

@fixture
def conta(cliente):
    conta = ContaBancaria(1, cliente)
    return conta 
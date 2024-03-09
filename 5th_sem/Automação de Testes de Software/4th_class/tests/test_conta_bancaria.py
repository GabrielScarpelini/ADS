from src.conta_bancaria import ContaBancaria
from src.cliente import Cliente


def test_criar_conta_bancaria_devolve_numero_correto():
    cliente = Cliente('Jose da Silva', '123456789-00', '1234')
    contaBancaria = ContaBancaria(1, cliente)
    assert contaBancaria.numero == 1

def test_criar_conta_bancaria_devolve_numero_correto():
    cliente = Cliente('Jose da Silva', '123456789-00', '1234')
    conta = ContaBancaria(1, cliente)
    assert conta.numero == 1


def test_criar_conta_bancaria_devolve_saldo_zerado():
    cliente = Cliente('Jose da Silva', '123456789-00', '1234')
    conta = ContaBancaria(1, cliente)
    assert conta.get_saldo(senha='1234') == 0

def test_depositar_valor_em_conta_devolve_saldo_aumentado():
    cliente = Cliente('Jose da Silva', '123456789-00', '1234')
    conta = ContaBancaria(1, cliente)
    assert conta.get_saldo(senha='1234') == 0
    conta.depositar(100, '1234')
    assert conta.get_saldo(senha='1234') == 100


def test_sacar_valor_em_conta_bancaria_devolve_saldo_menor():
    cliente = Cliente('Jose da Silva', '123456789-00', '1234')
    conta = ContaBancaria(1, cliente)
    conta.depositar(100, '1234')
    assert conta.get_saldo(senha='1234') == 100
    conta.sacar(20, '1234')
    assert conta.get_saldo(senha='1234') == 80
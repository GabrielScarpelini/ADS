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

def test_criar_cliente_deve_devolver_nome_de_cliente_valido(cliente):

    assert cliente.nome == 'Jose da Silva'


def test_criar_cliente_deve_devolver_cpf_do_cliente_valido(cliente):
    assert cliente.get_cpf() == '123456789-00'

def test_criar_cliente_deve_devolver_senha_do_cliente_valida(cliente):
    assert cliente.get_senha() == '1234'
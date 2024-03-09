import pytest


from src.cliente import Cliente


@pytest.fixture

def cliente():
    return Cliente('Jose da Silva', '123456789-00', '1234')

def test_criar_cliente_deve_devolver_nome_de_cliente_valido(cliente):
    assert cliente.nome == 'Jose da Silva'

def test_criar_cliente_deve_devolver_cpf_do_cliente_valido(cliente):
    assert cliente.get_cpf() == '123456789-00'

def test_criar_cliente_deve_devolver_senha_do_cliente_valida(cliente):
    assert cliente.get_senha() == '1234'
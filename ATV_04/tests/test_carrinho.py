"""Carrinho de compras feature tests."""

from pytest import fixture
from app.carrinho import CarrinhoCompras
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@fixture
def context():
    return CarrinhoCompras()


@scenario('../features/carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""



@scenario('../features/carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""


@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def _(context):
    """que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99."""
    context.adicionar_item("Camiseta", 29.99)


@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def _(context):
    """eu adiciono o item "Calça" com o preço R$ 49.99."""
    context.adicionar_item("Calça", 49.99)


@when('eu removo o item do carrinho')
def _(context):
    """eu removo o item do carrinho."""
    context.remover_item()


@then('o carrinho de compras deve estar vazio')
def _(context):
    """o carrinho de compras deve estar vazio."""
    assert context.esta_vazio()


@then('o total do carrinho de compras deve ser R$ 79.98')
def _(context):
    """o total do carrinho de compras deve ser R$ 79.98."""
    assert context.total() == 79.98


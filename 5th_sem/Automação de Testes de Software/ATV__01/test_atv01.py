import pytest
from atv_01 import atv1

def test_salarioLiquido():
    with pytest.raises(TypeError):
        atv1.salarioLiquido("6.25", 160, 1.3)
        atv1.salarioLiquido(6.25, "160", 1.3)
        atv1.salarioLiquido(6.25, 160, "1.3")
    assert atv1.salarioLiquido(6.25, 160, 1.3) == 987.00
    assert atv1.salarioLiquido(20.5, 240, 1.7) == 4836.36
    assert atv1.salarioLiquido(13.9, 200, 6.48) == 2599.86

def test_aplicaDesconto9():
    # with pytest.raises(TypeError):
    #     salarioLiquido(6.25, 160, 1.3) == 987.0
    assert atv1.aplicaDesconto9(100) == (91.00, 9.00)
    assert atv1.aplicaDesconto9(1500) == (1365.00, 135.00)
    assert atv1.aplicaDesconto9(60000) == (54600.00, 5400.00)

def test_aplicaDescontoReal():
    # with pytest.raises(TypeError):
    #     salarioLiquido(6.25, 160, 1.3) == 987.0
    assert atv1.aplicaDescontoReal(500.00, 50.00) == 450.00
    assert atv1.aplicaDescontoReal(10500.00, 500.00) == 10000.00
    assert atv1.aplicaDescontoReal(90.00, 0.80) == 89.20

def test_calculaTaxaGarcoml():
    # with pytest.raises(TypeError):
    #     salarioLiquido(6.25, 160, 1.3) == 987.0
    assert atv1.calculaTaxaGarcom(75.00) == (82.50, 7.5)
    assert atv1.calculaTaxaGarcom(125) == (137.50, 12.5)
    assert atv1.calculaTaxaGarcom(350.87) == (385.96, 35.09)

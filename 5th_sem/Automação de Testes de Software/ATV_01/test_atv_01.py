import pytest

class  atv1:

    def salarioLiquido(vlrHora, qtdAulas, percentInss):
        valorBruto = vlrHora * qtdAulas
        valorDeconto = valorBruto * (percentInss/100)

        return float("{:.{}f}".format(valorBruto - valorDeconto, 2))

    def aplicaDesconto9(valorProduto):
        vlrRemove = valorProduto * 0.09
        newVLR = valorProduto - vlrRemove

        return float("{:.{}f}".format(newVLR, 2)), float("{:.{}f}".format(vlrRemove, 2)) 

    def aplicaDescontoReal(vlrProduto, vlrOff):
        return float("{:.{}f}".format(vlrProduto - vlrOff, 2))

    def calculaTaxaGarcom(vlrComanda):
        valorTaxa = vlrComanda * 0.1
        valorTotal = vlrComanda + valorTaxa
        return float("{:.{}f}".format(valorTotal, 2)), float("{:.{}f}".format(valorTaxa, 2))


def test_salarioLiquido():
    with pytest.raises(TypeError):
        atv1.salarioLiquido("X", 0, 0)
        atv1.salarioLiquido(0, "X", 0)
        atv1.salarioLiquido(0, 0, "x")
    assert atv1.salarioLiquido(6.25, 160, 1.3) == 987.00
    assert atv1.salarioLiquido(20.5, 240, 1.7) == 4836.36
    assert atv1.salarioLiquido(13.9, 200, 6.48) == 2599.86

def test_aplicaDesconto9():
    with pytest.raises(TypeError):
        atv1.salarioLiquido("X")
    assert atv1.aplicaDesconto9(100) == (91.00, 9.00)
    assert atv1.aplicaDesconto9(1500) == (1365.00, 135.00)
    assert atv1.aplicaDesconto9(60000) == (54600.00, 5400.00)

def test_aplicaDescontoReal():
    with pytest.raises(TypeError):
        atv1.aplicaDescontoReal("X", 0)
        atv1.aplicaDescontoReal(0, "X")
    assert atv1.aplicaDescontoReal(500.00, 50.00) == 450.00
    assert atv1.aplicaDescontoReal(10500.00, 500.00) == 10000.00
    assert atv1.aplicaDescontoReal(90.00, 0.80) == 89.20



def test_calculaTaxaGarcoml():
    with pytest.raises(TypeError):
        atv1.calculaTaxaGarcom("X")
    assert atv1.calculaTaxaGarcom(75.00) == (82.50, 7.5)
    assert atv1.calculaTaxaGarcom(125) == (137.50, 12.5)
    assert atv1.calculaTaxaGarcom(350.87) == (385.96, 35.09)

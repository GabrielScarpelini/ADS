class atv1:

    def salarioLiquido(vlrHora, qtdAulas, percentInss):
        valorBruto = vlrHora * qtdAulas
        valorDeconto = valorBruto * (percentInss/100)

        return float("{:.{}f}".format(valorBruto - valorDeconto, 2))
        return valorBruto - valorDeconto

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
    
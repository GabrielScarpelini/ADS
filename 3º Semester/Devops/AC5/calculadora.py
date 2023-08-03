import abc
from unittest import TestCase, main

class Calculadora():

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        return n1 * n2

    def dividir(self, n1, n2):
        if n2 == 0:
            return 0
        return n1 / n2

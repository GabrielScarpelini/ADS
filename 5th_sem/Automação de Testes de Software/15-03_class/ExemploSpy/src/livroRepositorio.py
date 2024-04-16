from abc import ABCMeta, abstractmethod
from src.livro import Livro

class LivroRepositorio(metaclass=ABCMeta):

    @abstractmethod
    def inserir(self, livro: Livro):
        pass 
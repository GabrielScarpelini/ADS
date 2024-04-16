from abc import ABCMeta, abstractmethod
from src.livro import Livro

class LivroRepositorio(metaclass=ABCMeta):

    @abstractmethod
    def obter_livro(self, id: str) -> Livro:
        pass 
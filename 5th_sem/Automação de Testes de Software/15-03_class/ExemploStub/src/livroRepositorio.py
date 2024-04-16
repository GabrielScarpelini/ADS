from abc import ABCMeta, abstractmethod
from src.livro import Livro

class LivroRepositorio(metaclass=ABCMeta):

    @abstractmethod
    def inserir(self, livro: Livro):
        pass


    @abstractmethod
    def buscar_todos(self) -> list:
        pass

    @abstractmethod
    def obter_tamanho(self) -> int:
        pass    

    @abstractmethod
    def obter_por_id(self, id: str) -> Livro:
        pass 
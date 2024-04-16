from src.livro import Livro
from src.livroRepositorio import LivroRepositorio

class LivroRepositorioSpy(LivroRepositorio):

    def __init__(self):
        self.__contagem_insercao = 0
        self.__ultimo_livro = None

    def inserir(self, livro: Livro):
        self.__contagem_insercao += 1
        self.__ultimo_livro = livro

    def numero_de_insercoes(self):
        return self.__contagem_insercao

    def verificar_ultimo_livro_inserido(self, id: str):
        return self.__ultimo_livro.id == id 
from datetime import date

from src.livro import Livro
from src.livroRepositorio import LivroRepositorio

class ExcecaoLivroNaoEncontrado(Exception):
    pass


class LivroRepositorioMock(LivroRepositorio):

    def __init__(self):
        self.__contagem_chamadas = 0
        l1 = Livro('111', 'Python para iniciantes', 50.0, date.today) 
        self.__livro = l1


    def obter_livro(self, id: str) -> Livro:
        self.__contagem_chamadas += 1
        
        if id == '111':
            return self.__livro
        raise ExcecaoLivroNaoEncontrado

    def numero_de_chamadas(self):
        return self.__contagem_chamadas
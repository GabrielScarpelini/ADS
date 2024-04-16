from datetime import date
from src.livro import Livro
from src.livroRepositorio import LivroRepositorio

class ExcecaoLivroNaoEncontrado(Exception):
    pass

class LivroRepositorioStub(LivroRepositorio):

    def __init__(self):
        self.livros = []
        l1 = Livro('111', 'Python para iniciantes', 50.0, date.today) 
        l2 = Livro('222', 'Testes automatizados', 70.0, date.today)
        self.inserir(l1)
        self.inserir(l2)

    def inserir(self, livro: Livro):
        self.livros.append(livro)

    def buscar_todos(self) -> list:
        return list(self.livros)


    def obter_tamanho(self) -> int:
        return len(self.livros)

    def obter_por_id(self, id: str) -> Livro:

        for livro in self.livros:
            if livro.id == id:
                return livro
            
        raise ExcecaoLivroNaoEncontrado
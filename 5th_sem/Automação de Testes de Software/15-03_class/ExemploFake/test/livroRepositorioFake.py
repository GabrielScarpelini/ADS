from src.livro import Livro
from src.livroRepositorio import LivroRepositorio

class LivroRepositorioFake(LivroRepositorio):

    def __init__(self):
        self.livros = []
        
    def inserir(self, livro: Livro):
        self.livros.append(livro)

    def buscar_todos(self) -> list:
        return list(self.livros)

    def obter_tamanho(self) -> int:
        return len(self.livros)
from src.livro import Livro
from src.livroRepositorio import LivroRepositorio

class LivroServico:

    def __init__(self, livroRepositorio: LivroRepositorio):
        self.livroRepositorio = livroRepositorio

    def insere_livro(self, livro: Livro):
        self.livroRepositorio.inserir(livro) 
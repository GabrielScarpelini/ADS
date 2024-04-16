from src.livro import Livro
from src.livroRepositorio import LivroRepositorio
from src.emailServico import EmailServico


class LivroServico:

    def __init__(self, livroRepositorio: LivroRepositorio, \
        emailServico: EmailServico):
        self.livroRepositorio = livroRepositorio
        self.emailServico = emailServico

    def insere_livro(self, livro: Livro):
        self.livroRepositorio.inserir(livro)

    def obter_tamanho(self):
        return self.livroRepositorio.obter_tamanho()
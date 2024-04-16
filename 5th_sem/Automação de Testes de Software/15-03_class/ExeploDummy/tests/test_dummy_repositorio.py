from datetime import date

from livroRepositorioFake import LivroRepositorioFake
from emailServicoDummy import EmailServicoDummy
from src.livro import Livro
from src.livroServico import LivroServico


def test_inserir_dois_livros_deve_retornar_contagem_2():

    livroRepositorio = LivroRepositorioFake()
    emailServico = EmailServicoDummy()
    livroServico = LivroServico(livroRepositorio, emailServico)

    l1 = Livro('111', 'Python para iniciantes', 50.0, date.today) 
    l2 = Livro('222', 'Testes automatizados', 70.0, date.today)

    livroServico.insere_livro(l1)
    livroServico.insere_livro(l2)

    assert livroServico.obter_tamanho() == 2


import pytest
from datetime import date

from tests.livroRepositorioSpy import LivroRepositorioSpy
from src.livro import Livro
from src.livroServico import LivroServico


def test_inserir_2_livros_retornar_numero_de_insercoes_2():

    livroRepositorio = LivroRepositorioSpy()
    livroServico = LivroServico(livroRepositorio)
    l1 = Livro('111', 'Python para iniciantes', 50.0, date.today) 
    l2 = Livro('222', 'Testes automatizados', 70.0, date.today)
    livroServico.insere_livro(l1)
    livroServico.insere_livro(l2)
    assert livroRepositorio.numero_de_insercoes() == 2
    assert livroRepositorio.verificar_ultimo_livro_inserido('222') 
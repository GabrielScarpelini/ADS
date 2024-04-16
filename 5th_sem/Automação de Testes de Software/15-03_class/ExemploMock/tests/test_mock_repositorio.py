import pytest

from tests.livroRepositorioMock import LivroRepositorioMock 
from tests.livroRepositorioMock import ExcecaoLivroNaoEncontrado
from src.livro import Livro


def test_busca_livro_por_id():
    livroRepositorio = LivroRepositorioMock()
    livro = livroRepositorio.obter_livro('111')
    assert livro.id == '111'
    assert livro.titulo == 'Python para iniciantes'
    assert livroRepositorio.numero_de_chamadas() == 1

def test_busca_livro_por_id_inexistente_gera_excecao():
    with pytest.raises(ExcecaoLivroNaoEncontrado):
        livroRepositorio = LivroRepositorioMock()
        livroRepositorio.obter_livro('222')
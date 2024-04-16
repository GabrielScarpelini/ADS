import pytest
from ExemploStub.tests.livroRepositorioStub import LivroRepositorioStub
from ExemploStub.tests.livroRepositorioStub import ExcecaoLivroNaoEncontrado
from src.livroServico import LivroServico


@pytest.fixture

def servico():
    livroRepositorio = LivroRepositorioStub()
    livroServico = LivroServico(livroRepositorio)
    return livroServico

def test_objeto_stub_deve_devolver_contagem_igual_2(servico):
    assert servico.obter_tamanho() == 2

def test_busca_por_id_deve_devolver_livro_com_id_111(servico):
    l1 = servico.obter_por_id('111') 
    assert l1.id == '111' 

def test_busca_por_id_deve_devolver_livro_com_id_222(servico):
    l1 = servico.obter_por_id('222') 
    assert l1.id == '222' 

def test_busca_por_id_333_deve_devolver_excecao(servico):
    with pytest.raises(ExcecaoLivroNaoEncontrado):
        l1 = servico.obter_por_id('333')
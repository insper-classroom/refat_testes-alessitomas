import json
import pytest
from classes.PessoaFisica import PessoaFisica
import requests

@pytest.mark.pessoa_fisica
# testar criacao de pessoa
def test_construcao_obj_tds_argumentos():
    nome = 'Tomás'
    email = 'tomasalessi@hotmail.com'
    cpf = '00000000000'
    pessoa = PessoaFisica(nome, email, cpf)
    assert pessoa.nome == 'Tomás'
    assert pessoa.email == "tomasalessi@hotmail.com"
    assert pessoa.cpf == '00000000000'
    

@pytest.mark.pessoa_fisica
# testar criacao de pessoa com nome vazio
def test_construcao_obj_nome_vazio():
    pessoa=PessoaFisica()
    assert pessoa.nome == 'Visitante'


@pytest.mark.pessoa_fisica
# testar busca de nome
def test_busca_nomes_iguais():
    pessoa1 = PessoaFisica('Milton')
    pessoa2 = PessoaFisica('Milton')
    pessoa3 = PessoaFisica('Milton')
    lista_nomes = PessoaFisica.busca_nome('Milton')
    assert lista_nomes == ['Milton','Milton','Milton']

@pytest.mark.pessoa_fisica
# testar adiconar endereco
def test_adicionar_endreco():
    pessoa1 = PessoaFisica('Milton')
    resp = pessoa1.adicionar_endereco('Casa','Carlos Gelenski')
    assert resp == {'Casa':'Carlos Gelenski'}

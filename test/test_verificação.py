# testes consultar cep
import json
import pytest
from classes.Endereco import Endereco
import requests

@pytest.mark.construcao_obj
def test_construcao_obj_2_argumentos():
    cep = 82030590
    endereco = Endereco(cep, 10)
    
    assert endereco.rua == 'Rua Carlos Gelenski'
    assert endereco.estado == 'PR'
    assert endereco.cidade == 'Curitiba'

@pytest.mark.construcao_obj
def test_construcao_obj_todos_argumentos():
    cep = 82030590
    endereco = Endereco(cep, 10, 'Rua Carlos Gelenski', 'PR', 'Curitiba','casa 31')
    
    assert endereco.rua == 'Rua Carlos Gelenski'
    assert endereco.estado == 'PR'
    assert endereco.cidade == 'Curitiba'
    assert endereco.complemento == 'casa 31'

@pytest.mark.consulta_cep
def test_consulta_cep_int():
    cep = 82030590
    json = Endereco.consultar_cep(cep)
    assert json['logradouro'] == 'Rua Carlos Gelenski'
    assert json['uf'] == 'PR'
    assert json['localidade'] == 'Curitiba'

@pytest.mark.consulta_cep
def test_consulta_cep_str():
    cep = '82030590'
    json = Endereco.consultar_cep(cep)
    assert json['logradouro'] == 'Rua Carlos Gelenski'
    assert json['uf'] == 'PR'
    assert json['localidade'] == 'Curitiba'

@pytest.mark.consulta_cep

def test_consulta_cep_não_existente():
    cep = "00000000"
    json = Endereco.consultar_cep(cep)
    assert json == False
  
# teste cep erro no fromato
def test_consulta_cep_invalido():
    cep = 0000000
    json = Endereco.consultar_cep(cep)
    assert json == False


# teste cep com erro na internet
def test_consulta_cep_internet():
    cep = 82030590
    
    with pytest.raises(requests.exceptions.ConnectionError) as erro_conexão:
        json = Endereco.consultar_cep(cep)
    assert "Connection" in str(erro_conexão.value)
        



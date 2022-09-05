import json
import pytest
from classes.Produto import Produto
import requests

@pytest.mark.produto
# teste criacao de produto
def test_criar_produto():
    produto = Produto(1, "sapato")
    assert produto.id == 1
    assert produto.nome == "sapato"
@pytest.mark.produto
# teste alterar id
def test_alterar_id():
    produto = Produto(1, "tenis")
    produto.set_id(2)
    assert produto.id == 2

@pytest.mark.produto
# teste alterar nome
def test_alterar_nome():
    produto = Produto(1, "sabonete")
    produto.nome = "morango"
    assert produto.nome == "morango"

@pytest.mark.produto
# teste busca nome
def test_busca_nome():
    Produto.busca_nome("tenis")
    assert Produto.busca_nome("tenis") == ["tenis"]
    
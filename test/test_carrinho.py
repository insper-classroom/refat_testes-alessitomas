import json
import pytest
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Produto import Produto
import requests

@pytest.mark.carrinho
# teste criacao de carrinho
def test_criar_carrinho():
    carrinho = Carrinho()
    assert str(carrinho) == '{}'
   

@pytest.mark.carrinho
# teste adicionar item
def test_adicionar_item():
    produto = Produto(1, "pc gamer")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 2)
    assert str(carrinho) == str({1:2})

@pytest.mark.carrinho
# teste remover item
def test_remover_item():
    produto = Produto(1, "pc gamer")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 2)
    carrinho.remover_item(produto)
    assert str(carrinho) == str({})


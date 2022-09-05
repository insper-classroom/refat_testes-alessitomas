import json
import pytest
from classes.Pedido import Pedido
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho

import requests

@pytest.mark.pedido
# teste criacao de pedido
def test_criar_pedido():
    pessoa = PessoaFisica("CR7", "CR7@gmail.com", "123456789")
    carrinho = Carrinho()
    produto = Produto(1, "pc gamer")
    carrinho.adicionar_item(produto, 2)
    pedido = Pedido(pessoa, "rua 1", carrinho)
    assert str(pedido) == str(pessoa) + "," + "rua 1" + "," + str(carrinho)


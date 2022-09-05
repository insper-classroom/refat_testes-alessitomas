import json
import pytest
import requests
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento

import copy
@pytest.mark.main2
#  teste Cria uma pessoa 
def test_criar_pessoa():
    pessoa1 = PessoaFisica("Carlos", 'tiago@email.com', '524.222.452-6')
    assert str(pessoa1) == "Carlos, 524.222.452-6, tiago@email.com"

@pytest.mark.main2
# teste Cria  um endereço
def test_criar_endereco():
    end = Endereco('08320330', 430)
    assert str(end) == "SP,Rua Clemente Falcão,430, , 08320330"

@pytest.mark.main2
# teste Cria um outro endereço
def test_criar_endereco2():
    end = Endereco('04546042', 300)
    assert str(end) == "SP,Rua Quatá,300, , 04546042"

@pytest.mark.main2
# teste Adiciona endereço à pessoa
def test_adicionar_endereco():
    pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    end1 = Endereco('08320330', 430)
    pessoa1.adicionar_endereco('casa', end1)
    assert pessoa1.listar_enderecos()== ['casa']
    
@pytest.mark.main2
# teste Adiciona endereço à pessoa
def test_adicionar_endereco():
    pessoa1 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    end2 = Endereco('04546042', 300)
    end1 = Endereco('08320330', 430)
    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)
    assert pessoa1.listar_enderecos()== ['casa', 'trabalho']
    
@pytest.mark.main2
# teste Criando um produto
def test_criar_produto():
    sabonete = Produto("0010342967", "Sabonete")
    assert str(sabonete.nome) == "Sabonete"

@pytest.mark.main2
# teste Criando um carrinho
def test_criar_carrinho():
    carrinho = Carrinho()
    assert str(carrinho) == "{}"

@pytest.mark.main2
# teste adicionar item
def test_adicionar_item():
    produto = Produto(1, "pc gamer")
    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 2)
    assert str(carrinho) == str({1:2})

@pytest.mark.main2
def test_criar_pedido():
    
    pessoa = PessoaFisica("CR7", "CR7@gmail.com", "123456789")
    carrinho = Carrinho()
    produto = Produto(1, "pc gamer")
    carrinho.adicionar_item(produto, 2)
    pedido = Pedido(pessoa, "rua 1", carrinho)
    assert str(pedido) == str(pessoa) + "," + "rua 1" + "," + str(carrinho)

@pytest.mark.main2
def test_criar_pagamento():
    pessoa = PessoaFisica("CR7", "CR7@gmail.com", "123456789")
    carrinho = Carrinho()
    produto = Produto(1, "pc gamer")
    carrinho.adicionar_item(produto, 2)
    pedido = Pedido(pessoa, "rua 1", carrinho)
    pag = Pagamento(pedido)
    pago = pag.processa_pagamento()
    assert pago == True

@pytest.mark.main2
# print pedido
def test_print_pedido():
    pessoa1 = PessoaFisica("C", 't', '524.222.452-6')
    carrinho = Carrinho()
    produto = Produto(1, "pc")
    carrinho.adicionar_item(produto, 2)
    pedido = Pedido(pessoa1, "", carrinho)
    assert str(pedido) == 'C, 524.222.452-6, t,,{1: 2}'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Produto:
    all_produtos =[]
    # metedo/funcao (self) pertencente a classe
    def __init__(self, id_produto, nome=""):
        # atributos 
        self.id = id_produto
        self.__nome = nome
        Produto.all_produtos.append(self)
        
    # metodos para alterar atributos
    def set_id(self, id_novo=''):
        self.id = id_novo
    def get_id(self):
        return self.id
    def to_dict(self):
        return {'id':self.id, 'nome':self.__nome}
    
    def busca_nome(nome_teste):
        lista_nomes = []
        for obj in Produto.all_produtos:
            if obj.nome == nome_teste:
                lista_nomes.append(obj.nome)
        return lista_nomes
    
    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
            self.__nome = novo_nome
            

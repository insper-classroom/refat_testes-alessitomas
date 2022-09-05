#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    all_pessoa = []
    def __init__(self,nome='Visitante', email="", cpf=""):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}
        PessoaFisica.all_pessoa.append(self)

    # escolher o estilo de retorno
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,novo_email):
        self.__email= novo_email
        

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,novo_cpf):
        self.cpf = novo_cpf
    

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        
        self.__enderecos[apelido_endereco] = end
        return self.__enderecos

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]
        return self.__enderecos

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        all_end = []
        for end in self.__enderecos:
            
            all_end.append(end)
            print(end)
            
        return all_end
        
    
    def busca_nome(nome_teste):
        lista_nomes = []
        for obj in PessoaFisica.all_pessoa:
            if obj.nome == nome_teste:
                lista_nomes.append(obj.nome)
        return lista_nomes




    def __str__(self):
        return f'{self.nome}, {self.cpf}, {self.email}'
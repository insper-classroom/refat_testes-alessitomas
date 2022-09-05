#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

import requests
import json


class Endereco: 
    '''
    Endereço de uma pessoa ou conta.
    Esta classe possui overload de Contrutor, caso envie apenas três parametros será encaminhado
    para o contrutor que consulta o cep para encontrar o endereço.
    '''

    def __init__(self, cep, numero ,rua='', estado='', cidade='', complemento=''):

        if (rua == '') or (estado == '') or (cidade == ''):
            end_json = Endereco.consultar_cep(cep)
            self.rua = end_json['logradouro']
            self.estado = end_json['uf']
            self.cidade = end_json['localidade']
            self.numero = numero
            self.complemento = complemento
            self.cep = str(cep)

        else:

            self.rua = rua
            self.estado = estado
            self.cidade = cidade
            self.numero = int(numero)
            self.complemento = complemento
            self.cep = str(cep)

    # método

    @classmethod
    def consultar_cep(cls, cep):
        '''
        Metodo realiza a consulta do cep em uma api publica para obter informações
        como estado, cidade e rua
        '''
        
        # não aceitar cep não int ou string
        tipos = [int, str]
        if type(cep) not in tipos:
            return False

        # garantir que o cep seja feito de 8 digitos
        if len(str(cep)) != 8:
            return False

        # garantir que o cep seja feito de numeros
        for digito in str(cep):
            if digito not in '0123456789':
                return False
        # continuam existindo variaveis locais, nem tudo é propriedade de objeto

        # end point da API de consulta ao cep
        url_api = f'https://viacep.com.br/ws/{str(cep)}/json/'

        # Sem corpo na requisição
        # Não é necessario nenhum cabeçalho HTTP especial
        payload = {}
        headers = {}

        # requisição GET na url de pesquisa do cep. Doc.: https://viacep.com.br/
        response = requests.request("GET", url_api, headers=headers, data=payload)

        # converte a resposta json em dict
        json_resp = response.json()
        
        # garante que em caso de erro retorna False
        if 'erro' in json_resp.keys():
            return False
        
        return json_resp


    def __str__(self):
        return f'{self.estado},{self.rua},{self.numero}, {self.complemento}, {self.cep}'







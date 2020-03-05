# -*- coding: utf-8 -*-
import json
import re
from datetime import date

from json import JSONEncoder


class LeiauteEncoder(JSONEncoder):
    def default(self, o): # pylint: disable=E0202
        if isinstance(o, date):
            return o.isoformat()
        return o.__dict__


def normalize_spaces(s):
    return re.sub(r'[\n\r\s]{2,}', ' ', s)


def normalize_quotes(s):
    return s.replace('“','"').replace('”','"')


def remove_space(s):
    return re.sub(r'\n|\r|\s', '', s)


def extrair_parametros(s):
    return [remove_space(r[1:-1]) for r in re.findall(r'\[[^\]]+\]', s)]


class Leiaute(object):
    def __init__(self, tipo, versao, data_inicio, blocos, registros):
        self.tipo = tipo
        self.versao = versao
        self.data_inicio = data_inicio
        self.blocos = blocos
        self.registros = registros


class Bloco(object):
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return '<Bloco(%s, %s)>' % (self.nome, self.descricao)


class Registro(object):
    def __init__(self, codigo, nome, regras, nivel, ocorrencia, campos_chave):
        self.codigo = codigo
        self.nome = nome
        self.regras = regras
        self.nivel = nivel
        self.ocorrencia = ocorrencia
        self.campos_chave = campos_chave
        self.campos = []

    def __repr__(self):
        return '<Registro(%s, %s)>' % (self.codigo, self.nome)


class Campo(object):
    def __init__(self, indice, nome, descricao, tipo, tamanho, decimal, valores, obrigatorio, regras):
        try:
            self.indice = int(indice)
        except:
            self.indice = None
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo

        try:
            self.tamanho = int(tamanho)
        except:
            self.tamanho = None

        try:
            self.decimal = int(decimal)
        except:
            self.decimal = None

        self.valores = normalize_quotes(valores)
        self.obrigatorio = obrigatorio
        self.regras = regras

    def __repr__(self):
        return '<Campo(%s, %s)>' % (self.indice, self.nome)

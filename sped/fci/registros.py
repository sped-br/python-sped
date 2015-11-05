# -*- coding: utf-8 -*-

from ..campos import CampoFixo, CampoAlfanumerico, CampoNumerico
from ..registros import Registro
from ..erros import CampoError


class Registro0000(Registro):
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoAlfanumerico(2, 'CNPJ_CONTRIBUINTE'),
        CampoAlfanumerico(3, 'NOME_CONTRIBUINTE'),
        CampoFixo(4, 'VERSAO_LEIAUTE', '1.0'),
        CampoAlfanumerico(5, 'HASH CODE', obrigatorio=False, tamanho=47),
        CampoAlfanumerico(6, 'DT_RECEPCAO_ARQUIVO', obrigatorio=False,
                          tamanho=20),
        CampoAlfanumerico(7, 'COD_RECEPCAO_ARQUIVO', obrigatorio=False,
                          tamanho=36),
        CampoAlfanumerico(8, 'DT_VALIDACAO_ARQUIVO', obrigatorio=False,
                          tamanho=20),
        CampoAlfanumerico(9, 'IN_VALIDACAO_ARQUIVO', obrigatorio=False,
                          tamanho=20)
    ]


class Registro0001(Registro):
    campos = [
        CampoFixo(1, 'REG', "0001"),
        CampoAlfanumerico(2, 'TEXTO_PADRAO_UTF8', obrigatorio=True)
    ]


class Registro0010(Registro):
    campos = [
        CampoFixo(1, 'REG', '0010'),
        CampoAlfanumerico(2, 'CNPJ_CONTRIBUINTE', obrigatorio=True),
        CampoAlfanumerico(3, 'NOME_RAZAO_SOCIAL', obrigatorio=True),
        CampoAlfanumerico(4, 'INSCRICAO_ESTADUAL', obrigatorio=True),
        CampoAlfanumerico(5, 'ENDERECO_ESTABELECIMENTO', obrigatorio=True),
        CampoNumerico(6, 'CEP', obrigatorio=True),
        CampoAlfanumerico(7, 'MUNICIPIO', obrigatorio=True),
        CampoAlfanumerico(8, 'UF', obrigatorio=True)
    ]


class Registro0990(Registro):
    campos = [
        CampoFixo(1, 'REG', '0990'),
        CampoNumerico(2, 'QUANTIDADE_LINHAS')
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)


class Registro5001(Registro):
    campos = [
        CampoFixo(1, 'REG', '5001'),
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)


class Registro5020(Registro):
    campos = [
        CampoFixo(1, 'REG', '5020'),
        CampoAlfanumerico(2, 'NOME_MERCADORIA', obrigatorio=True, tamanho=255),
        CampoNumerico(3, 'CODIGO_NCM', obrigatorio=True),
        CampoAlfanumerico(4, 'CODIGO_MERCADORIA', obrigatorio=True,
                          tamanho=50),
        CampoNumerico(5, 'CODIGO_GTIN'),
        CampoAlfanumerico(6, 'UNIDADE_MERCADORIA', tamanho=6,
                          obrigatorio=True),
        CampoNumerico(7, 'VALOR_SAIDA_MERCADORIA_INTERESTADUAL', precisao=2,
                      obrigatorio=True),
        CampoNumerico(8, 'VALOR_PARCELA_IMPORTADA_EXTERIOR', precisao=2,
                      obrigatorio=True),
        CampoNumerico(9, 'CONTEUDO_IMPORTACAO_CI', precisao=2,
                      obrigatorio=True),
        CampoAlfanumerico(10, 'CODIGO_FCI', obrigatorio=False, tamanho=36),
        CampoAlfanumerico(11, 'IN_VALIDACAO_FICHA', obrigatorio=False,
                          tamanho=20)
    ]


class Registro5990(Registro):
    campos = [
        CampoFixo(1, 'REG', '5990'),
        CampoNumerico(2, 'QUANTIDADE_LINHAS'),
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)


class Registro9001(Registro):
    campos = [
        CampoFixo(1, 'REG', '9001')
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)


class Registro9900(Registro):
    campos = [
        CampoFixo(1, 'REG', '9900'),
        CampoAlfanumerico(2, 'REG_SER_TOTALIZADO', tamanho=4),
        CampoNumerico(3, 'QUANTIDADE_LINHAS_REGISTRO_ANTERIOR')
    ]


class Registro9990(Registro):
    campos = [
        CampoFixo(1, 'REG', '9990'),
        CampoNumerico(2, 'QUANTIDADE_LINHAS')
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)


class Registro9999(Registro):
    campos = [
        CampoFixo(1, 'REG', '9999'),
        CampoNumerico(2, 'QUANTIDADE_LINHAS_ARQUIVO')
    ]

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 1)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)

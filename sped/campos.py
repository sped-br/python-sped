import re

from datetime import date
from datetime import datetime
from decimal import Decimal

from .erros import *


class Campo(object):
    """
    Classe base para definição de um campo de um registro do SPED.

    >>> campo = Campo(1, 'TESTE', True)
    >>> campo
    [Campo(1, 'TESTE')]
    >>> campo.indice
    1
    >>> campo.nome
    'TESTE'
    >>> campo.obrigatorio
    True
    """
    def __init__(self, indice, nome, obrigatorio=False):
        self._indice = indice
        self._nome = nome
        self._obrigatorio = obrigatorio

    def __repr__(self):
        return "[{0}({1}, {2!r})]".format(self.__class__.__name__, self._indice, self._nome)

    @property
    def indice(self):
        return self._indice

    @property
    def nome(self):
        return self._nome

    @property
    def obrigatorio(self):
        return self._obrigatorio

    def get(self, registro):
        return registro.valores[self._indice] or None

    def set(self, registro, valor):
        registro.valores[self._indice] = valor or ''


class CampoFixo(Campo):
    """
    Classe base para definição de um campo de um registro do SPED.

    >>> campo = CampoFixo(1, 'REG', '0000')
    >>> campo
    [CampoFixo(1, 'REG')]
    >>> campo.indice
    1
    >>> campo.nome
    'REG'
    >>> campo.obrigatorio
    True
    >>> campo.valor
    '0000'
    """
    def __init__(self, indice, nome, valor):
        super().__init__(indice, nome, True)
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def get(self, registro):
        return self._valor

    def set(self, registro, valor):
        raise CampoFixoError(registro, self.nome)


class CampoAlfanumerico(Campo):
    def __init__(self, indice, nome, obrigatorio=False, tamanho=255):
        super().__init__(indice, nome, obrigatorio)
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def set(self, registro, valor):
        valor = valor or ''
        valor = valor[:self._tamanho]
        super().set(registro, valor)


class CampoNumerico(Campo):
    def __init__(self, indice, nome, obrigatorio=False, precisao=0, minimo=0, maximo=1000):
        super().__init__(indice, nome, obrigatorio)
        self._precisao = precisao
        self._minimo = minimo
        self._maximo = maximo

    @property
    def precisao(self):
        return self._precisao

    @property
    def minimo(self):
        return self._minimo

    @property
    def maximo(self):
        return self._maximo

    def get(self, registro):
        valor = super().get(registro)
        if not valor:
            return None
        return Decimal(valor.replace(',', '.'))

    def set(self, registro, valor):
        if not valor:
            super().set(registro, None)
        elif isinstance(valor, Decimal) or isinstance(valor, float):
            super().set(registro, (('%.' + str(self._precisao) + 'f') % valor).replace('.', ','))
        elif isinstance(valor, int):
            super().set(registro, str(valor))
        else:
            raise FormatoInvalidoError(registro, self.nome)


class CampoData(Campo):
    def __init__(self, indice, nome, obrigatorio=False):
        super().__init__(indice, nome, obrigatorio)

    def get(self, registro):
        valor = super().get(registro)
        if not valor:
            return None
        return datetime.strptime(valor, '%d%m%Y').date()

    def set(self, registro, valor):
        if not valor:
            super().set(registro, None)
        elif isinstance(valor, date):
            super().set(registro, valor.strftime('%d%m%Y'))
        else:
            raise FormatoInvalidoError(registro, self.nome)


class CampoRegex(Campo):
    def __init__(self, indice, nome, obrigatorio=False, regex=None):
        super().__init__(indice, nome, obrigatorio)
        self._regex = re.compile('^' + regex + '$')

    def set(self, registro, valor):
        if not valor or self._regex.match(valor):
            super().set(registro, valor)
        else:
            raise FormatoInvalidoError(registro, self.nome)

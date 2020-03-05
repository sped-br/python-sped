# -*- coding: utf-8 -*-

from .campos import CampoData
from .campos import CampoFixo
from .campos import CampoRegex
from .erros import CampoError
from .erros import CampoInexistenteError
from .erros import RegistroError
import itertools

class Registro(object):
    """
    Classe abstrata para a manipulação dos registros.

    >>> class RegistroTest(Registro):
    ...     campos = [CampoFixo(1, 'REG', 'TEST'),
    ...               CampoData(2, 'DT_INI'),
    ...               CampoData(3, 'DT_FIM'),
    ...               CampoRegex(4, 'RETIFICADORA', obrigatorio=True, regex='[SN]'),]
    >>> line = '|ERRO|01012015||N|'
    >>> r = RegistroTest(line) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    CampoError: RegistroTest -> REG
    >>> line = '|TEST|01012015||N|'
    >>> r = RegistroTest(line)
    >>> r.REG
    'TEST'
    >>> r.REG = '0000' # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    CampoFixoError: RegistroTest -> REG
    >>> r.DT_INI
    datetime.date(2015, 1, 1)
    >>> r.DT_FIM
    >>> from datetime import date
    >>> r.DT_INI = date(2014, 2, 1)
    >>> r.DT_INI
    datetime.date(2014, 2, 1)
    >>> r.DT_INI = '01012014' # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    FormatoInvalidoError: RegistroTest -> DT_INI
    >>> r.DT_INI = ''
    >>> r.DT_INI
    >>> r.DT_INI = None
    >>> r.DT_INI
    >>> r.CAMPO_INEXISTENTE = '' # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    CampoInexistenteError: RegistroTest -> CAMPO_INEXISTENTE
    >>> r.CAMPO_INEXISTENTE # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    CampoInexistenteError: RegistroTest -> CAMPO_INEXISTENTE
    >>> r.RETIFICADORA
    'N'
    >>> r.RETIFICADORA = 'S'
    >>> r.RETIFICADORA
    'S'
    >>> r.RETIFICADORA = '0' # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    FormatoInvalidoError: RegistroTest -> RETIFICADORA
    """
    campos = []
    contador_de_linhas = itertools.count(1)

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 2)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
            self._numero_da_linha = None
        else:
            #self._valores = line.split('|')
            self._valores = [valor.strip() for valor in line.split('|')]
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)
            # Inicializar contador na leitura do registro de abertura '0000'
            # if self.__class__.__name__ == 'Registro0000':
            if self._valores[1] == '0000':
                Registro.contador_de_linhas = itertools.count(1)
            # Informação do número da linha do arquivo sped
            self._numero_da_linha = next(Registro.contador_de_linhas)

    @property
    def numero_da_linha(self):
        return self._numero_da_linha

    @property
    def valores(self):
        return self._valores

    def __getitem__(self, key):
        campo = ([c for c in self.campos if c.indice == key or c.nome == key] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, key)
        return campo.get(self)

    def __setitem__(self, key, value):
        campo = ([c for c in self.campos if c.indice == key or c.nome == key] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, key)
        campo.set(self, value)

    def __getattr__(self, name):
        campo = ([c for c in self.campos if c.nome == name] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, name)
        return campo.get(self)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Registro, self).__setattr__(name, value)
            return
        campo = ([c for c in self.campos if c.nome == name] or [None])[0]
        if not campo:
            raise CampoInexistenteError(self, name)
        campo.set(self, value)

    def as_line(self):
        return str(self)

    def __str__(self):
        return '|'.join(self._valores)

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__module__, self.__class__.__name__)

class RegistroIndefinido(Registro):
    def __init__(self):
        super(RegistroIndefinido, self).__init__()
        raise RegistroError(self)

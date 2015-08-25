# -*- coding: utf-8 -*-

from .campos import CampoData
from .campos import CampoFixo
from .campos import CampoRegex
from .erros import CampoError
from .erros import CampoInexistenteError


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

    def __init__(self, line=None):
        if not line:
            self._valores = [''] * (len(self.campos) + 2)
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    self._valores[c.indice] = c.valor
        else:
            self._valores = line.split('|')
            for c in self.campos:
                if isinstance(c, CampoFixo):
                    if self._valores[c.indice] != c.valor:
                        raise CampoError(self, c.nome)

    @property
    def campos(self):
        return self.__class__.campos

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
        return '|'.join(self._valores)

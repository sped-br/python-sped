# -*- coding: utf-8 -*-

from .registros import Registro

class Bloco(object):
    def __init__(self, nome=''):
        self._nome = nome
        self._registros = []

    def __repr__(self):
        return '<%s.%s(%s)>' % (self.__class__.__module__,
                                self.__class__.__name__, self._nome)

    @property
    def abertura(self):
        return self.registro_abertura

    @property
    def encerramento(self):
        return self.registro_encerramento

    @property
    def registros(self):
        return [self.abertura] + self._registros + [self.encerramento]

    def add(self, registro):
        self._registros.append(registro)

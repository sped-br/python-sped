# -*- coding: utf-8 -*-

from .registros import Registro

class Bloco(object):
    def __init__(self, nome=''):
        self._nome = nome
        self._registros = []
        #self.registro_abertura = Registro()
        #self.registro_encerramento = Registro()

    def __repr__(self):
        return '<%s.%s(%s)>' % (self.__class__.__module__,
                                self.__class__.__name__, self._nome)

    @property
    def abertura(self):
        # Define o indicador de movimento ou dados
        return self.registro_abertura

    @property
    def encerramento(self):
        # Define a quantidade de registros
        return self.registro_encerramento

    @property
    def registros(self):
        return [self.abertura] + self._registros + [self.encerramento]

    def add(self, registro):
        # Não adiciona o registro de abertura e fechamento
        self._registros.append(registro)

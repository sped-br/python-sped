# -*- coding: utf-8 -*-

from .registros import Registro


class Bloco(object):
    def __init__(self, nome=''):
        self._nome = nome
        self._registros = []
        self.registro_abertura = Registro()
        self.registro_encerramento = Registro()

    def __repr__(self):
        return f'<{self.__class__.__module__}.{self.__class__.__name__}({self._nome})>'

    @property
    def abertura(self):
        # Define o indicador de movimento ou dados
        self.registro_abertura[2] = '0' if self._registros else '1'
        print(self.registro_abertura)
        print(self.registro_abertura[2])
        return self.registro_abertura

    @property
    def encerramento(self):
        # Define a quantidade de registros
        if self.registro_abertura.REG[0] == '0' or self.registro_abertura.REG[0] == '9':
            self.registro_encerramento[2] = len(self._registros) + 3
        else:
            self.registro_encerramento[2] = len(self._registros) + 2
        return self.registro_encerramento

    @property
    def registros(self):
        return [self.abertura] + self._registros + [self.encerramento]

    def add(self, registro):
        # Não adiciona o registro de abertura e fechamento
        if not registro.__class__ == self.registro_abertura.__class__ and \
           not registro.__class__ == self.registro_encerramento.__class__:
            self._registros.append(registro)

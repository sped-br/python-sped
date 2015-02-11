# -*- coding: utf-8 -*-


class Bloco(object):
    registro_abertura = None
    registro_fechamento = None

    def __init__(self):
        self._registros = []

    @property
    def abertura(self):
        registro = self.__class__.registro_abertura()
        # Define o indicador de movimento ou dados
        registro[2] = '0' if self._registros else '1'
        return registro

    @property
    def fechamento(self):
        registro = self.__class__.registro_fechamento()
        # Define a quantidade de registros
        registro[2] = len(self._registros) + 2
        return registro

    @property
    def registros(self):
        return [self.abertura] + self._registros + [self.fechamento]

    def add(self, registro):
        # Não adiciona o registro de abertura e fechamento
        if not registro.__class__ == self.__class__.registro_abertura and \
           not registro.__class__ == self.__class__.registro_fechamento:
            self._registros.append(registro)

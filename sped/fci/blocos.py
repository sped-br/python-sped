# -*- coding: utf-8 -*-

from ..blocos import Bloco

from .registros import Registro0001
from .registros import Registro0990
from .registros import Registro5001
from .registros import Registro5990
from .registros import Registro9001
from .registros import Registro9990


class Bloco0(Bloco):
    """
    Cabeçalho da FCI: Identificação do contribuinte
    """
    registro_abertura = Registro0001
    registro_fechamento = Registro0990

    @property
    def abertura(self):
        registro = self.__class__.registro_abertura()
        return registro

    @property
    def fechamento(self):
        registro = self.__class__.registro_fechamento()
        # Define a quantidade de registros
        registro[2] = len(self._registros) + 3
        return registro

    def add(self, registro):
        self._registros.append(registro)


class Bloco5(Bloco):
    registro_abertura = Registro5001
    registro_fechamento = Registro5990

    @property
    def abertura(self):
        registro = self.__class__.registro_abertura()
        return registro


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001
    registro_fechamento = Registro9990

    @property
    def abertura(self):
        registro = self.__class__.registro_abertura()
        return registro

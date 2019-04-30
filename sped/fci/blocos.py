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
    registro_abertura = Registro0001()
    registro_encerramento = Registro0990()

    @property
    def abertura(self):
        return self.registro_abertura

    @property
    def fechamento(self):
        # Define a quantidade de registros
        self.registro_encerramento[2] = len(self._registros) + 3
        return self.registro_encerramento

    def add(self, registro):
        self._registros.append(registro)


class Bloco5(Bloco):
    registro_abertura = Registro5001()
    registro_encerramento = Registro5990()

    @property
    def abertura(self):
        return self.registro_abertura


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001()
    registro_encerramento = Registro9990()

    @property
    def abertura(self):
        return self.registro_abertura

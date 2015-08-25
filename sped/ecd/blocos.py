# -*- coding: utf-8 -*-

from ..blocos import Bloco
from .registros import Registro0001
from .registros import Registro0990
from .registros import RegistroI001
from .registros import RegistroI990
from .registros import RegistroJ001
from .registros import RegistroJ990
from .registros import Registro9001
from .registros import Registro9990


class Bloco0(Bloco):
    """
    Abertura, Identificação e Referências
    """
    registro_abertura = Registro0001
    registro_fechamento = Registro0990

    @property
    def fechamento(self):
        registro = Bloco.fechamento.fget(self)
        registro[2] += 1
        return registro


class BlocoI(Bloco):
    """
    Lançamentos Contábeis
    """
    registro_abertura = RegistroI001
    registro_fechamento = RegistroI990


class BlocoJ(Bloco):
    """
    Demonstrações Contábeis
    """
    registro_abertura = RegistroJ001
    registro_fechamento = RegistroJ990


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001
    registro_fechamento = Registro9990

    @property
    def fechamento(self):
        registro = super(Bloco9, self).fechamento
        registro[2] += 1
        return registro

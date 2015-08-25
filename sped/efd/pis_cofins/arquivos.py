# -*- coding: utf-8 -*-

from ...arquivos import ArquivoDigital
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import Bloco1
from .blocos import Bloco9
from .blocos import BlocoA
from .blocos import BlocoC
from .blocos import BlocoD
from .blocos import BlocoF
from .blocos import BlocoI
from .blocos import BlocoM
from .blocos import BlocoP
from .registros import Registro0000
from .registros import Registro9999


class ArquivoDigital(ArquivoDigital):
    registro_abertura = Registro0000
    registro_fechamento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super(ArquivoDigital, self).__init__()
        self._blocos['0'] = Bloco0()
        self._blocos['A'] = BlocoA()
        self._blocos['C'] = BlocoC()
        self._blocos['D'] = BlocoD()
        self._blocos['F'] = BlocoF()
        self._blocos['I'] = BlocoI()
        self._blocos['M'] = BlocoM()
        self._blocos['P'] = BlocoP()
        self._blocos['1'] = Bloco1()
        self._blocos['9'] = Bloco9()

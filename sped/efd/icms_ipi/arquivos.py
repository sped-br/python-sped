# -*- coding: utf-8 -*-

from ...arquivos import ArquivoDigital
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import BlocoC
from .blocos import BlocoD
from .blocos import BlocoE
from .blocos import BlocoG
from .blocos import BlocoH
from .blocos import BlocoK
from .blocos import Bloco1
from .blocos import Bloco9
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
        self._blocos['C'] = BlocoC()
        self._blocos['D'] = BlocoD()
        self._blocos['E'] = BlocoE()
        self._blocos['G'] = BlocoG()
        self._blocos['H'] = BlocoH()
        self._blocos['K'] = BlocoK()
        self._blocos['1'] = Bloco1()
        self._blocos['9'] = Bloco9()

# -*- coding: utf-8 -*-

from ..arquivos import ArquivoDigital
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import BlocoC
from .blocos import BlocoE
from .blocos import BlocoJ
from .blocos import BlocoK
from .blocos import BlocoL
from .blocos import BlocoM
from .blocos import BlocoN
from .blocos import BlocoP
from .blocos import BlocoT
from .blocos import BlocoU
from .blocos import BlocoX
from .blocos import BlocoY
from .blocos import Bloco9
from .registros import Registro0000
from .registros import Registro9999


class ArquivoDigital(ArquivoDigital):
    registro_abertura = Registro0000
    registro_fechamento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super().__init__()
        self._blocos['0'] = Bloco0()
        self._blocos['C'] = BlocoC()
        self._blocos['E'] = BlocoE()
        self._blocos['J'] = BlocoJ()
        self._blocos['K'] = BlocoK()
        self._blocos['L'] = BlocoL()
        self._blocos['M'] = BlocoM()
        self._blocos['N'] = BlocoN()
        self._blocos['P'] = BlocoP()
        self._blocos['T'] = BlocoT()
        self._blocos['U'] = BlocoU()
        self._blocos['X'] = BlocoX()
        self._blocos['Y'] = BlocoY()
        self._blocos['9'] = Bloco9()

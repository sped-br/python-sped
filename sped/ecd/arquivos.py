# -*- coding: utf-8 -*-

from ..arquivos import ArquivoDigital
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import BlocoI
from .blocos import BlocoJ
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
        self._blocos['I'] = BlocoI()
        self._blocos['J'] = BlocoJ()
        self._blocos['9'] = Bloco9()

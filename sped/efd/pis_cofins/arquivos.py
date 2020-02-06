# -*- coding: utf-8 -*-

from ... import arquivos
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

class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        #print(f'efd.pis_cofins.arquivos.py Inicio: {self.__class__.__name__ = } ; {self.__dict__ = }')
        super(ArquivoDigital, self).__init__()
        #print(f'efd.pis_cofins.arquivos.py Ler Bloco0: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['0'] = Bloco0()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoA: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['A'] = BlocoA()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoC: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['C'] = BlocoC()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoD: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['D'] = BlocoD()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoF: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['F'] = BlocoF()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoI: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['I'] = BlocoI()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoM: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['M'] = BlocoM()
        #print(f'efd.pis_cofins.arquivos.py Ler BlocoP: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['P'] = BlocoP()
        #print(f'efd.pis_cofins.arquivos.py Ler Bloco1: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['1'] = Bloco1()
        #print(f'efd.pis_cofins.arquivos.py Ler Bloco9: {self.__class__.__name__ = } ; {self.__dict__ = }')
        self._blocos['9'] = Bloco9()
        #print(f'efd.pis_cofins.arquivos.py Fim: {self.__class__.__name__ = } ; {self.__dict__ = }')

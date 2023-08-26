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
from .registros import Registro9900
from .registros import Registro9999


class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
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

    def prepare(self):
        bloco_9 = self._blocos['9'] = Bloco9()
        for bloco in self._blocos.values():
            regs = {}
            for reg in bloco.registros:
                if reg.REG not in regs:
                    regs[reg.REG] = 0
                regs[reg.REG] += 1
            total = sum([x for x in regs.values()])
            bloco.registro_abertura.IND_MOV = '1' if total <= 2 else '0'
            if bloco == self._blocos['0']:
                bloco.registro_encerramento.QTD_LIN_0 = total + 1
                regs['0000'] = 1
            if bloco == self._blocos['A']:
                bloco.registro_encerramento.QTD_LIN_A = total
            if bloco == self._blocos['C']:
                bloco.registro_encerramento.QTD_LIN_C = total
            if bloco == self._blocos['D']:
                bloco.registro_encerramento.QTD_LIN_D = total
            if bloco == self._blocos['F']:
                bloco.registro_encerramento.QTD_LIN_F = total
            if bloco == self._blocos['I']:
                bloco.registro_encerramento.QTD_LIN_I = total
            if bloco == self._blocos['M']:
                bloco.registro_encerramento.QTD_LIN_M = total
            if bloco == self._blocos['P']:
                bloco.registro_encerramento.QTD_LIN_P = total
            if bloco == self._blocos['1']:
                bloco.registro_encerramento.QTD_LIN_1 = total
            if bloco == self._blocos['9']:
                bloco.registro_encerramento.QTD_LIN_9 = total + 5
            if bloco == bloco_9:
                regs['9999'] = 1
                regs['9900'] += len(regs.keys())
            for reg in regs.keys():
                registro = Registro9900()
                registro.REG_BLC = reg
                registro.QTD_REG_BLC = str(regs[reg])
                bloco_9.add(registro)

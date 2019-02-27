# -*- coding: utf-8 -*-

from .. import arquivos
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import BlocoI
from .blocos import BlocoJ
from .blocos import Bloco9
from .registros import Registro0000
from .registros import Registro9900
from .registros import Registro9999
from .registros import RegistroI030
from .registros import RegistroJ900


class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super(ArquivoDigital, self).__init__()
        self._blocos['0'] = Bloco0('0')
        self._blocos['I'] = BlocoI('I')
        self._blocos['J'] = BlocoJ('J')
        self._blocos['9'] = Bloco9('9')

    def prepare(self):
        bloco_9 = self._blocos['9'] = Bloco9('9')

        for bloco in self._blocos.values():
            regs = {}
            for reg in bloco.registros:
                if reg.REG not in regs:
                    regs[reg.REG] = 0
                regs[reg.REG] += 1
            if bloco == self._blocos['0']:
                bloco.registro_encerramento.QTD_LIN_0 = sum(
                    [x for x in regs.values()]) + 1
                regs['0000'] = 1
            if bloco == self._blocos['I']:
                bloco.registro_encerramento.QTD_LIN_I = sum(
                    [x for x in regs.values()])
            if bloco == self._blocos['J']:
                bloco.registro_encerramento.QTD_LIN_J = sum(
                    [x for x in regs.values()])
            if bloco == bloco_9:
                regs['9999'] = 1
                regs['9900'] += len(regs.keys())
            for reg in regs.keys():
                registro = Registro9900()
                registro.REG_BLC = reg
                registro.QTD_REG_BLC = regs[reg]
                bloco_9.add(registro)

            if bloco == self._blocos['9']:
                bloco.registro_encerramento.QTD_LIN_9 = sum(
                    [x for x in regs.values()])

        reg_count = 2
        for bloco in self._blocos.values():
            reg_count += len(bloco.registros)

        encerramentoI = [x for x in self._blocos['I'].registros
                         if isinstance(x, RegistroI030)]
        encerramentoI[0].QTD_LIN = reg_count

        encerramentoJ = [x for x in self._blocos['J'].registros
                         if isinstance(x, RegistroJ900)]
        encerramentoJ[0].QTD_LIN = reg_count

        # self._blocos['J'].registros[1].QTD_LIN = reg_count
        self._registro_encerramento.QTD_LIN = reg_count

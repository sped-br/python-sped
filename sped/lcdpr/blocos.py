# -*- coding: utf-8 -*-

from ..blocos import Bloco
from .registros import RegistroQ100
from .registros import RegistroQ200

class Bloco0(Bloco):
    """
    Abertura e Identificação
    """
    registro_abertura = None
    registro_encerramento = None


class BlocoQ(Bloco):
    """
    Demonstrativo do Resultado da Atividade Rural
    """
    registro_abertura = None
    registro_encerramento = None

    @property
    def registros(self):
        regs = []

        if self.abertura is not None:
            regs.append(self.abertura)

        regs = regs + [r for r in self._registros if isinstance(r, RegistroQ100)]
        regs = regs + [r for r in self._registros if isinstance(r, RegistroQ200)]

        if self.encerramento is not None:
            regs.append(self.encerramento)

        return regs


class Bloco9(Bloco):
    """
    Identificação do Contador e Encerramento do Arquivo Digital
    """
    registro_abertura = None
    registro_encerramento = None


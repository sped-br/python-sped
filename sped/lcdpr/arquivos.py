# -*- coding: utf-8 -*-

from sped import arquivos
from sped.lcdpr import blocos
from sped.lcdpr import registros
from sped.lcdpr.blocos import Bloco0
from sped.lcdpr.blocos import BlocoQ
from sped.lcdpr.blocos import Bloco9
from sped.lcdpr.registros import Registro0000
from sped.lcdpr.registros import Registro9999


class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super(ArquivoDigital, self).__init__()
        self._blocos['0'] = Bloco0()
        self._blocos['Q'] = BlocoQ()
        self._blocos['9'] = Bloco9()

    def prepare(self):
        reg_count = 0

        for bloco in self._blocos.values():
            reg_count += len(bloco.registros)

        self.registro_encerramento._numero_linhas = reg_count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

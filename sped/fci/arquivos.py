# -*- coding: utf-8 -*-

from ..arquivos import ArquivoDigital
from . import blocos
from . import registros
from .blocos import Bloco0
from .blocos import Bloco5
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
        self._blocos['5'] = Bloco5()
        self._blocos['9'] = Bloco9()

    def read_registro(self, line):

        # caso o usuario insira linha sem pip
        pipe = '|' if line[0] != '|' else ''
        line = pipe + line
        reg_id = line.split('|')[1]

        try:
            registro_class = \
                getattr(self.__class__.registros, 'Registro' + reg_id)
        except AttributeError:
            raise RuntimeError(u"Arquivo inválido para FCI")

        registro = registro_class(line)
        if registro.__class__ == self.__class__.registro_abertura:
            self._registro_abertura = registro
        elif registro.__class__ == self.__class__.registro_fechamento:
            self._registro_fechamento = registro
        elif registro.__class__ == \
                self.__class__.blocos.Bloco0.registro_abertura:
            self.blocos.Bloco0.abertura = registro
        else:
            if reg_id == '9900' and (len(self._blocos['9'].registros)) == 4:
               registro._valores[3] = str((len(self._blocos['5'].registros))-2)

            bloco_id = reg_id[0]
            bloco = self._blocos[bloco_id]
            bloco.add(registro)

    def write_to(self, buffer):

        self._adiciona_registro_fixo_bloco9()

        linha_abertura = self._registro_abertura.as_line()[1:]
        buffer.write(linha_abertura + u'\r\n')
        reg_count = 2
        for key in self._blocos.keys():
            bloco = self._blocos[key]
            reg_count += len(bloco.registros)
            for r in bloco.registros:
                a = r.as_line()
                a = a[1:]
                buffer.write(a + u'\r\n')

        self._registro_fechamento[2] = reg_count
        linha_fechamento = self._registro_fechamento.as_line()[1:]
        buffer.write(linha_fechamento + u'\r\n')

    def _adiciona_registro_fixo_bloco9(self):
        self.read_registro('|9900|0000|1')
        self.read_registro('|9900|0010|1')
        self.read_registro('|9900|5020|')

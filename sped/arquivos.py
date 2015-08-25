# -*- coding: utf-8 -*-


from collections import OrderedDict
from io import StringIO


class ArquivoDigital(object):
    registro_abertura = None
    registro_fechamento = None
    registros = None
    blocos = None

    def __init__(self):
        self._registro_abertura = self.__class__.registro_abertura()
        self._registro_fechamento = self.__class__.registro_fechamento()
        self._blocos = OrderedDict()

    def readfile(self, filename):
        with open(filename) as file:
            for line in [line.rstrip('\r\n') for line in file]:
                self.read_registro(line)

    def read_registro(self, line):
        reg_id = line.split('|')[1]

        try:
            registro_class = getattr(self.__class__.registros, 'Registro' + reg_id)
        except AttributeError:
            raise RuntimeError("Arquivo inválido para EFD - PIS/COFINS")

        registro = registro_class(line)

        if registro.__class__ == self.__class__.registro_abertura:
            self._registro_abertura = registro
        elif registro.__class__ == self.__class__.registro_fechamento:
            self._registro_fechamento = registro
        else:
            bloco_id = reg_id[0]
            bloco = self._blocos[bloco_id]
            bloco.add(registro)

    def write_to(self, buffer):
        buffer.write(self._registro_abertura.as_line() + u'\r\n')
        reg_count = 2
        for key in self._blocos.keys():
            bloco = self._blocos[key]
            reg_count += len(bloco.registros)
            for r in bloco.registros:
                buffer.write(r.as_line() + u'\r\n')

        self._registro_fechamento[2] = reg_count

        buffer.write(self._registro_fechamento.as_line() + u'\r\n')

    def getstring(self):
        buffer = StringIO()
        self.write_to(buffer)
        return buffer.getvalue()

# -*- coding: utf-8 -*-


from collections import OrderedDict
from io import StringIO

from .registros import RegistroIndefinido


class ArquivoDigital(object):
    registros = None
    blocos = None

    registro_abertura = RegistroIndefinido
    registro_encerramento = RegistroIndefinido

    def __init__(self):
        self._registro_abertura = self.registro_abertura()
        self._registro_encerramento = self.registro_encerramento()
        self._blocos = OrderedDict()

    def readfile(self, filename):
        with open(filename) as spedfile:
            for line in [line.rstrip('\r\n') for line in spedfile]:
                self.read_registro(line.decode('utf8'))

    def read_registro(self, line):
        reg_id = line.split('|')[1]

        try:
            registro_class = getattr(self.__class__.registros,
                                     'Registro' + reg_id)
        except AttributeError:
            raise RuntimeError(u"Arquivo inválido para EFD - PIS/COFINS")

        registro = registro_class(line)

        if registro.__class__ == self.__class__.registro_abertura:
            self._registro_abertura = registro
        elif registro.__class__ == self.__class__.registro_encerramento:
            self._registro_encerramento = registro
        else:
            bloco_id = reg_id[0]
            bloco = self._blocos[bloco_id]
            bloco.add(registro)

    def write_to(self, buff):
        buff.write(self._registro_abertura.as_line() + u'\r\n')
        reg_count = 2
        for key in self._blocos.keys():
            bloco = self._blocos[key]
            reg_count += len(bloco.registros)
            for registro in bloco.registros:
                buff.write(registro.as_line() + u'\r\n')

        self._registro_encerramento[2] = reg_count

        buff.write(self._registro_encerramento.as_line() + u'\r\n')

    def getstring(self):
        buff = StringIO()
        self.write_to(buff)
        return buff.getvalue()

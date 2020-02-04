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

    def readfile(self, filename, codificacao='utf-8', verbose=None):
        with open(filename, 'r', encoding=codificacao) as spedfile: # encoding='utf-8', 'latin-1'
            for line in [line.strip() for line in spedfile]:
                reg = self.read_registro(line)
                # Ler arquivo até a última linha válida da EFD que contém o registro |9999|.
                if reg == '9999':
                    break
        if verbose:
            print(f"Successfully read the file: \n'{filename}'")

    def read_registro(self, line):
        reg_id = line.split('|')[1].upper() # 'c170' --> 'C170'
        
        try:
            registro_class = getattr(self.__class__.registros, 'Registro' + reg_id)
        except AttributeError:
            raise RuntimeError(u"Arquivo inválido para EFD - PIS/COFINS")

        registro = registro_class(line)
        bloco_id = reg_id[0]
        bloco = self._blocos[bloco_id]

        if registro.__class__ == self.__class__.registro_abertura:
			# Atualizar o registro de abertura 0000
            self._registro_abertura = registro
        elif registro.__class__ == self.__class__.registro_encerramento:
			# Atualizar o registro de encerramento 9999
            self._registro_encerramento = registro
        elif registro.__class__ == bloco.registro_abertura.__class__:
			# Atualizar os registros de abertura: 0001, A001, C001, ...
            bloco.registro_abertura = registro           
        elif registro.__class__ == bloco.registro_encerramento.__class__:
			# Atualizar os registros de encerramento: 0990, A990, C990, ...
            bloco.registro_encerramento = registro
        else:
			# Adicionar novos registros a cada linha obtida de filename
            bloco.add(registro)
                    
        return reg_id

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

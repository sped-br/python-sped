# -*- coding: utf-8 -*-

import re
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
        sucesso = False
        with open(filename, 'r', encoding=codificacao) as spedfile: # encoding='utf-8', 'latin-1'
            for line in [line.strip() for line in spedfile]:
                # a simple way to remove multiple spaces in a string
                line = re.sub('\s{2,}', ' ', line)
                # Em algumas EFDs foram encontrados registros digitados incorretamente em minúsculo.
                # Por exemplo, o registro 'c491' deve ser corrigido para 'C491'.
                line = line[:6].upper() + line[6:] # line = '|c491|...' --> '|C491|...'
                regt = self.read_registro(line)
                # Verificar se foi lido o arquivo SPED até a última linha válida que contém o registro '9999'.
                if regt.__class__ == self.__class__.registro_encerramento:
                    sucesso = True
                    break
        if not sucesso:
            raise RuntimeError(u"\nOcorreu uma falha ao ler o arquivo: '%s'.\n" % filename)
        elif verbose:
            print(u"O arquivo SPED '%s' foi lido com sucesso.\n" % filename)

    def read_registro(self, line):
        reg_id = line.split('|')[1]
        
        try:
            registro_class = getattr(self.__class__.registros, 'Registro' + reg_id)
        except AttributeError:
            raise RuntimeError(u"Arquivo inválido para EFD - PIS/COFINS. Registro: %s" % reg_id)

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

        return registro

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

# -*- coding: utf-8 -*-

from .. import arquivos
from . import registros
from . import blocos
from .blocos import Bloco0
from .blocos import Bloco5
from .blocos import Bloco9
from .registros import Registro0000
from .registros import Registro9999


class ArquivoDigital(arquivos.ArquivoDigital):
    registro_abertura = Registro0000
    registro_encerramento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super(ArquivoDigital, self).__init__()
        self._blocos['0'] = Bloco0()
        self._blocos['5'] = Bloco5()
        self._blocos['9'] = Bloco9()

        utf = (u"0001|Texto em caracteres UTF-8: (dígrafo BR)'ção',(dígrafo "
               u"espanhol-enhe)'ñ',(trema)'Ü',(ordinais)'ªº',(ligamento s+z a"
               u"lemão)'ß'.")
        self.read_registro(utf)
        self.read_registro('|9900|0000|1')
        self.read_registro('|9900|0010|1')
        self.read_registro('|9900|5020|')

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
        elif registro.__class__ == self.__class__.registro_encerramento:
            self._registro_encerramento = registro
        elif registro.__class__ == \
                self.__class__.blocos.Bloco0.registro_abertura:
            self.blocos.Bloco0.abertura = registro
        else:
            bloco_id = reg_id[0]
            bloco = self._blocos[bloco_id]
            bloco.add(registro)

            # Contabiliza os registros 5020
            if reg_id == '5020':
                registros_9 = self._blocos['9'].registros[3]
                registros_9.valores[3] = \
                    str((len(self._blocos['5'].registros)) - 2)

    def write_to(self, buffer):

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

        self._registro_encerramento[2] = reg_count
        linha_fechamento = self._registro_encerramento.as_line()[1:]
        buffer.write(linha_fechamento + u'\r\n')

    def readfile(self, filename):

        with open(filename) as arq:
            for line in [line.rstrip('\r\n') for line in arq]:
                if (line[:4] != '9900' and line[:4] != '0001' and line[:4] != '0990'):
                    self.read_registro(line.decode('utf-8-sig'))

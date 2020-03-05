# -*- coding: utf-8 -*-

import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.efd.icms_ipi.arquivos import ArquivoDigital
from sped.efd.icms_ipi.registros import Registro0100

class TestSpedPisCofins(unittest.TestCase):

    def test_read_registro(self):
        txt = u"""|0000|010|0|01102016|30102016|KMEE INFORMATICA LTDA|53.939.351/0001-29|333.333.333-33|SP|222.222.222.222|1234567|5999|0123|A|1|
|0001|0|
|0100|Daniel Sadamo|12334532212|532212|||Rua dos ferroviario|123|Agonia||||||
|0990|3|
|C001|1|
|C990|2|
|D001|1|
|D990|2|
|E001|1|
|E990|2|
|G001|1|
|G990|2|
|H001|1|
|H990|2|
|K001|1|
|K990|2|
|1001|1|
|1990|2|
|9001|1|
|9990|2|
|9999|21|
""".replace('\n', '\r\n')

        # Permite validacao de string grandes
        self.maxDiff = None
        arq = ArquivoDigital()

        arq._registro_abertura.COD_VER = '010'
        arq._registro_abertura.COD_FIN = '0'
        arq._registro_abertura.DT_INI = '01102016'
        arq._registro_abertura.DT_FIN = '30102016'
        arq._registro_abertura.NOME = 'KMEE INFORMATICA LTDA'
        arq._registro_abertura.CNPJ = '53.939.351/0001-29'
        arq._registro_abertura.CPF = '333.333.333-33'
        arq._registro_abertura.UF = 'SP'
        arq._registro_abertura.IE = '222.222.222.222'
        arq._registro_abertura.COD_MUN = '1234567'
        arq._registro_abertura.IM = '5999'
        arq._registro_abertura.SUFRAMA = '0123'
        arq._registro_abertura.IND_PERFIL = 'A'
        arq._registro_abertura.IND_ATIV = '1'

        contabilista = Registro0100()
        contabilista.NOME = 'Daniel Sadamo'
        contabilista.CPF = '12334532212'
        contabilista.CRC = '532212'
        contabilista.END = 'Rua dos ferroviario'
        contabilista.NUM = '123'
        contabilista.COMPL = 'Agonia'

        arq._blocos['0'].add(contabilista)
        self.assertEqual(txt, arq.getstring())

if __name__ == '__main__':
    unittest.main()

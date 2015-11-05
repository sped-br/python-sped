# -*- coding: utf-8 -*-

import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.fci import arquivos


class TestArquivoDigital(unittest.TestCase):

    def test_read_registro(self):
        txt = u"""0000|11111111000191|EMPRESA TESTE|1.0
0001|Texto em caracteres UTF-8: (dígrafo BR)'ção',(dígrafo espanhol-enhe)'ñ',(trema)'Ü',(ordinais)'ªº',(ligamento s+z alemão)'ß'.
0010|46377222000129|Contribuinte de Teste S/A|686001664111|Rua XV de novembro, 1.234|01506000|São João|SP
0990|4
5001
5020|Motor de pistão por ignição, cilindrada igual a 2.000 cm³ - R123-A4-5|84073490|12j8ai.5d0-ao4p|07123456789012|unid|9123,45|4567,89|50,07
5020|Motor de pistão por ignição, cilindrada igual a 2.000 cm³ - R123-A4-5|84073490|12j8ai.5d0-ao4p|07123456789012|unid|9123,45|4567,89|50,07
5020|Motor de pistão por ignição, cilindrada igual a 2.000 cm³ - R123-A4-5|84073490|12j8ai.5d0-ao4p|07123456789012|unid|9123,45|4567,89|50,07
5990|5
9001
9900|0000|1
9900|0010|1
9900|5020|3
9990|5
9999|15
""".replace('\n', '\r\n')

        # Permite validacao de string grandes
        self.maxDiff = None
        arq = arquivos.ArquivoDigital()

        arq.read_registro('0000|11111111000191|EMPRESA TESTE|1.0')

        arq.read_registro(u"|0001|Texto em caracteres UTF-8: (dígrafo BR)'ção',"
                          u"(dígrafo espanhol-enhe)'ñ',(trema)'Ü',(ordinais"
                          u")'ªº',(ligamento s+z alemão)'ß'.")

        arq.read_registro( u'|0010|46377222000129|Contribuinte de Teste '
                           u'S/A|686001664111|Rua XV de novembro, 1.234|'
                           u'01506000|São João|SP')

        arq.read_registro(u'|5020|Motor de pistão por ignição, cilindrada '
                          u'igual a 2.000 cm³ - R123-A4-5|84073490|'
                          u'12j8ai.5d0-ao4p|07123456789012|unid|9123,45|'
                          u'4567,89|50,07')

        arq.read_registro(u'|5020|Motor de pistão por ignição, cilindrada '
                          u'igual a 2.000 cm³ - R123-A4-5|84073490|'
                          u'12j8ai.5d0-ao4p|07123456789012|unid|9123,45|'
                          u'4567,89|50,07')

        arq.read_registro(u'|5020|Motor de pistão por ignição, cilindrada '
                          u'igual a 2.000 cm³ - R123-A4-5|84073490|'
                          u'12j8ai.5d0-ao4p|07123456789012|unid|9123,45|'
                          u'4567,89|50,07')

        self.assertEqual(txt, arq.getstring())

if __name__ == '__main__':
    unittest.main()

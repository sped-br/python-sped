# -*- coding: utf-8 -*-

from pathlib import Path
from .campos import Campo
from .campos import CampoBool
from .campos import CampoAlfanumerico
from .campos import CampoCPF
from .campos import CampoCPFouCNPJ
from .campos import CampoCNPJ
from .campos import CampoData
from .campos import CampoFixo
from .campos import CampoNumerico
from .campos import CampoRegex
from .blocos import Bloco
from .registros import Registro

import json
import re
import types


ECD='ecd'
ECF='ecf'
EFD_ICMS_IPI='efd_icms_ipi'
EFD_PIS_COFINS='efd_pis_cofins'

class Escrituracao(object):
    """
    >>> escrituracao = Escrituracao(ECD, 2016)
    >>> escrituracao
    <sped.escrituracao.Escrituracao(ecd, 2016)>
    >>> escrituracao = Escrituracao(ECD, 2017)
    >>> escrituracao
    <sped.escrituracao.Escrituracao(ecd, 2017)>
    >>> escrituracao.registro_abertura.__class__ == escrituracao.registros.Registro0000
    True
    >>> escrituracao.registro_encerramento.__class__ == escrituracao.registros.Registro9999
    True
    >>> escrituracao._blocos['0'].registro_abertura.__class__ == escrituracao.registros.Registro0001
    True
    >>> escrituracao._blocos['0'].registro_encerramento.__class__ == escrituracao.registros.Registro0990
    True
    >>> escrituracao.registros.Registro == escrituracao._registro_escrituracao
    True
    >>> registro = escrituracao.registros.Registro0000()
    >>> registro
    <sped.escrituracao.Registro0000>
    >>> isinstance(registro, escrituracao._registro_escrituracao)
    True
    >>> registro.escrituracao
    <sped.escrituracao.Escrituracao(ecd, 2017)>
    >>> registro.IDENT_MF = 'M'
    Traceback (most recent call last):
    ...
    sped.erros.FormatoInvalidoError: Registro0000 -> IDENT_MF
    >>> registro.IDENT_MF = True
    >>> registro.IDENT_MF = False
    >>> registro.CNPJ = '1'
    Traceback (most recent call last):
    ...
    sped.erros.FormatoInvalidoError: Registro0000 -> CNPJ
    >>> registro.CNPJ = '10711130000196'
    >>> r = escrituracao.registros.Registro0000('|0000|LECD|01012015|31122015|EMPRESA TESTE|11111111000199|AM||3434401|99999||0|1|0||0|0||N|N|')
    >>> r.CNPJ
    '11111111000199'
    >>> r.IDENT_MF
    False
    >>> r = escrituracao.registros.Registro0000('|0000|LECD|01012017|31122017|GINX LTDA - ME|10711130000196|PR||4106902|01015622961||0|1|0||0|0||N|N|')
    >>> r.COD_SCP
    >>> r.TIP_ECD
    '0'
    >>> escrituracao = Escrituracao(ECF, 2017)
    >>> escrituracao
    <sped.escrituracao.Escrituracao(ecf, 2017)>
    """
    def __init__(self, tipo: str, ano_calendario: int):
        self._tipo = tipo
        self._ano_calendario = ano_calendario

        self._registros = types.ModuleType('registros')
        self._blocos = {}

        self._registro_escrituracao = type('Registro', (Registro,), { 'escrituracao': self })
        self._add_registro(self._registro_escrituracao)

        sped_path = Path(__file__).parent

        leiaute_path = '%s/leiautes/%s_%s.json' % (sped_path, self._tipo,
                                                   self._ano_calendario)
        leiaute_ecd = Path(leiaute_path)

        with leiaute_ecd.open(encoding='utf-8', newline='\n') as f:
            p = json.load(f)

        for bloco in p['blocos']:
            self._blocos[bloco['nome']] = Bloco(bloco['nome'])

        for registro in p['registros']:
            campos = []

            for campo in registro['campos']:
                indice = campo['indice']
                nome = campo['nome']
                valores = campo['valores']
                regras = campo['regras']
                tipo = campo['tipo']
                obrigatorio = campo['obrigatorio']

                # Campos Fixo
                m = re.match(r'"([a-z0-9]+)"', valores, re.IGNORECASE)
                if m:
                    campos.append(CampoFixo(indice, nome, m.group(1)))
                    continue

                m = re.match(r'\[([a-z0-9]+)\]', valores, re.IGNORECASE)
                if m:
                    campos.append(CampoFixo(indice, nome, m.group(1)))
                    continue

                # Campos Regex
                m = re.match(r'\[([^\]]+)\]', valores)
                if m:
                    valoresValidos = m.groups()[0].replace(' ', '').replace('"', '').replace('\n', '').replace(',', ';').split(';')
                    if set(valoresValidos) == set(['S', 'N']):
                        campos.append(CampoBool(indice, nome, obrigatorio=obrigatorio))
                        continue
                    else:
                        campos.append(CampoRegex(indice, nome, obrigatorio=obrigatorio, regex='|'.join(valoresValidos)))
                        continue

                # Campos Data
                if nome.startswith('DT_') or nome.startswith('DATA_'):
                    campos.append(CampoData(indice, nome, obrigatorio=obrigatorio))
                    continue

                # Campo CNPJ ou CPF
                if 'REGRA_VALIDA_CNPJ' in regras and 'REGRA_VALIDA_CPF' in regras or nome == 'IDENT_CPF_CNPJ' or nome == 'CPF_CNPJ':
                    campos.append(CampoCPFouCNPJ(indice, nome, obrigatorio=obrigatorio))
                    continue

                # Campo CNPJ
                if 'REGRA_VALIDA_CNPJ' in regras or nome == 'CNPJ':
                    campos.append(CampoCNPJ(indice, nome, obrigatorio=obrigatorio))
                    continue

                # Campo CPF
                if 'REGRA_VALIDA_CPF' in regras:
                    campos.append(CampoCPF(indice, nome, obrigatorio=obrigatorio))
                    continue

                # CampoAlfaNumerico
                if tipo == 'C':
                    campos.append(CampoAlfanumerico(indice, nome, obrigatorio=obrigatorio, tamanho=campo['tamanho']))
                    continue

                # Campos Decimal
                if tipo == 'N':
                    campos.append(CampoNumerico(indice, nome, obrigatorio=obrigatorio, precisao=campo['decimal']))
                    continue

                # Campos Decimal
                if tipo == 'NS':
                    campos.append(CampoNumerico(indice, nome, obrigatorio=obrigatorio, precisao=campo['decimal']))
                    continue

                # CampoNumerico
                if indice is not None:
                    campos.append(Campo(indice, nome, obrigatorio=obrigatorio))

            nome_registro = registro['nome']
            r = type('Registro' + registro['codigo'], (self._registro_escrituracao,), { 'campos': campos })
            if re.match(r'ABERTURA DO ARQUIVO DIGITAL', nome_registro):
                self.registro_abertura = r()
            if re.match(r'ENCERRAMENTO DO ARQUIVO DIGITAL', nome_registro):
                self.registro_encerramento = r()
            m = re.match(r'ABERTURA DO BLOCO (.)', nome_registro)
            if m:
                self._blocos[m.group(1)].registro_abertura = r()
            m = re.match(r'ENCERRAMENTO DO BLOCO (.)', nome_registro)
            if m:
                self._blocos[m.group(1)].registro_encerramento = r()
            self._add_registro(r)

    def _add_registro(self, registro: type):
        setattr(self._registros, registro.__name__, registro)

    @property
    def blocos(self) -> list:
        return self._blocos

    @property
    def registros(self) -> types.ModuleType:
        return self._registros

    def prepare(self):
        bloco_9 = self._blocos['9']

        for bloco in self._blocos.values():
            regs = {}

            for reg in bloco.registros:
                if reg.REG not in regs:
                    regs[reg.REG] = 0
                regs[reg.REG] += 1

            if bloco == self._blocos['0']:
                regs['0000'] = 1

            if bloco == bloco_9:
                regs['9999'] = 1
                regs['9900'] += len(regs.keys())

            for reg in regs.keys():
                registro = self.registros.Registro9900() # pylint: disable=E1101
                try:
                    registro.REG_BLC = reg
                except:
                    for rrr in bloco.registros:
                        print(rrr)
                    print(locals())
                    raise
                registro.QTD_REG_BLC = regs[reg]
                bloco_9.add(registro)

        reg_count = 2
        for bloco in self._blocos.values():
            reg_count += len(bloco.registros)

        self.registro_encerramento[2] = reg_count

    def write_to(self, buff):
        buff.write('%s\r\n' % self.registro_abertura)
        reg_count = 2
        for bloco in self._blocos.values():
            reg_count += len(bloco.registros)
            for registro in bloco.registros:
                buff.write('%s\r\n' % registro)

        self.registro_encerramento[2] = reg_count

        buff.write('%s\r\n' % self.registro_encerramento)

    def add(self, registro: Registro):
        pass

    def __repr__(self):
        return '<%s.%s(%s, %s)>' % (self.__class__.__module__,
                                    self.__class__.__name__,
                                    self._tipo, self._ano_calendario)

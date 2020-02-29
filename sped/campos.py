# -*- coding: utf-8 -*-

import re

from datetime import date
from datetime import datetime
from decimal import Decimal

from .erros import CampoFixoError
from .erros import CampoObrigatorioError
from .erros import FormatoInvalidoError


class Campo(object):
    """
    Classe base para definição de um campo de um registro do SPED.

    >>> campo = Campo(1, 'TESTE', True)
    >>> campo
    <sped.campos.Campo(1, TESTE)>
    >>> campo.indice
    1
    >>> campo.nome
    'TESTE'
    >>> campo.obrigatorio
    True
    """
    def __init__(self, indice, nome, obrigatorio=False):
        self._indice = indice
        self._nome = nome
        self._obrigatorio = obrigatorio

    def __repr__(self):
        return '<%s.%s(%s, %s)>' % (self.__class__.__module__,
                                    self.__class__.__name__,
                                    self._indice, self._nome)

    @property
    def indice(self):
        return self._indice

    @property
    def nome(self):
        return self._nome

    @property
    def obrigatorio(self):
        return self._obrigatorio

    def get(self, registro):
        return registro.valores[self._indice] or None

    def set(self, registro, valor):
        if self._obrigatorio and not valor:
            raise CampoObrigatorioError(registro, self.nome)
        if not valor:
            registro.valores[self._indice] = ''
            return
        if valor and not self.__class__.validar(valor):
            raise FormatoInvalidoError(registro, self.nome)
        if not isinstance(valor, str):
            raise FormatoInvalidoError(registro, self.nome)
        registro.valores[self._indice] = valor or ''

    @staticmethod
    def validar(valor):
        return True


class CampoFixo(Campo):
    """
    Classe base para definição de um campo de um registro do SPED.

    >>> campo = CampoFixo(1, 'REG', '0000')
    >>> campo
    <sped.campos.CampoFixo(1, REG)>
    >>> campo.indice
    1
    >>> campo.nome
    'REG'
    >>> campo.obrigatorio
    True
    >>> campo.valor
    '0000'
    """
    def __init__(self, indice, nome, valor):
        super().__init__(indice, nome, True)
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def get(self, registro):
        return self._valor

    def set(self, registro, valor):
        if valor != self._valor:
            raise CampoFixoError(registro, self.nome)


class CampoAlfanumerico(Campo):
    def __init__(self, indice, nome, obrigatorio=False, tamanho=None):
        super().__init__(indice, nome, obrigatorio)
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def set(self, registro, valor):
        valor = valor or ''
        if self._tamanho is not None:
            valor = valor[:self._tamanho]
        super().set(registro, valor)


class CampoBool(Campo):
    def __init__(self, indice, nome, obrigatorio=False, valorVerdadeiro='S', valorFalso='N'):
        super().__init__(indice, nome, obrigatorio)
        self.valorVerdadeiro = valorVerdadeiro
        self.valorFalso = valorFalso

    def get(self, registro):
        valor = super().get(registro)
        if not valor:
            return None
        return valor == self.valorVerdadeiro

    def set(self, registro, valor):
        if isinstance(valor, bool):
            super().set(registro, self.valorVerdadeiro if valor else self.valorFalso)
        elif valor is None:
            super().set(registro, None)
        else:
            raise FormatoInvalidoError(registro, self.nome)


class CampoNumerico(Campo):
    def __init__(self, indice, nome, obrigatorio=False,
                 precisao=None, minimo=0, maximo=1000):
        super().__init__(indice, nome, obrigatorio)
        self._precisao = precisao if precisao is not None else 0
        self._minimo = minimo
        self._maximo = maximo

    @property
    def precisao(self):
        return self._precisao

    @property
    def minimo(self):
        return self._minimo

    @property
    def maximo(self):
        return self._maximo

    def get(self, registro):
        valor = super().get(registro)
        if not valor:
            return None
        return Decimal(valor.replace(',', '.'))

    def set(self, registro, valor):
        if isinstance(valor, str):
            valor = Decimal(valor.replace(',', '.'))

        if isinstance(valor, Decimal) or isinstance(valor, float):
            super().set(registro, (('%.' + str(self._precisao) + 'f') % valor).replace('.', ','))
        elif isinstance(valor, int):
            super().set(registro, str(valor))
        elif not valor:
            super().set(registro, '0')
        else:
            raise FormatoInvalidoError(registro, self.nome)


class CampoData(Campo):
    def __init__(self, indice, nome, obrigatorio=False):
        super().__init__(indice, nome, obrigatorio)

    def get(self, registro):
        valor = super().get(registro)
        if not valor:
            return None
        return datetime.strptime(valor, '%d%m%Y').date()

    def set(self, registro, valor):
        # https://stackoverflow.com/questions/19887353/attributeerror-str-object-has-no-attribute-strftime
        valor = datetime.strptime(valor, '%d%m%Y')
        if isinstance(valor, date):
            super().set(registro, valor.strftime('%d%m%Y'))
        elif not valor:
            super().set(registro, None)
        else:
            raise FormatoInvalidoError(registro, self.nome)

    @staticmethod
    def formatar(data_in):
        dt = datetime.strptime(data_in, "%d%m%Y") # ddmmaaaa
        #data_out =  dt.isoformat('T')
        #data_out = dt.strftime('%x %X') # excel date format
        data_out = dt.strftime("%d/%m/%Y")
        return data_out


class CampoRegex(Campo):
    def __init__(self, indice, nome, obrigatorio=False, regex=None):
        super().__init__(indice, nome, obrigatorio)
        self._regex = re.compile('^' + regex + '$')

    def set(self, registro, valor):
        if not isinstance(valor, str):
            valor = str(valor)
        if not valor or self._regex.match(valor):
            super().set(registro, valor)
        else:
            raise FormatoInvalidoError(registro, str(self))

    # def __repr__(self):
    #     return '' f'{self.__class__.__name__}({self.indice}, {self.nome}, {self._obrigatorio}, {self._regex})'


class CampoCNPJ(Campo):
    @staticmethod
    def validar(valor):
        # valor = '53.939.351/0001-29'
        # remover os caracteres não dígitos (\D)
        valor = re.sub(r'\D', '', valor)

        if not re.search(r'^\d{14}$', str(valor)):
            return False

        multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        cnpj = [int(c) for c in valor]

        soma1 = sum([cnpj[i] * multiplicadores[i+1] for i in range(12)])
        soma2 = sum([cnpj[i] * multiplicadores[i] for i in range(13)])
        digito1 = 11 - (soma1 % 11)
        digito2 = 11 - (soma2 % 11)

        if digito1 >= 10:
            digito1 = 0

        if digito2 >= 10:
            digito2 = 0

        if cnpj[12] != digito1 or cnpj[13] != digito2:
            return False

        return True

    @staticmethod
    def formatar(cnpj):
        cnpj = re.sub(r'\D', '', cnpj)
        mensagem_de_validacao = ''
        if len(cnpj) >= 1:
            if not CampoCNPJ.validar(cnpj):
                mensagem_de_validacao = ' : dígito verificador do cnpj inválido!'
            if len(cnpj) == 14:
                cnpj = "%s.%s.%s/%s-%s" % (cnpj[0:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:14])
        return cnpj + mensagem_de_validacao


class CampoCPF(Campo):
    @staticmethod
    def validar(valor):
        # valor = '333.333.333-33'
        # remover os caracteres não dígitos (\D)
        valor = re.sub(r'\D', '', valor)

        if not re.search(r'^\d{11}$', str(valor)):
            return False

        multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        cpf = [int(c) for c in valor]

        soma1 = sum([cpf[i] * multiplicadores[i+1] for i in range(9)])
        soma2 = sum([cpf[i] * multiplicadores[i] for i in range(10)])
        digito1 = 11 - (soma1 % 11)
        digito2 = 11 - (soma2 % 11)

        if digito1 >= 10:
            digito1 = 0

        if digito2 >= 10:
            digito2 = 0

        if cpf[9] != digito1 or cpf[10] != digito2:
            return False

        return True
    
    @staticmethod
    def formatar(cpf):
        cpf = re.sub(r'\D', '', cpf)
        mensagem_de_validacao = ''
        if len(cpf) >= 1:
            if not CampoCPF.validar(cpf):
                mensagem_de_validacao = ' : dígito verificador do cpf inválido!'
            if len(cpf) == 11:
                cpf = "%s.%s.%s-%s" % (cpf[0:3],cpf[3:6],cpf[6:9],cpf[9:11])
        return cpf + mensagem_de_validacao


class CampoCPFouCNPJ(Campo):
    @staticmethod
    def validar(valor):
        # remover os caracteres não dígitos (\D)
        valor = re.sub(r'\D', '', valor)

        if len(valor) == 14:
            return CampoCNPJ.validar(valor)
        if len(valor) == 11:
            return CampoCPF.validar(valor)
        return False

    @staticmethod
    def formatar(digt):
        digt = re.sub(r'\D', '', digt)
        mensagem_de_validacao = ''
        if len(digt) >= 1:
            if len(digt) == 11 and not CampoCPF.validar(digt):
                mensagem_de_validacao = ' : dígito verificador do cpf inválido!'
            elif len(digt) == 14 and not CampoCNPJ.validar(digt):
                mensagem_de_validacao = ' : dígito verificador do cnpj inválido!'

            if len(digt) == 11:
                digt = "CPF %s.%s.%s-%s" % (digt[0:3],digt[3:6],digt[6:9],digt[9:11])
            elif len(digt) == 14:
                digt = "CNPJ %s.%s.%s/%s-%s" % (digt[0:2],digt[2:5],digt[5:8],digt[8:12],digt[12:14])
        return digt + mensagem_de_validacao


# Fonte: 'NFe Manual_de_Orientacao_Contribuinte_v_6.00.pdf', pg 144.
# 5.4 Cálculo do Dígito Verificador da Chave de Acesso da NF-e
class CampoChaveEletronica(Campo):
    @staticmethod
    def validar(valor):
        # remover os caracteres não dígitos (\D)
        valor = re.sub(r'\D', '', valor)

        if not re.search(r'^\d{44}$', str(valor)):
            return False

        chave = [int(digito) for digito in valor]
        multiplicadores = [4, 3, 2] + [9, 8, 7, 6, 5, 4, 3, 2] * 5 + [0]

        soma = sum([chave[i] * multiplicadores[i] for i in range(44)])

        resto_da_divisao = soma % 11
        digito_verificador = 11 - resto_da_divisao

        if digito_verificador >= 10:
            digito_verificador = 0

        if chave[-1] != digito_verificador:
            return False

        # dentro da chave eletrônica há o CNPJ do emitente
        # que também será verificado
        cnpj = str(valor)[6:20]

        return CampoCNPJ.validar(cnpj)

    @staticmethod
    def formatar(chave):
        chave = re.sub(r'\D', '', chave)
        mensagem_de_validacao = ''
        if len(chave) >= 1:
            if not CampoChaveEletronica.validar(chave):
                mensagem_de_validacao = ' : dígito verificador da chave inválido!'
            if len(chave) == 44:
                chave = "%s.%s.%s.%s.%s.%s.%s.%s-%s" % (chave[0:2],chave[2:6],chave[6:20],chave[20:22],chave[22:25],chave[25:34],chave[34:35],chave[35:43],chave[43:44])
        return chave + mensagem_de_validacao


class CampoNCM(Campo):
    @staticmethod
    def formatar(ncm):
        if len(ncm) == 8:
            ncm = "%s.%s.%s" % (ncm[0:4],ncm[4:6],ncm[6:8])
        return ncm
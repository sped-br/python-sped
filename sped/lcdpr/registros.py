# -*- coding: utf-8 -*-

from ..campos import *
from ..registros import Registro
from ..registros import RegistroAbertura
from ..registros import RegistroEncerramento


class Registro0000(RegistroAbertura):
    """
    ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA PESSOA FÍSICA
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoFixo(2, 'NOME_ESC', 'LCDPR'),
        CampoAlfanumerico(3, 'COD_VER', obrigatorio=True, tamanho=4),
        CampoCPF(4, 'CPF', obrigatorio=True),
        CampoAlfanumerico(5, 'NOME', obrigatorio=True),
        CampoRegex(6, 'IND_SIT_INI_PER', obrigatorio=True, regex='[0-2]'),
        CampoRegex(7, 'SIT_ESPECIAL', obrigatorio=True, regex='[0-3]'),
        CampoData(8, 'DT_SIT_ESP'),
        CampoData(9, 'DT_INI', obrigatorio=True),
        CampoData(10, 'DT_FIN', obrigatorio=True),
    ]


class Registro0010(Registro):
    """
    PARÂMETROS DE TRIBUTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '0010'),
        CampoRegex(2, 'FORMA_APUR', obrigatorio=True, regex='[1-2]'),
    ]

class Registro0030(Registro):
    """
    DADOS CADASTRAIS DO CONTRIBUINTE
    """
    campos = [
        CampoFixo(1, 'REG', '0030'),
        Campo(2, 'ENDERECO'),
        Campo(3, 'NUM'),
        Campo(4, 'COMPL'),
        Campo(5, 'BAIRRO'),
        Campo(6, 'UF'),
        Campo(7, 'COD_MUN'),
        Campo(8, 'CEP'),
        Campo(9, 'NUM_TEL'),
        Campo(10, 'EMAIL'),
    ]


class Registro0040(Registro):
    """
    CADASTRO DOS IMÓVEIS RURAIS
    """
    campos = [
        CampoFixo(1, 'REG', '0040'),
        Campo(2, 'COD_IMÓVEL'),
        Campo(3, 'PAIS'),
        Campo(4, 'MOEDA'),
        Campo(5, 'CAD_ITR'),
        Campo(6, 'CAEPF'),
        Campo(7, 'INSCR_ESTADUAL'),
        Campo(8, 'NOME_IMÓVEL'),
        Campo(9, 'ENDERECO'),
        Campo(10, 'NUM'),
        Campo(11, 'COMPL'),
        Campo(12, 'BAIRRO'),
        Campo(13, 'UF'),
        Campo(14, 'COD_MUN'),
        Campo(15, 'CEP'),
        Campo(16, 'TIPO_EXPLORAÇÃO'),
        Campo(17, 'PARTICIPAÇÃO'),
    ]


class Registro0045(Registro):
    """
    CADASTRO DE TERCEIROS
    """
    campos = [
        CampoFixo(1, 'REG', '0045'),
        Campo(2, 'COD_IMÓVEL'),
        Campo(3, 'TIPO_CONTRAPARTE'),
        Campo(4, 'ID_CONTRAPARTE'),
        Campo(5, 'NOME_CONTRAPARTE'),
        Campo(6, 'PERC_CONTRAPARTE'),
    ]


class Registro0050(Registro):
    """
    CADASTRO DAS CONTAS BANCÁRIAS DO PRODUTOR RURAL
    """
    campos = [
        CampoFixo(1, 'REG', '0050'),
        Campo(2, 'COD_CONTA'),
        Campo(3, 'PAIS_CTA'),
        Campo(4, 'BANCO'),
        Campo(5, 'NOME_BANCO'),
        Campo(6, 'AGENCIA'),
        Campo(7, 'NUM_CONTA'),
    ]


class RegistroQ100(Registro):
    """
    DEMONSTRATIVO DO RESULTADO DA ATIVIDADE RURAL
    """
    campos = [
        CampoFixo(1, 'REG', 'Q100'),
        CampoData(2, 'DATA'),
        Campo(3, 'COD_IMÓVEL'),
        Campo(4, 'COD_CONTA'),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'TIPO_DOC'),
        Campo(7, 'HIST'),
        Campo(8, 'ID_PARTIC'),
        Campo(9, 'TIPO_LANC'),
        CampoNumerico2(10, 'VL_ENTRADA', precisao=19),
        CampoNumerico2(11, 'VL_SAIDA', precisao=19),
        CampoNumerico2(12, 'SLD_FIN', precisao=19),
        Campo(13, 'NAT_SLD_FIN'),
    ]


class RegistroQ200(Registro):
    """
    RESUMO MENSAL DO DEMONSTRATIVO DO RESULTADO DA ATIVIDADE RURAL
    """
    campos = [
        CampoFixo(1, 'REG', 'Q200'),
        Campo(2, 'MÊS'),
        CampoNumerico2(3, 'VL_ENTRADA'),
        CampoNumerico2(4, 'VL_SAIDA'),
        CampoNumerico2(5, 'SLD_FIN'),
        Campo(6, 'NAT_SLD_FIN'),
    ]


class Registro9999(RegistroEncerramento):
    """
    Encerramento do Arquivo Digital
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        Campo(2, 'IDENT_NOM'),
        Campo(3, 'IDENT_CPF_CNPJ'),
        Campo(4, 'IND_CRC'),
        Campo(5, 'EMAIL'),
        Campo(6, 'FONE'),
        CampoNumerico(7, 'QTD_LIN'),
    ]

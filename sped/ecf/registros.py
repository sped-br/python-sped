# -*- coding: utf-8 -*-

from ..campos import *
from ..registros import Registro


class Registro0000(Registro):
    """
    Abertura do Arquivo Digital e Identificação da Pessoa Jurídica

    >>> r = Registro0000()
    >>> r.REG
    '0000'
    >>> r.NOME_ESC
    'LECF'
    >>> line='|0000|LECF|1.00|11111111000191|EMPRESA TESTE|0|0|||01012014|31122014|N||0||'
    >>> r = Registro0000(line)
    >>> r.as_line()
    '|0000|LECF|1.00|11111111000191|EMPRESA TESTE|0|0|||01012014|31122014|N||0||'
    >>> r.REG
    '0000'
    >>> r.NOME_ESC
    'LECF'
    >>> r.COD_VER
    '1.00'
    >>> r.CNPJ
    '11111111000191'
    >>> r.NOME
    'EMPRESA TESTE'
    >>> r.DT_INI
    datetime.date(2014, 1, 1)
    >>> r.NOME = 'EMPRESA DEMO'
    >>> r.NOME
    'EMPRESA DEMO'
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoFixo(2, 'NOME_ESC', 'LECF'),
        CampoAlfanumerico(3, 'COD_VER', obrigatorio=True, tamanho=4),
        CampoCNPJ(4, 'CNPJ', obrigatorio=True),
        CampoAlfanumerico(5, 'NOME', obrigatorio=True),
        CampoRegex(6, 'IND_SIT_INI_PER', obrigatorio=True, regex='[0-4]'),
        CampoRegex(7, 'SIT_ESPECIAL', obrigatorio=True, regex='[0-9]'),
        CampoNumerico(8, 'PAT_REMAN_CIS', precisao=2, minimo=Decimal(0), maximo=Decimal(100)),
        CampoData(9, 'DT_SIT_ESP'),
        CampoData(10, 'DT_INI', obrigatorio=True),
        CampoData(11, 'DT_FIN', obrigatorio=True),
        CampoRegex(12, 'RETIFICADORA', obrigatorio=True, regex='[SN]'),
        CampoAlfanumerico(13, 'NUM_REC', tamanho=41),
        CampoRegex(14, 'TIP_ECF', obrigatorio=True, regex='[0-2]'),
        CampoAlfanumerico(15, 'COD_SCP', tamanho=14)
    ]


class Registro0001(Registro):
    """
    Abertura do Bloco 0
    """
    campos = [
        CampoFixo(1, 'REG', '0001'),
        Campo(2, 'IND_DAD'),
    ]


class Registro0010(Registro):
    """
    Parâmetros de Tributação
    """
    campos = [
        CampoFixo(1, 'REG', '0010'),
        Campo(2, 'HASH_ECF_ANTERIOR'),
        Campo(3, 'OPT_REFIS'),
        Campo(4, 'OPT_PAES'),
        CampoNumerico(5, 'FORMA_TRIB'),
        Campo(6, 'FORMA_APUR'),
        Campo(7, 'COD_QUALIF_PJ'),
        Campo(8, 'FORMA_TRIB_PER'),
        Campo(9, 'MES_BAL_RED'),
        Campo(10, 'TIP_ESC_PRE'),
        Campo(11, 'TIP_ENT'),
        Campo(12, 'FORMA_APUR_I'),
        Campo(13, 'APUR_CSLL'),
        Campo(14, 'OPT_EXT_RTT'),
        Campo(15, 'DIF_FCONT'),
    ]


class Registro0020(Registro):
    """
    Parâmetros Complementares
    """
    campos = [
        CampoFixo(1, 'REG', '0020'),
        Campo(2, 'IND_ALIQ_CSLL'),
        Campo(3, 'IND_QTE_SCP'),
        Campo(4, 'IND_ADM_FUN_CLU'),
        Campo(5, 'IND_PART_CONS'),
        Campo(6, 'IND_OP_EXT'),
        Campo(7, 'IND_OP_VINC'),
        Campo(8, 'IND_PJ_ENQUAD'),
        Campo(9, 'IND_PART_EXT'),
        Campo(10, 'IND_ATIV_RURAL'),
        Campo(11, 'IND_LUC_EXP'),
        Campo(12, 'IND_RED_ISEN'),
        Campo(13, 'IND_FIN'),
        Campo(14, 'IND_DOA_ELEIT'),
        Campo(15, 'IND_PART_COLIG'),
        Campo(16, 'IND_VEND_EXP'),
        Campo(17, 'IND_REC_EXT'),
        Campo(18, 'IND_ATIV_EXT'),
        Campo(19, 'IND_COM_EXP'),
        Campo(20, 'IND_PGTO_EXT'),
        Campo(21, 'IND_E_COM_TI'),
        Campo(22, 'IND_ROY_REC'),
        Campo(23, 'IND_ROY_PAG'),
        Campo(24, 'IND_REND_SERV'),
        Campo(25, 'IND_PGTO_REM'),
        Campo(26, 'IND_INOV_TEC'),
        Campo(27, 'IND_CAP_INF'),
        Campo(28, 'IND_PJ_HAB'),
        Campo(29, 'IND_POLO_AM'),
        Campo(30, 'IND_ZON_EXP'),
        Campo(31, 'IND_AREA_COM'),
    ]


class Registro0030(Registro):
    """
    Dados Cadastrais
    """
    campos = [
        CampoFixo(1, 'REG', '0030'),
        Campo(2, 'COD_NAT'),
        Campo(3, 'CNAE_FISCAL'),
        Campo(4, 'ENDERECO'),
        Campo(5, 'NUM'),
        Campo(6, 'COMPL'),
        Campo(7, 'BAIRRO'),
        Campo(8, 'UF'),
        Campo(9, 'COD_MUN'),
        Campo(10, 'CEP'),
        Campo(11, 'NUM_TEL'),
        Campo(12, 'EMAIL'),
    ]


class Registro0035(Registro):
    """
    Identificação das SCP
    """
    campos = [
        CampoFixo(1, 'REG', '0035'),
        Campo(2, 'COD_SCP'),
        Campo(3, 'NOME_SCP'),
    ]


class Registro0930(Registro):
    """
    Identificação dos Signatários da ECF
    """
    campos = [
        CampoFixo(1, 'REG', '0930'),
        Campo(2, 'IDENT_NOM'),
        Campo(3, 'IDENT_CPF_CNPJ'),
        Campo(4, 'IDENT_QUALIF'),
        Campo(5, 'IND_CRC'),
        Campo(6, 'EMAIL'),
        Campo(7, 'FONE'),
    ]


class Registro0990(Registro):
    """
    Encerramento do Bloco 0
    """
    campos = [
        CampoFixo(1, 'REG', '0990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroC001(Registro):
    """
    Abertura do Bloco C – Informações Recuperadas da ECD
    """
    campos = [
        CampoFixo(1, 'REG', 'C001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroC040(Registro):
    """
    Identificador da ECD
    """
    campos = [
        CampoFixo(1, 'REG', 'C040'),
        Campo(2, 'HASH_ECD'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIN'),
        Campo(5, 'IND_SIT_ESP'),
        CampoCNPJ(6, 'CNPJ'),
        CampoNumerico(7, 'NUM_ORD'),
        Campo(8, 'NIRE'),
        Campo(9, 'NAT_LIVR'),
        Campo(10, 'COD_VER_LC'),
        Campo(11, 'IND_ESC'),
    ]


class RegistroC050(Registro):
    """
    Plano de Contas da ECD
    """
    campos = [
        CampoFixo(1, 'REG', 'C050'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_NAT'),
        Campo(4, 'IND_CTA'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'COD_CTA_SUP'),
        Campo(8, 'CTA'),
    ]


class RegistroC051(Registro):
    """
    Plano de Contas Referencial
    """
    campos = [
        CampoFixo(1, 'REG', 'C051'),
        Campo(2, 'COD_ENT_REF'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'COD_CTA_REF'),
    ]


class RegistroC053(Registro):
    """
    Subcontas Correlatas
    """
    campos = [
        CampoFixo(1, 'REG', 'C053'),
        Campo(2, 'COD_IDT'),
        Campo(3, 'COD_CNT_CORR'),
        Campo(4, 'NAT_SUB_CNT'),
    ]


class RegistroC100(Registro):
    """
    Centro de Custos
    """
    campos = [
        CampoFixo(1, 'REG', 'C100'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'CCUS'),
    ]


class RegistroC150(Registro):
    """
    Identificação do Período dos Saldos Periódicos das Contas Patrimoniais
    """
    campos = [
        CampoFixo(1, 'REG', 'C150'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]


class RegistroC155(Registro):
    """
    Detalhes dos Saldos Contábeis das Contas Patrimoniais
    """
    campos = [
        CampoFixo(1, 'REG', 'C155'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_INI', precisao=2),
        Campo(5, 'IND_VL_SLD_INI'),
        CampoNumerico(6, 'VL_DEB', precisao=2),
        CampoNumerico(7, 'VL_CRED', precisao=2),
        CampoNumerico(8, 'VL_SLD_FIN', precisao=2),
        Campo(9, 'IND_VL_SLD_FIN'),
        Campo(10, 'LINHA_ECD'),
    ]


class RegistroC157(Registro):
    """
    Transferência de Saldos do Plano de Contas Anterior
    """
    campos = [
        CampoFixo(1, 'REG', 'C157'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_FIN', precisao=2),
        Campo(5, 'IND_VL_SLD_FIN'),
        Campo(6, 'LINHA_ECD'),
    ]


class RegistroC350(Registro):
    """
    Identificação da Data dos Saldos das Contas de Resultado Antes do Encerramento
    """
    campos = [
        CampoFixo(1, 'REG', 'C350'),
        CampoData(2, 'DT_RES'),
    ]


class RegistroC355(Registro):
    """
    Detalhes dos Saldos das Contas de Resultado Antes do Encerramento
    """
    campos = [
        CampoFixo(1, 'REG', 'C355'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_CTA', precisao=2),
        Campo(5, 'IND_VL_CTA'),
        Campo(6, 'LINHA_ECD'),
    ]


class RegistroC990(Registro):
    """
    Encerramento do Bloco C
    """
    campos = [
        CampoFixo(1, 'REG', 'C990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroE001(Registro):
    """
    Abertura do Bloco E – Informações Recuperadas da ECF Anterior e Cálculo Fiscal dos Dados Recuperados da ECD
    """
    campos = [
        CampoFixo(1, 'REG', 'E001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroE010(Registro):
    """
    Saldos Finais Recuperados da ECF Anterior
    """
    campos = [
        CampoFixo(1, 'REG', 'E010'),
        Campo(2, 'COD_NAT'),
        Campo(3, 'COD_CTA_REF'),
        Campo(4, 'DESC_CTA_REF'),
        CampoNumerico(5, 'VAL_CTA_REF', precisao=2),
        Campo(6, 'IND_VAL_CTA_REF'),
    ]


class RegistroE015(Registro):
    """
    Contas Contábeis Mapeadas
    """
    campos = [
        CampoFixo(1, 'REG', 'E015'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'DESC_CTA'),
        CampoNumerico(5, 'VAL_CTA', precisao=2),
        Campo(6, 'IND_VAL_CTA'),
    ]


class RegistroE020(Registro):
    """
    Saldos Finais das Contas da Parte B do e-Lalur da ECF Imediatamente Anterior
    """
    campos = [
        CampoFixo(1, 'REG', 'E020'),
        Campo(2, 'COD_CTA_B'),
        Campo(3, 'DESC_CTA_LAL'),
        CampoData(4, 'DT_AP_LAL'),
        Campo(5, 'COD_LAN_ORIG'),
        Campo(6, 'DESC_LAN_ORIG'),
        CampoData(7, 'DT_LIM_LAL'),
        Campo(8, 'TRIBUTO'),
        CampoNumerico(9, 'VL_SALDO_FIN', precisao=2),
        Campo(10, 'IND_VL_SALDO_FIN'),
    ]


class RegistroE030(Registro):
    """
    Identificação do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'E030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroE155(Registro):
    """
    Detalhes dos Saldos Contábeis Calculados com Base nas ECD
    """
    campos = [
        CampoFixo(1, 'REG', 'E155'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_INI', precisao=2),
        Campo(5, 'IND_VL_SLD_INI'),
        CampoNumerico(6, 'VL_DEB', precisao=2),
        CampoNumerico(7, 'VL_CRED', precisao=2),
        CampoNumerico(8, 'VL_SLD_FIN', precisao=2),
        Campo(9, 'IND_VL_SLD_FIN'),
    ]


class RegistroE355(Registro):
    """
    Detalhes dos Saldos das Contas de Resultado Antes do Encerramento
    """
    campos = [
        CampoFixo(1, 'REG', 'E355'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_FIN', precisao=2),
        Campo(5, 'IND_VL_SLD_FIN'),
    ]


class RegistroE990(Registro):
    """
    Encerramento do Bloco E
    """
    campos = [
        CampoFixo(1, 'REG', 'E990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroJ001(Registro):
    """
    Abertura do Bloco J – Plano de Contas e Mapeamento
    """
    campos = [
        CampoFixo(1, 'REG', 'J001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroJ050(Registro):
    """
    Plano de Contas do Contribuinte
    """
    campos = [
        CampoFixo(1, 'REG', 'J050'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_NAT'),
        Campo(4, 'IND_CTA'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'COD_CTA_SUP'),
        Campo(8, 'CTA'),
    ]


class RegistroJ051(Registro):
    """
    Plano de Contas Referencial
    """
    campos = [
        CampoFixo(1, 'REG', 'J051'),
        Campo(2, 'COD_CCUS'),
        Campo(3, 'COD_CTA_REF'),
    ]


class RegistroJ053(Registro):
    """
    Subcontas Correlatas
    """
    campos = [
        CampoFixo(1, 'REG', 'J053'),
        Campo(2, 'COD_IDT'),
        Campo(3, 'COD_CNT_CORR'),
        Campo(4, 'NAT_SUB_CNT'),
    ]


class RegistroJ100(Registro):
    """
    Centro de Custos
    """
    campos = [
        CampoFixo(1, 'REG', 'J100'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'CCUS'),
    ]


class RegistroJ990(Registro):
    """
    Encerramento do Bloco J
    """
    campos = [
        CampoFixo(1, 'REG', 'J990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroK001(Registro):
    """
    Abertura do Bloco K – Saldos das Contas Contábeis e Referenciais
    """
    campos = [
        CampoFixo(1, 'REG', 'K001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroK030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
    """
    campos = [
        CampoFixo(1, 'REG', 'K030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroK155(Registro):
    """
    Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)
    """
    campos = [
        CampoFixo(1, 'REG', 'K155'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_INI', precisao=2),
        Campo(5, 'IND_VL_SLD_INI'),
        CampoNumerico(6, 'VL_DEB', precisao=2),
        CampoNumerico(7, 'VL_CRED', precisao=2),
        CampoNumerico(8, 'VL_SLD_FIN', precisao=2),
        Campo(9, 'IND_VL_SLD_FIN'),
    ]


class RegistroK156(Registro):
    """
    Mapeamento Referencial do Saldo Final
    """
    campos = [
        CampoFixo(1, 'REG', 'K156'),
        Campo(2, 'COD_CTA_REF'),
        CampoNumerico(3, 'VL_SLD_FIN', precisao=2),
        Campo(4, 'IND_VL_SLD_FIN'),
    ]


class RegistroK355(Registro):
    """
    Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
    """
    campos = [
        CampoFixo(1, 'REG', 'K355'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_FIN', precisao=2),
        Campo(5, 'IND_VL_SLD_FIN'),
    ]


class RegistroK356(Registro):
    """
    Mapeamento Referencial dos Saldos Finais das Contas de Resultado Antes do Encerramento
    """
    campos = [
        CampoFixo(1, 'REG', 'K356'),
        Campo(2, 'COD_CTA_REF'),
        CampoNumerico(3, 'VL_SLD_FIN', precisao=2),
        Campo(4, 'IND_VL_SLD_FIN'),
    ]


class RegistroK990(Registro):
    """
    Encerramento do Bloco K
    """
    campos = [
        CampoFixo(1, 'REG', 'K990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroL001(Registro):
    """
    Abertura do Bloco L – Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'L001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroL030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
    """
    campos = [
        CampoFixo(1, 'REG', 'L030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroL100(Registro):
    """
    Balanço Patrimonial
    """
    campos = [
        CampoFixo(1, 'REG', 'L100'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VAL_CTA_REF_INI', precisao=2),
        Campo(9, 'IND_VAL_CTA_REF_INI'),
        CampoNumerico(10, 'VAL_CTA_REF_FIN', precisao=2),
        Campo(11, 'IND_VAL_CTA_REF_FIN'),
    ]


class RegistroL200(Registro):
    """
    Método de Avaliação do Estoque Final
    """
    campos = [
        CampoFixo(1, 'REG', 'L200'),
        Campo(2, 'IND_AVAL_ESTOQ'),
    ]


class RegistroL210(Registro):
    """
    Informativo da Composição de Custos
    """
    campos = [
        CampoFixo(1, 'REG', 'L210'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroL300(Registro):
    """
    Demonstração do Resultado do Exercício
    """
    campos = [
        CampoFixo(1, 'REG', 'L300'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VALOR', precisao=2),
        Campo(9, 'IND_VALOR'),
    ]


class RegistroL990(Registro):
    """
    Encerramento do Bloco L
    """
    campos = [
        CampoFixo(1, 'REG', 'L990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroM001(Registro):
    """
    Abertura do Bloco M – Livro Eletrônico de
    Apuração do Lucro Real (e-Lalur) e Licro Eletrônico
    de Apuração da Base de Cálculo da CSLL (e-Lacs)
    """
    campos = [
        CampoFixo(1, 'REG', 'M001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroM010(Registro):
    """
    Identificação da Conta na Parte B e-Lalur e do e-Lacs
    """
    campos = [
        CampoFixo(1, 'REG', 'M010'),
        Campo(2, 'COD_CTA_B'),
        Campo(3, 'DESC_CTA_LAL'),
        CampoData(4, 'DT_AP_LAL'),
        Campo(5, 'COD_LAN_ORIG'),
        Campo(6, 'DESC_LAN_ORIG'),
        CampoData(7, 'DT_LIM_LAL'),
        Campo(8, 'TRIBUTO'),
        CampoNumerico(9, 'VL_SALDO_INI', precisao=2),
        Campo(10, 'IND_VL_SALDO_INI'),
        CampoCNPJ(11, 'CNPJ_SIT_ESP'),
    ]


class RegistroM030(Registro):
    """
    Identificação do Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'M030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroM300(Registro):
    """
    Lançamentos da Parte A do e-Lalur
    """
    campos = [
        CampoFixo(1, 'REG', 'M300'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO_LANCAMENTO'),
        Campo(5, 'IND_RELACAO'),
        CampoNumerico(6, 'VALOR', precisao=2),
        Campo(7, 'HIST_LAN_LAL'),
    ]


class RegistroM305(Registro):
    """
    Conta da Parte B do e-Lalur
    """
    campos = [
        CampoFixo(1, 'REG', 'M305'),
        Campo(2, 'COD_CTA_B'),
        CampoNumerico(3, 'VL_CTA', precisao=2),
        Campo(4, 'IND_VL_CTA'),
    ]


class RegistroM310(Registro):
    """
    Contas Contábeis Relacionadas ao Lançamento da
    Parte A do e-Lalur.
    """
    campos = [
        CampoFixo(1, 'REG', 'M310'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_CTA', precisao=2),
        Campo(5, 'IND_VL_CTA'),
        Campo(6, 'IND_TIPO'),
    ]


class RegistroM312(Registro):
    """
    Números dos Lançamentos Relacionados à Conta Contábil
    """
    campos = [
        CampoFixo(1, 'REG', 'M312'),
        Campo(2, 'NUM_LCTO'),
    ]


class RegistroM315(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    campos = [
        CampoFixo(1, 'REG', 'M315'),
        Campo(2, 'IND_PROC'),
        Campo(3, 'NUM_PROC'),
    ]


class RegistroM350(Registro):
    """
    Lançamentos da Parte A do e-Lacs
    """
    campos = [
        CampoFixo(1, 'REG', 'M350'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO_LANCAMENTO'),
        Campo(5, 'IND_RELACAO'),
        CampoNumerico(6, 'VALOR', precisao=2),
        Campo(7, 'HIST_LAN_LAL'),
    ]


class RegistroM355(Registro):
    """
    Conta da Parte B do e-Lacs
    """
    campos = [
        CampoFixo(1, 'REG', 'M355'),
        Campo(2, 'COD_CTA_B'),
        CampoNumerico(3, 'VL_CTA', precisao=2),
        Campo(4, 'IND_VL_CTA'),
    ]


class RegistroM360(Registro):
    """
    Contas Contábeis Relacionadas ao Lançamento da
    Parte A do e-Lacs.
    """
    campos = [
        CampoFixo(1, 'REG', 'M360'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_CTA', precisao=2),
        Campo(5, 'IND_VL_CTA'),
        Campo(6, 'IND_TIPO'),
    ]


class RegistroM362(Registro):
    """
    Números dos Lançamentos Relacionados à Conta
    Contábil
    """
    campos = [
        CampoFixo(1, 'REG', 'M362'),
        Campo(2, 'NUM_LCTO'),
    ]


class RegistroM365(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    campos = [
        CampoFixo(1, 'REG', 'M365'),
        Campo(2, 'IND_PROC'),
        Campo(3, 'NUM_PROC'),
    ]


class RegistroM410(Registro):
    """
    Lançamentos na Conta da Parte B do e-Lalur e do e-
    Lacs Sem Reflexo na Parte A
    """
    campos = [
        CampoFixo(1, 'REG', 'M410'),
        Campo(2, 'COD_CTA_B'),
        Campo(3, 'COD_TRIBUTO'),
        CampoNumerico(4, 'VAL_LAN_LALB_PB', precisao=2),
        Campo(5, 'IND_VAL_LAN_LALB_PB'),
        Campo(6, 'COD_CTA_B_CTP'),
        Campo(7, 'HIST_LAN_LALB'),
        Campo(8, 'IND_LAN_ANT'),
    ]


class RegistroM415(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    campos = [
        CampoFixo(1, 'REG', 'M415'),
        Campo(2, 'IND_PROC'),
        Campo(3, 'NUM_PROC'),
    ]


class RegistroM500(Registro):
    """
    Controle de Saldos das Contas da Parte B do e-Lalur
    e do e-Lacs
    """
    campos = [
        CampoFixo(1, 'REG', 'M500'),
        Campo(2, 'COD_CTA_B'),
        Campo(3, 'COD_TRIBUTO'),
        Campo(4, 'SD_INI_LAL'),
        Campo(5, 'IND_SD_INI_LAL'),
        CampoNumerico(6, 'VL_LCTO_PARTE_A', precisao=2),
        Campo(7, 'IND_VL_LCTO_PARTE_A'),
        CampoNumerico(8, 'VL_LCTO_PARTEB', precisao=2),
        Campo(9, 'IND_ VL_LCTO_PARTEB'),
        Campo(10, 'SD_FIM_LAL'),
        Campo(11, 'IND_SD_FIM_LAL'),
    ]


class RegistroM990(Registro):
    """
    Encerramento do Bloco M
    """
    campos = [
        CampoFixo(1, 'REG', 'M990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroN001(Registro):
    """
    Abertura do bloco N – Cálculo do IRPJ e da CSLL
    """
    campos = [
        CampoFixo(1, 'REG', 'N001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroN030(Registro):
    """
    Identificação do Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'N030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroN500(Registro):
    """
    Base de Cálculo do IRPJ Sobre o Lucro Real Após
    as Compensações de Prejuízo
    """
    campos = [
        CampoFixo(1, 'REG', 'N500'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN600(Registro):
    """
    Demonstração do Lucro da Exploração
    """
    campos = [
        CampoFixo(1, 'REG', 'N600'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN610(Registro):
    """
    Cálculo da Isenção e Redução do Imposto sobre
    Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'N610'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN615(Registro):
    """
    Informações da Base de Cálculo de Incentivos Fiscais
    """
    campos = [
        CampoFixo(1, 'REG', 'N615'),
        Campo(2, 'BASE_CALC'),
        Campo(3, 'PER_INCEN_FINOR'),
        CampoNumerico(4, 'VL_LIQ_INCEN_FINOR', precisao=2),
        Campo(5, 'PER_INCEN_FINAM'),
        CampoNumerico(6, 'VL_LIQ_INCEN_FINAM', precisao=2),
        CampoNumerico(7, 'VL_SUBTOTAL', precisao=2),
        Campo(8, 'PER_VL_SUBTOTAL'),
        Campo(9, 'PER_INCEN_FUNRES'),
        CampoNumerico(10, 'VL_LIQ_INCEN_FUNRES', precisao=2),
        CampoNumerico(11, 'VL_TOTAL', precisao=2),
        Campo(12, 'PER_VL_TOTAL'),
    ]


class RegistroN620(Registro):
    """
    Cálculo do IRPJ Mensal por Estimativa
    """
    campos = [
        CampoFixo(1, 'REG', 'N620'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN630(Registro):
    """
    Cálculo do IRPJ Com Base no Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'N630'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN650(Registro):
    """
    Base de Cálculo da CSLL Após Compensações das
    Bases de Cálculo Negativa
    """
    campos = [
        CampoFixo(1, 'REG', 'N650'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN660(Registro):
    """
    Cálculo da CSLL Mensal por Estimativa
    """
    campos = [
        CampoFixo(1, 'REG', 'N660'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN670(Registro):
    """
    Cálculo da CSLL Com Base no Lucro Real
    """
    campos = [
        CampoFixo(1, 'REG', 'N670'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroN990(Registro):
    """
    Encerramento do Bloco N
    """
    campos = [
        CampoFixo(1, 'REG', 'N990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroP001(Registro):
    """
    Abertura do Bloco P – Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroP030(Registro):
    """
    Identificação dos Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroP100(Registro):
    """
    Balanço Patrimonial
    """
    campos = [
        CampoFixo(1, 'REG', 'P100'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VAL_CTA_REF_INI', precisao=2),
        Campo(9, 'IND_VAL_CTA_REF_INI'),
        CampoNumerico(10, 'VAL_CTA_REF_FIN', precisao=2),
        Campo(11, 'IND_VAL_CTA_REF_FIN'),
    ]


class RegistroP130(Registro):
    """
    Demonstração das Receitas Incentivadas do Lucro
    Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P130'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP150(Registro):
    """
    Demonstração do Resultado
    """
    campos = [
        CampoFixo(1, 'REG', 'P150'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VALOR', precisao=2),
        Campo(9, 'IND_VALOR'),
    ]


class RegistroP200(Registro):
    """
    Apuração da Base de Cálculo do Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P200'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP230(Registro):
    """
    Cálculo da Isenção e Redução do Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P230'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP300(Registro):
    """
    Cálculo do IRPJ com Base no Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P300'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP400(Registro):
    """
    Apuração da Base de Cálculo da CSLL com Base no
    Lucro Presumido
    """
    campos = [
        CampoFixo(1, 'REG', 'P400'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP500(Registro):
    """
    Cálculo da CSLL com Base no Lucro Líquido
    """
    campos = [
        CampoFixo(1, 'REG', 'P500'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroP990(Registro):
    """
    Encerramento do Bloco P
    """
    campos = [
        CampoFixo(1, 'REG', 'P990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroT001(Registro):
    """
    Abertura do Bloco T – Lucro Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroT030(Registro):
    """
    Identificação dos Período e Forma de Apuração do
    IRPJ e CSLL das Empresas Tributadas pelo Lucro
    Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroT120(Registro):
    """
    Apuração da Base de Cálculo do IRPJ com Base no
    Lucro Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T120'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroT150(Registro):
    """
    Cálculo do Imposto de Renda com Base no Lucro
    Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T150'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroT170(Registro):
    """
    Apuração da Base de Cálculo da CSLL com Base no
    Lucro Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T170'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroT181(Registro):
    """
    Cálculo da CSLL com Base no Lucro Arbitrado
    """
    campos = [
        CampoFixo(1, 'REG', 'T181'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroT990(Registro):
    """
    Encerramento do Bloco T
    """
    campos = [
        CampoFixo(1, 'REG', 'T990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroU001(Registro):
    """
    Abertura do Bloco U – Imunes e Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'U001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroU030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do
    IPRJ e da CSLL das Empressa Imunes e Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'U030'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'PER_APUR'),
    ]


class RegistroU100(Registro):
    """
    Balanço Patrimonial
    """
    campos = [
        CampoFixo(1, 'REG', 'U100'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VAL_CTA_REF_INI', precisao=2),
        Campo(9, 'IND_VAL_CTA_REF_INI'),
        CampoNumerico(10, 'VAL_CTA_REF_FIN', precisao=2),
        Campo(11, 'IND_VAL_CTA_REF_FIN'),
    ]


class RegistroU150(Registro):
    """
    Demonstração do Resultado
    """
    campos = [
        CampoFixo(1, 'REG', 'U150'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        Campo(4, 'TIPO'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_NAT'),
        Campo(7, 'COD_CTA_SUP'),
        CampoNumerico(8, 'VALOR', precisao=2),
        Campo(9, 'IND_VALOR'),
    ]


class RegistroU180(Registro):
    """
    Cálculo do IRPJ das Empresas Imunes ou Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'U180'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroU182(Registro):
    """
    Cálculo da CSLL das Empresas Imunes ou Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'U182'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroU990(Registro):
    """
    Encerramento do Bloco U
    """
    campos = [
        CampoFixo(1, 'REG', 'U990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroX001(Registro):
    """
    Abertura do Bloco X – Informações Econômicas
    """
    campos = [
        CampoFixo(1, 'REG', 'X001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroX280(Registro):
    """
    Atividades Incentivadas - PJ em Geral
    """
    campos = [
        CampoFixo(1, 'REG', 'X280'),
        Campo(2, 'IND_ATIV'),
        Campo(3, 'IND_PROJ'),
        Campo(4, 'ATO_CONC'),
        Campo(5, 'VIG_INI'),
        Campo(6, 'VIG_FIM'),
    ]


class RegistroX291(Registro):
    """
    Operações com o Exterior - Pessoa
    Vinculada/Interposta/País com Tributação
    Favorecida.
    """
    campos = [
        CampoFixo(1, 'REG', 'X291'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX292(Registro):
    """
    Operações com o Exterior - Pessoa Não Vinculada/
    Não Interposta/País sem Tributação Favorecida
    """
    campos = [
        CampoFixo(1, 'REG', 'X292'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX300(Registro):
    """
    Operações com o Exterior - Exportações (Entradas
    de Divisas)
    """
    campos = [
        CampoFixo(1, 'REG', 'X300'),
        Campo(2, 'NUM_ORDEM'),
        Campo(3, 'TIP_EXP'),
        Campo(4, 'DESC_EXP'),
        CampoNumerico(5, 'TOT_OPER', precisao=2),
        Campo(6, 'COD_NCM'),
        CampoNumerico(7, 'QTDE'),
        Campo(8, 'UNI_MED'),
        Campo(9, 'IND_OPER'),
        Campo(10, 'TIP_MET'),
        CampoNumerico(11, 'VL_PAR', precisao=2),
        CampoNumerico(12, 'VL_PRAT', precisao=2),
        CampoNumerico(13, 'VL_AJ', precisao=2),
        CampoNumerico(14, 'VL_JUR', precisao=2),
        CampoNumerico(15, 'VL_JUR_MIN', precisao=2),
        CampoNumerico(16, 'VL_JUR_MAX', precisao=2),
        Campo(17, 'COD_CNC'),
        Campo(18, 'TIP_MOEDA'),
    ]


class RegistroX310(Registro):
    """
    Operações com o Exterior - Contratantes das
    Exportações
    """
    campos = [
        CampoFixo(1, 'REG', 'X310'),
        Campo(2, 'NOME'),
        CampoNumerico(3, 'PAIS'),
        CampoNumerico(4, 'VL_OPER', precisao=2),
        Campo(5, 'COND_PES'),
    ]


class RegistroX320(Registro):
    """
    Operações com o Exterior - Importações (Saídas de Divisas)
    """
    campos = [
        CampoFixo(1, 'REG', 'X320'),
        Campo(2, 'NUM_ORD'),
        Campo(3, 'TIP_IMP'),
        Campo(4, 'DESC_IMP'),
        CampoNumerico(5, 'TOT_OPER', precisao=2),
        Campo(6, 'COD_NCM'),
        CampoNumerico(7, 'QTDE'),
        Campo(8, 'UNI_MED'),
        Campo(9, 'TIP_MET'),
        CampoNumerico(10, 'VL_PAR', precisao=2),
        CampoNumerico(11, 'VL_PRAT', precisao=2),
        CampoNumerico(12, 'VL_AJ', precisao=2),
        CampoNumerico(13, 'VL_JUR', precisao=2),
        CampoNumerico(14, 'VL_JUR_MIN', precisao=2),
        CampoNumerico(15, 'VL_JUR_MAX', precisao=2),
        Campo(16, 'COD_CNC'),
        Campo(17, 'TIP_MOEDA'),
    ]


class RegistroX330(Registro):
    """
    Operações com o Exterior - Contratantes das
    Importações
    """
    campos = [
        CampoFixo(1, 'REG', 'X330'),
        Campo(2, 'NOME'),
        CampoNumerico(3, 'PAIS'),
        CampoNumerico(4, 'VL_OPER', precisao=2),
        Campo(5, 'COND_PES'),
    ]


class RegistroX340(Registro):
    """
    Identificação da Participação no Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'X340'),
        Campo(2, 'RAZ_SOCIAL'),
        Campo(3, 'NIF'),
        Campo(4, 'IND_CONTROLE'),
        CampoNumerico(5, 'PAIS'),
        Campo(6, 'IND_REPETRO'),
        Campo(7, 'IND_CONSOL'),
        Campo(8, 'MOT_NAO_CONSOL'),
    ]


class RegistroX350(Registro):
    """
    Participações no Exterior - Resultado do Período de
    Apuração
    """
    campos = [
        CampoFixo(1, 'REG', 'X350'),
        CampoNumerico(2, 'REC_LIQ'),
        CampoNumerico(3, 'CUSTOS'),
        CampoNumerico(4, 'LUC_BRUTO'),
        CampoNumerico(5, 'REC_AUFERIDAS'),
        CampoNumerico(6, 'REC_OUTRAS_OPER'),
        CampoNumerico(7, 'DESP_BRASIL'),
        CampoNumerico(8, 'DESP_OPER'),
        CampoNumerico(9, 'LUC_OPER'),
        CampoNumerico(10, 'REC_PARTIC'),
        CampoNumerico(11, 'REC_OUTRAS'),
        CampoNumerico(12, 'DESP_OUTRAS'),
        CampoNumerico(13, 'LUC_LIQ_ANT_IR'),
        CampoNumerico(14, 'IMP_DEV'),
        CampoNumerico(15, 'LUC_LIQ'),
        CampoNumerico(16, 'LUC_ARB_ANT_IMP'),
        CampoNumerico(17, 'IMP_DEV_ARB'),
        CampoNumerico(18, 'LUC_ARB_PER_APUR'),
    ]


class RegistroX351(Registro):
    """
    Demonstrativo de Resultados e de Imposto a Pagar
    no Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'X351'),
        CampoNumerico(2, 'RES_INV_PER'),
        CampoNumerico(3, 'RES_INV_PER_REAL'),
        CampoNumerico(4, 'RES_REPRETO_PER'),
        CampoNumerico(5, 'RES_REPRETO_PER_REAL'),
        CampoNumerico(6, 'RES_NEG_ACUM'),
        CampoNumerico(7, 'RES_POS_TRIB'),
        CampoNumerico(8, 'RES_POS_TRIB_REAL'),
        CampoNumerico(9, 'IMP_PAG'),
        CampoNumerico(10, 'IMP_PAG_REAL'),
        CampoNumerico(11, 'IMP_PAG_REND'),
        CampoNumerico(12, 'IMP_PAG_REND_REAL'),
    ]


class RegistroX352(Registro):
    """
    Demonstrativo de Resultados no Exterior de
    Coligadas em Regime de Caixa
    """
    campos = [
        CampoFixo(1, 'REG', 'X352'),
        CampoNumerico(2, 'RES_PER'),
        CampoNumerico(3, 'RES_PER_REAL'),
        CampoNumerico(4, 'LUC_DISP'),
        CampoNumerico(5, 'LUC_DISP_REAL'),
    ]


class RegistroX353(Registro):
    """
    Demonstrativo de Consolidação
    """
    campos = [
        CampoFixo(1, 'REG', 'X353'),
        CampoNumerico(2, 'RES_NEG_UTIL'),
        CampoNumerico(3, 'RES_NEG_UTIL_REAL'),
        CampoNumerico(4, 'SALDO_RES_NEG_NAO_UTIL'),
        CampoNumerico(5, 'SALDO_RES_NEG_NAO_UTIL_REAL'),
    ]


class RegistroX354(Registro):
    """
    Demonstrativo de Prejuízos Acumulados
    """
    campos = [
        CampoFixo(1, 'REG', 'X354'),
        CampoNumerico(2, 'RES_NEG'),
        CampoNumerico(3, 'RES_NEG_REAL'),
        CampoNumerico(4, 'SALDO_RES_NEG'),
    ]


class RegistroX355(Registro):
    """
    Demonstrativo de Rendas Ativas e passivas
    """
    campos = [
        CampoFixo(1, 'REG', 'X355'),
        CampoNumerico(2, 'REND_PASS_PROP'),
        CampoNumerico(3, 'REND_PASS_PROP_REAL'),
        CampoNumerico(4, 'REND_TOTAL'),
        CampoNumerico(5, 'REND_TOTAL_REAL'),
        CampoNumerico(6, 'REND_ATIV_PROP'),
        CampoNumerico(7, 'REND_ATIV_PROP_REAL'),
        CampoNumerico(8, 'PERCENTUAL'),
    ]


class RegistroX356(Registro):
    """
    Demonstrativo de Estrutura Societária
    """
    campos = [
        CampoFixo(1, 'REG', 'X356'),
        CampoNumerico(2, 'PERC_PART'),
        CampoNumerico(3, 'ATIVO_TOTAL'),
        CampoNumerico(4, 'PAT_LIQUIDO'),
    ]


class RegistroX356(Registro):
    """
    Demonstrativo de Imposto Pago no Exterior
    """
    # TODO: Registro não definido no arquivo ECF
    campos = [
        CampoFixo(1, 'REG', 'X366'),
    ]


class RegistroX390(Registro):
    """
    Origem e Aplicação de Recursos - Imunes ou Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'X390'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX400(Registro):
    """
    Comércio Eletrônico e Tecnologia da Informação
    """
    campos = [
        CampoFixo(1, 'REG', 'X400'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX410(Registro):
    """
    Comércio Eletrônico
    """
    campos = [
        CampoFixo(1, 'REG', 'X410'),
        CampoNumerico(2, 'PAIS'),
        Campo(3, 'IND_HOME_DISP'),
        Campo(4, 'IND_SERV_DISP'),
    ]


class RegistroX420(Registro):
    """
    Royalties Recebidos ou Pagos a Beneficiários do
    Brasil e do Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'X420'),
        Campo(2, 'TIP_ROY'),
        CampoNumerico(3, 'PAIS'),
        CampoNumerico(4, 'VL_EXPL_DIR_SW', precisao=2),
        CampoNumerico(5, 'VL_EXPL_DIR_AUT', precisao=2),
        CampoNumerico(6, 'VL_EXPL_MARCA', precisao=2),
        CampoNumerico(7, 'VL_EXPL_PAT', precisao=2),
        CampoNumerico(8, 'VL_EXPL_KNOW', precisao=2),
        CampoNumerico(9, 'VL_EXPL_FRANQ', precisao=2),
        CampoNumerico(10, 'VL_EXPL_INT', precisao=2),
    ]


class RegistroX430(Registro):
    """
    Rendimentos Relativos a Serviços, Juros e
    Dividendos Recebidos do Brasil e do Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'X430'),
        CampoNumerico(2, 'PAIS'),
        CampoNumerico(3, 'VL_SERV_ASSIST', precisao=2),
        CampoNumerico(4, 'VL_SERV_SEM_ASSIST', precisao=2),
        CampoNumerico(5, 'VL_SERV_SEM_ASSIST_EXT', precisao=2),
        CampoNumerico(6, 'VL_JURO', precisao=2),
        CampoNumerico(7, 'VL_DEMAIS_JUROS', precisao=2),
        CampoNumerico(8, 'VL_DIVID', precisao=2),
    ]


class RegistroX450(Registro):
    """
    Pagamentos/Remessas Relativos a Serviços, Juros e
    Dividendos Recebidos do Brasil e do Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'X450'),
        CampoNumerico(2, 'PAIS'),
        CampoNumerico(3, 'VL_SERV_ASSIST', precisao=2),
        CampoNumerico(4, 'VL_SERV_SEM_ASSIST', precisao=2),
        CampoNumerico(5, 'VL_SERV_SEM_ASSIST_EXT', precisao=2),
        CampoNumerico(6, 'VL_JURO_PF', precisao=2),
        CampoNumerico(7, 'VL_JURO_PJ', precisao=2),
        CampoNumerico(8, 'VL_DEMAIS_JUROS', precisao=2),
        CampoNumerico(9, 'VL_DIVID_PF', precisao=2),
        CampoNumerico(10, 'VL_DIVID_PJ', precisao=2),
    ]


class RegistroX460(Registro):
    """
    Inovação Tecnológica e Desenvolvimento
    Tecnológico
    """
    campos = [
        CampoFixo(1, 'REG', 'X460'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX470(Registro):
    """
    Capacitação de Informática e Inclusão Digital
    """
    campos = [
        CampoFixo(1, 'REG', 'X470'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX480(Registro):
    """
    Repes, Recap, Padis, PATVD, Reidi, Repenec,
    Reicomp, Retaero, Recine, Resíduos Sólidos,
    Recopa, Copa do Mundo, Retid, REPNBL-Redes,
    Reif e Olimpíadas
    """
    campos = [
        CampoFixo(1, 'REG', 'X480'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX490(Registro):
    """
    Pólo Industrial de Manaus e Amazônia Ocidental
    """
    campos = [
        CampoFixo(1, 'REG', 'X490'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX500(Registro):
    """
    Zonas de Processamento de Exportação (ZPE)
    """
    campos = [
        CampoFixo(1, 'REG', 'X500'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX510(Registro):
    """
    Áreas de Livre Comércio (ALC)
    """
    campos = [
        CampoFixo(1, 'REG', 'X510'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroX990(Registro):
    """
    Encerramento do Bloco X
    """
    campos = [
        CampoFixo(1, 'REG', 'X990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class RegistroY001(Registro):
    """
    Abertura do Bloco Y – Informações Gerais
    """
    campos = [
        CampoFixo(1, 'REG', 'Y001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroY520(Registro):
    """
    Pagamentos/Recebimentos do Exterior ou de Não
    Residentes
    """
    campos = [
        CampoFixo(1, 'REG', 'Y520'),
        Campo(2, 'TIP_EXT'),
        CampoNumerico(3, 'PAIS'),
        Campo(4, 'FORMA'),
        Campo(5, 'NAT_OPER'),
        CampoNumerico(6, 'VL_PERIODO', precisao=2),
    ]


class RegistroY540(Registro):
    """
    Discriminação da Receita de Vendas dos
    Estabelecimentos por Atividade Econômica
    """
    campos = [
        CampoFixo(1, 'REG', 'Y540'),
        CampoCNPJ(2, 'CNPJ_ESTAB'),
        CampoNumerico(3, 'VL_REC_ESTAB', precisao=2),
        Campo(4, 'CNAE'),
    ]


class RegistroY550(Registro):
    """
    Vendas a Comercial Exportadora com Fim
    Específico de Exportação
    """
    campos = [
        CampoFixo(1, 'REG', 'Y550'),
        CampoCNPJ(2, 'CNPJ_EXP'),
        Campo(3, 'COD_NCM'),
        CampoNumerico(4, 'VL_VENDA', precisao=2),
    ]


class RegistroY560(Registro):
    """
    Detalhamento das Exportações da Comercial
    Exportadora
    """
    campos = [
        CampoFixo(1, 'REG', 'Y560'),
        CampoCNPJ(2, 'CNPJ'),
        Campo(3, 'COD_NCM'),
        CampoNumerico(4, 'VL_COMPRA', precisao=2),
        CampoNumerico(5, 'VL_EXP', precisao=2),
    ]


class RegistroY570(Registro):
    """
    Demonstrativo do Imposto de Renda e CSLL
    Retidos na Fonte
    """
    campos = [
        CampoFixo(1, 'REG', 'Y570'),
        CampoCNPJ(2, 'CNPJ_FON'),
        Campo(3, 'NOM_EMP'),
        Campo(4, 'IND_ORG_PUB'),
        Campo(5, 'COD_REC'),
        CampoNumerico(6, 'VL_REND', precisao=2),
        CampoNumerico(7, 'IR_RET', precisao=2),
        CampoNumerico(8, 'CSLL_RET', precisao=2),
    ]


class RegistroY580(Registro):
    """
    Doações a Campanhas Eleitorais
    """
    campos = [
        CampoFixo(1, 'REG', 'Y580'),
        CampoCNPJ(2, 'CNPJ'),
        Campo(3, 'TIP_BENEF'),
        Campo(4, 'FORM_DOA'),
        CampoNumerico(5, 'VL_DOA', precisao=2),
    ]


class RegistroY590(Registro):
    """
    Ativos no Exterior
    """
    campos = [
        CampoFixo(1, 'REG', 'Y590'),
        Campo(2, 'TIP_ATIVO'),
        CampoNumerico(3, 'PAIS'),
        Campo(4, 'DISCRIMINACAO'),
        CampoNumerico(5, 'VL_ANT', precisao=2),
        CampoNumerico(6, 'VL_ATUAL', precisao=2),
    ]


class RegistroY600(Registro):
    """
    Identificação de Sócios ou Titular
    """
    campos = [
        CampoFixo(1, 'REG', 'Y600'),
        CampoData(2, 'DT_ALT_SOC'),
        CampoData(3, 'DT_FIM_SOC'),
        CampoNumerico(4, 'PAIS'),
        Campo(5, 'IND_QUALIF_SOCIO'),
        Campo(6, 'CPF_CNPJ'),
        Campo(7, 'NOM_EMP'),
        Campo(8, 'QUALIF'),
        CampoNumerico(9, 'PERC_CAP_TOT'),
        CampoNumerico(10, 'PERC_CAP_VOT'),
        Campo(11, 'CPF_REP_LEG'),
        Campo(12, 'QUALIF_REP_LEG'),
    ]


class RegistroY611(Registro):
    """
    Rendimentos de Dirigentes, Conselheiros, Sócios ou
    Titular
    """
    campos = [
        CampoFixo(1, 'REG', 'Y611'),
        CampoNumerico(2, 'PAIS'),
        Campo(3, 'IND_PF_PJ'),
        Campo(4, 'CPF_CNPJ'),
        Campo(5, 'NOM_EMP'),
        Campo(6, 'QUALIF'),
        CampoNumerico(7, 'VL_REM_TRAB', precisao=2),
        CampoNumerico(8, 'VL_LUC_DIV', precisao=2),
        CampoNumerico(9, 'VL_JUR_CAP', precisao=2),
        CampoNumerico(10, 'VL_DEM_REND', precisao=2),
        CampoNumerico(11, 'VL_IR_RET', precisao=2),
    ]


class RegistroY612(Registro):
    """
    Rendimentos de Dirigentes e Conselheiros - Imunes
    ou Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'Y612'),
        Campo(2, 'CPF'),
        Campo(3, 'NOME'),
        Campo(4, 'QUALIF'),
        CampoNumerico(5, 'VL_REM_TRAB', precisao=2),
        CampoNumerico(6, 'VL_DEM_REND', precisao=2),
        CampoNumerico(7, 'VL_IR_RET', precisao=2),
    ]


class RegistroY620(Registro):
    """
    Participação Avaliada pelo Método de Equivalência
    Patrimonial
    """
    campos = [
        CampoFixo(1, 'REG', 'Y620'),
        CampoNumerico(2, 'PAIS'),
        CampoCNPJ(3, 'CNPJ'),
        Campo(4, 'NOM_EMP'),
        CampoNumerico(5, 'VALOR_REAIS'),
        CampoNumerico(6, 'VALOR_ESTR'),
        CampoNumerico(7, 'PERC_CAP_TOT'),
        CampoNumerico(8, 'PERC_CAP_VOT'),
        CampoNumerico(9, 'RES_EQ_PAT'),
        Campo(10, 'DATA_AQUIS'),
        Campo(11, 'IND_PROC_CART'),
        Campo(12, 'NUM_PROC_CART'),
        Campo(13, 'NOME_CART'),
        Campo(14, 'IND_PROC_RFB'),
        Campo(15, 'NUM_PROC_RFB'),
    ]


class RegistroY630(Registro):
    """
    Fundos/Clubes de Investimento
    """
    campos = [
        CampoFixo(1, 'REG', 'Y630'),
        CampoCNPJ(2, 'CNPJ'),
        Campo(3, 'QTE_QUOT'),
        Campo(4, 'QTE_QUOTA'),
        Campo(5, 'PATR_FIN_PER'),
        Campo(6, 'DAT_ABERT'),
        Campo(7, 'DAT_ENCER'),
    ]


class RegistroY640(Registro):
    """
    Participações em Consórcios de Empresas
    """
    campos = [
        CampoFixo(1, 'REG', 'Y640'),
        CampoCNPJ(2, 'CNPJ'),
        Campo(3, 'COND_DECL'),
        CampoNumerico(4, 'VL_CONS', precisao=2),
        CampoCNPJ(5, 'CNPJ_LID'),
        CampoNumerico(6, 'VL_DECL', precisao=2),
    ]


class RegistroY650(Registro):
    """
    Participantes do Consórcio
    """
    campos = [
        CampoFixo(1, 'REG', 'Y650'),
        CampoCNPJ(2, 'CNPJ'),
        CampoNumerico(3, 'VL_PART', precisao=2),
    ]


class RegistroY660(Registro):
    """
    Dados de Sucessoras
    """
    campos = [
        CampoFixo(1, 'REG', 'Y660'),
        CampoCNPJ(2, 'CNPJ'),
        Campo(3, 'NOM_EMP'),
        CampoNumerico(4, 'PERC_PAT_LIQ'),
    ]


class RegistroY665(Registro):
    """
    Demonstrativo das Diferenças na Adoção Inicial
    """
    campos = [
        CampoFixo(1, 'REG', 'Y665'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'DESC_CTA'),
        CampoNumerico(5, 'VL_SALDO_SOC', precisao=2),
        Campo(6, 'IND_VL_SALDO_SOC'),
        CampoNumerico(7, 'VL_SALDO_FIS', precisao=2),
        Campo(8, 'IND_VL_SALDO_FIS'),
        Campo(9, 'DIF_SALDOS'),
        Campo(10, 'IND_DIF_SALDOS'),
        Campo(11, 'MET_CONTR'),
        Campo(12, 'COD_SUBCONT'),
        Campo(13, 'COD_CCUS_SUB'),
        Campo(14, 'DESC_SUB'),
    ]


class RegistroY671(Registro):
    """
    Outras Informações
    """
    campos = [
        CampoFixo(1, 'REG', 'Y671'),
        CampoNumerico(2, 'VL_AQ_MAQ', precisao=2),
        CampoNumerico(3, 'VL_DOA_CRIANCA', precisao=2),
        CampoNumerico(4, 'VL_DOA_IDOSO', precisao=2),
        CampoNumerico(5, 'VL_AQ_IMOBILIZADO', precisao=2),
        CampoNumerico(6, 'VL_BX_IMOBILIZADO', precisao=2),
        CampoNumerico(7, 'VL_INC_INI', precisao=2),
        CampoNumerico(8, 'VL_INC_FIN', precisao=2),
        CampoNumerico(9, 'VL_CSLL_DEPREC_INI', precisao=2),
        CampoNumerico(10, 'VL_DIF_IC_VC', precisao=2),
        CampoNumerico(11, 'VL_OC_SEM_IOF', precisao=2),
        CampoNumerico(12, 'VL_FOLHA_ALIQ_RED', precisao=2),
        CampoNumerico(13, 'VL_ALIQ_RED', precisao=2),
        Campo(14, 'IND_ALTER_CAPITAL'),
        Campo(15, 'IND_BCN_CSLL'),
    ]


class RegistroY672(Registro):
    """
    Outras Informações (Lucro Presumido ou Lucro
    Arbitrado)
    """
    campos = [
        CampoFixo(1, 'REG', 'Y672'),
        CampoNumerico(2, 'VL_CAPITAL_ANT', precisao=2),
        CampoNumerico(3, 'VL_CAPITAL', precisao=2),
        CampoNumerico(4, 'VL_ESTOQUE_ANT', precisao=2),
        CampoNumerico(5, 'VL_ESTOQUES', precisao=2),
        CampoNumerico(6, 'VL_CAIXA_ANT', precisao=2),
        CampoNumerico(7, 'VL_CAIXA', precisao=2),
        CampoNumerico(8, 'VL_APLIC_FIN_ANT', precisao=2),
        CampoNumerico(9, 'VL_APLIC_FIN', precisao=2),
        CampoNumerico(10, 'VL_CTA_REC_ANT', precisao=2),
        CampoNumerico(11, 'VL_CTA_REC', precisao=2),
        CampoNumerico(12, 'VL_CTA_PAG_ANT', precisao=2),
        CampoNumerico(13, 'VL_CTA_PAG', precisao=2),
        CampoNumerico(14, 'VL_COMPRA_MERC', precisao=2),
        CampoNumerico(15, 'VL_COMPRA_ATIVO', precisao=2),
        CampoNumerico(16, 'VL_RECEITAS', precisao=2),
        CampoNumerico(17, 'TOT_ATIVO', precisao=2),
        CampoNumerico(18, 'VL_FOLHA', precisao=2),
        CampoNumerico(19, 'VL_ALIQ_RED', precisao=2),
        Campo(20, 'IND_REG_APUR'),
        Campo(21, 'IND_AVAL_ESTOQ'),
    ]


class RegistroY680(Registro):
    """
    Mês das Informações de Optantes pelo Refis (Lucro
    Real, Presumido e Arbitrado)
    """
    campos = [
        CampoFixo(1, 'REG', 'Y680'),
        Campo(2, 'MES'),
    ]


class RegistroY681(Registro):
    """
    Informações de Optantes pelo Refis (Lucro Real,
    Presumido e Arbitrado)
    """
    campos = [
        CampoFixo(1, 'REG', 'Y681'),
        Campo(2, 'CODIGO'),
        CampoAlfanumerico(3, 'DESCRICAO'),
        CampoNumerico(4, 'VALOR', precisao=2),
    ]


class RegistroY682(Registro):
    """
    Informações de Optantes pelo Refis - Imunes ou
    Isentas
    """
    campos = [
        CampoFixo(1, 'REG', 'Y682'),
        Campo(2, 'MES'),
        Campo(3, 'ACRES_PATR'),
    ]


class RegistroY690(Registro):
    """
    Informações de Optantes pelo Paes
    """
    campos = [
        CampoFixo(1, 'REG', 'Y690'),
        Campo(2, 'MES'),
        CampoNumerico(3, 'VL_REC_BRU', precisao=2),
    ]


class RegistroY800(Registro):
    """
    Outras Informações
    """
    campos = [
        CampoFixo(1, 'REG', 'Y800'),
        Campo(2, 'ARQ_RTF'),
        Campo(3, 'IND_FIM_RTF'),
    ]


class RegistroY990(Registro):
    """
    Encerramento do Bloco Y
    """
    campos = [
        CampoFixo(1, 'REG', 'Y990'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class Registro9001(Registro):
    """
    Abertura do Bloco 9
    """
    campos = [
        CampoFixo(1, 'REG', '9001'),
        Campo(2, 'IND_DAD'),
    ]


class Registro9100(Registro):
    """
    Avisos da Escrituração
    """
    campos = [
        CampoFixo(1, 'REG', '9100'),
        # TODO: Campo 2 não está definido
        Campo(2, ''),
        Campo(3, 'MSG_REGRA'),
        Campo(4, 'REGISTRO'),
        Campo(5, 'CAMPO'),
        Campo(6, 'CONTEÚDO'),
        CampoNumerico(7, 'VALOR_ESPERADO'),
    ]


class Registro9900(Registro):
    """
    Registros do Arquivo
    """
    campos = [
        CampoFixo(1, 'REG', '9900'),
        Campo(2, 'REG_BLC'),
        CampoNumerico(3, 'QTD_REG_BLC'),
        Campo(4, 'VERSAO'),
        Campo(5, 'ID_TAB_DIN'),
    ]


class Registro9099(Registro):
    """
    Encerramento do Bloco 9
    """
    campos = [
        CampoFixo(1, 'REG', '9099'),
        CampoNumerico(2, 'QTD_LIN'),
    ]


class Registro9999(Registro):
    """
    Encerramento do Arquivo Digital
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        CampoNumerico(2, 'QTD_LIN'),
    ]

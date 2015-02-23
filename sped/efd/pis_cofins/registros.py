# -*- coding: utf-8 -*-

from ...campos import Campo
from ...campos import CampoAlfanumerico
from ...campos import CampoCNPJ
from ...campos import CampoData
from ...campos import CampoFixo
from ...campos import CampoNumerico
from ...campos import CampoRegex
from ...registros import Registro


class Registro0000(Registro):
    """
    Abertura do Arquivo Digital e Identificação da Pessoa Jurídica

    >>> line = '|0000|002|0|||01042011|30042011|EMPRESA YYY|77777777000191|MG|3106200||00|0|'
    >>> r = Registro0000(line)
    >>> r.REG
    '0000'
    >>> r.COD_VER
    '002'
    >>> r.TIPO_ESCRIT
    '0'
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoAlfanumerico(2, 'COD_VER', obrigatorio=True, tamanho=3),
        CampoRegex(3, 'TIPO_ESCRIT', obrigatorio=True, regex='[01]'),
        CampoRegex(4, 'IND_SIT_ESP', regex='[0-4]'),
        CampoAlfanumerico(5, 'NUM_REC_ANTERIOR', tamanho=41),
        CampoData(6, 'DT_INI', obrigatorio=True),
        CampoData(7, 'DT_FIN', obrigatorio=True),
        Campo(8, 'NOME', obrigatorio=True),
        CampoCNPJ(9, 'CNPJ', obrigatorio=True),
        Campo(10, 'UF', obrigatorio=True),
        Campo(11, 'COD_MUN', obrigatorio=True),
        Campo(12, 'SUFRAMA'),
        Campo(13, 'IND_NAT_PJ'),
        Campo(14, 'IND_ATIV', obrigatorio=True),
    ]


class Registro0001(Registro):
    """
    Abertura do Bloco 0
    """
    campos = [
        CampoFixo(1, 'REG', '0001'),
        Campo(2, 'IND_MOV', obrigatorio=True)
    ]


class Registro0035(Registro):
    """
    Identificação da Sociedade em Conta de Participação - SCP
    """
    campos = [
        CampoFixo(1, 'REG', '0035'),
        Campo(2, 'COD_SCP', obrigatorio=True),
        Campo(3, 'DESC_SCP', obrigatorio=True),
        Campo(4, 'INF_COMP', obrigatorio=True),
    ]


class Registro0100(Registro):
    """
    Dados do Contabilista
    """
    campos = [
        CampoFixo(1, 'REG', '0100'),
        Campo(2, 'NOME', obrigatorio=True),
        Campo(3, 'CPF', obrigatorio=True),
        Campo(4, 'CRC', obrigatorio=True),
        CampoCNPJ(5, 'CNPJ'),
        Campo(6, 'CEP'),
        Campo(7, 'END'),
        Campo(8, 'NUM'),
        Campo(9, 'COMPL'),
        Campo(10, 'BAIRRO'),
        Campo(11, 'FONE'),
        Campo(12, 'FAX'),
        Campo(13, 'EMAIL'),
        Campo(14, 'COD_MUN'),
    ]


class Registro0110(Registro):
    """
    Regimes de Apuração da Contribuição Social e de Apropriação de Crédito
    """
    campos = [
        CampoFixo(1, 'REG', '0110'),
        Campo(2, 'COD_INC_TRIB', obrigatorio=True),
        Campo(3, 'IND_APRO_CRED'),
        Campo(4, 'COD_TIPO_CONT'),
        Campo(5, 'IND_REG_CUM'),
    ]


class Registro0111(Registro):
    """
    Tabela de Receita Bruta Mensal para Fins de Rateio de Créditos Comuns
    """
    campos = [
        CampoFixo(1, 'REG', '0111'),
        CampoNumerico(2, 'REC_BRU_NCUM_TRIB_MI', obrigatorio=True),
        CampoNumerico(3, 'REC_BRU_NCUM_NT_MI', obrigatorio=True),
        CampoNumerico(4, 'REC_BRU_NCUM_EXP', obrigatorio=True),
        CampoNumerico(5, 'REC_BRU_CUM', obrigatorio=True),
        CampoNumerico(6, 'REC_BRU_TOTAL', obrigatorio=True),
    ]


class Registro0120(Registro):
    """
    Identificação de Períodos Dispensados da Escrituração Digital
    """
    campos = [
        CampoFixo(1, 'REG', '0120'),
        Campo(2, 'MES_DISPENSA', obrigatorio=True),
        Campo(3, 'INF_COMP'),
    ]


class Registro0140(Registro):
    """
    Tabela de Cadastro de Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', '0140'),
        Campo(2, 'COD_EST'),
        Campo(3, 'NOME', obrigatorio=True),
        CampoCNPJ(4, 'CNPJ', obrigatorio=True),
        Campo(5, 'UF', obrigatorio=True),
        Campo(6, 'IE'),
        Campo(7, 'COD_MUN', obrigatorio=True),
        Campo(8, 'IM'),
        Campo(9, 'SUFRAMA'),
    ]


class Registro0145(Registro):
    """
    Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta
    """
    campos = [
        CampoFixo(1, 'REG', '0145'),
        Campo(2, 'COD_INC_TRIB', obrigatorio=True),
        CampoNumerico(3, 'VL_REC_TOT', obrigatorio=True),
        CampoNumerico(4, 'VL_REC_ATIV', obrigatorio=True),
        CampoNumerico(5, 'VL_REC_DEMAIS_ATIV'),
        Campo(6, 'INFO_COMPL'),
    ]


class Registro0150(Registro):
    """
    Tabela de Cadastro do Participante
    """
    campos = [
        CampoFixo(1, 'REG', '0150'),
        Campo(2, 'COD_PART', obrigatorio=True),
        Campo(3, 'NOME', obrigatorio=True),
        Campo(4, 'COD_PAIS', obrigatorio=True),
        CampoCNPJ(5, 'CNPJ'),
        Campo(6, 'CPF'),
        Campo(7, 'IE'),
        Campo(8, 'COD_MUN'),
        Campo(9, 'SUFRAMA'),
        Campo(10, 'END'),
        Campo(11, 'NUM'),
        Campo(12, 'COMPL'),
        Campo(13, 'BAIRRO'),
    ]


class Registro0190(Registro):
    """
    Identificação das Unidades de Medida
    """
    campos = [
        CampoFixo(1, 'REG', '0190'),
        Campo(2, 'UNID', obrigatorio=True),
        Campo(3, 'DESCR', obrigatorio=True),
    ]


class Registro0200(Registro):
    """
    Tabela de Identificação do Item (Produtos e Serviços)
    """
    campos = [
        CampoFixo(1, 'REG', '0200'),
        Campo(2, 'COD_ITEM', obrigatorio=True),
        Campo(3, 'DESCR_ITEM', obrigatorio=True),
        Campo(4, 'COD_BARRA'),
        Campo(5, 'COD_ANT_ITEM'),
        Campo(6, 'UNID_INV'),
        Campo(7, 'TIPO_ITEM', obrigatorio=True),
        Campo(8, 'COD_NCM'),
        Campo(9, 'EX_IPI'),
        Campo(10, 'COD_GEN'),
        Campo(11, 'COD_LST'),
        CampoNumerico(12, 'ALIQ_ICMS'),
    ]


class Registro0205(Registro):
    """
    Alteração do Item
    """
    campos = [
        CampoFixo(1, 'REG', '0205'),
        Campo(2, 'DESCR_ANT_ITEM'),
        CampoData(3, 'DT_INI', obrigatorio=True),
        CampoData(4, 'DT_FIM', obrigatorio=True),
        Campo(5, 'COD_ANT_ITEM'),
    ]


class Registro0206(Registro):
    """
    Código de Produto conforme Tabela ANP (Combustíveis)
    """
    campos = [
        CampoFixo(1, 'REG', '0206'),
        Campo(2, 'COD_COMB', obrigatorio=True),
    ]


class Registro0208(Registro):
    """
    Código de Grupos por Marca Comercial – REFRI (Bebidas Frias)
    """
    campos = [
        CampoFixo(1, 'REG', '0208'),
        Campo(2, 'COD_TAB', obrigatorio=True),
        Campo(3, 'COD_GRU', obrigatorio=True),
        Campo(4, 'MARCA_COM', obrigatorio=True),
    ]


class Registro0400(Registro):
    """
    Tabela de Natureza da Operação/ Prestação
    """
    campos = [
        CampoFixo(1, 'REG', '0400'),
        Campo(2, 'COD_NAT', obrigatorio=True),
        Campo(3, 'DESCR_NAT', obrigatorio=True),
    ]


class Registro0450(Registro):
    """
    Tabela de Informação Complementar do Documento Fiscal
    """
    campos = [
        CampoFixo(1, 'REG', '0450'),
        Campo(2, 'COD_INF', obrigatorio=True),
        Campo(3, 'TXT', obrigatorio=True),
    ]


class Registro0500(Registro):
    """
    Plano de Contas Contábeis – Contas Informadas
    """
    campos = [
        CampoFixo(1, 'REG', '0500'),
        CampoData(2, 'DT_ALT', obrigatorio=True),
        Campo(3, 'COD_NAT_CC', obrigatorio=True),
        Campo(4, 'IND_CTA', obrigatorio=True),
        Campo(5, 'NÍVEL', obrigatorio=True),
        Campo(6, 'COD_CTA', obrigatorio=True),
        Campo(7, 'NOME_CTA', obrigatorio=True),
        Campo(8, 'COD_CTA_REF'),
        CampoCNPJ(9, 'CNPJ_EST'),
    ]


class Registro0600(Registro):
    """
    Centro de Custos
    """
    campos = [
        CampoFixo(1, 'REG', '0600'),
        CampoData(2, 'DT_ALT', obrigatorio=True),
        Campo(3, 'COD_CCUS', obrigatorio=True),
        Campo(4, 'CCUS', obrigatorio=True),
    ]


class Registro0990(Registro):
    """
    Encerramento do Bloco 0
    """
    campos = [
        CampoFixo(1, 'REG', '0990'),
        CampoNumerico(2, 'QTD_LIN_0', obrigatorio=True),
    ]


class RegistroA001(Registro):
    """
    Abertura do Bloco A
    """
    campos = [
        CampoFixo(1, 'REG', 'A001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroA010(Registro):
    """
    Identificação do Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', 'A010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
    ]


class RegistroA100(Registro):
    """
    Documento – Nota Fiscal de Serviço
    """
    campos = [
        CampoFixo(1, 'REG', 'A100'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'IND_EMIT', obrigatorio=True),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_SIT', obrigatorio=True),
        Campo(6, 'SER'),
        Campo(7, 'SUB'),
        Campo(8, 'NUM_DOC', obrigatorio=True),
        Campo(9, 'CHV_NFSE'),
        CampoData(10, 'DT_DOC', obrigatorio=True),
        CampoData(11, 'DT_EXE_SERV', obrigatorio=True),
        CampoNumerico(12, 'VL_DOC'),
        Campo(13, 'IND_PGTO', obrigatorio=True),
        CampoNumerico(14, 'VL_DESC'),
        CampoNumerico(15, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(16, 'VL_PIS', obrigatorio=True),
        CampoNumerico(17, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(18, 'VL_COFINS', obrigatorio=True),
        CampoNumerico(19, 'VL_PIS_RET',),
        CampoNumerico(20, 'VL_COFINS_RET'),
        CampoNumerico(21, 'VL_ISS'),
    ]


class RegistroA110(Registro):
    """
    Complemento de Documento – Informação Complementar da NF
    """
    campos = [
        CampoFixo(1, 'REG', 'A110'),
        Campo(2, 'COD_INF', obrigatorio=True),
        Campo(3, 'TXT_COMPL'),
    ]


class RegistroA111(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'A111'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroA120(Registro):
    """
    Informação Complementar – Operações de Importação
    """
    campos = [
        CampoFixo(1, 'REG', 'A120'),
        CampoNumerico(2, 'VL_TOT_SERV', obrigatorio=True),
        CampoNumerico(3, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_PIS_IMP'),
        CampoData(5, 'DT_PAG_PIS'),
        CampoNumerico(6, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(7, 'VL_COFINS_IMP'),
        CampoData(8, 'DT_PAG_COFINS'),
        Campo(9, 'LOC_EXE_SERV', obrigatorio=True),
    ]


class RegistroA170(Registro):
    """
    Complemento de Documento – Itens do Documento
    """
    campos = [
        CampoFixo(1, 'REG', 'A170'),
        Campo(2, 'NUM_ITEM', obrigatorio=True),
        Campo(3, 'COD_ITEM', obrigatorio=True),
        Campo(4, 'DESCR_COMPL'),
        CampoNumerico(5, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(6, 'VL_DESC'),
        Campo(7, 'NAT_BC_CRED'),
        Campo(8, 'IND_ORIG_CRED'),
        Campo(9, 'CST_PIS', obrigatorio=True),
        CampoNumerico(10, 'VL_BC_PIS'),
        CampoNumerico(11, 'ALIQ_PIS'),
        CampoNumerico(12, 'VL_PIS'),
        Campo(13, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(14, 'VL_BC_COFINS'),
        CampoNumerico(15, 'ALIQ_COFINS'),
        CampoNumerico(16, 'VL_COFINS'),
        Campo(17, 'COD_CTA'),
        Campo(18, 'COD_CCUS'),
    ]


class RegistroA990(Registro):
    """
    Encerramento do Bloco A
    """
    campos = [
        CampoFixo(1, 'REG', 'A990'),
        CampoNumerico(2, 'QTD_LIN_A', obrigatorio=True),
    ]


class RegistroC001(Registro):
    """
    Abertura do Bloco C
    """
    campos = [
        CampoFixo(1, 'REG', 'C001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroC010(Registro):
    """
    Identificação do Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', 'C010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        Campo(3, 'IND_ESCRI'),
    ]


class RegistroC100(Registro):
    """
    Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04) e
    NF-e (código 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C100'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'IND_EMIT', obrigatorio=True),
        Campo(4, 'COD_PART', obrigatorio=True),
        Campo(5, 'COD_MOD', obrigatorio=True),
        Campo(6, 'COD_SIT;', obrigatorio=True),
        Campo(7, 'SER'),
        Campo(8, 'NUM_DOC', obrigatorio=True),
        Campo(9, 'CHV_NFE'),
        Campo(10, 'CHV_NFE', obrigatorio=True),
        CampoData(11, 'DT_DOC'),
        CampoData(12, 'DT_E_S', obrigatorio=True),
        CampoNumerico(13, 'VL_DOC', obrigatorio=True),
        CampoNumerico(14, 'VL_DESC'),
        CampoNumerico(15, 'VL_ABAT_NT'),
        CampoNumerico(16, 'VL_MERC'),
        Campo(17, 'IND_FRT', obrigatorio=True),
        CampoNumerico(18, 'VL_FRT'),
        CampoNumerico(19, 'VL_SEG'),
        CampoNumerico(20, 'VL_OUT_DA'),
        CampoNumerico(21, 'VL_BC_ICMS'),
        CampoNumerico(22, 'VL_ICMS'),
        CampoNumerico(23, 'VL_BC_ICMS_ST'),
        CampoNumerico(24, 'VL_ICMS_ST'),
        CampoNumerico(25, 'VL_IPI'),
        CampoNumerico(26, 'VL_PIS'),
        CampoNumerico(27, 'VL_COFINS'),
        CampoNumerico(28, 'VL_PIS_ST'),
        CampoNumerico(29, 'VL_COFINS_ST'),
    ]


class RegistroC110(Registro):
    """
    Complemento de Documento – Informação Complementar da Nota Fiscal (códigos 01, 1B, 04 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C110'),
        Campo(2, 'COD_INF', obrigatorio=True),
        Campo(3, 'TXT_COMPL'),
    ]


class RegistroC111(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C111'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC120(Registro):
    """
    Complemento de Documento – Operações de Importação (código 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C120'),
        Campo(2, 'COD_DOC_IMP', obrigatorio=True),
        Campo(3, 'NUM_DOC_IMP', obrigatorio=True),
        CampoNumerico(4, 'VL_PIS_IMP'),
        CampoNumerico(5, 'VL_COFINS_IMP'),
        Campo(6, 'NUM_ACDRAW'),
    ]


class RegistroC170(Registro):
    """
    Complemento de Documento – Itens do Documento (códigos 01, 1B, 04 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C170'),
        Campo(2, 'NUM_ITEM', obrigatorio=True),
        Campo(3, 'COD_ITEM', obrigatorio=True),
        Campo(4, 'DESCR_COMPL'),
        Campo(5, 'QTD'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(8, 'VL_DESC'),
        Campo(9, 'IND_MOV'),
        Campo(10, 'CST_ICMS'),
        Campo(11, 'CFOP', obrigatorio=True),
        Campo(12, 'COD_NAT'),
        CampoNumerico(13, 'VL_BC_ICMS'),
        CampoNumerico(14, 'ALIQ_ICMS'),
        CampoNumerico(15, 'VL_ICMS'),
        CampoNumerico(16, 'VL_BC_ICMS_ST'),
        CampoNumerico(17, 'ALIQ_ST'),
        CampoNumerico(18, 'VL_ICMS_ST'),
        Campo(19, 'IND_APUR'),
        Campo(20, 'CST_IPI'),
        Campo(21, 'COD_ENQ'),
        CampoNumerico(22, 'VL_BC_IPI'),
        CampoNumerico(23, 'ALIQ_IPI'),
        CampoNumerico(24, 'VL_IPI'),
        Campo(25, 'CST_PIS', obrigatorio=True),
        CampoNumerico(26, 'VL_BC_PIS'),
        CampoNumerico(27, 'ALIQ_PIS'),
        Campo(28, 'QUANT_BC_PIS'),
        CampoNumerico(29, 'ALIQ_PIS_QUANT'),
        CampoNumerico(30, 'VL_PIS'),
        Campo(31, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(32, 'VL_BC_COFINS'),
        CampoNumerico(33, 'ALIQ_COFINS'),
        Campo(34, 'QUANT_BC_COFINS'),
        CampoNumerico(35, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(36, 'VL_COFINS'),
        Campo(37, 'COD_CTA'),
    ]


class RegistroC175(Registro):
    """
    Registro Analítico do Documento (código 65)
    """
    campos = [
        CampoFixo(1, 'REG', 'C175'),
        Campo(2, 'CFOP', obrigatorio=True),
        CampoNumerico(3, 'VL_OPR', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC'),
        Campo(5, 'CST_PIS'),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        Campo(8, 'QUANT_BC_PIS'),
        CampoNumerico(9, 'ALIQ_PIS_QUANT'),
        CampoNumerico(10, 'VL_PIS'),
        Campo(11, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(12, 'VL_BC_COFINS'),
        CampoNumerico(13, 'ALIQ_COFINS'),
        Campo(14, 'QUANT_BC_COFINS'),
        CampoNumerico(15, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(16, 'VL_COFINS'),
        Campo(17, 'COD_CTA'),
        Campo(18, 'INFO_COMPL'),
    ]


class RegistroC180(Registro):
    """
    Consolidação de Notas Fiscais Eletrônicas Emitidas pela Pessoa Jurídica (Código 55) – Operações de Vendas
    """
    campos = [
        CampoFixo(1, 'REG', 'C180'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        CampoData(3, 'DT_DOC_INI', obrigatorio=True),
        CampoData(4, 'DT_DOC_FIN', obrigatorio=True),
        Campo(5, 'COD_ITEM', obrigatorio=True),
        Campo(6, 'COD_NCM'),
        Campo(7, 'EX_IPI'),
        CampoNumerico(8, 'VL_TOT_ITEM', obrigatorio=True),
    ]


class RegistroC181(Registro):
    """
    Detalhamento da Consolidação - Operações de Vendas - PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C181'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        Campo(3, 'CFOP', obrigatorio=True),
        CampoNumerico(4, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(5, 'VL_DESC'),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        Campo(8, 'QUANT_BC_PIS'),
        CampoNumerico(9, 'ALIQ_PIS_QUANT'),
        CampoNumerico(10, 'VL_PIS'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroC185(Registro):
    """
    Detalhamento da Consolidação - Operações de Vendas – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C185'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        Campo(3, 'CFOP', obrigatorio=True),
        CampoNumerico(4, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(5, 'VL_DESC'),
        CampoNumerico(6, 'VL_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS'),
        Campo(8, 'QUANT_BC_COFINS'),
        CampoNumerico(9, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(10, 'VL_COFINS'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroC188(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C188'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC190(Registro):
    """
    Consolidação de Notas Fiscais Eletrônicas (Código 55) – Operações de Aquisição com Direito a Crédito, e Operações de
    Devolução de Compras e Vendas.
    """
    campos = [
        CampoFixo(1, 'REG', 'C190'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        CampoData(3, 'DT_REF_INI', obrigatorio=True),
        CampoData(4, 'DT_REF_FIN', obrigatorio=True),
        Campo(5, 'COD_ITEM', obrigatorio=True),
        Campo(6, 'COD_NCM'),
        Campo(7, 'EX_IPI'),
        CampoNumerico(8, 'VL_TOT_ITEM', obrigatorio=True),
    ]


class RegistroC191(Registro):
    """
    Detalhamento da Consolidação – Operações de Aquisição com Direito a Crédito, e Operações de Devolução de Compras e
    Vendas – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C191'),
        Campo(2, 'CNPJ_CPF_PART', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        Campo(4, 'CFOP', obrigatorio=True),
        CampoNumerico(5, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(6, 'VL_DESC'),
        CampoNumerico(7, 'VL_BC_PIS'),
        CampoNumerico(8, 'ALIQ_PIS'),
        Campo(9, 'QUANT_BC_PIS'),
        CampoNumerico(10, 'ALIQ_PIS_QUANT'),
        CampoNumerico(11, 'VL_PIS'),
        Campo(12, 'COD_CTA'),
    ]


class RegistroC195(Registro):
    """
    Detalhamento da Consolidação - Operações de Aquisição com Direito a Crédito, e Operações de Devolução de Compras e
    Vendas – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C195'),
        Campo(2, 'CNPJ_CPF_PART', obrigatorio=True),
        Campo(3, 'CST_COFINS', obrigatorio=True),
        Campo(4, 'CFOP', obrigatorio=True),
        CampoNumerico(5, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(6, 'VL_DESC'),
        CampoNumerico(7, 'VL_BC_COFINS'),
        CampoNumerico(8, 'ALIQ_COFINS'),
        Campo(9, 'QUANT_BC_COFINS'),
        CampoNumerico(10, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(11, 'VL_COFINS'),
        Campo(12, 'COD_CTA'),
    ]


class RegistroC198(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C198'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC199(Registro):
    """
    Complemento de Documento – Operações de Importação (código 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C199'),
        Campo(2, 'COD_DOC_IMP', obrigatorio=True),
        Campo(3, 'NUM_DOC__IMP', obrigatorio=True),
        CampoNumerico(4, 'VL_PIS_IMP'),
        CampoNumerico(5, 'VL_COFINS_IMP'),
        Campo(6, 'NUM_ACDRAW'),
    ]


class RegistroC380(Registro):
    """
    Nota Fiscal de Venda a Consumidor (Código 02) - Consolidação de Documentos Emitidos
    """
    campos = [
        CampoFixo(1, 'REG', 'C380'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        CampoData(3, 'DT_DOC_INI', obrigatorio=True),
        CampoData(4, 'DT_DOC_FIN', obrigatorio=True),
        Campo(5, 'NUM_DOC_INI'),
        Campo(6, 'NUM_DOC_FIN'),
        CampoNumerico(7, 'VL_DOC', obrigatorio=True),
        CampoNumerico(8, 'VL_DOC_CANC', obrigatorio=True),
    ]


class RegistroC381(Registro):
    """
    Detalhamento da Consolidação – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C381'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        Campo(3, 'COD_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(5, 'VL_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS'),
        Campo(7, 'QUANT_BC_PIS'),
        CampoNumerico(8, 'ALIQ_PIS_QUANT'),
        CampoNumerico(9, 'VL_PIS', obrigatorio=True),
        Campo(10, 'COD_CTA'),
    ]


class RegistroC385(Registro):
    """
    Detalhamento da Consolidação – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C385'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        Campo(3, 'COD_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(5, 'VL_BC_COFINS'),
        CampoNumerico(6, 'ALIQ_COFINS'),
        Campo(7, 'QUANT_BC_COFINS'),
        CampoNumerico(8, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(9, 'VL_COFINS', obrigatorio=True),
        Campo(10, 'COD_CTA'),
    ]


class RegistroC395(Registro):
    """
    Notas Fiscais de Venda a Consumidor (Códigos 02, 2D, 2E e 59) – Aquisições/Entradas com Crédito
    """
    campos = [
        CampoFixo(1, 'REG', 'C395'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'COD_PART'),
        Campo(4, 'SER', obrigatorio=True),
        Campo(5, 'SUB_SER'),
        Campo(6, 'NUM_DOC', obrigatorio=True),
        CampoData(7, 'DT_DOC', obrigatorio=True),
        CampoNumerico(8, 'VL_DOC', obrigatorio=True),
    ]


class RegistroC396(Registro):
    """
    Itens do Documento (Códigos 02, 2D, 2E e 59) – Aquisições/Entradas com Crédito
    """
    campos = [
        CampoFixo(1, 'REG', 'C396'),
        Campo(2, 'COD_ITEM', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC'),
        Campo(5, 'NAT_BC_CRED', obrigatorio=True),
        Campo(6, 'CST_PIS', obrigatorio=True),
        CampoNumerico(7, 'VL_BC_PIS'),
        CampoNumerico(8, 'ALIQ_PIS'),
        CampoNumerico(9, 'VL_PIS'),
        Campo(10, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(11, 'VL_BC_COFINS'),
        CampoNumerico(12, 'ALIQ_COFINS'),
        CampoNumerico(13, 'VL_COFINS'),
        Campo(14, 'COD_CTA'),
    ]


class RegistroC400(Registro):
    """
    Equipamento ECF (códigos 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C400'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'ECF_MOD', obrigatorio=True),
        Campo(4, 'ECF_FAB', obrigatorio=True),
        Campo(5, 'ECF_CX', obrigatorio=True),
    ]


class RegistroC405(Registro):
    """
    Redução Z (códigos 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C405'),
        CampoData(2, 'DT_DOC', obrigatorio=True),
        Campo(3, 'CRO', obrigatorio=True),
        Campo(4, 'CRZ', obrigatorio=True),
        Campo(5, 'NUM_COO_FIN', obrigatorio=True),
        Campo(6, 'GT_FIN', obrigatorio=True),
        CampoNumerico(7, 'VL_BRT', obrigatorio=True),
    ]


class RegistroC481(Registro):
    """
    Resumo Diário de Documentos Emitidos por ECF – PIS/PASEP (Códigos 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C481'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_PIS'),
        CampoNumerico(5, 'ALIQ_PIS'),
        Campo(6, 'QUANT_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS_QUANT'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'COD_ITEM'),
        Campo(10, 'COD_CTA'),
    ]


class RegistroC485(Registro):
    """
    Resumo Diário de Documentos Emitidos por ECF – COFINS (Códigos 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C485'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_COFINS'),
        CampoNumerico(5, 'ALIQ_COFINS'),
        Campo(6, 'QUANT_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(8, 'VL_COFINS'),
        Campo(9, 'COD_ITEM'),
        Campo(10, 'COD_CTA'),
    ]


class RegistroC489(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C489'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC490(Registro):
    """
    Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D, 59 e 60)
    """
    campos = [
        CampoFixo(1, 'REG', 'C490'),
        CampoData(2, 'DT_DOC_INI', obrigatorio=True),
        CampoData(3, 'DT_DOC_FIN', obrigatorio=True),
        Campo(4, 'COD_MOD', obrigatorio=True),
    ]


class RegistroC491(Registro):
    """
    Detalhamento da Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D, 59 e 60) – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C491'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'CST_PIS', obrigatorio=True),
        Campo(4, 'CFOP'),
        CampoNumerico(5, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        Campo(8, 'QUANT_BC_PIS'),
        CampoNumerico(9, 'ALIQ_PIS_QUANT'),
        CampoNumerico(10, 'VL_PIS'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroC495(Registro):
    """
    Detalhamento da Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D, 59 e 60) – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C495'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'CST_COFINS', obrigatorio=True),
        Campo(4, 'CFOP'),
        CampoNumerico(5, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS'),
        Campo(8, 'QUANT_BC_COFINS'),
        CampoNumerico(9, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(10, 'VL_COFINS'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroC499(Registro):
    """
    Processo Referenciado - Documentos Emitidos Por ECF
    """
    campos = [
        CampoFixo(1, 'REG', 'C499'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC500(Registro):
    """
    Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal/Conta de fornecimento D’água Canalizada (Código 29) e
    Nota Fiscal/Consumo Fornecimento de Gás (Código 28) – Documentos de Entrada / Aquisição com Crédito
    """
    campos = [
        CampoFixo(1, 'REG', 'C500'),
        Campo(2, 'COD_PART', obrigatorio=True),
        Campo(3, 'COD_MOD', obrigatorio=True),
        Campo(4, 'COD_SIT', obrigatorio=True),
        Campo(5, 'SER'),
        Campo(6, 'SUB'),
        Campo(7, 'NUM_DOC', obrigatorio=True),
        CampoData(8, 'DT_DOC', obrigatorio=True),
        CampoData(9, 'DT_ENT'),
        CampoNumerico(10, 'VL_DOC', obrigatorio=True),
        CampoNumerico(11, 'VL_ICMS'),
        Campo(12, 'COD_INF'),
        CampoNumerico(13, 'VL_PIS'),
        CampoNumerico(14, 'VL_COFINS'),
    ]


class RegistroC501(Registro):
    """
    Complemento da operação (Códigos 06, 28 e 29) – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C501'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'NAT_BC_CRED'),
        CampoNumerico(5, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(6, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(7, 'VL_PIS', obrigatorio=True),
        Campo(8, 'COD_CTA'),
    ]


class RegistroC505(Registro):
    """
    Complemento da operação (Códigos 06, 28 e 29) – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C505'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'NAT_BC_CRED'),
        CampoNumerico(5, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(6, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(7, 'VL_COFINS', obrigatorio=True),
        Campo(8, 'COD_CTA'),
    ]


class RegistroC509(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C509'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC600(Registro):
    """
    Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento
    d´água (Código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) (Empresas Obrigadas ou Não Obrigadas Ao
    Convenio ICMS 115/03) - Documentos de Saídas
    """
    campos = [
        CampoFixo(1, 'REG', 'C600'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'COD_MUN'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'COD_CONS'),
        CampoNumerico(7, 'QTD_CONS', obrigatorio=True),
        CampoNumerico(8, 'QTD_CANC'),
        CampoData(9, 'DT_DOC', obrigatorio=True),
        CampoNumerico(10, 'VL_DOC', obrigatorio=True),
        CampoNumerico(11, 'VL_DESC'),
        Campo(12, 'CONS'),
        CampoNumerico(13, 'VL_FORN'),
        CampoNumerico(14, 'VL_SERV_NT'),
        CampoNumerico(15, 'VL_TERC'),
        CampoNumerico(16, 'VL_DA'),
        CampoNumerico(17, 'VL_BC_ICMS'),
        CampoNumerico(18, 'VL_ICMS'),
        CampoNumerico(19, 'VL_BC_ICMS_ST'),
        CampoNumerico(20, 'VL_ICMS_ST'),
        CampoNumerico(21, 'VL_PIS', obrigatorio=True),
        CampoNumerico(22, 'VL_COFINS', obrigatorio=True),
    ]


class RegistroC601(Registro):
    """
    Complemento da Consolidação Diária (Códigos 06, 29 e 28) – Documentos de Saidas - PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'C601'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(5, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(6, 'VL_PIS', obrigatorio=True),
        Campo(7, 'COD_CTA'),
    ]


class RegistroC605(Registro):
    """
    Complemento da Consolidação Diária (Códigos 06, 29 e 28) – Documentos de Saidas – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C605'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(5, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(6, 'VL_COFINS', obrigatorio=True),
        Campo(7, 'COD_CTA'),
    ]


class RegistroC609(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C609'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC800(Registro):
    """
    Cupom Fiscal Eletrônico – CF-e (Código 59)
    """
    campos = [
        CampoFixo(1, 'REG', 'C800'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'COD_SIT', obrigatorio=True),
        Campo(4, 'NUM_CFE', obrigatorio=True),
        CampoData(5, 'DT_DOC', obrigatorio=True),
        CampoNumerico(6, 'VL_CFE', obrigatorio=True),
        CampoNumerico(7, 'VL_PIS'),
        CampoNumerico(8, 'VL_COFINS'),
        Campo(9, 'CNPJ_CPF'),
        Campo(10, 'NR_SAT'),
        Campo(11, 'CHV_CFE'),
        CampoNumerico(12, 'VL_DESC'),
        CampoNumerico(13, 'VL_MERC'),
        CampoNumerico(14, 'VL_OUT_DA'),
        CampoNumerico(15, 'VL_ICMS'),
        CampoNumerico(16, 'VL_PIS_ST'),
        CampoNumerico(17, 'VL_COFINS_ST'),
    ]


class RegistroC810(Registro):
    """
    Detalhamento do Cupom Fiscal Eletrônico – CF-e (Código 59) – PIS/PASEP e COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C810'),
        Campo(2, 'CFOP', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'COD_ITEM'),
        Campo(5, 'CST_PIS', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(10, 'VL_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_CTA'),
    ]


class RegistroC820(Registro):
    """
    Detalhamento do Cupom Fiscal Eletrônico – CF-e  (código 59) – PIS/PASEP e COFINS Apurado por Unidade de Medida de
    Produto
    """
    campos = [
        CampoFixo(1, 'REG', 'C820'),
        Campo(2, 'CFOP', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'COD_ITEM'),
        Campo(5, 'CST_PIS', obrigatorio=True),
        Campo(6, 'QUANT_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS_QUANT'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'CST_COFINS', obrigatorio=True),
        Campo(10, 'QUANT_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_CTA'),
    ]


class RegistroC830(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C830'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC860(Registro):
    """
    Identificação do Equipamento SAT-CF-e
    """
    campos = [
        CampoFixo(1, 'REG', 'C860'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'NR_SAT', obrigatorio=True),
        CampoData(4, 'DT_DOC'),
        Campo(5, 'DOC_INI'),
        Campo(6, 'DOC_FIM'),
    ]


class RegistroC870(Registro):
    """
    Detalhamento do Cupom Fiscal Eletrônico (Código 59) – PIS/PASEP e COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'C870'),
        Campo(2, 'CFOP', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'COD_ITEM'),
        Campo(5, 'CST_PIS', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(10, 'VL_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_CTA'),
    ]


class RegistroC880(Registro):
    """
    Detalhamento do Cupom Fiscal Eletrônico (Código 59) – PIS/PASEP e COFINS Apurado por Unidade de Medida de Produto
    """
    campos = [
        CampoFixo(1, 'REG', 'C880'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'CFOP', obrigatorio=True),
        CampoNumerico(4, 'VL_ITEM', obrigatorio=True),
        Campo(5, 'CST_PIS', obrigatorio=True),
        Campo(6, 'QUANT_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS_QUANT'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'CST_COFINS', obrigatorio=True),
        Campo(10, 'QUANT_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_CTA'),
    ]


class RegistroC890(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'C890'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroC990(Registro):
    """
    Encerramento do Bloco C
    """
    campos = [
        CampoFixo(1, 'REG', 'C990'),
        CampoNumerico(2, 'QTD_LIN_C', obrigatorio=True),
    ]


class RegistroD001(Registro):
    """
    Abertura do Bloco D
    """
    campos = [
        CampoFixo(1, 'REG', 'D001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroD010(Registro):
    """
    Identificação do Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', 'D010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
    ]


class RegistroD100(Registro):
    """
    Aquisição de Serviços de Transportes (Códigos 07, 08, 8B, 09, 10, 11, 26, 27 e 57).
    """
    campos = [
        CampoFixo(1, 'REG', 'D100'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'IND_EMIT', obrigatorio=True),
        Campo(4, 'COD_PART', obrigatorio=True),
        Campo(5, 'COD_MOD', obrigatorio=True),
        Campo(6, 'COD_SIT', obrigatorio=True),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'NUM_DOC', obrigatorio=True),
        Campo(10, 'CHV_CTE'),
        CampoData(11, 'DT_DOC', obrigatorio=True),
        CampoData(12, 'DT_A_P'),
        Campo(13, 'TP_CT-e'),
        Campo(14, 'CHV_CTE_REF'),
        CampoNumerico(15, 'VL_DOC', obrigatorio=True),
        CampoNumerico(16, 'VL_DESC'),
        Campo(17, 'IND_FRT', obrigatorio=True),
        CampoNumerico(18, 'VL_SERV', obrigatorio=True),
        CampoNumerico(19, 'VL_BC_ICMS'),
        CampoNumerico(20, 'VL_ICMS'),
        CampoNumerico(21, 'VL_NT'),
        Campo(22, 'COD_INF'),
        Campo(23, 'COD_CTA'),
    ]


class RegistroD101(Registro):
    """
    Complemento do Documento de Transporte – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'D101'),
        Campo(2, 'IND_NAT_FRT', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'CST_PIS', obrigatorio=True),
        Campo(5, 'NAT_BC_CRED'),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'COD_CTA'),
    ]


class RegistroD105(Registro):
    """
    Complemento do Documento de Transporte – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'D105'),
        Campo(2, 'IND_NAT_FRT', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'CST_COFINS', obrigatorio=True),
        Campo(5, 'NAT_BC_CRED'),
        CampoNumerico(6, 'VL_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS'),
        CampoNumerico(8, 'VL_COFINS'),
        Campo(9, 'COD_CTA'),
    ]


class RegistroD111(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D111'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD200(Registro):
    """
    Resumo da Escrituração Diária – Prestação de Serviços de Transportes (Códigos 07, 08, 8B, 09, 10, 11, 26, 27 e 57).
    """
    campos = [
        CampoFixo(1, 'REG', 'D200'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'COD_SIT', obrigatorio=True),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'NUM_DOC_INI', obrigatorio=True),
        Campo(7, 'NUM_DOC_FIN', obrigatorio=True),
        Campo(8, 'CFOP', obrigatorio=True),
        CampoData(9, 'DT_REF', obrigatorio=True),
        CampoNumerico(10, 'VL_DOC', obrigatorio=True),
        CampoNumerico(11, 'VL_DESC'),
    ]


class RegistroD201(Registro):
    """
    Totalização do Resumo Diário – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'D201'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_PIS'),
        CampoNumerico(5, 'ALIQ_PIS'),
        CampoNumerico(6, 'VL_PIS'),
        Campo(7, 'COD_CTA'),
    ]


class RegistroD205(Registro):
    """
    Totalização do Resumo Diário – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'D205'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_COFINS'),
        CampoNumerico(5, 'ALIQ_COFINS'),
        CampoNumerico(6, 'VL_COFINS'),
        Campo(7, 'COD_CTA'),
    ]


class RegistroD209(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D209'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD300(Registro):
    """
    Resumo da Escrituração Diária (Códigos 13, 14, 15, 16 e 18).
    """
    campos = [
        CampoFixo(1, 'REG', 'D300'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'SER'),
        Campo(4, 'SUB'),
        Campo(5, 'NUM_DOC_INI'),
        Campo(6, 'NUM_DOC_FIN'),
        Campo(7, 'CFOP', obrigatorio=True),
        CampoData(8, 'DT_REF', obrigatorio=True),
        CampoNumerico(9, 'VL_DOC', obrigatorio=True),
        CampoNumerico(10, 'VL_DESC'),
        Campo(11, 'CST_PIS', obrigatorio=True),
        CampoNumerico(12, 'VL_BC_PIS'),
        CampoNumerico(13, 'ALIQ_PIS'),
        CampoNumerico(14, 'VL_PIS'),
        Campo(15, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(16, 'VL_BC_COFINS'),
        CampoNumerico(17, 'ALIQ_COFINS'),
        CampoNumerico(18, 'VL_COFINS'),
        Campo(19, 'COD_CTA'),
    ]


class RegistroD309(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D309'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD350(Registro):
    """
    Resumo Diário de Cupom Fiscal Emitido por ECF (Códigos 2E, 13, 14, 15 e 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D350'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'ECF_MOD', obrigatorio=True),
        Campo(4, 'ECF_FAB', obrigatorio=True),
        CampoData(5, 'DT_DOC', obrigatorio=True),
        Campo(6, 'CRO', obrigatorio=True),
        Campo(7, 'CRZ', obrigatorio=True),
        Campo(8, 'NUM_COO_FIN', obrigatorio=True),
        Campo(9, 'GT_FIN', obrigatorio=True),
        CampoNumerico(10, 'VL_BRT', obrigatorio=True),
        Campo(11, 'CST_PIS', obrigatorio=True),
        CampoNumerico(12, 'VL_BC_PIS'),
        CampoNumerico(13, 'ALIQ_PIS'),
        Campo(14, 'QUANT_BC_PIS'),
        CampoNumerico(15, 'ALIQ_PIS_QUANT'),
        CampoNumerico(16, 'VL_PIS'),
        Campo(17, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(18, 'VL_BC_COFINS'),
        CampoNumerico(19, 'ALIQ_COFINS'),
        Campo(20, 'QUANT_BC_COFINS'),
        CampoNumerico(21, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(22, 'VL_COFINS'),
        Campo(23, 'COD_CTA'),
    ]


class RegistroD359(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D359'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD500(Registro):
    """
    Nota Fiscal de Serviço de Comunicação (Código 21) e Serviço de Telecomunicação (Código 22) - Operação de Aquisição
    com Direito a Crédito
    """
    campos = [
        CampoFixo(1, 'REG', 'D500'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'IND_EMIT', obrigatorio=True),
        Campo(4, 'COD_PART', obrigatorio=True),
        Campo(5, 'COD_MOD', obrigatorio=True),
        Campo(6, 'COD_SIT', obrigatorio=True),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'NUM_DOC', obrigatorio=True),
        CampoData(10, 'DT_DOC', obrigatorio=True),
        CampoData(11, 'DT_A_P', obrigatorio=True),
        CampoNumerico(12, 'VL_DOC', obrigatorio=True),
        CampoNumerico(13, 'VL_DESC'),
        CampoNumerico(14, 'VL_SERV', obrigatorio=True),
        CampoNumerico(15, 'VL_SERV_NT'),
        CampoNumerico(16, 'VL_TERC'),
        CampoNumerico(17, 'VL_DA'),
        CampoNumerico(18, 'VL_BC_ICMS'),
        CampoNumerico(19, 'VL_ICMS'),
        Campo(20, 'COD_INF'),
        CampoNumerico(21, 'VL_PIS'),
        CampoNumerico(22, 'VL_COFINS'),
    ]


class RegistroD501(Registro):
    """
    Complemento da Operação (Código 21 e 22) – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'D501'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'NAT_BC_CRED'),
        CampoNumerico(5, 'VL_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS'),
        CampoNumerico(7, 'VL_PIS'),
        Campo(8, 'COD_CTA'),
    ]


class RegistroD505(Registro):
    """
    Complemento da Operação (Código 21 e 22) – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'D505'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        Campo(4, 'NAT_BC_CRED'),
        CampoNumerico(5, 'VL_BC_COFINS'),
        CampoNumerico(6, 'ALIQ_COFINS'),
        CampoNumerico(7, 'VL_COFINS'),
        Campo(8, 'COD_CTA'),
    ]


class RegistroD509(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D509'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD600(Registro):
    """
    Consolidação da Prestação de Serviços – Notas de Serviço de Comunicação (Código 21) e de Serviço de Telecomunicação
    (Código 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D600'),
        Campo(2, 'COD_MOD', obrigatorio=True),
        Campo(3, 'COD_MUN'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'IND_REC', obrigatorio=True),
        CampoNumerico(7, 'QTD_CONS', obrigatorio=True),
        CampoData(8, 'DT_DOC_INI', obrigatorio=True),
        CampoData(9, 'DT_DOC_FIN', obrigatorio=True),
        CampoNumerico(10, 'VL_DOC', obrigatorio=True),
        CampoNumerico(11, 'VL_DESC'),
        CampoNumerico(12, 'VL_SERV', obrigatorio=True),
        CampoNumerico(13, 'VL_SERV_NT'),
        CampoNumerico(14, 'VL_TERC'),
        CampoNumerico(15, 'VL_DA'),
        CampoNumerico(16, 'VL_BC_ICMS'),
        CampoNumerico(17, 'VL_ICMS'),
        CampoNumerico(18, 'VL_PIS'),
        CampoNumerico(19, 'VL_COFINS'),
    ]


class RegistroD601(Registro):
    """
    Complemento da Consolidação da Prestação de Serviços (Código 21 e 22) – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'D601'),
        Campo(2, 'COD_CLASS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC'),
        Campo(5, 'CST_PIS', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS'),
        CampoNumerico(8, 'VL_PIS'),
        Campo(9, 'COD_CTA'),
    ]


class RegistroD605(Registro):
    """
    Complemento da Consolidação da Prestação de Serviços (Código 21 e 22) – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'D605'),
        Campo(2, 'COD_CLASS', obrigatorio=True),
        CampoNumerico(3, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC'),
        Campo(5, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS'),
        CampoNumerico(8, 'VL_COFINS'),
        Campo(9, 'COD_CTA'),
    ]


class RegistroD609(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'D609'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroD990(Registro):
    """
    Encerramento do Bloco D
    """
    campos = [
        CampoFixo(1, 'REG', 'D990'),
        CampoNumerico(2, 'QTD_LIN_D', obrigatorio=True),
    ]


class RegistroF001(Registro):
    """
    Abertura do Bloco F
    """
    campos = [
        CampoFixo(1, 'REG', 'F001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroF010(Registro):
    """
    Identificação do Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', 'F010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
    ]


class RegistroF100(Registro):
    """
    Demais Documentos e Operações Geradoras de Contribuição e Créditos
    """
    campos = [
        CampoFixo(1, 'REG', 'F100'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'COD_PART'),
        Campo(4, 'COD_ITEM'),
        CampoData(5, 'DT_OPER', obrigatorio=True),
        CampoNumerico(6, 'VL_OPER', obrigatorio=True),
        Campo(7, 'CST_PIS', obrigatorio=True),
        CampoNumerico(8, 'VL_BC_PIS'),
        CampoNumerico(9, 'ALIQ_PIS'),
        CampoNumerico(10, 'VL_PIS'),
        Campo(11, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(12, 'VL_BC_COFINS'),
        CampoNumerico(13, 'ALIQ_COFINS'),
        CampoNumerico(14, 'VL_COFINS'),
        Campo(15, 'NAT_BC_CRED'),
        Campo(16, 'IND_ORIG_CRED'),
        Campo(17, 'COD_CTA'),
        Campo(18, 'COD_CCUS'),
        Campo(19, 'DESC_DOC_OPER'),
    ]


class RegistroF111(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F111'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF120(Registro):
    """
    Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Créditos com base nos Encargos de
    Depreciação/Amortização
    """
    campos = [
        CampoFixo(1, 'REG', 'F120'),
        Campo(2, 'NAT_BC_CRED', obrigatorio=True),
        Campo(3, 'IDENT_BEM_IMOB', obrigatorio=True),
        Campo(4, 'IND_ORIG_CRED'),
        Campo(5, 'IND_UTIL_BEM_IMOB', obrigatorio=True),
        CampoNumerico(6, 'VL_OPER_DEP', obrigatorio=True),
        Campo(7, 'PARC_OPER_NAO_BC_CRED'),
        Campo(8, 'CST_PIS', obrigatorio=True),
        CampoNumerico(9, 'VL_BC_PIS'),
        CampoNumerico(10, 'ALIQ_PIS'),
        CampoNumerico(11, 'VL_PIS'),
        Campo(12, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(13, 'VL_BC_COFINS'),
        CampoNumerico(14, 'ALIQ_COFINS'),
        CampoNumerico(15, 'VL_COFINS'),
        Campo(16, 'COD_CTA'),
        Campo(17, 'COD_CCUS'),
        Campo(18, 'DESC_BEM_IMOB'),
    ]


class RegistroF129(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F129'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF130(Registro):
    """
    Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Créditos com base no Valor de Aquisição
    """
    campos = [
        CampoFixo(1, 'REG', 'F130'),
        Campo(2, 'NAT_BC_CRED', obrigatorio=True),
        Campo(3, 'IDENT_BEM_IMOB', obrigatorio=True),
        Campo(4, 'IND_ORIG_CRED'),
        Campo(5, 'IND_UTIL_BEM_IMOB', obrigatorio=True),
        Campo(6, 'MES_OPER_AQUIS'),
        CampoNumerico(7, 'VL_OPER_AQUIS', obrigatorio=True),
        Campo(8, 'PARC_OPER_NAO_BC_CRED'),
        CampoNumerico(9, 'VL_BC_CRED', obrigatorio=True),
        Campo(10, 'IND_NR_PARC', obrigatorio=True),
        Campo(11, 'CST_PIS', obrigatorio=True),
        CampoNumerico(12, 'VL_BC_PIS'),
        CampoNumerico(13, 'ALIQ_PIS'),
        CampoNumerico(14, 'VL_PIS'),
        Campo(15, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(16, 'VL_BC_COFINS'),
        CampoNumerico(17, 'ALIQ_COFINS'),
        CampoNumerico(18, 'VL_COFINS'),
        Campo(19, 'COD_CTA'),
        Campo(20, 'COD_CCUS'),
        Campo(21, 'DESC_BEM_IMOB'),
    ]


class RegistroF139(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F139'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF150(Registro):
    """
    Crédito Presumido sobre Estoque de Abertura
    """
    campos = [
        CampoFixo(1, 'REG', 'F150'),
        Campo(2, 'NAT_BC_CRED', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_EST', obrigatorio=True),
        Campo(4, 'EST_IMP'),
        CampoNumerico(5, 'VL_BC_EST', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_MEN_EST', obrigatorio=True),
        Campo(7, 'CST_PIS', obrigatorio=True),
        CampoNumerico(8, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(9, 'VL_CRED_PIS', obrigatorio=True),
        Campo(10, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(11, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(12, 'VL_CRED_COFINS', obrigatorio=True),
        Campo(13, 'DESC_EST'),
        Campo(14, 'COD_CTA'),
    ]


class RegistroF200(Registro):
    """
    Operações da Atividade Imobiliária – Unidade Imobiliária Vendida
    """
    campos = [
        CampoFixo(1, 'REG', 'F200'),
        Campo(2, 'IND_OPER', obrigatorio=True),
        Campo(3, 'UNID_IMOB', obrigatorio=True),
        Campo(4, 'IDENT_EMP', obrigatorio=True),
        Campo(5, 'DESC_UNID_IMOB'),
        Campo(6, 'NUM_CONT'),
        Campo(7, 'CPF_CNPJ_ADQU', obrigatorio=True),
        CampoData(8, 'DT_OPER', obrigatorio=True),
        CampoNumerico(9, 'VL_TOT_VEND', obrigatorio=True),
        CampoNumerico(10, 'VL_REC_ACUM'),
        CampoNumerico(11, 'VL_TOT_REC', obrigatorio=True),
        Campo(12, 'CST_PIS', obrigatorio=True),
        CampoNumerico(13, 'VL_BC_PIS'),
        CampoNumerico(14, 'ALIQ_PIS'),
        CampoNumerico(15, 'VL_PIS'),
        Campo(16, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(17, 'VL_BC_COFINS'),
        CampoNumerico(18, 'ALIQ_COFINS'),
        CampoNumerico(19, 'VL_COFINS'),
        Campo(20, 'PERC_REC_RECEB'),
        Campo(21, 'IND_NAT_EMP'),
        Campo(22, 'INF_COMP'),
    ]


class RegistroF205(Registro):
    """
    Operações da Atividade Imobiliária – Custo Incorrido da Unidade Imobiliária
    """
    campos = [
        CampoFixo(1, 'REG', 'F205'),
        CampoNumerico(2, 'VL_CUS_INC_ACUM_ANT', obrigatorio=True),
        CampoNumerico(3, 'VL_CUS_INC_PER_ESC', obrigatorio=True),
        CampoNumerico(4, 'VL_CUS_INC_ACUM', obrigatorio=True),
        CampoNumerico(5, 'VL_EXC_BC_CUS_INC_ACUM', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_CUS_INC', obrigatorio=True),
        Campo(7, 'CST_PIS', obrigatorio=True),
        CampoNumerico(8, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(9, 'VL_CRED_PIS_ACUM', obrigatorio=True),
        CampoNumerico(10, 'VL_CRED_PIS_DESC_ANT', obrigatorio=True),
        CampoNumerico(11, 'VL_CRED_PIS_DESC', obrigatorio=True),
        CampoNumerico(12, 'VL_CRED_PIS_DESC_FUT', obrigatorio=True),
        Campo(13, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(14, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(15, 'VL_CRED_COFINS_ACUM', obrigatorio=True),
        CampoNumerico(16, 'VL_CRED_COFINS_DESC_ANT', obrigatorio=True),
        CampoNumerico(17, 'VL_CRED_COFINS_DESC', obrigatorio=True),
        CampoNumerico(18, 'VL_CRED_COFINS_DESC_FUT', obrigatorio=True),
    ]


class RegistroF210(Registro):
    """
    Operações da Atividade Imobiliária – Custo Orçado da Unidade Imobiliária Vendida
    """
    campos = [
        CampoFixo(1, 'REG', 'F210'),
        CampoNumerico(2, 'VL_CUS_ORC', obrigatorio=True),
        CampoNumerico(3, 'VL_EXC', obrigatorio=True),
        CampoNumerico(4, 'VL_CUS_ORC_AJU', obrigatorio=True),
        CampoNumerico(5, 'VL_BC_CRED', obrigatorio=True),
        Campo(6, 'CST_PIS', obrigatorio=True),
        CampoNumerico(7, 'ALIQ_PIS'),
        CampoNumerico(8, 'VL_CRED_PIS_UTIL'),
        Campo(9, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(10, 'ALIQ_COFINS'),
        CampoNumerico(11, 'VL_CRED_COFINS_UTIL'),
    ]


class RegistroF211(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F211'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF500(Registro):
    """
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido –
    Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa
    """
    campos = [
        CampoFixo(1, 'REG', 'F500'),
        CampoNumerico(2, 'VL_REC_CAIXA', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC_PIS'),
        CampoNumerico(5, 'VL_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS'),
        CampoNumerico(7, 'VL_PIS'),
        Campo(8, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(9, 'VL_DESC_COFINS'),
        CampoNumerico(10, 'VL_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_MOD'),
        Campo(14, 'CFOP'),
        Campo(15, 'COD_CTA'),
        Campo(16, 'INFO_COMPL'),
    ]


class RegistroF509(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F509'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF510(Registro):
    """
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido  –
    Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa (Apuração da Contribuição por Unidade de Medida de Produto)
    """
    campos = [
        CampoFixo(1, 'REG', 'F510'),
        CampoNumerico(2, 'VL_REC_CAIXA', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC_PIS'),
        Campo(5, 'QUANT_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS_QUANT'),
        CampoNumerico(7, 'VL_PIS'),
        Campo(8, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(9, 'VL_DESC_COFINS'),
        Campo(10, 'QUANT_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_MOD'),
        Campo(14, 'CFOP'),
        Campo(15, 'COD_CTA'),
        Campo(16, 'INFO_COMPL'),
    ]


class RegistroF519(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F519'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF525(Registro):
    """
    Composição da Receita Escriturada no Período – Detalhamento da Receita Recebida pelo Regime de Caixa
    """
    campos = [
        CampoFixo(1, 'REG', 'F525'),
        CampoNumerico(2, 'VL_REC', obrigatorio=True),
        Campo(3, 'IND_REC', obrigatorio=True),
        Campo(4, 'CNPJ_CPF'),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'COD_ITEM'),
        CampoNumerico(7, 'VL_REC_DET', obrigatorio=True),
        Campo(8, 'CST_PIS'),
        Campo(9, 'CST_COFINS'),
        Campo(10, 'INFO_COMPL'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroF550(Registro):
    """
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido –
    Incidência do PIS/Pasep e da Cofins pelo Regime de Competência
    """
    campos = [
        CampoFixo(1, 'REG', 'F550'),
        CampoNumerico(2, 'VL_REC_COMP', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC_PIS'),
        CampoNumerico(5, 'VL_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS'),
        CampoNumerico(7, 'VL_PIS'),
        Campo(8, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(9, 'VL_DESC_COFINS'),
        CampoNumerico(10, 'VL_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_MOD'),
        Campo(14, 'CFOP'),
        Campo(15, 'COD_CTA'),
        Campo(16, 'INFO_COMPL'),
    ]


class RegistroF559(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F559'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF560(Registro):
    """
    Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido –
    Incidência do PIS/Pasep e da Cofins pelo Regime de Competência (Apuração da Contribuição por Unidade de Medida de
    Produto)
    """
    campos = [
        CampoFixo(1, 'REG', 'F560'),
        CampoNumerico(2, 'VL_REC_COMP', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_DESC_PIS'),
        Campo(5, 'QUANT_BC_PIS'),
        CampoNumerico(6, 'ALIQ_PIS_QUANT'),
        CampoNumerico(7, 'VL_PIS'),
        Campo(8, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(9, 'VL_DESC_COFINS'),
        Campo(10, 'QUANT_BC_COFINS'),
        CampoNumerico(11, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(12, 'VL_COFINS'),
        Campo(13, 'COD_MOD'),
        Campo(14, 'CFOP'),
        Campo(15, 'COD_CTA'),
        Campo(16, 'INFO_COMPL'),
    ]


class RegistroF569(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'F569'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroF600(Registro):
    """
    Contribuição Retida na Fonte
    """
    campos = [
        CampoFixo(1, 'REG', 'F600'),
        Campo(2, 'IND_NAT_RET', obrigatorio=True),
        CampoData(3, 'DT_RET', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_RET', obrigatorio=True),
        CampoNumerico(5, 'VL_RET', obrigatorio=True),
        Campo(6, 'COD_REC'),
        Campo(7, 'IND_NAT_REC'),
        CampoCNPJ(8, 'CNPJ', obrigatorio=True),
        CampoNumerico(9, 'VL_RET_PIS', obrigatorio=True),
        CampoNumerico(10, 'VL_RET_COFINS', obrigatorio=True),
        Campo(11, 'IND_DEC', obrigatorio=True),
    ]


class RegistroF700(Registro):
    """
    Deduções Diversas
    """
    campos = [
        CampoFixo(1, 'REG', 'F700'),
        Campo(2, 'IND_ORI_DED', obrigatorio=True),
        Campo(3, 'IND_NAT_DED', obrigatorio=True),
        CampoNumerico(4, 'VL_DED_PIS', obrigatorio=True),
        CampoNumerico(5, 'VL_DED_COFINS', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_OPER', obrigatorio=True),
        CampoCNPJ(7, 'CNPJ'),
        Campo(8, 'INF_COMP'),
    ]


class RegistroF800(Registro):
    """
    Créditos Decorrentes de Eventos de Incorporação, Fusão e Cisão
    """
    campos = [
        CampoFixo(1, 'REG', 'F800'),
        Campo(2, 'IND_NAT_EVEN', obrigatorio=True),
        CampoData(3, 'DT_EVEN', obrigatorio=True),
        CampoCNPJ(4, 'CNPJ_SUCED', obrigatorio=True),
        Campo(5, 'PA_CONT_CRED', obrigatorio=True),
        Campo(6, 'COD_CRED', obrigatorio=True),
        CampoNumerico(7, 'VL_CRED_PIS', obrigatorio=True),
        CampoNumerico(8, 'VL_CRED_COFINS', obrigatorio=True),
        Campo(9, 'PER_CRED_CIS'),
    ]


class RegistroF990(Registro):
    """
    Encerramento do Bloco F
    """
    campos = [
        CampoFixo(1, 'REG', 'F990'),
        CampoNumerico(2, 'QTD_LIN_F', obrigatorio=True),
    ]


class RegistroI001(Registro):
    """
    Abertura do Bloco I
    """
    campos = [
        CampoFixo(1, 'REG', 'I001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroI010(Registro):
    """
    Identificação da Pessoa Jurídica
    """
    campos = [
        CampoFixo(1, 'REG', 'I010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        Campo(3, 'IND_ATIV', obrigatorio=True),
        Campo(4, 'INFO_COMPL'),
    ]


class RegistroI100(Registro):
    """
    Consolidação das Operações do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'I100'),
        CampoNumerico(2, 'VL_REC', obrigatorio=True),
        Campo(3, 'CST_PIS_COFINS', obrigatorio=True),
        CampoNumerico(4, 'VL_TOT_DED_GER', obrigatorio=True),
        CampoNumerico(5, 'VL_TOT_DED_ESP', obrigatorio=True),
        CampoNumerico(6, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(7, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(8, 'VL_PIS', obrigatorio=True),
        CampoNumerico(9, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(10, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(11, 'VL_COFINS', obrigatorio=True),
        Campo(12, 'INFO_COMPL', obrigatorio=True),
    ]


class RegistroI199(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'I199'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroI200(Registro):
    """
    Composição das Receitas, Deduções e/ou Exclusões do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'I200'),
        Campo(2, 'NUM_CAMPO', obrigatorio=True),
        Campo(3, 'COD_DET', obrigatorio=True),
        Campo(4, 'DET_VALOR', obrigatorio=True),
        Campo(5, 'COD_CTA', obrigatorio=True),
        Campo(6, 'INFO_COMPL', obrigatorio=True),
    ]


class RegistroI299(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'I299'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroI300(Registro):
    """
    Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'I300'),
        Campo(2, 'COD_COMP', obrigatorio=True),
        Campo(3, 'DET_VALOR', obrigatorio=True),
        Campo(4, 'COD_CTA', obrigatorio=True),
        Campo(5, 'INFO_COMPL', obrigatorio=True),
    ]


class RegistroI399(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'I399'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroI990(Registro):
    """
    Encerramento do Bloco I
    """
    campos = [
        CampoFixo(1, 'REG', 'I990'),
        CampoNumerico(2, 'QTD_LIN_I', obrigatorio=True),
    ]


class RegistroM001(Registro):
    """
    Abertura do Bloco M
    """
    campos = [
        CampoFixo(1, 'REG', 'M001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroM100(Registro):
    """
    Crédito de PIS/PASEP Relativo ao Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M100'),
        Campo(2, 'COD_CRED', obrigatorio=True),
        Campo(3, 'IND_CRED_ORI', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_PIS'),
        CampoNumerico(5, 'ALIQ_PIS'),
        Campo(6, 'QUANT_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS_QUANT'),
        CampoNumerico(8, 'VL_CRED', obrigatorio=True),
        CampoNumerico(9, 'VL_AJUS_ACRES', obrigatorio=True),
        CampoNumerico(10, 'VL_AJUS_REDUC', obrigatorio=True),
        CampoNumerico(11, 'VL_CRED_DIF', obrigatorio=True),
        CampoNumerico(12, 'VL_CRED_DISP', obrigatorio=True),
        Campo(13, 'IND_DESC_CRED', obrigatorio=True),
        CampoNumerico(14, 'VL_CRED_DESC'),
        Campo(15, 'SLD_CRED', obrigatorio=True),
    ]


class RegistroM105(Registro):
    """
    Detalhamento da Base de Cálculo do Crédito Apurado no Período – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'M105'),
        Campo(2, 'NAT_BC_CRED', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_PIS_TOT'),
        CampoNumerico(5, 'VL_BC_PIS_CUM'),
        CampoNumerico(6, 'VL_BC_PIS_NC'),
        CampoNumerico(7, 'VL_BC_PIS'),
        Campo(8, 'QUANT_BC_PIS_TOT'),
        Campo(9, 'QUANT_BC_PIS'),
        Campo(10, 'DESC_CRED'),
    ]


class RegistroM110(Registro):
    """
    Ajustes do Crédito de PIS/PASEP Apurado
    """
    campos = [
        CampoFixo(1, 'REG', 'M110'),
        Campo(2, 'IND_AJ', obrigatorio=True),
        CampoNumerico(3, 'VL_AJ', obrigatorio=True),
        Campo(4, 'COD_AJ', obrigatorio=True),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DESCR_AJ'),
        CampoData(7, 'DT_REF'),
    ]


class RegistroM115(Registro):
    """
    Detalhamento dos Ajustes do Crédito de Pis/Pasep Apurado
    """
    campos = [
        CampoFixo(1, 'REG', 'M115'),
        Campo(2, 'DET_VALOR_AJ', obrigatorio=True),
        Campo(3, 'CST_PIS'),
        Campo(4, 'DET_BC_CRED'),
        Campo(5, 'DET_ALIQ'),
        CampoData(6, 'DT_OPER_AJ', obrigatorio=True),
        Campo(7, 'DESC_AJ'),
        Campo(8, 'COD_CTA'),
        Campo(9, 'INFO_COMPL'),
    ]


class RegistroM200(Registro):
    """
    Consolidação da Contribuição para o PIS/PASEP do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M200'),
        CampoNumerico(2, 'VL_TOT_CONT_NC_PER', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_CRED_DESC', obrigatorio=True),
        CampoNumerico(4, 'VL_TOT_CRED_DESC_ANT', obrigatorio=True),
        CampoNumerico(5, 'VL_TOT_CONT_NC_DEV', obrigatorio=True),
        CampoNumerico(6, 'VL_RET_NC', obrigatorio=True),
        CampoNumerico(7, 'VL_OUT_DED_NC', obrigatorio=True),
        CampoNumerico(8, 'VL_CONT_NC_REC', obrigatorio=True),
        CampoNumerico(9, 'VL_TOT_CONT_CUM_PER', obrigatorio=True),
        CampoNumerico(10, 'VL_RET_CUM', obrigatorio=True),
        CampoNumerico(11, 'VL_OUT_DED_CUM', obrigatorio=True),
        CampoNumerico(12, 'VL_CONT_CUM_REC', obrigatorio=True),
        CampoNumerico(13, 'VL_TOT_CONT_REC', obrigatorio=True),
    ]


class RegistroM205(Registro):
    """
    Contribuição para o PIS/Pasep a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)
    """
    campos = [
        CampoFixo(1, 'REG', 'M205'),
        Campo(2, 'NUM_CAMPO', obrigatorio=True),
        Campo(3, 'COD_REC', obrigatorio=True),
        CampoNumerico(4, 'VL_DEBITO', obrigatorio=True),
    ]


class RegistroM210(Registro):
    """
    Detalhamento da Contribuição para o PIS/PASEP do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M210'),
        Campo(2, 'COD_CONT', obrigatorio=True),
        CampoNumerico(3, 'VL_REC_BRT', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_CONT', obrigatorio=True),
        CampoNumerico(5, 'ALIQ_PIS'),
        Campo(6, 'QUANT_BC_PIS'),
        CampoNumerico(7, 'ALIQ_PIS_QUANT'),
        CampoNumerico(8, 'VL_CONT_APUR', obrigatorio=True),
        CampoNumerico(9, 'VL_AJUS_ACRES', obrigatorio=True),
        CampoNumerico(10, 'VL_AJUS_REDUC', obrigatorio=True),
        CampoNumerico(11, 'VL_CONT_DIFER'),
        CampoNumerico(12, 'VL_CONT_DIFER_ANT'),
        CampoNumerico(13, 'VL_CONT_PER', obrigatorio=True),
    ]


class RegistroM211(Registro):
    """
    Sociedades Cooperativas – Composição da Base de Cálculo – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'M211'),
        Campo(2, 'IND_TIP_COOP', obrigatorio=True),
        CampoNumerico(3, 'VL_BC_CONT_ANT_EXC_COOP', obrigatorio=True),
        CampoNumerico(4, 'VL_EXC_COOP_GER'),
        CampoNumerico(5, 'VL_EXC_ESP_COOP'),
        CampoNumerico(6, 'VL_BC_CONT', obrigatorio=True),
    ]


class RegistroM220(Registro):
    """
    Ajustes da Contribuição para o PIS/PASEP Apurada
    """
    campos = [
        CampoFixo(1, 'REG', 'M220'),
        Campo(2, 'IND_AJ', obrigatorio=True),
        CampoNumerico(3, 'VL_AJ', obrigatorio=True),
        Campo(4, 'COD_AJ', obrigatorio=True),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DESCR_AJ'),
        CampoData(7, 'DT_REF'),
    ]


class RegistroM225(Registro):
    """
    Detalhamento dos Ajustes da Contribuição para o Pis/Pasep Apurada
    """
    campos = [
        CampoFixo(1, 'REG', 'M225'),
        Campo(2, 'DET_VALOR_AJ', obrigatorio=True),
        Campo(3, 'CST_PIS'),
        Campo(4, 'DET_BC_CRED'),
        Campo(5, 'DET_ALIQ'),
        CampoData(6, 'DT_OPER_AJ', obrigatorio=True),
        Campo(7, 'DESC_AJ'),
        Campo(8, 'COD_CTA'),
        Campo(9, 'INFO_COMPL'),
    ]


class RegistroM230(Registro):
    """
    Informações Adicionais de Diferimento
    """
    campos = [
        CampoFixo(1, 'REG', 'M230'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        CampoNumerico(3, 'VL_VEND', obrigatorio=True),
        CampoNumerico(4, 'VL_NAO_RECEB', obrigatorio=True),
        CampoNumerico(5, 'VL_CONT_DIF', obrigatorio=True),
        CampoNumerico(6, 'VL_CRED_DIF'),
        Campo(7, 'COD_CRED'),
    ]


class RegistroM300(Registro):
    """
    Contribuição de PIS/PASEP Diferida em Períodos Anteriores - Valores a Pagar no Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M300'),
        Campo(2, 'COD_CONT', obrigatorio=True),
        CampoNumerico(3, 'VL_CONT_APUR_DIFER', obrigatorio=True),
        Campo(4, 'NAT_CRED_DESC'),
        CampoNumerico(5, 'VL_CRED_DESC_DIFER'),
        CampoNumerico(6, 'VL_CONT_DIFER_ANT', obrigatorio=True),
        Campo(7, 'PER_APUR', obrigatorio=True),
        CampoData(8, 'DT_RECEB'),
    ]


class RegistroM350(Registro):
    """
    PIS/PASEP - Folha de Salários
    """
    campos = [
        CampoFixo(1, 'REG', 'M350'),
        CampoNumerico(2, 'VL_TOT_FOL', obrigatorio=True),
        CampoNumerico(3, 'VL_EXC_BC', obrigatorio=True),
        CampoNumerico(4, 'VL_TOT_BC', obrigatorio=True),
        CampoNumerico(5, 'ALIQ_PIS_FOL', obrigatorio=True),
        CampoNumerico(6, 'VL_TOT_CONT_FOL', obrigatorio=True),
    ]


class RegistroM400(Registro):
    """
    Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com
    Suspensão – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'M400'),
        Campo(2, 'CST_PIS', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_REC', obrigatorio=True),
        Campo(4, 'COD_CTA'),
        Campo(5, 'DESC_COMPL'),
    ]


class RegistroM410(Registro):
    """
    Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de
    Vendas com Suspensão – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', 'M410'),
        Campo(2, 'NAT_REC', obrigatorio=True),
        CampoNumerico(3, 'VL_REC', obrigatorio=True),
        Campo(4, 'COD_CTA', obrigatorio=True),
        Campo(5, 'DESC_COMPL', obrigatorio=True),
    ]


class RegistroM500(Registro):
    """
    Crédito de COFINS Relativo ao Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M500'),
        Campo(2, 'COD_CRED', obrigatorio=True),
        Campo(3, 'IND_CRED_ORI', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_COFINS'),
        CampoNumerico(5, 'ALIQ_COFINS'),
        Campo(6, 'QUANT_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(8, 'VL_CRED', obrigatorio=True),
        CampoNumerico(9, 'VL_AJUS_ACRES', obrigatorio=True),
        CampoNumerico(10, 'VL_AJUS_REDUC', obrigatorio=True),
        CampoNumerico(11, 'VL_CRED_DIFER', obrigatorio=True),
        CampoNumerico(12, 'VL_CRED_DISP', obrigatorio=True),
        Campo(13, 'IND_DESC_CRED', obrigatorio=True),
        CampoNumerico(14, 'VL_CRED_DESC'),
        Campo(15, 'SLD_CRED', obrigatorio=True),
    ]


class RegistroM505(Registro):
    """
    Detalhamento da Base de Cálculo do Crédito Apurado no Período – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'M505'),
        Campo(2, 'NAT_BC_CRED', obrigatorio=True),
        Campo(3, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_COFINS_TOT'),
        CampoNumerico(5, 'VL_BC_COFINS_CUM'),
        CampoNumerico(6, 'VL_BC_COFINS_NC'),
        CampoNumerico(7, 'VL_BC_COFINS'),
        Campo(8, 'QUANT_BC_COFINS_TOT'),
        Campo(9, 'QUANT_BC_COFINS'),
        Campo(10, 'DESC_CRED'),
    ]


class RegistroM510(Registro):
    """
    Ajustes do Crédito de COFINS Apurado
    """
    campos = [
        CampoFixo(1, 'REG', 'M510'),
        Campo(2, 'IND_AJ', obrigatorio=True),
        CampoNumerico(3, 'VL_AJ', obrigatorio=True),
        Campo(4, 'COD_AJ', obrigatorio=True),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DESCR_AJ'),
        CampoData(7, 'DT_REF'),
    ]


class RegistroM515(Registro):
    """
    Detalhamento dos Ajustes do Crédito de Cofins Apurado
    """
    campos = [
        CampoFixo(1, 'REG', 'M515'),
        Campo(2, 'DET_VALOR_AJ', obrigatorio=True),
        Campo(3, 'CST_COFINS', obrigatorio=True),
        Campo(4, 'DET_BC_CRED'),
        Campo(5, 'DET_ALIQ'),
        CampoData(6, 'DT_OPER_AJ', obrigatorio=True),
        Campo(7, 'DESC_AJ'),
        Campo(8, 'COD_CTA'),
        Campo(9, 'INFO_COMPL'),
    ]


class RegistroM600(Registro):
    """
    Consolidação da Contribuição para a Seguridade Social - COFINS do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M600'),
        CampoNumerico(2, 'VL_TOT_CONT_NC_PER', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_CRED_DESC', obrigatorio=True),
        CampoNumerico(4, 'VL_TOT_CRED_DESC_ANT', obrigatorio=True),
        CampoNumerico(5, 'VL_TOT_CONT_NC_DEV', obrigatorio=True),
        CampoNumerico(6, 'VL_RET_NC', obrigatorio=True),
        CampoNumerico(7, 'VL_OUT_DED_NC', obrigatorio=True),
        CampoNumerico(8, 'VL_CONT_NC_REC', obrigatorio=True),
        CampoNumerico(9, 'VL_TOT_CONT_CUM_PER', obrigatorio=True),
        CampoNumerico(10, 'VL_RET_CUM', obrigatorio=True),
        CampoNumerico(11, 'VL_OUT_DED_CUM', obrigatorio=True),
        CampoNumerico(12, 'VL_CONT_CUM_REC', obrigatorio=True),
        CampoNumerico(13, 'VL_TOT_CONT_REC', obrigatorio=True),
    ]


class RegistroM605(Registro):
    """
    Contribuição para a Seguridade Social - COFINS a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)
    """
    campos = [
        CampoFixo(1, 'REG', 'M605'),
        Campo(2, 'NUM_CAMPO', obrigatorio=True),
        Campo(3, 'COD_REC', obrigatorio=True),
        CampoNumerico(4, 'VL_DEBITO', obrigatorio=True),
    ]


class RegistroM610(Registro):
    """
    Detalhamento da Contribuição para a Seguridade Social - COFINS do Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M610'),
        Campo(2, 'COD_CONT', obrigatorio=True),
        CampoNumerico(3, 'VL_REC_BRT', obrigatorio=True),
        CampoNumerico(4, 'VL_BC_CONT', obrigatorio=True),
        CampoNumerico(5, 'ALIQ_COFINS'),
        Campo(6, 'QUANT_BC_COFINS'),
        CampoNumerico(7, 'ALIQ_COFINS_QUANT'),
        CampoNumerico(8, 'VL_CONT_APUR', obrigatorio=True),
        CampoNumerico(9, 'VL_AJUS_ACRES', obrigatorio=True),
        CampoNumerico(10, 'VL_AJUS_REDUC', obrigatorio=True),
        CampoNumerico(11, 'VL_CONT_DIFER'),
        CampoNumerico(12, 'VL_CONT_DIFER_ANT'),
        CampoNumerico(13, 'VL_CONT_PER', obrigatorio=True),
    ]


class RegistroM611(Registro):
    """
    Sociedades Cooperativas – Composição da Base de Cálculo – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'M611'),
        Campo(2, 'IND_TIP_COOP', obrigatorio=True),
        CampoNumerico(3, 'VL_BC_CONT_ANT_EXC_COOP', obrigatorio=True),
        CampoNumerico(4, 'VL_EXC_COOP_GER'),
        CampoNumerico(5, 'VL_EXC_ESP_COOP'),
        CampoNumerico(6, 'VL_BC_CONT', obrigatorio=True),
    ]


class RegistroM620(Registro):
    """
    Ajustes da COFINS Apurada
    """
    campos = [
        CampoFixo(1, 'REG', 'M620'),
        Campo(2, 'IND_AJ', obrigatorio=True),
        CampoNumerico(3, 'VL_AJ', obrigatorio=True),
        Campo(4, 'COD_AJ', obrigatorio=True),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DESCR_AJ'),
        CampoData(7, 'DT_REF'),
    ]


class RegistroM625(Registro):
    """
    Detalhamento dos Ajustes da Cofins Apurada
    """
    campos = [
        CampoFixo(1, 'REG', 'M625'),
        Campo(2, 'DET_VALOR_AJ', obrigatorio=True),
        Campo(3, 'CST_COFINS'),
        Campo(4, 'DET_BC_CRED'),
        Campo(5, 'DET_ALIQ'),
        CampoData(6, 'DT_OPER_AJ', obrigatorio=True),
        Campo(7, 'DESC_AJ'),
        Campo(8, 'COD_CTA'),
        Campo(9, 'INFO_COMPL'),
    ]


class RegistroM630(Registro):
    """
    Informações Adicionais de Diferimento
    """
    campos = [
        CampoFixo(1, 'REG', 'M630'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        CampoNumerico(3, 'VL_VEND', obrigatorio=True),
        CampoNumerico(4, 'VL_NAO_RECEB', obrigatorio=True),
        CampoNumerico(5, 'VL_CONT_DIF', obrigatorio=True),
        CampoNumerico(6, 'VL_CRED_DIF'),
        Campo(7, 'COD_CRED'),
    ]


class RegistroM700(Registro):
    """
    COFINS Diferida em Períodos Anteriores – Valores a Pagar no Período
    """
    campos = [
        CampoFixo(1, 'REG', 'M700'),
        Campo(2, 'COD_CONT', obrigatorio=True),
        CampoNumerico(3, 'VL_CONT_APUR_DIFER', obrigatorio=True),
        Campo(4, 'NAT_CRED_DESC'),
        CampoNumerico(5, 'VL_CRED_DESC_DIFER'),
        CampoNumerico(6, 'VL_CONT_DIFER_ANT', obrigatorio=True),
        Campo(7, 'PER_APUR', obrigatorio=True),
        CampoData(8, 'DT_RECEB'),
    ]


class RegistroM800(Registro):
    """
    Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com
    Suspensão – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'M800'),
        Campo(2, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_REC', obrigatorio=True),
        Campo(4, 'COD_CTA'),
        Campo(5, 'DESC_COMPL'),
    ]


class RegistroM810(Registro):
    """
    Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de
    Vendas com Suspensão – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', 'M810'),
        Campo(2, 'NAT_REC', obrigatorio=True),
        CampoNumerico(3, 'VL_REC', obrigatorio=True),
        Campo(4, 'COD_CTA'),
        Campo(5, 'DESC_COMPL'),
    ]


class RegistroM990(Registro):
    """
    Encerramento do Bloco M
    """
    campos = [
        CampoFixo(1, 'REG', 'M990'),
        CampoNumerico(2, 'QTD_LIN_M', obrigatorio=True),
    ]


class RegistroP001(Registro):
    """
    Abertura do Bloco P
    """
    campos = [
        CampoFixo(1, 'REG', 'P001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class RegistroP010(Registro):
    """
    Identificação do Estabelecimento
    """
    campos = [
        CampoFixo(1, 'REG', 'P010'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
    ]


class RegistroP100(Registro):
    """
    Contribuição Previdenciária sobre a Receita Bruta
    """
    campos = [
        CampoFixo(1, 'REG', 'P100'),
        CampoData(2, 'DT_INI', obrigatorio=True),
        CampoData(3, 'DT_FIN', obrigatorio=True),
        CampoNumerico(4, 'VL_REC_TOT_EST', obrigatorio=True),
        Campo(5, 'COD_ATIV_ECON', obrigatorio=True),
        CampoNumerico(6, 'VL_REC_ATIV_ESTAB', obrigatorio=True),
        CampoNumerico(7, 'VL_EXC'),
        CampoNumerico(8, 'VL_BC_CONT', obrigatorio=True),
        CampoNumerico(9, 'ALIQ_CONT', obrigatorio=True),
        CampoNumerico(10, 'VL_CONT_APU', obrigatorio=True),
        Campo(11, 'COD_CTA'),
        Campo(12, 'INFO_COMPL'),
    ]


class RegistroP110(Registro):
    """
    Complemento da Escrituração – Detalhamento da Apuração da Contribuição
    """
    campos = [
        CampoFixo(1, 'REG', 'P110'),
        Campo(2, 'NUM_CAMPO', obrigatorio=True),
        Campo(3, 'COD_DET'),
        Campo(4, 'DET_VALOR', obrigatorio=True),
        Campo(5, 'INF_COMPL'),
    ]


class RegistroP199(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', 'P199'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class RegistroP200(Registro):
    """
    Consolidação da Contribuição Previdenciária sobre a Receita Bruta
    """
    campos = [
        CampoFixo(1, 'REG', 'P200'),
        Campo(2, 'PER_REF', obrigatorio=True),
        CampoNumerico(3, 'VL_TOT_CONT_APU', obrigatorio=True),
        CampoNumerico(4, 'VL_TOT_AJ_REDUC'),
        CampoNumerico(5, 'VL_TOT_AJ_ACRES'),
        CampoNumerico(6, 'VL_TOT_CONT_DEV', obrigatorio=True),
        Campo(7, 'COD_REC', obrigatorio=True),
    ]


class RegistroP210(Registro):
    """
    Ajuste da Contribuição Previdenciária Apurada sobre a Receita Bruta
    """
    campos = [
        CampoFixo(1, 'REG', 'P210'),
        Campo(2, 'IND_AJ', obrigatorio=True),
        CampoNumerico(3, 'VL_AJ', obrigatorio=True),
        Campo(4, 'COD_AJ', obrigatorio=True),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DESCR_AJ'),
        CampoData(7, 'DT_REF'),
    ]


class RegistroP990(Registro):
    """
    Encerramento do Bloco P
    """
    campos = [
        CampoFixo(1, 'REG', 'P990'),
        CampoNumerico(2, 'QTD_LIN_P', obrigatorio=True),
    ]


class Registro1001(Registro):
    """
    Abertura do Bloco 1
    """
    campos = [
        CampoFixo(1, 'REG', '1001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class Registro1010(Registro):
    """
    Processo Referenciado – Ação Judicial
    """
    campos = [
        CampoFixo(1, 'REG', '1010'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'ID_SEC_JUD', obrigatorio=True),
        Campo(4, 'ID_VARA', obrigatorio=True),
        Campo(5, 'IND_NAT_ACAO', obrigatorio=True),
        Campo(6, 'DESC_DEC_JUD'),
        CampoData(7, 'DT_SENT_JUD'),
    ]


class Registro1020(Registro):
    """
    Processo Referenciado – Processo Administrativo
    """
    campos = [
        CampoFixo(1, 'REG', '1020'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_NAT_ACAO', obrigatorio=True),
        CampoData(4, 'DT_DEC_ADM', obrigatorio=True),
    ]


class Registro1100(Registro):
    """
    Controle de Créditos Fiscais – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1100'),
        Campo(2, 'PER_APU_CRED', obrigatorio=True),
        Campo(3, 'ORIG_CRED', obrigatorio=True),
        CampoCNPJ(4, 'CNPJ_SUC'),
        Campo(5, 'COD_CRED', obrigatorio=True),
        CampoNumerico(6, 'VL_CRED_APU', obrigatorio=True),
        CampoNumerico(7, 'VL_CRED_EXT_APU'),
        CampoNumerico(8, 'VL_TOT_CRED_APU', obrigatorio=True),
        CampoNumerico(9, 'VL_CRED_DESC_PA_ANT', obrigatorio=True),
        CampoNumerico(10, 'VL_CRED_PER_PA_ANT'),
        CampoNumerico(11, 'VL_CRED_DCOMP_PA_ANT'),
        Campo(12, 'SD_CRED_DISP_EFD', obrigatorio=True),
        CampoNumerico(13, 'VL_CRED_DESC_EFD'),
        CampoNumerico(14, 'VL_CRED_PER_EFD'),
        CampoNumerico(15, 'VL_CRED_DCOMP_EFD'),
        CampoNumerico(16, 'VL_CRED_TRANS'),
        CampoNumerico(17, 'VL_CRED_OUT'),
        Campo(18, 'SLD_CRED_FIM'),
    ]


class Registro1101(Registro):
    """
    Apuração de Crédito Extemporâneo - Documentos e Operações de Períodos Anteriores – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1101'),
        Campo(2, 'COD_PART', obrigatorio=True),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_MOD'),
        Campo(5, 'SER'),
        Campo(6, 'SUB_SER'),
        Campo(7, 'NUM_DOC'),
        CampoData(8, 'DT_OPER', obrigatorio=True),
        Campo(9, 'CHV_NFE'),
        CampoNumerico(10, 'VL_OPER', obrigatorio=True),
        Campo(11, 'CFOP'),
        Campo(12, 'NAT_BC_CRED', obrigatorio=True),
        Campo(13, 'IND_ORIG_CRED', obrigatorio=True),
        Campo(14, 'CST_PIS', obrigatorio=True),
        CampoNumerico(15, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(16, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(17, 'VL_PIS', obrigatorio=True),
        Campo(18, 'COD_CTA'),
        Campo(19, 'COD_CCUS'),
        Campo(20, 'DESC_COMPL'),
        Campo(21, 'PER_ESCRIT'),
        CampoCNPJ(22, 'CNPJ', obrigatorio=True),
    ]


class Registro1102(Registro):
    """
    Detalhamento do Crédito Extemporâneo, Vinculado a mais de um Tipo de Receita – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1102'),
        CampoNumerico(2, 'VL_CRED_PIS_TRIB_MI'),
        CampoNumerico(3, 'VL_CRED_PIS_NT_MI'),
        CampoNumerico(4, 'VL_CRED_PIS_EXP'),
    ]


class Registro1200(Registro):
    """
    Contribuição Social Extemporânea – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1200'),
        Campo(2, 'PER_APUR_ANT', obrigatorio=True),
        Campo(3, 'NAT_CONT_REC', obrigatorio=True),
        CampoNumerico(4, 'VL_CONT_APUR', obrigatorio=True),
        CampoNumerico(5, 'VL_CRED_PIS_DESC', obrigatorio=True),
        CampoNumerico(6, 'VL_CONT_DEV', obrigatorio=True),
        CampoNumerico(7, 'VL_OUT_DED', obrigatorio=True),
        CampoNumerico(8, 'VL_CONT_EXT', obrigatorio=True),
        CampoNumerico(9, 'VL_MUL'),
        CampoNumerico(10, 'VL_JUR'),
        CampoData(11, 'DT_RECOL'),
    ]


class Registro1210(Registro):
    """
    Detalhamento da Contribuição Social Extemporânea – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1210'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        Campo(3, 'CST_PIS', obrigatorio=True),
        Campo(4, 'COD_PART'),
        CampoData(5, 'DT_OPER', obrigatorio=True),
        CampoNumerico(6, 'VL_OPER', obrigatorio=True),
        CampoNumerico(7, 'VL_BC_PIS', obrigatorio=True),
        CampoNumerico(8, 'ALIQ_PIS', obrigatorio=True),
        CampoNumerico(9, 'VL_PIS', obrigatorio=True),
        Campo(10, 'COD_CTA'),
        Campo(11, 'DESC_COMPL'),
    ]


class Registro1220(Registro):
    """
    Demonstração do Crédito a Descontar da Contribuição Extemporânea – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1220'),
        Campo(2, 'PER_APU_CRED', obrigatorio=True),
        Campo(3, 'ORIG_CRED', obrigatorio=True),
        Campo(4, 'COD_CRED', obrigatorio=True),
        CampoNumerico(5, 'VL_CRED', obrigatorio=True),
    ]


class Registro1300(Registro):
    """
    Controle dos Valores Retidos na Fonte – PIS/PASEP
    """
    campos = [
        CampoFixo(1, 'REG', '1300'),
        Campo(2, 'IND_NAT_RET', obrigatorio=True),
        Campo(3, 'PR_REC_RET', obrigatorio=True),
        CampoNumerico(4, 'VL_RET_APU', obrigatorio=True),
        CampoNumerico(5, 'VL_RET_DED', obrigatorio=True),
        CampoNumerico(6, 'VL_RET_PER', obrigatorio=True),
        CampoNumerico(7, 'VL_RET_DCOMP', obrigatorio=True),
        Campo(8, 'SLD_RET', obrigatorio=True),
    ]


class Registro1500(Registro):
    """
    Controle de Créditos Fiscais – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1500'),
        Campo(2, 'PER_APU_CRED', obrigatorio=True),
        Campo(3, 'ORIG_CRED', obrigatorio=True),
        CampoCNPJ(4, 'CNPJ_SUC'),
        Campo(5, 'COD_CRED', obrigatorio=True),
        CampoNumerico(6, 'VL_CRED_APU', obrigatorio=True),
        CampoNumerico(7, 'VL_CRED_EXT_APU'),
        CampoNumerico(8, 'VL_TOT_CRED_APU', obrigatorio=True),
        CampoNumerico(9, 'VL_CRED_DESC_PA_ANT', obrigatorio=True),
        CampoNumerico(10, 'VL_CRED_PER_PA_ANT'),
        CampoNumerico(11, 'VL_CRED_DCOMP_PA_ANT'),
        Campo(12, 'SD_CRED_DISP_EFD', obrigatorio=True),
        CampoNumerico(13, 'VL_CRED_DESC_EFD'),
        CampoNumerico(14, 'VL_CRED_PER_EFD'),
        CampoNumerico(15, 'VL_CRED_DCOMP_EFD'),
        CampoNumerico(16, 'VL_CRED_TRANS'),
        CampoNumerico(17, 'VL_CRED_OUT'),
        Campo(18, 'SLD_CRED_FIM', obrigatorio=True),
    ]


class Registro1501(Registro):
    """
    Apuração de Crédito Extemporâneo - Documentos e Operações de Períodos Anteriores – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1501'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_MOD'),
        Campo(5, 'SER'),
        Campo(6, 'SUB_SER'),
        Campo(7, 'NUM_DOC'),
        CampoData(8, 'DT_OPER', obrigatorio=True),
        Campo(9, 'CHV_NFE'),
        CampoNumerico(10, 'VL_OPER', obrigatorio=True),
        Campo(11, 'CFOP'),
        Campo(12, 'NAT_BC_CRED', obrigatorio=True),
        Campo(13, 'IND_ORIG_CRED', obrigatorio=True),
        Campo(14, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(15, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(16, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(17, 'VL_COFINS', obrigatorio=True),
        Campo(18, 'COD_CTA'),
        Campo(19, 'COD_CCUS'),
        Campo(20, 'DESC_COMPL'),
        Campo(21, 'PER_ESCRIT'),
        CampoCNPJ(22, 'CNPJ', obrigatorio=True),
    ]


class Registro1502(Registro):
    """
    Detalhamento do Crédito Extemporâneo, Vinculado a mais de um Tipo de Receita – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1502'),
        CampoNumerico(2, 'VL_CRED_COFINS_TRIB_MI'),
        CampoNumerico(3, 'VL_CRED_COFINS_NT_MI'),
        CampoNumerico(4, 'VL_CRED_COFINS_EXP'),
    ]


class Registro1600(Registro):
    """
    Contribuição Social Extemporânea – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1600'),
        Campo(2, 'PER_APUR_ANT', obrigatorio=True),
        Campo(3, 'NAT_CONT_REC', obrigatorio=True),
        CampoNumerico(4, 'VL_CONT_APUR', obrigatorio=True),
        CampoNumerico(5, 'VL_CRED_COFINS_DESC', obrigatorio=True),
        CampoNumerico(6, 'VL_CONT_DEV', obrigatorio=True),
        CampoNumerico(7, 'VL_OUT_DED', obrigatorio=True),
        CampoNumerico(8, 'VL_CONT_EXT', obrigatorio=True),
        CampoNumerico(9, 'VL_MUL'),
        CampoNumerico(10, 'VL_JUR'),
        CampoData(11, 'DT_RECOL'),
    ]


class Registro1610(Registro):
    """
    Detalhamento da Contribuição Social Extemporânea – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1610'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        Campo(3, 'CST_COFINS', obrigatorio=True),
        Campo(4, 'COD_PART'),
        CampoData(5, 'DT_OPER', obrigatorio=True),
        CampoNumerico(6, 'VL_OPER', obrigatorio=True),
        CampoNumerico(7, 'VL_BC_COFINS', obrigatorio=True),
        CampoNumerico(8, 'ALIQ_COFINS', obrigatorio=True),
        CampoNumerico(9, 'VL_COFINS', obrigatorio=True),
        Campo(10, 'COD_CTA'),
        Campo(11, 'DESC_COMPL'),
    ]


class Registro1620(Registro):
    """
    Demonstração do Crédito a Descontar da Contribuição Extemporânea – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1620'),
        Campo(2, 'PER_APU_CRED', obrigatorio=True),
        Campo(3, 'ORIG_CRED', obrigatorio=True),
        Campo(4, 'COD_CRED', obrigatorio=True),
        CampoNumerico(5, 'VL_CRED', obrigatorio=True),
    ]


class Registro1700(Registro):
    """
    Controle dos Valores Retidos na Fonte – COFINS
    """
    campos = [
        CampoFixo(1, 'REG', '1700'),
        Campo(2, 'IND_NAT_RET', obrigatorio=True),
        Campo(3, 'PR_REC_RET', obrigatorio=True),
        CampoNumerico(4, 'VL_RET_APU', obrigatorio=True),
        CampoNumerico(5, 'VL_RET_DED', obrigatorio=True),
        CampoNumerico(6, 'VL_RET_PER', obrigatorio=True),
        CampoNumerico(7, 'VL_RET_DCOMP', obrigatorio=True),
        Campo(8, 'SLD_RET', obrigatorio=True),
    ]


class Registro1800(Registro):
    """
    Incorporação Imobiliária – RET
    """
    campos = [
        CampoFixo(1, 'REG', '1800'),
        Campo(2, 'INC_IMOB', obrigatorio=True),
        CampoNumerico(3, 'REC_RECEB_RET', obrigatorio=True),
        CampoNumerico(4, 'REC_FIN_RET'),
        Campo(5, 'BC_RET', obrigatorio=True),
        CampoNumerico(6, 'ALIQ_RET', obrigatorio=True),
        CampoNumerico(7, 'VL_REC_UNI', obrigatorio=True),
        CampoData(8, 'DT_REC_UNI'),
        Campo(9, 'COD_REC'),
    ]


class Registro1809(Registro):
    """
    Processo Referenciado
    """
    campos = [
        CampoFixo(1, 'REG', '1809'),
        Campo(2, 'NUM_PROC', obrigatorio=True),
        Campo(3, 'IND_PROC', obrigatorio=True),
    ]


class Registro1900(Registro):
    """
    Consolidação dos Documentos Emitidos por Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro
    Presumido – Regime de Caixa ou de Competência
    """
    campos = [
        CampoFixo(1, 'REG', '1900'),
        CampoCNPJ(2, 'CNPJ', obrigatorio=True),
        Campo(3, 'COD_MOD', obrigatorio=True),
        Campo(4, 'SER'),
        Campo(5, 'SUB_SER'),
        Campo(6, 'COD_SIT'),
        CampoNumerico(7, 'VL_TOT_REC', obrigatorio=True),
        Campo(8, 'QUANT_DOC'),
        Campo(9, 'CST_PIS'),
        Campo(10, 'CST_COFINS'),
        Campo(11, 'CFOP'),
        Campo(12, 'INF_COMPL'),
        Campo(13, 'COD_CTA'),
    ]


class Registro1990(Registro):
    """
    Encerramento do Bloco 1
    """
    campos = [
        CampoFixo(1, 'REG', '1990'),
        CampoNumerico(2, 'QTD_LIN_1', obrigatorio=True),
    ]


class Registro9001(Registro):
    """
    Abertura do Bloco 9
    """
    campos = [
        CampoFixo(1, 'REG', '9001'),
        Campo(2, 'IND_MOV', obrigatorio=True),
    ]


class Registro9900(Registro):
    """
    Registros do Arquivo
    """
    campos = [
        CampoFixo(1, 'REG', '9900'),
        Campo(2, 'REG_BLC', obrigatorio=True),
        CampoNumerico(3, 'QTD_REG_BLC', obrigatorio=True),
    ]


class Registro9990(Registro):
    """
    Encerramento do Bloco 9
    """
    campos = [
        CampoFixo(1, 'REG', '9990'),
        CampoNumerico(2, 'QTD_LIN_9', obrigatorio=True),
    ]


class Registro9999(Registro):
    """
    Encerramento do Arquivo Digital
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        CampoNumerico(2, 'QTD_LIN', obrigatorio=True),
    ]

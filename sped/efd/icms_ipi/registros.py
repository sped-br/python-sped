# -*- coding: utf-8 -*-

from ...registros import Registro
from ...campos import Campo
from ...campos import CampoData
from ...campos import CampoFixo


class Registro0000(Registro):
    """
    ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA ENTIDADE
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        Campo(2, 'COD_VER'),
        Campo(3, 'COD_FIN'),
        Campo(4, 'DT_INI'),
        Campo(5, 'DT_FIN'),
        Campo(6, 'NOME'),
        Campo(7, 'CNPJ'),
        Campo(8, 'CPF'),
        Campo(9, 'UF'),
        Campo(10, 'IE'),
        Campo(11, 'COD_MUN'),
        Campo(12, 'IM'),
        Campo(13, 'SUFRAMA'),
        Campo(14, 'IND_PERFIL'),
        Campo(15, 'IND_ATIV'),
    ]


class Registro0001(Registro):
    """
    ABERTURA DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0001'),
        Campo(2, 'IND_MOV'),
    ]


class Registro0005(Registro):
    """
    DADOS COMPLEMENTARES DA ENTIDADE
    """
    campos = [
        CampoFixo(1, 'REG', '0005'),
        Campo(2, 'FANTASIA'),
        Campo(3, 'CEP'),
        Campo(4, 'END'),
        Campo(5, 'NUM'),
        Campo(6, 'COMPL'),
        Campo(7, 'BAIRRO'),
        Campo(8, 'FONE'),
        Campo(9, 'FAX'),
        Campo(10, 'EMAIL'),
    ]


class Registro0015(Registro):
    """
    DADOS DO CONTRIBUINTE SUBSTITUTO
    """
    campos = [
        CampoFixo(1, 'REG', '0015'),
        Campo(2, 'UF_ST'),
        Campo(3, 'IE_ST'),
    ]


class Registro0100(Registro):
    """
    DADOS DO CONTABILISTA
    """
    campos = [
        CampoFixo(1, 'REG', '0100'),
        Campo(2, 'NOME'),
        Campo(3, 'CPF'),
        Campo(4, 'CRC'),
        Campo(5, 'CNPJ'),
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


class Registro0150(Registro):
    """
    TABELA DE CADASTRO DO PARTICIPANTE
    """
    campos = [
        CampoFixo(1, 'REG', '0150'),
        Campo(2, 'COD_PART'),
        Campo(3, 'NOME'),
        Campo(4, 'COD_PAIS'),
        Campo(5, 'CNPJ'),
        Campo(6, 'CPF'),
        Campo(7, 'IE'),
        Campo(8, 'COD_MUN'),
        Campo(9, 'SUFRAMA'),
        Campo(10, 'END'),
        Campo(11, 'NUM'),
        Campo(12, 'COMPL'),
        Campo(13, 'BAIRRO'),
    ]


class Registro0175(Registro):
    """
    ALTERAÇÃO DA TABELA DE CADASTRO DE PARTICIPANTE
    """
    campos = [
        CampoFixo(1, 'REG', '0175'),
        Campo(2, 'DT_ALT'),
        Campo(3, 'NR_CAMPO'),
        Campo(4, 'CONT_ANT'),
    ]


class Registro0190(Registro):
    """
    IDENTIFICAÇÃO DAS UNIDADES DE MEDIDA
    """
    campos = [
        CampoFixo(1, 'REG', '0190'),
        Campo(2, 'UNID'),
        Campo(3, 'DESCR'),
    ]


class Registro0200(Registro):
    """
    TABELA DE IDENTIFICAÇÃO DO ITEM (PRODUTO E SERVIÇOS)
    """
    campos = [
        CampoFixo(1, 'REG', '0200'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'DESCR_ITEM'),
        Campo(4, 'COD_BARRA'),
        Campo(5, 'COD_ANT_ITEM'),
        Campo(6, 'UNID_INV'),
        Campo(7, 'TIPO_ITEM'),
        Campo(8, 'COD_NCM'),
        Campo(9, 'EX_IPI'),
        Campo(10, 'COD_GEN'),
        Campo(11, 'COD_LST'),
        Campo(12, 'ALIQ_ICMS'),
    ]


class Registro0205(Registro):
    """
    ALTERAÇÃO DO ITEM
    """
    campos = [
        CampoFixo(1, 'REG', '0205'),
        Campo(2, 'DESCR_ANT_ITEM'),
        Campo(3, 'DT_INI'),
        Campo(4, 'DT_FIM'),
        Campo(5, 'COD_ANT_ITEM'),
    ]


class Registro0206(Registro):
    """
    CÓDIGO DE PRODUTO CONFORME TABELA PUBLICADA PELA ANP (COMBUSTÍVEIS)
    """
    campos = [
        CampoFixo(1, 'REG', '0206'),
        Campo(2, 'COD_COMB'),
    ]


class Registro0220(Registro):
    """
    FATORES DE CONVERSÃO DE UNIDADES
    """
    campos = [
        CampoFixo(1, 'REG', '0220'),
        Campo(2, 'UNID_CONV'),
        Campo(3, 'FAT_CONV'),
    ]


class Registro0300(Registro):
    """
    CADASTRO DE BENS OU COMPONENTES DO ATIVO IMOBILIZADO
    """
    campos = [
        CampoFixo(1, 'REG', '0300'),
        Campo(2, 'COD_IND_BEM'),
        Campo(3, 'IDENT_MERC'),
        Campo(4, 'DESCR_ITEM'),
        Campo(5, 'COD_PRNC'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'NR_PARC'),
    ]


class Registro0305(Registro):
    """
    INFORMAÇÃO SOBRE A UTILIZAÇÃO DO BEM
    """
    campos = [
        CampoFixo(1, 'REG', '0305'),
        Campo(2, 'COD_CCUS'),
        Campo(3, 'FUNC'),
        Campo(4, 'VIDA_UTIL'),
    ]


class Registro0400(Registro):
    """
    TABELA DE NATUREZA DA OPERAÇÃO/PRESTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '0400'),
        Campo(2, 'COD_NAT'),
        Campo(3, 'DESCR_NAT'),
    ]


class Registro0450(Registro):
    """
    TABELA DE INFORMAÇÃO COMPLEMENTAR DO DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', '0450'),
        Campo(2, 'COD_INF'),
        Campo(3, 'TXT'),
    ]


class Registro0460(Registro):
    """
    TABELA DE OBSERVAÇÕES DO LANÇAMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', '0460'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT'),
    ]


class Registro0500(Registro):
    """
    PLANO DE CONTAS CONTÁBEIS
    """
    campos = [
        CampoFixo(1, 'REG', '0500'),
        Campo(2, 'DT_ALT'),
        Campo(3, 'COD_NAT_CC'),
        Campo(4, 'IND_CTA'),
        Campo(5, 'NÍVEL'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'NOME_CTA'),
    ]


class Registro0600(Registro):
    """
    CENTRO DE CUSTOS
    """
    campos = [
        CampoFixo(1, 'REG', '0600'),
        Campo(2, 'DT_ALT'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'CCUS'),
    ]


class Registro0990(Registro):
    """
    ENCERRAMENTO DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0990'),
        Campo(2, 'QTD_LIN_0'),
    ]


class RegistroC001(Registro):
    """
    ABERTURA DO BLOCO C
    """
    campos = [
        CampoFixo(1, 'REG', 'C001'),
        Campo(2, 'IND_MOV'),
    ]


class RegistroC100(Registro):
    """
    DADOS NOTA FISCAL (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C100'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'COD_SIT'),
        Campo(7, 'SER'),
        Campo(8, 'NUM_DOC'),
        Campo(9, 'CHV_NFE'),
        Campo(10, 'DT_DOC'),
        Campo(11, 'DT_E_S'),
        Campo(12, 'VL_DOC'),
        Campo(13, 'IND_PGTO'),
        Campo(14, 'VL_DESC'),
        Campo(15, 'VL_ABAT_NT'),
        Campo(16, 'VL_MERC'),
        Campo(17, 'IND_FRT'),
        Campo(18, 'VL_FRT'),
        Campo(19, 'VL_SEG'),
        Campo(20, 'VL_OUT_DA'),
        Campo(21, 'VL_BC_ICMS'),
        Campo(22, 'VL_ICMS'),
        Campo(23, 'VL_BC_ICMS_ST'),
        Campo(24, 'VL_ICMS_ST'),
        Campo(25, 'VL_IPI'),
        Campo(26, 'VL_PIS'),
        Campo(27, 'VL_COFINS'),
        Campo(28, 'VL_PIS_ST'),
        Campo(29, 'VL_COFINS_ST'),
    ]


class RegistroC105(Registro):
    """
    OPERAÇÕES COM ICMS ST RECOLHIDO PARA UF DIVERSA DO DESTINATÁRIO DO DOCUMENTO FISCAL (CÓDIGO 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C105'),
        Campo(2, 'OPER'),
        Campo(3, 'UF'),
    ]


class RegistroC110(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DA NOTA FISCAL (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C110'),
        Campo(2, 'COD_INF'),
        Campo(3, 'TXT_COMPL'),
    ]


class RegistroC111(Registro):
    """
    PROCESSO REFERENCIADO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C111'),
        Campo(2, 'NUM_PROC'),
        Campo(3, 'IND_PROC'),
    ]


class RegistroC112(Registro):
    """
    DOCUMENTO DE ARRECADAÇÃO REFERENCIADO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C112'),
        Campo(2, 'COD_DA'),
        Campo(3, 'UF'),
        Campo(4, 'NUM_DA'),
        Campo(5, 'COD_AUT'),
        Campo(6, 'VL_DA'),
        Campo(7, 'DT_VCTO'),
        Campo(8, 'DT_PGTO'),
    ]


class RegistroC113(Registro):
    """
    DOCUMENTO FISCAL REFERENCIADO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C113'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'SER'),
        Campo(7, 'SUB'),
        Campo(8, 'NUM_DOC'),
        Campo(9, 'DT_DOC'),
    ]


class RegistroC114(Registro):
    """
    CUPOM FISCAL REFERENCIADO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C114'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'ECF_FAB'),
        Campo(4, 'ECF_CX'),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DT_DOC'),
    ]


class RegistroC115(Registro):
    """
    LOCAL DA COLETA E/OU ENTREGA (CÓDIGO 01, 1B, 04)
    """
    campos = [
        CampoFixo(1, 'REG', 'C115'),
        Campo(2, 'IND_CARGA'),
        Campo(3, 'CNPJ_COL'),
        Campo(4, 'IE_COL'),
        Campo(5, 'CPF_COL'),
        Campo(6, 'COD_MUN_COL'),
        Campo(7, 'CNPJ_ENTG'),
        Campo(8, 'IE_ENTG'),
        Campo(9, 'CPF_ENTG'),
        Campo(10, 'COD_MUN_ENTG'),
    ]


class RegistroC116(Registro):
    """
    CUPOM FISCAL ELETRÔNICO REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C116'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'NR_SAT'),
        Campo(4, 'CHV_CFE'),
        Campo(5, 'NUM_CFE'),
        Campo(6, 'DT_DOC'),
    ]


class RegistroC120(Registro):
    """
    OPERAÇÕES DE IMPORTAÇÃO (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C120'),
        Campo(2, 'COD_DOC_IMP'),
        Campo(3, 'NUM_DOC IMP'),
        Campo(4, 'PIS_IMP'),
        Campo(5, 'COFINS_IMP'),
        Campo(6, 'NUM_ACDRAW'),
    ]


class RegistroC130(Registro):
    """
    ISSQN, IRRF E PREVIDÊNCIA SOCIAL
    """
    campos = [
        CampoFixo(1, 'REG', 'C130'),
        Campo(2, 'VL_SERV_NT'),
        Campo(3, 'VL_BC_ISSQN'),
        Campo(4, 'VL_ISSQN'),
        Campo(5, 'VL_BC_IRRF'),
        Campo(6, 'VL_ IRRF'),
        Campo(7, 'VL_BC_PREV'),
        Campo(8, 'VL_ PREV'),
    ]


class RegistroC140(Registro):
    """
    FATURA (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C140'),
        Campo(2, 'IND_EMIT'),
        Campo(3, 'IND_TIT'),
        Campo(4, 'DESC_TIT'),
        Campo(5, 'NUM_TIT'),
        Campo(6, 'QTD_PARC'),
        Campo(7, 'VL_TIT'),
    ]


class RegistroC141(Registro):
    """
    VENCIMENTO DA FATURA (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C141'),
        Campo(2, 'NUM_PARC'),
        Campo(3, 'DT_VCTO'),
        Campo(4, 'VL_PARC'),
    ]


class RegistroC160(Registro):
    """
    VOLUMES TRANSPORTADOS (CÓDIGO 01 E 04) - EXCETO COMBUSTÍVEIS
    """
    campos = [
        CampoFixo(1, 'REG', 'C160'),
        Campo(2, 'COD_PART'),
        Campo(3, 'VEIC_ID'),
        Campo(4, 'QTD_VOL'),
        Campo(5, 'PESO_BRT'),
        Campo(6, 'PESO_LIQ'),
        Campo(7, 'UF_ID'),
    ]


class RegistroC165(Registro):
    """
    OPERAÇÕES COM COMBUSTÍVEIS
    """
    campos = [
        CampoFixo(1, 'REG', 'C165'),
        Campo(2, 'COD_PART'),
        Campo(3, 'VEIC_ID'),
        Campo(4, 'COD_AUT'),
        Campo(5, 'NR_PASSE'),
        Campo(6, 'HORA'),
        Campo(7, 'TEMPER'),
        Campo(8, 'QTD_VOL'),
        Campo(9, 'PESO_BRT'),
        Campo(10, 'PESO_LIQ'),
        Campo(11, 'NOM_MOT'),
        Campo(12, 'CPF'),
        Campo(13, 'UF_ID'),
    ]


class RegistroC170(Registro):
    """
    ITENS DO DOCUMENTO
    """
    campos = [
        CampoFixo(1, 'REG', 'C170'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'DESCR_COMPL'),
        Campo(5, 'QTD'),
        Campo(6, 'UNID'),
        Campo(7, 'VL_ITEM'),
        Campo(8, 'VL_DESC'),
        Campo(9, 'IND_MOV'),
        Campo(10, 'CST_ICMS'),
        Campo(11, 'CFOP'),
        Campo(12, 'COD_NAT'),
        Campo(13, 'VL_BC_ICMS'),
        Campo(14, 'ALIQ_ICMS'),
        Campo(15, 'VL_ICMS'),
        Campo(16, 'VL_BC_ICMS_ST'),
        Campo(17, 'ALIQ_ST'),
        Campo(18, 'VL_ICMS_ST'),
        Campo(19, 'IND_APUR'),
        Campo(20, 'CST_IPI'),
        Campo(21, 'COD_ENQ'),
        Campo(22, 'VL_BC_IPI'),
        Campo(23, 'ALIQ_IPI'),
        Campo(24, 'VL_IPI'),
        Campo(25, 'CST_PIS'),
        Campo(26, 'VL_BC_PIS'),
        Campo(27, 'ALIQ_PIS'),
        Campo(28, 'QUANT_BC_PIS'),
        Campo(29, 'ALIQ_PIS'),
        Campo(30, 'VL_PIS'),
        Campo(31, 'CST_COFINS'),
        Campo(32, 'VL_BC_COFINS'),
        Campo(33, 'ALIQ_COFINS'),
        Campo(34, 'QUANT_BC_COFINS'),
        Campo(35, 'ALIQ_COFINS'),
        Campo(36, 'VL_COFINS'),
        Campo(37, 'COD_CTA'),
    ]


class RegistroC171(Registro):
    """
    ARMAZENAMENTO DE COMBUSTÍVEIS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C171'),
        Campo(2, 'NUM_TANQUE'),
        Campo(3, 'QTDE'),
    ]


class RegistroC172(Registro):
    """
    OPERAÇÕES COM ISSQN (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C172'),
        Campo(2, 'VL_BC_ISSQN'),
        Campo(3, 'ALIQ_ISSQN'),
        Campo(4, 'VL_ISSQN'),
    ]


class RegistroC173(Registro):
    """
    OPERAÇÕES COM MEDICAMENTOS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C173'),
        Campo(2, 'LOTE_MED'),
        Campo(3, 'QTD_ITEM'),
        Campo(4, 'DT_FAB'),
        Campo(5, 'DT_VAL'),
        Campo(6, 'IND_MED'),
        Campo(7, 'TP_PROD'),
        Campo(8, 'VL_TAB_MAX'),
    ]


class RegistroC174(Registro):
    """
    OPERAÇÕES COM ARMAS DE FOGO (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C174'),
        Campo(2, 'IND_ARM'),
        Campo(3, 'NUM_ARM'),
        Campo(4, 'DESCR_COMPL'),
    ]


class RegistroC175(Registro):
    """
    OPERAÇÕES COM VEÍCULOS NOVOS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C175'),
        Campo(2, 'IND_VEIC_OPER'),
        Campo(3, 'CNPJ'),
        Campo(4, 'UF'),
        Campo(5, 'CHASSI_VEIC'),
    ]


class RegistroC176(Registro):
    """
    RESSARCIMENTO DE ICMS EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C176'),
        Campo(2, 'COD_MOD_ULT_E'),
        Campo(3, 'NUM_DOC_ULT_E'),
        Campo(4, 'SER_ULT_E'),
        Campo(5, 'DT_ULT_E'),
        Campo(6, 'COD_PART_ULT_E'),
        Campo(7, 'QUANT_ULT_E'),
        Campo(8, 'VL_UNIT_ULT_E'),
        Campo(9, 'VL_UNIT_BC_ST'),
    ]


class RegistroC177(Registro):
    """
    OPERAÇÕES COM PRODUTOS SUJEITOS A SELO DE CONTROLE IPI (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C177'),
        Campo(2, 'COD_SELO_IPI'),
        Campo(3, 'QT_SELO_IPI'),
    ]


class RegistroC178(Registro):
    """
    OPERAÇÕES COM PRODUTOS SUJEITOS À TRIBUTAÇÃO DE IPI POR UNIDADE OU QUANTIDADE DE PRODUTO (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C178'),
        Campo(2, 'CL_ENQ'),
        Campo(3, 'VL_UNID'),
        Campo(4, 'QUANT_PAD'),
    ]


class RegistroC179(Registro):
    """
    INFORMAÇÕES COMPLEMENTARES ST (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C179'),
        Campo(2, 'BC_ST_ORIG_DEST'),
        Campo(3, 'ICMS_ST_REP'),
        Campo(4, 'ICMS_ST_COMPL'),
        Campo(5, 'BC_RET'),
        Campo(6, 'ICMS_RET'),
    ]


class RegistroC190(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C190'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS_ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'VL_IPI'),
        Campo(12, 'COD_OBS'),
    ]


class RegistroC195(Registro):
    """
    OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 01, 1B E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C195'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT_COMPL'),
    ]


class RegistroC197(Registro):
    """
    OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'C197'),
        Campo(2, 'COD_AJ'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'COD_ITEM'),
        Campo(5, 'VL_BC_ICMS'),
        Campo(6, 'ALIQ_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_OUTROS'),
    ]


class RegistroC300(Registro):
    """
    RESUMO DIÁRIO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C300'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'SUB'),
        Campo(5, 'NUM_DOC_INI'),
        Campo(6, 'NUM_DOC_FIN'),
        Campo(7, 'DT_DOC'),
        Campo(8, 'VL_DOC'),
        Campo(9, 'VL_PIS'),
        Campo(10, 'VL_COFINS'),
        Campo(11, 'COD_CTA'),
    ]


class RegistroC310(Registro):
    """
    DOCUMENTOS CANCELADOS DE NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C310'),
        Campo(2, 'NUM_DOC_CANC'),
    ]


class RegistroC320(Registro):
    """
    REGISTRO ANALÍTICO DO RESUMO DIÁRIO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C320'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]


class RegistroC321(Registro):
    """
    ITENS DO RESUMO DIÁRIO DOS DOCUMENTOS (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C321'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'QTD'),
        Campo(4, 'UNID'),
        Campo(5, 'VL_ITEM'),
        Campo(6, 'VL_DESC'),
        Campo(7, 'VL_BC_ICMS'),
        Campo(8, 'VL_ICMS'),
        Campo(9, 'VL_PIS'),
        Campo(10, 'VL_COFINS'),
    ]


class RegistroC350(Registro):
    """
    NOTA FISCAL DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C350'),
        Campo(2, 'SER'),
        Campo(3, 'SUB_SER'),
        Campo(4, 'NUM_DOC'),
        Campo(5, 'DT_DOC'),
        Campo(6, 'CNPJ_CPF'),
        Campo(7, 'VL_MERC'),
        Campo(8, 'VL_DOC'),
        Campo(9, 'VL_DESC'),
        Campo(10, 'VL_PIS'),
        Campo(11, 'VL_COFINS'),
    ]


class RegistroC370(Registro):
    """
    ITENS DO DOCUMENTO (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C370'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'UNID'),
        Campo(6, 'VL_ITEM'),
        Campo(7, 'VL_DESC'),
    ]


class RegistroC390(Registro):
    """
    REGISTRO ANALÍTICO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C390'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]


class RegistroC400(Registro):
    """
    EQUIPAMENTO ECF (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C400'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'ECF_MOD'),
        Campo(4, 'ECF_FAB'),
        Campo(5, 'ECF_CX'),
    ]


class RegistroC405(Registro):
    """
    REDUÇÃO Z (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C405'),
        Campo(2, 'DT_DOC'),
        Campo(3, 'CRO'),
        Campo(4, 'CRZ'),
        Campo(5, 'NUM_COO_FIN'),
        Campo(6, 'GT_FIN'),
        Campo(7, 'VL_BRT'),
    ]


class RegistroC410(Registro):
    """
    PIS E COFINS TOTALIZADOS NO DIA (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C410'),
        Campo(2, 'VL_PIS'),
        Campo(3, 'VL_COFINS'),
    ]


class RegistroC420(Registro):
    """
    REGISTRO DOS TOTALIZADORES PARCIAIS DA REDUÇÃO Z (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C420'),
        Campo(2, 'COD_TOT_PAR'),
        Campo(3, 'VLR_ACUM_TOT'),
        Campo(4, 'NR_TOT'),
        Campo(5, 'DESCR_NR_TOT'),
    ]


class RegistroC425(Registro):
    """
    RESUMO DE ITENS DO MOVIMENTO DIÁRIO (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C425'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'QTD'),
        Campo(4, 'UNID'),
        Campo(5, 'VL_ITEM'),
        Campo(6, 'VL_PIS'),
        Campo(7, 'VL_COFINS'),
    ]


class RegistroC460(Registro):
    """
    DOCUMENTO FISCAL EMITIDO POR ECF (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C460'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'COD_SIT'),
        Campo(4, 'NUM_DOC'),
        Campo(5, 'DT_DOC'),
        Campo(6, 'VL_DOC'),
        Campo(7, 'VL_PIS'),
        Campo(8, 'VL_COFINS'),
        Campo(9, 'CPF_CNPJ'),
        Campo(10, 'NOM_ADQ'),
    ]


class RegistroC470(Registro):
    """
    ITENS DO DOCUMENTO FISCAL EMITIDO POR ECF (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C470'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'QTD'),
        Campo(4, 'QTD_CANC'),
        Campo(5, 'UNID'),
        Campo(6, 'VL_ITEM'),
        Campo(7, 'CST_ICMS'),
        Campo(8, 'CFOP'),
        Campo(9, 'ALIQ_ICMS'),
        Campo(10, 'VL_PIS'),
        Campo(11, 'VL_COFINS'),
    ]


class RegistroC490(Registro):
    """
    REGISTRO ANALÍTICO DO MOVIMENTO DIÁRIO (CÓDIGO 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C490'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]


class RegistroC495(Registro):
    """
    RESUMO MENSAL DE ITENS DO ECF POR ESTABELECIMENTO (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C495'),
        Campo(2, 'ALIQ_ICMS'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'QTD_CANC'),
        Campo(6, 'UNID'),
        Campo(7, 'VL_ITEM'),
        Campo(8, 'VL_DESC'),
        Campo(9, 'VL_CANC'),
        Campo(10, 'VL_ACMO'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'VL_ICMS'),
        Campo(13, 'VL_ISEN'),
        Campo(14, 'VL_NT'),
        Campo(15, 'VL_ICMS_ST'),
    ]


class RegistroC500(Registro):
    """
    NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA, NOTA FISCAL CONSUMO FORNECIMENTO DE GÁS E NOTA FISCAL/CONTA DE FORNECIMENTO
    DÁGUA CANALIZADA (CÓDIGO 06, 28 e 29)
    """
    campos = [
        CampoFixo(1, 'REG', 'C500'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'COD_SIT'),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'COD_CONS'),
        Campo(10, 'NUM_DOC'),
        Campo(11, 'DT_DOC'),
        Campo(12, 'DT_E_S'),
        Campo(13, 'VL_DOC'),
        Campo(14, 'VL_DESC'),
        Campo(15, 'VL_FORN'),
        Campo(16, 'VL_SERV_NT'),
        Campo(17, 'VL_TERC'),
        Campo(18, 'VL_DA'),
        Campo(19, 'VL_BC_ICMS'),
        Campo(20, 'VL_ICMS'),
        Campo(21, 'VL_BC_ICMS_ST'),
        Campo(22, 'VL_ICMS_ST'),
        Campo(23, 'COD_INF'),
        Campo(24, 'VL_PIS'),
        Campo(25, 'VL_COFINS'),
        Campo(26, 'TP_LIGACAO'),
        Campo(27, 'COD_GRUPO_TENSAO'),
    ]


class RegistroC510(Registro):
    """
    ITENS DO DOCUMENTO NOTA FISCAL/CONTA ENERGIA ELÉTRICA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS (CÓDIGO 06 E 28)
    """
    campos = [
        CampoFixo(1, 'REG', 'C510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        Campo(5, 'QTD'),
        Campo(6, 'UNID'),
        Campo(7, 'VL_ITEM'),
        Campo(8, 'VL_DESC'),
        Campo(9, 'CST_ICMS'),
        Campo(10, 'CFOP'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'ALIQ_ICMS'),
        Campo(13, 'VL_ICMS'),
        Campo(14, 'VL_BC_ICMS_ST'),
        Campo(15, 'ALIQ_ST'),
        Campo(16, 'VL_ICMS_ST'),
        Campo(17, 'IND_REC'),
        Campo(18, 'COD_PART'),
        Campo(19, 'VL_PIS'),
        Campo(20, 'VL_COFINS'),
        Campo(21, 'COD_CTA'),
    ]


class RegistroC590(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO - NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA E NOTA FISCAL CONSUMO FORNECIMENTO DE GÁS
    (CÓDIGO 06 E 28)
    """
    campos = [
        CampoFixo(1, 'REG', 'C590'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS_ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroC600(Registro):
    """
    CONSOLIDAÇÃO DIÁRIA DE NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE FORNECIMENTO DÁGUA CANALIZADA
    E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS (EMPRESAS NÃO OBRIGADAS AO CONVÊNIO ICMS 115/03) - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C600'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'COD_MUN'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'COD_CONS'),
        Campo(7, 'QTD_CONS'),
        Campo(8, 'QTD_CANC'),
        Campo(9, 'DT_DOC'),
        Campo(10, 'VL_DOC'),
        Campo(11, 'VL_DESC'),
        Campo(12, 'CONS'),
        Campo(13, 'VL_FORN'),
        Campo(14, 'VL_SERV_NT'),
        Campo(15, 'VL_TERC'),
        Campo(16, 'VL_DA'),
        Campo(17, 'VL_BC_ICMS'),
        Campo(18, 'VL_ICMS'),
        Campo(19, 'VL_BC_ICMS_ST'),
        Campo(20, 'VL_ICMS_ST'),
        Campo(21, 'VL_PIS'),
        Campo(22, 'VL_COFINS'),
    ]


class RegistroC601(Registro):
    """
    DOCUMENTOS CANCELADOS - CONSOLIDAÇÃO DIÁRIA DE NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE
    FORNECIMENTO DÁGUA CANALIZADA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C601'),
        Campo(2, 'NUM_DOC_CANC'),
    ]


class RegistroC610(Registro):
    """
    ITENS DO DOCUMENTO CONSOLIDADO, NOTA FISCAL/CONTA DE FORNECIMENTO DÁGUA CANALIZADA E NOTA FISCAL/CONTA DE
    FORNECIMENTO DE GÁS (EMPRESAS NÃO OBRIGADAS AO CONVÊNIO ICMS 115/03) - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C610'),
        Campo(2, 'COD_CLASS'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'UNID'),
        Campo(6, 'VL_ITEM'),
        Campo(7, 'VL_DESC'),
        Campo(8, 'CST_ICMS'),
        Campo(9, 'CFOP'),
        Campo(10, 'ALIQ_ICMS'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'VL_ICMS'),
        Campo(13, 'VL_BC_ICMS_ST'),
        Campo(14, 'VL_ICMS_ST'),
        Campo(15, 'VL_PIS'),
        Campo(16, 'VL_COFINS'),
        Campo(17, 'COD_CTA'),
    ]


class RegistroC690(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE FORNECIMENTO D’ÁGUA
    CANALIZADA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C690'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_RED_BC'),
        Campo(9, 'VL_BC_ICMS_ST'),
        Campo(10, 'VL_ICMS_ST'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroC700(Registro):
    """
    CONSOLIDAÇÃO DOS DOCUMENTOS NOTA FISCAL/CONTA ENERGIA ELÉTRICA, EMITIDAS EM VIA ÚNICA (EMPRESAS OBRIGADAS AO
    CONVÊNIO ICMS 115/03) E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS CANALIZADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C700'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'NRO_ORD_INI'),
        Campo(5, 'NRO_ORD_FIN'),
        Campo(6, 'DT_DOC_INI'),
        Campo(7, 'DT_DOC_FIN'),
        Campo(8, 'NOM_MEST'),
    ]


class RegistroC790(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS
    """
    campos = [
        CampoFixo(1, 'REG', 'C790'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS_ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroC791(Registro):
    """
    REGISTRO DE INFORMAÇÕES DE ST POR UF
    """
    campos = [
        CampoFixo(1, 'REG', 'C791'),
        Campo(2, 'UF'),
        Campo(3, 'VL_BC_ICMS_ST'),
        Campo(4, 'VL_ICMS_ST'),
    ]


class RegistroC800(Registro):
    """
    CUPOM FISCAL ELETRÔNICO (CÓDIGO 59)
    """
    campos = [
        CampoFixo(1, 'REG', 'C800'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'COD_SIT'),
        Campo(4, 'NUM_CFE'),
        Campo(5, 'DT_DOC'),
        Campo(6, 'VL_CFE'),
        Campo(7, 'VL_PIS'),
        Campo(8, 'VL_COFINS'),
        Campo(9, 'CNPJ_CPF'),
        Campo(10, 'NR_SAT'),
        Campo(11, 'CHV_CFE'),
        Campo(12, 'VL_DESC'),
        Campo(13, 'VL_MERC'),
        Campo(14, 'VL_OUT_DA'),
        Campo(15, 'VL_ICMS'),
        Campo(16, 'VL_PIS_ST'),
        Campo(17, 'VL_COFINS_ST'),
    ]


class RegistroC850(Registro):
    """
    REGISTRO ANALÍTICO DO CF-E (CODIGO 59)
    """
    campos = [
        CampoFixo(1, 'REG', 'C850'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]


class RegistroC860(Registro):
    """
    IDENTIFICAÇÃO DO EQUIPAMENTO SAT-CF-E
    """
    campos = [
        CampoFixo(1, 'REG', 'C860'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'NR_SAT'),
        Campo(4, 'DT_DOC'),
        Campo(5, 'DOC_INI'),
        Campo(6, 'DOC_FIM'),
    ]


class RegistroC890(Registro):
    """
    RESUMO DIÁRIO DO CF-E (CÓDIGO 59) POR EQUIPAMENTO SAT-CF-E
    """
    campos = [
        CampoFixo(1, 'REG', 'C890'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]


class RegistroC990(Registro):
    """
    ENCERRAMENTO DO BLOCO C
    """
    campos = [
        CampoFixo(1, 'REG', 'C990'),
        Campo(2, 'QTD_LIN_C'),
    ]


class RegistroD001(Registro):
    """
    ABERTURA DO BLOCO D
    """
    campos = [
        CampoFixo(1, 'REG', 'D001'),
        Campo(2, 'IND_MOV'),
    ]


class RegistroD100(Registro):
    """
    NOTA FISCAL DE SERVIÇO DE TRANSPORTE E CONHECIMENTOS DE TRANSPORTE RODOVIÁRIO DE CARGAS, CONHECIMENTOS DE TRANSPORTE
    DE CARGAS AVULSO (CÓDIGO 8B), AQUAVIÁRIO DE CARGAS, AÉREO, FERROVIÁRIO DE CARGAS E MULTIMODAL DE CARGAS, NOTA FISCAL
    DE TRANSPORTE FERROVIÁRIO DE CARGA E CONHECIMENTO DE TRANSPORTE ELETRÔNICO - CT-E - (CÓDIGO 07, 08, 09, 10, 11, 26,
    27 E 57)
    """
    campos = [
        CampoFixo(1, 'REG', 'D100'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'COD_SIT'),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'NUM_DOC'),
        Campo(10, 'CHV_CTE'),
        Campo(11, 'DT_DOC'),
        Campo(12, 'DT_A_P'),
        Campo(13, 'TP_CT-e'),
        Campo(14, 'CHV_CTE_REF'),
        Campo(15, 'VL_DOC'),
        Campo(16, 'VL_DESC'),
        Campo(17, 'IND_FRT'),
        Campo(18, 'VL_SERV'),
        Campo(19, 'VL_BC_ICMS'),
        Campo(20, 'VL_ICMS'),
        Campo(21, 'VL_NT'),
        Campo(22, 'COD_INF'),
        Campo(23, 'COD_CTA'),
    ]


class RegistroD110(Registro):
    """
    ITENS DO DOCUMENTO - NOTA FISCAL DE SERVIÇOS DE TRANSPORTE (CÓDIGO 07)
    """
    campos = [
        CampoFixo(1, 'REG', 'D110'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'VL_SERV'),
        Campo(5, 'VL_OUT'),
    ]


class RegistroD120(Registro):
    """
    COMPLEMENTO DA NOTA FISCAL DE SERVIÇOS DE TRANSPORTE (CÓDIGO 07)
    """
    campos = [
        CampoFixo(1, 'REG', 'D120'),
        Campo(2, 'COD_MUN_ORIG'),
        Campo(3, 'COD_MUN_DEST'),
        Campo(4, 'VEIC_ID'),
        Campo(5, 'UF_ID'),
    ]


class RegistroD130(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO RODOVIÁRIO DE CARGAS E DO CONHECIMENTO RODOVIÁRIO DE CARGAS AVULSO (CÓDIGO 08 E 08B)
    """
    campos = [
        CampoFixo(1, 'REG', 'D130'),
        Campo(2, 'COD_PART_CONSG'),
        Campo(3, 'COD_PART_RED'),
        Campo(4, 'IND_FRT_RED'),
        Campo(5, 'COD_MUN_ORIG'),
        Campo(6, 'COD_MUN_DEST'),
        Campo(7, 'VEIC_ID'),
        Campo(8, 'VL_LIQ_FRT'),
        Campo(9, 'VL_SEC_CAT'),
        Campo(10, 'VL_DESP'),
        Campo(11, 'VL_PEDG'),
        Campo(12, 'VL_OUT'),
        Campo(13, 'VL_FRT'),
        Campo(14, 'UF_ID'),
    ]


class RegistroD140(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO AQUAVIÁRIO DE CARGAS (CÓDIGO 09)
    """
    campos = [
        CampoFixo(1, 'REG', 'D140'),
        Campo(2, 'COD_PART_CONSG'),
        Campo(3, 'COD_MUN_ORIG'),
        Campo(4, 'COD_MUN_DEST'),
        Campo(5, 'IND_VEIC'),
        Campo(6, 'VEIC_ID'),
        Campo(7, 'IND_NAV'),
        Campo(8, 'VIAGEM'),
        Campo(9, 'VL_FRT_LIQ'),
        Campo(10, 'VL_DESP_PORT'),
        Campo(11, 'VL_DESP_CAR_DESC'),
        Campo(12, 'VL_OUT'),
        Campo(13, 'VL_FRT_BRT'),
        Campo(14, 'VL_FRT_MM'),
    ]


class RegistroD150(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO AÉREO (CÓDIGO 10)
    """
    campos = [
        CampoFixo(1, 'REG', 'D150'),
        Campo(2, 'COD_MUN_ORIG'),
        Campo(3, 'COD_MUN_DEST'),
        Campo(4, 'VEIC_ID'),
        Campo(5, 'VIAGEM'),
        Campo(6, 'IND_TFA'),
        Campo(7, 'VL_PESO_TX'),
        Campo(8, 'VL_TX_TERR'),
        Campo(9, 'VL_TX_RED'),
        Campo(10, 'VL_OUT'),
        Campo(11, 'VL_TX_ADV'),
    ]


class RegistroD160(Registro):
    """
    CARGA TRANSPORTADA (CÓDIGO 08, 8B, 09, 10, 11, 26 E 27)
    """
    campos = [
        CampoFixo(1, 'REG', 'D160'),
        Campo(2, 'DESPACHO'),
        Campo(3, 'CNPJ_CPF_REM'),
        Campo(4, 'IE_REM'),
        Campo(5, 'COD_MUN_ORI'),
        Campo(6, 'CNPJ_CPF_DEST'),
        Campo(7, 'IE_DEST'),
        Campo(8, 'COD_MUN_DEST'),
    ]


class RegistroD161(Registro):
    """
    LOCAL DA COLETA E ENTREGA (CÓDIGO 08, 8B, 09, 10, 11 E 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D161'),
        Campo(2, 'IND_CARGA'),
        Campo(3, 'CNPJ_CPF_COL'),
        Campo(4, 'IE_COL'),
        Campo(5, 'COD_MUN_COL'),
        Campo(6, 'CNPJ_CPF_ENTG'),
        Campo(7, 'IE_ENTG'),
        Campo(8, 'COD_MUN_ENTG'),
    ]


class RegistroD162(Registro):
    """
    IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS (CÓDIGOS 08, 8B, 09, 10, 11, 26 E 27)
    """
    campos = [
        CampoFixo(1, 'REG', 'D162'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'NUM_DOC'),
        Campo(5, 'DT_DOC'),
        Campo(6, 'VL_DOC'),
        Campo(7, 'VL_MERC'),
        Campo(8, 'QTD_VOL'),
        Campo(9, 'PESO_BRT'),
        Campo(10, 'PESO_LIQ'),
    ]


class RegistroD170(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO MULTIMODAL DE CARGAS (CÓDIGO 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D170'),
        Campo(2, 'COD_PART_CONSG'),
        Campo(3, 'COD_PART_RED'),
        Campo(4, 'COD_MUN_ORIG'),
        Campo(5, 'COD_MUN_DEST'),
        Campo(6, 'OTM'),
        Campo(7, 'IND_NAT_FRT'),
        Campo(8, 'VL_LIQ_FRT'),
        Campo(9, 'VL_GRIS'),
        Campo(10, 'VL_PDG'),
        Campo(11, 'VL_OUT'),
        Campo(12, 'VL_FRT'),
        Campo(13, 'VEIC_ID'),
        Campo(14, 'UF_ID'),
    ]


class RegistroD180(Registro):
    """
    MODAIS (CÓDIGO 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D180'),
        Campo(2, 'NUM_SEQ'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'CNPJ_CPF_EMIT'),
        Campo(5, 'UF_EMIT'),
        Campo(6, 'IE_EMIT'),
        Campo(7, 'COD_MUN_ORIG'),
        Campo(8, 'CNPJ_CPF_TOM'),
        Campo(9, 'UF_TOM'),
        Campo(10, 'IE_TOM'),
        Campo(11, 'COD_MUN_DEST'),
        Campo(12, 'COD_MOD'),
        Campo(13, 'SER'),
        Campo(14, 'SUB'),
        Campo(15, 'NUM_DOC'),
        Campo(16, 'DT_DOC'),
        Campo(17, 'VL_DOC'),
    ]


class RegistroD190(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27 E 57)
    """
    campos = [
        CampoFixo(1, 'REG', 'D190'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]


class RegistroD195(Registro):
    """
    OBSERVAÇOES DO LANÇAMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'D195'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT_COMPL'),
    ]


class RegistroD197(Registro):
    """
    OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'D197'),
        Campo(2, 'COD_AJ'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'COD_ITEM'),
        Campo(5, 'VL_BC_ICMS'),
        Campo(6, 'ALIQ_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_OUTROS'),
    ]


class RegistroD300(Registro):
    """
    REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE PASSAGEM RODOVIÁRIO, DE PASSAGEM AQUAVIÁRIO, DE PASSAGEM E NOTA DE
    BAGAGEM E DE PASSAGEM FERROVIÁRIO (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D300'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'SUB'),
        Campo(5, 'NUM_DOC_INI'),
        Campo(6, 'NUM_DOC_FIN'),
        Campo(7, 'CST_ICMS'),
        Campo(8, 'CFOP'),
        Campo(9, 'ALIQ_ICMS'),
        Campo(10, 'DT_DOC'),
        Campo(11, 'VL_OPR'),
        Campo(12, 'VL_DESC'),
        Campo(13, 'VL_SERV'),
        Campo(14, 'VL_SEG'),
        Campo(15, 'VL_OUT DESP'),
        Campo(16, 'VL_BC_ICMS'),
        Campo(17, 'VL_ICMS'),
        Campo(18, 'VL_RED_BC'),
        Campo(19, 'COD_OBS'),
        Campo(20, 'COD_CTA'),
    ]


class RegistroD301(Registro):
    """
    DOCUMENTOS CANCELADOS DOS BILHETES DE PASSAGEM RODOVIÁRIO, DE PASSAGEM AQUAVIÁRIO, DE PASSAGEM E NOTA DE BAGAGEM E
    DE PASSAGEM FERROVIÁRIO (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D301'),
        Campo(2, 'NUM_DOC_CANC'),
    ]


class RegistroD310(Registro):
    """
    COMPLEMENTO DOS BILHETES (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D310'),
        Campo(2, 'COD_MUN_ORIG'),
        Campo(3, 'VL_SERV'),
        Campo(4, 'VL_BC_ICMS'),
        Campo(5, 'VL_ICMS'),
    ]


class RegistroD350(Registro):
    """
    EQUIPAMENTO ECF (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D350'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'ECF_MOD'),
        Campo(4, 'ECF_FAB'),
        Campo(5, 'ECF_CX'),
    ]


class RegistroD355(Registro):
    """
    REDUÇÃO Z (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D355'),
        Campo(2, 'DT_DOC'),
        Campo(3, 'CRO'),
        Campo(4, 'CRZ'),
        Campo(5, 'NUM_COO_FIN'),
        Campo(6, 'GT_FIN'),
        Campo(7, 'VL_BRT'),
    ]


class RegistroD360(Registro):
    """
    PIS E COFINS TOTALIZADOS NO DIA (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D360'),
        Campo(2, 'VL_PIS'),
        Campo(3, 'VL_COFINS'),
    ]


class RegistroD365(Registro):
    """
    REGISTRO DOS TOTALIZADORES PARCIAIS DA REDUÇÃO Z (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D365'),
        Campo(2, 'COD_TOT_PAR'),
        Campo(3, 'VLR_ACUM_TOT'),
        Campo(4, 'NR_TOT'),
        Campo(5, 'DESCR_NR_TOT'),
    ]


class RegistroD370(Registro):
    """
    COMPLEMENTO DOS DOCUMENTOS INFORMADOS (CÓDIGOS 13, 14, 15 E 16 E 2E)
    """
    campos = [
        CampoFixo(1, 'REG', 'D370'),
        Campo(2, 'COD_MUN_ORIG'),
        Campo(3, 'VL_SERV'),
        Campo(4, 'QTD_BILH'),
        Campo(5, 'VL_BC_ICMS'),
        Campo(6, 'VL_ICMS'),
    ]


class RegistroD390(Registro):
    """
    REGISTRO ANALÍTICO DO MOVIMENTO DIÁRIO (CÓDIGOS 13, 14, 15, 16 E 2E)
    """
    campos = [
        CampoFixo(1, 'REG', 'D390'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ISSQN'),
        Campo(7, 'ALIQ_ISSQN'),
        Campo(8, 'VL_ISSQN'),
        Campo(9, 'VL_BC_ICMS'),
        Campo(10, 'VL_ICMS'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroD400(Registro):
    """
    RESUMO DE MOVIMENTO DIÁRIO - RMD (CÓDIGO 18)
    """
    campos = [
        CampoFixo(1, 'REG', 'D400'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'COD_SIT'),
        Campo(5, 'SER'),
        Campo(6, 'SUB'),
        Campo(7, 'NUM_DOC'),
        Campo(8, 'DT_DOC'),
        Campo(9, 'VL_DOC'),
        Campo(10, 'VL_DESC'),
        Campo(11, 'VL_SERV'),
        Campo(12, 'VL_BC_ICMS'),
        Campo(13, 'VL_ICMS'),
        Campo(14, 'VL_PIS'),
        Campo(15, 'VL_COFINS'),
        Campo(16, 'COD_CTA'),
    ]


class RegistroD410(Registro):
    """
    DOCUMENTOS INFORMADOS (CÓDIGOS 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D410'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'SUB'),
        Campo(5, 'NUM_DOC_INI'),
        Campo(6, 'NUM_DOC_FIN'),
        Campo(7, 'DT_DOC'),
        Campo(8, 'CST_ICMS'),
        Campo(9, 'CFOP'),
        Campo(10, 'ALIQ_ICMS'),
        Campo(11, 'VL_OPR'),
        Campo(12, 'VL_DESC'),
        Campo(13, 'VL_SERV'),
        Campo(14, 'VL_BC_ICMS'),
        Campo(15, 'VL_ICMS'),
    ]


class RegistroD411(Registro):
    """
    DOCUMENTOS CANCELADOS DOS DOCUMENTOS INFORMADOS (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D411'),
        Campo(2, 'NUM_DOC_CANC'),
    ]


class RegistroD420(Registro):
    """
    COMPLEMENTO DOS DOCUMENTOS INFORMADOS (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D420'),
        Campo(2, 'COD_MUN_ORIG'),
        Campo(3, 'VL_SERV'),
        Campo(4, 'VL_BC_ICMS'),
        Campo(5, 'VL_ICMS'),
    ]


class RegistroD500(Registro):
    """
    NOTA FISCAL DE SERVIÇO DE COMUNICAÇÃO E NOTA FISCAL DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D500'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'COD_SIT'),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'NUM_DOC'),
        Campo(10, 'DT_DOC'),
        Campo(11, 'DT_A_P'),
        Campo(12, 'VL_DOC'),
        Campo(13, 'VL_DESC'),
        Campo(14, 'VL_SERV'),
        Campo(15, 'VL_SERV_NT'),
        Campo(16, 'VL_TERC'),
        Campo(17, 'VL_DA'),
        Campo(18, 'VL_BC_ICMS'),
        Campo(19, 'VL_ICMS'),
        Campo(20, 'COD_INF'),
        Campo(21, 'VL_PIS'),
        Campo(22, 'VL_COFINS'),
        Campo(23, 'COD_CTA'),
        Campo(24, 'TP_ASSINANTE'),
    ]


class RegistroD510(Registro):
    """
    ITENS DO DOCUMENTO - NOTA FISCAL DE SERVIÇO DE COMUNICAÇÃO E SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        Campo(5, 'QTD'),
        Campo(6, 'UNID'),
        Campo(7, 'VL_ITEM'),
        Campo(8, 'VL_DESC'),
        Campo(9, 'CST_ICMS'),
        Campo(10, 'CFOP'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'ALIQ_ICMS'),
        Campo(13, 'VL_ICMS'),
        Campo(14, 'VL_BC_ICMS_ST'),
        Campo(15, 'VL_ICMS_ST'),
        Campo(16, 'IND_REC'),
        Campo(17, 'COD_PART'),
        Campo(18, 'VL_PIS'),
        Campo(19, 'VL_COFINS'),
        Campo(20, 'COD_CTA'),
    ]


class RegistroD530(Registro):
    """
    TERMINAL FATURADO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D530'),
        Campo(2, 'IND_SERV'),
        Campo(3, 'DT_INI_SERV'),
        Campo(4, 'DT_FIN_SERV'),
        Campo(5, 'PER_FISCAL'),
        Campo(6, 'COD_AREA'),
        Campo(7, 'TERMINAL'),
    ]


class RegistroD590(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D590'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS_ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroD600(Registro):
    """
    CONSOLIDAÇÃO DA PRESTAÇÃO DE SERVIÇOS - NOTAS DE SERVIÇO DE COMUNICAÇÃO E DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21
    E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D600'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'COD_MUN'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'COD_CONS'),
        Campo(7, 'QTD_CONS'),
        Campo(8, 'DT_DOC'),
        Campo(9, 'VL_DOC'),
        Campo(10, 'VL_DESC'),
        Campo(11, 'VL_SERV'),
        Campo(12, 'VL_SERV_N T'),
        Campo(13, 'VL_TERC'),
        Campo(14, 'VL_DA'),
        Campo(15, 'VL_BC_ICMS'),
        Campo(16, 'VL_ICMS'),
        Campo(17, 'VL_PIS'),
        Campo(18, 'VL_COFINS'),
    ]


class RegistroD610(Registro):
    """
    ITENS DO DOCUMENTO CONSOLIDADO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D610'),
        Campo(2, 'COD_CLASS'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'UNID'),
        Campo(6, 'VL_ITEM'),
        Campo(7, 'VL_DESC'),
        Campo(8, 'CST_ICMS'),
        Campo(9, 'CFOP'),
        Campo(10, 'ALIQ_ICMS'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'VL_ICMS'),
        Campo(13, 'VL_BC_ICMS _ST'),
        Campo(14, 'VL_ICMS_ST'),
        Campo(15, 'VL_RED_BC'),
        Campo(16, 'VL_PIS'),
        Campo(17, 'VL_COFINS'),
        Campo(18, 'COD_CTA'),
    ]


class RegistroD690(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D690'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS _ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroD695(Registro):
    """
    CONSOLIDAÇÃO DA PRESTAÇÃO DE SERVIÇOS - NOTAS DE SERVIÇO DE COMUNICAÇÃO E DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21
    E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D695'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        Campo(4, 'NRO_ORD_INI'),
        Campo(5, 'NRO_ORD_FIN'),
        Campo(6, 'DT_DOC_INI'),
        Campo(7, 'DT_DOC_FIN'),
        Campo(8, 'NOM_MEST'),
    ]


class RegistroD696(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D696'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'CFOP'),
        Campo(4, 'ALIQ_ICMS'),
        Campo(5, 'VL_OPR'),
        Campo(6, 'VL_BC_ICMS'),
        Campo(7, 'VL_ICMS'),
        Campo(8, 'VL_BC_ICMS_ST'),
        Campo(9, 'VL_ICMS_ST'),
        Campo(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]


class RegistroD697(Registro):
    """
    REGISTRO DE INFORMAÇÕES DE OUTRAS UFs, RELATIVAMENTE AOS SERVIÇOS “NÃO-MEDIDOS” DE TELEVISÃO POR ASSINATURA VIA
    SATÉLITE
    """
    campos = [
        CampoFixo(1, 'REG', 'D697'),
        Campo(2, 'UF'),
        Campo(3, 'VL_BC_ICMS'),
        Campo(4, 'VL_ICMS'),
    ]


class RegistroD990(Registro):
    """
    ENCERRAMENTO DO BLOCO D
    """
    campos = [
        CampoFixo(1, 'REG', 'D990'),
        Campo(2, 'QTD_LIN_D'),
    ]


class RegistroE001(Registro):
    """
    ABERTURA DO BLOCO E
    """
    campos = [
        CampoFixo(1, 'REG', 'E001'),
        Campo(2, 'IND_MOV'),
    ]


class RegistroE100(Registro):
    """
    PERÍODO DA APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', 'E100'),
        Campo(2, 'DT_INI'),
        Campo(3, 'DT_FIN'),
    ]


class RegistroE110(Registro):
    """
    APURAÇÃO DO ICMS - OPERAÇÕES PRÓPRIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'E110'),
        Campo(2, 'VL_TOT_DEBITOS'),
        Campo(3, 'VL_AJ_DEBITOS'),
        Campo(4, 'VL_TOT_AJ_DEBITOS'),
        Campo(5, 'VL_ESTORNOS_CRED'),
        Campo(6, 'VL_TOT_CREDITOS'),
        Campo(7, 'VL_AJ_CREDITOS'),
        Campo(8, 'VL_TOT_AJ_CREDITOS'),
        Campo(9, 'VL_ESTORNOS_DEB'),
        Campo(10, 'VL_SLD_CREDOR_ANT'),
        Campo(11, 'VL_SLD_APURADO'),
        Campo(12, 'VL_TOT_DED'),
        Campo(13, 'VL_ICMS_RECOLHER'),
        Campo(14, 'VL_SLD_CREDOR_TRANSPORTAR'),
        Campo(15, 'DEB_ESP'),
    ]


class RegistroE111(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', 'E111'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'VL_AJ_APUR'),
    ]


class RegistroE112(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', 'E112'),
        Campo(2, 'NUM_DA'),
        Campo(3, 'NUM_PROC'),
        Campo(4, 'IND_PROC'),
        Campo(5, 'PROC'),
        Campo(6, 'TXT_COMPL'),
    ]


class RegistroE113(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS - IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', 'E113'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'NUM_DOC'),
        Campo(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        Campo(9, 'VL_AJ_ITEM'),
    ]


class RegistroE115(Registro):
    """
    INFORMAÇÕES ADICIONAIS DA APURAÇÃO - VALORES DECLARATÓRIOS
    """
    campos = [
        CampoFixo(1, 'REG', 'E115'),
        Campo(2, 'COD_INF_ADIC'),
        Campo(3, 'VL_INF_ADIC'),
        Campo(4, 'DESCR_COMPL_AJ'),
    ]


class RegistroE116(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - OPERAÇÕES PRÓPRIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'E116'),
        Campo(2, 'COD_OR'),
        Campo(3, 'VL_OR'),
        Campo(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
    ]


class RegistroE200(Registro):
    """
    PERÍODO DA APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E200'),
        Campo(2, 'UF'),
        Campo(3, 'DT_INI'),
        Campo(4, 'DT_FIN'),
    ]


class RegistroE210(Registro):
    """
    APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E210'),
        Campo(2, 'IND_MOV_ST'),
        Campo(3, 'VL_SLD_CRED_ANT_ST'),
        Campo(4, 'VL_DEVOL_ST'),
        Campo(5, 'VL_RESSARC_ST'),
        Campo(6, 'VL_OUT_CRED_ST'),
        Campo(7, 'VL_AJ_CREDITOS_ST'),
        Campo(8, 'VL_RETENÇAO_ST'),
        Campo(9, 'VL_OUT_DEB_ST'),
        Campo(10, 'VL_AJ_DEBITOS_ST'),
        Campo(11, 'VL_SLD_DEV_ANT_ST'),
        Campo(12, 'VL_DEDUÇÕES_ST'),
        Campo(13, 'VL_ICMS_RECOL_ST'),
        Campo(14, 'VL_SLD_CRED_ST_TRAN SPORTAR'),
        Campo(15, 'DEB_ESP_ST'),
    ]


class RegistroE220(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E220'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'VL_AJ_APUR'),
    ]


class RegistroE230(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E230'),
        Campo(2, 'NUM_DA'),
        Campo(3, 'NUM_PROC'),
        Campo(4, 'IND_PROC'),
        Campo(5, 'PROC'),
        Campo(6, 'TXT_COMPL'),
    ]


class RegistroE240(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA - IDENTIFICAÇÃO DOS DOCUMENTOS
    FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', 'E240'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'NUM_DOC'),
        Campo(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        Campo(9, 'VL_AJ_ITEM'),
    ]


class RegistroE250(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E250'),
        Campo(2, 'COD_OR'),
        Campo(3, 'VL_OR'),
        Campo(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]


class RegistroE500(Registro):
    """
    PERÍODO DE APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E500'),
        Campo(2, 'IND_APUR'),
        Campo(3, 'DT_INI'),
        Campo(4, 'DT_FIN'),
    ]


class RegistroE510(Registro):
    """
    CONSOLIDAÇÃO DOS VALORES DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E510'),
        Campo(2, 'CFOP'),
        Campo(3, 'CST_IPI'),
        Campo(4, 'VL_CONT_IPI'),
        Campo(5, 'VL_BC_IPI'),
        Campo(6, 'VL_IPI'),
    ]


class RegistroE520(Registro):
    """
    APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E520'),
        Campo(2, 'VL_SD_ANT_IPI'),
        Campo(3, 'VL_DEB_IPI'),
        Campo(4, 'VL_CRED_IPI'),
        Campo(5, 'VL_OD_IPI'),
        Campo(6, 'VL_OC_IPI'),
        Campo(7, 'VL_SC_IPI'),
        Campo(8, 'VL_SD_IPI'),
    ]


class RegistroE530(Registro):
    """
    AJUSTES DA APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E530'),
        Campo(2, 'IND_AJ'),
        Campo(3, 'VL_AJ'),
        Campo(4, 'COD_AJ'),
        Campo(5, 'IND_DOC'),
        Campo(6, 'NUM_DOC'),
        Campo(7, 'DESCR_AJ'),
    ]


class RegistroE990(Registro):
    """
    ENCERRAMENTO DO BLOCO E
    """
    campos = [
        CampoFixo(1, 'REG', 'E990'),
        Campo(2, 'QTD_LIN_E'),
    ]


class RegistroG001(Registro):
    """
    ABERTURA DO BLOCO G
    """
    campos = [
        CampoFixo(1, 'REG', 'G001'),
        Campo(2, 'IND_MO V'),
    ]


class RegistroG110(Registro):
    """
    ICMS ATIVO PERMANENTE CIAP
    """
    campos = [
        CampoFixo(1, 'REG', 'G110'),
        Campo(2, 'DT_INI'),
        Campo(3, 'DT_FIN'),
        Campo(4, 'SALDO_IN_ICMS'),
        Campo(5, 'SOM_PARC'),
        Campo(6, 'VL_TRIB_EXP'),
        Campo(7, 'VL_TOTAL'),
        Campo(8, 'IND_PER_SAI'),
        Campo(9, 'ICMS_APROP'),
        Campo(10, 'SOM_ICMS_OC'),
    ]


class RegistroG125(Registro):
    """
    MOVIMENTAÇÃO DE BEM OU COMPONENTE DO ATIVO IMOBILIZADO
    """
    campos = [
        CampoFixo(1, 'REG', 'G125'),
        Campo(2, 'COD_IND_BEM'),
        Campo(3, 'DT_MOV'),
        Campo(4, 'TIPO_MOV'),
        Campo(5, 'VL_IMOB_ICMS_OP'),
        Campo(6, 'VL_IMOB_ICMS_ST'),
        Campo(7, 'VL_IMOB_ICMS_FRT'),
        Campo(8, 'VL_IMOB_ICMS_DIF'),
        Campo(9, 'NUM_PARC'),
        Campo(10, 'VL_PARC_PASS'),
    ]


class RegistroG126(Registro):
    """
    OUTROS CRÉDITOS CIAP
    """
    campos = [
        CampoFixo(1, 'REG', 'G126'),
        Campo(2, 'DT_INI'),
        Campo(3, 'DT_FIM'),
        Campo(4, 'NUM_PARC'),
        Campo(5, 'VL_PARC_PASS'),
        Campo(6, 'VL_TRIB_OC'),
        Campo(7, 'VL_TOTAL'),
        Campo(8, 'IND_PER_SAI'),
        Campo(9, 'VL_PARC_APRO P'),
    ]


class RegistroG130(Registro):
    """
    IDENTIFICAÇÃO DO DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'G130'),
        Campo(2, 'IND_EMIT'),
        Campo(3, 'COD_PART'),
        Campo(4, 'COD_MOD'),
        Campo(5, 'SERIE'),
        Campo(6, 'NUM_DOC'),
        Campo(7, 'CHV_NFE_CTE'),
        Campo(8, 'DT_DOC'),
    ]


class RegistroG140(Registro):
    """
    IDENTIFICAÇÃO DO ITEM DO DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'G140'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
    ]


class RegistroG990(Registro):
    """
    ENCERRAMENTO DO BLOCO G
    """
    campos = [
        CampoFixo(1, 'REG', 'G990'),
        Campo(2, 'QTD_LIN_G'),
    ]


class RegistroH001(Registro):
    """
    ABERTURA DO BLOCO H
    """
    campos = [
        CampoFixo(1, 'REG', 'H001'),
        Campo(2, 'IND_MO V'),
    ]


class RegistroH005(Registro):
    """
    TOTAIS DO INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H005'),
        Campo(2, 'DT_INV'),
        Campo(3, 'VL_INV'),
        Campo(4, 'MOT_INV'),
    ]


class RegistroH010(Registro):
    """
    INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H010'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'UNID'),
        Campo(4, 'QTD'),
        Campo(5, 'VL_UNIT'),
        Campo(6, 'VL_ITEM'),
        Campo(7, 'IND_PROP'),
        Campo(8, 'COD_PART'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'COD_CTA'),
    ]


class RegistroH020(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DO INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H020'),
        Campo(2, 'CST_ICMS'),
        Campo(3, 'BC_ICMS'),
        Campo(4, 'VL_ICMS'),
    ]


class RegistroH990(Registro):
    """
    ENCERRAMENTO DO BLOCO H
    """
    campos = [
        CampoFixo(1, 'REG', 'H990'),
        Campo(2, 'QTD_LIN_H'),
    ]


class RegistroK001(Registro):
    """
    ABERTURA DO BLOCO K
    """
    campos = [
        CampoFixo(1, 'REG', 'K001'),
        Campo(2, 'IND_MOV'),
    ]


class RegistroK100(Registro):
    """
    PERÍODO DE APURAÇÃO DO ICMS/IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'K100'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]


class RegistroK200(Registro):
    """
    ESTOQUE ESCRITURADO
    """
    campos = [
        CampoFixo(1, 'REG', 'K200'),
        CampoData(2, 'DT_EST'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'IND_EST'),
        Campo(6, 'COD_PART'),
    ]


class RegistroK220(Registro):
    """
    OUTRAS MOVIMENTAÇÕES INTERNAS ENTRE MERCADORIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'K220'),
        CampoData(2, 'DT_MOV'),
        Campo(3, 'COD_ITEM_ORI'),
        Campo(4, 'COD_ITEM_DEST'),
        Campo(5, 'QTD'),
    ]


class RegistroK230(Registro):
    """
    ITENS PRODUZIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K230'),
        CampoData(2, 'DT_INI_OP'),
        CampoData(3, 'DT_FIN_OP'),
        Campo(4, 'COD_DOC_OP'),
        Campo(5, 'COD_ITEM'),
        Campo(6, 'QTD_ENC'),
    ]


class RegistroK235(Registro):
    """
    INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K235'),
        CampoData(2, 'DT_SAÍDA'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'COD_INS_SUBST'),
    ]


class RegistroK250(Registro):
    """
    INDUSTRIALIZAÇÃO EFETUADA POR TERCEIROS – ITENS PRODUZIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K250'),
        CampoData(2, 'DT_PROD'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
    ]


class RegistroK255(Registro):
    """
    INDUSTRIALIZAÇÃO EM TERCEIROS – INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K255'),
        CampoData(2, 'DT_CONS'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'QTD'),
        Campo(5, 'COD_INS_SUBST'),
    ]


class RegistroK990(Registro):
    """
    ENCERRAMENTO DO BLOCO K
    """
    campos = [
        CampoFixo(1, 'REG', 'K990'),
        Campo(2, 'QTD_LIN_K'),
    ]


class Registro1001(Registro):
    """
    ABERTURA DO BLOCO 1
    """
    campos = [
        CampoFixo(1, 'REG', '1001'),
        Campo(2, 'IND_MOV'),
    ]


class Registro1010(Registro):
    """
    OBRIGATORIEDADE DE REGISTROS DO BLOCO 1
    """
    campos = [
        CampoFixo(1, 'REG', '1010'),
        Campo(2, 'IND_EXP'),
        Campo(3, 'IND_CCRF'),
        Campo(4, 'IND_COMB'),
        Campo(5, 'IND_USINA'),
        Campo(6, 'IND_VA'),
        Campo(7, 'IND_EE'),
        Campo(8, 'IND_CART'),
        Campo(9, 'IND_FORM'),
        Campo(10, 'IND_AER'),
    ]


class Registro1100(Registro):
    """
    REGISTRO DE INFORMAÇÕES SOBRE EXPORTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1100'),
        Campo(2, 'IND_DOC'),
        Campo(3, 'NRO_DE'),
        Campo(4, 'DT_DE'),
        Campo(5, 'NAT_EXP'),
        Campo(6, 'NRO_RE'),
        Campo(7, 'DT_RE'),
        Campo(8, 'CHC_EMB'),
        Campo(9, 'DT_CHC'),
        Campo(10, 'DT_AVB'),
        Campo(11, 'TP_CHC'),
        Campo(12, 'PAIS'),
    ]


class Registro1105(Registro):
    """
    DOCUMENTOS FISCAIS DE EXPORTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1105'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SERIE'),
        Campo(4, 'NUM_DOC'),
        Campo(5, 'CHV_NFE'),
        Campo(6, 'DT_DOC'),
        Campo(7, 'COD_ITEM'),
    ]


class Registro1110(Registro):
    """
    OPERAÇÕES DE EXPORTAÇÃO INDIRETA DE PRODUTOS NÃO INDUSTRIALIZADOS PELO ESTABELECIMENTO EMITENTE
    """
    campos = [
        CampoFixo(1, 'REG', '1110'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        Campo(5, 'NUM_DOC'),
        Campo(6, 'DT_DOC'),
        Campo(7, 'CHV_NFE'),
        Campo(8, 'NR_ MEMO'),
        Campo(9, 'QTD'),
        Campo(10, 'UNID'),
    ]


class Registro1200(Registro):
    """
    CONTROLE DE CRÉDITOS FISCAIS - ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1200'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'SLD_CRED'),
        Campo(4, 'CRÉD_APR'),
        Campo(5, 'CRED_RECEB'),
        Campo(6, 'CRED_UTIL'),
        Campo(7, 'SLD_CRED_FIM'),
    ]


class Registro1210(Registro):
    """
    UTILIZAÇÃO DE CRÉDITOS FISCAIS - ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1210'),
        Campo(2, 'TIPO_UTIL'),
        Campo(3, 'NR_DOC'),
    ]


class Registro1300(Registro):
    """
    MOVIMENTAÇÃO DIÁRIA DE COMBUSTÍVEIS
    """
    campos = [
        CampoFixo(1, 'REG', '1300'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'DT_FECH'),
        Campo(4, 'ESTQ_ABERT'),
        Campo(5, 'VOL_ENTR'),
        Campo(6, 'VOL_DISP'),
        Campo(7, 'VOL_SAIDAS'),
        Campo(8, 'ESTQ_ESCR'),
        Campo(9, 'VAL_AJ_PERDA'),
        Campo(10, 'VAL_AJ_GANHO'),
        Campo(11, 'FECH_FISICO'),
    ]


class Registro1310(Registro):
    """
    MOVIMENTAÇÃO DIÁRIA DE COMBUSTÍVEIS POR TANQUE
    """
    campos = [
        CampoFixo(1, 'REG', '1310'),
        Campo(2, 'NUM_TANQUE'),
        Campo(3, 'ESTQ_ABERT'),
        Campo(4, 'VOL_ENTR'),
        Campo(5, 'VOL_DISP'),
        Campo(6, 'VOL_SAIDAS'),
        Campo(7, 'ESTQ_ESCR'),
        Campo(8, 'VAL_AJ_PERDA'),
        Campo(9, 'VAL_AJ_GANHO'),
        Campo(10, 'FECH_FISICO'),
    ]


class Registro1320(Registro):
    """
    VOLUME DE VENDAS
    """
    campos = [
        CampoFixo(1, 'REG', '1320'),
        Campo(2, 'NUM_BICO'),
        Campo(3, 'NR_INTERV'),
        Campo(4, 'MOT_INTERV'),
        Campo(5, 'NOM_INTERV'),
        Campo(6, 'CNPJ_INTERV'),
        Campo(7, 'CPF_INTERV'),
        Campo(8, 'VAL_FECHA'),
        Campo(9, 'VAL_ABERT'),
        Campo(10, 'VOL_AFERI'),
        Campo(11, 'VOL_VENDAS'),
    ]


class Registro1350(Registro):
    """
    BOMBAS
    """
    campos = [
        CampoFixo(1, 'REG', '1350'),
        Campo(2, 'SERIE'),
        Campo(3, 'FABRICANTE'),
        Campo(4, 'MODELO'),
        Campo(5, 'TIPO_MEDICAO'),
    ]


class Registro1360(Registro):
    """
    LACRES DA BOMBA
    """
    campos = [
        CampoFixo(1, 'REG', '1360'),
        Campo(2, 'NUM_LACRE'),
        Campo(3, 'DT_APLICACAO'),
    ]


class Registro1370(Registro):
    """
    BICOS DA BOMBA
    """
    campos = [
        CampoFixo(1, 'REG', '1370'),
        Campo(2, 'NUM_BICO'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'NUM_TANQUE'),
    ]


class Registro1390(Registro):
    """
    CONTROLE DE PRODUÇÃO DE USINA
    """
    campos = [
        CampoFixo(1, 'REG', '1390'),
        Campo(2, 'COD_PROD'),
    ]


class Registro1391(Registro):
    """
    PRODUÇÃO DIÁRIA DA USINA
    """
    campos = [
        CampoFixo(1, 'REG', '1391'),
        Campo(2, 'DT_REGISTRO'),
        Campo(3, 'QTD_MOID'),
        Campo(4, 'ESTQ_INI'),
        Campo(5, 'QTD_PRODUZ'),
        Campo(6, 'ENT_ANID_HID'),
        Campo(7, 'OUTR_ENTR'),
        Campo(8, 'PERDA'),
        Campo(9, 'CONS'),
        Campo(10, 'SAI_ANI_HID'),
        Campo(11, 'SAÍDAS'),
        Campo(12, 'ESTQ_FIN'),
        Campo(13, 'ESTQ_INI_MEL'),
        Campo(14, 'PROD_DIA_MEL'),
        Campo(15, 'UTIL_MEL'),
        Campo(16, 'PROD_ALC_MEL'),
        Campo(17, 'OBS'),
    ]


class Registro1400(Registro):
    """
    INFORMAÇÃO SOBRE VALORES AGREGADOS
    """
    campos = [
        CampoFixo(1, 'REG', '1400'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'MUN'),
        Campo(4, 'VALOR'),
    ]


class Registro1500(Registro):
    """
    NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA (CÓDIGO 06) - OPERAÇÕES INTERESTADUAIS
    """
    campos = [
        CampoFixo(1, 'REG', '1500'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'COD_SIT'),
        Campo(7, 'SER'),
        Campo(8, 'SUB'),
        Campo(9, 'COD_CONS'),
        Campo(10, 'NUM_DOC'),
        Campo(11, 'DT_DOC'),
        Campo(12, 'DT_E_S'),
        Campo(13, 'VL_DOC'),
        Campo(14, 'VL_DESC'),
        Campo(15, 'VL_FORN'),
        Campo(16, 'VL_SERV_NT'),
        Campo(17, 'VL_TERC'),
        Campo(18, 'VL_DA'),
        Campo(19, 'VL_BC_ICMS'),
        Campo(20, 'VL_ICMS'),
        Campo(21, 'VL_BC_ICMS_ST'),
        Campo(22, 'VL_ICMS_ST'),
        Campo(23, 'COD_INF'),
        Campo(24, 'VL_PIS'),
        Campo(25, 'VL_COFINS'),
        Campo(26, 'TP_LIGACAO'),
        Campo(27, 'COD_GRUPO_TENSAO'),
    ]


class Registro1510(Registro):
    """
    ITENS DO DOCUMENTO NOTA FISCAL/CONTA ENERGIA ELÉTRICA (CÓDIGO 06)
    """
    campos = [
        CampoFixo(1, 'REG', '1510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        Campo(5, 'QTD'),
        Campo(6, 'UNID'),
        Campo(7, 'VL_ITEM'),
        Campo(8, 'VL_DESC'),
        Campo(9, 'CST_ICMS'),
        Campo(10, 'CFOP'),
        Campo(11, 'VL_BC_ICMS'),
        Campo(12, 'ALIQ_ICMS'),
        Campo(13, 'VL_ICMS'),
        Campo(14, 'VL_BC_ICMS_ST'),
        Campo(15, 'ALIQ_ST'),
        Campo(16, 'VL_ICMS_ST'),
        Campo(17, 'IND_REC'),
        Campo(18, 'COD_PART'),
        Campo(19, 'VL_PIS'),
        Campo(20, 'VL_COFINS'),
        Campo(21, 'COD_CTA'),
    ]


class Registro1600(Registro):
    """
    TOTAL DAS OPERAÇÕES COM CARTÃO DE CRÉDITO E/OU DÉBITO
    """
    campos = [
        CampoFixo(1, 'REG', '1600'),
        Campo(2, 'COD_PART'),
        Campo(3, 'TOT_CREDITO'),
        Campo(4, 'TOT_DEBITO'),
    ]


class Registro1700(Registro):
    """
    DOCUMENTOS FISCAIS UTILIZADOS
    """
    campos = [
        CampoFixo(1, 'REG', '1700'),
        Campo(2, 'COD_DISP'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'NUM_DOC_INI'),
        Campo(7, 'NUM_DOC_FIN'),
        Campo(8, 'NUM_AUT'),
    ]


class Registro1710(Registro):
    """
    DOCUMENTOS FISCAIS CANCELADOS/INUTILIZADOS
    """
    campos = [
        CampoFixo(1, 'REG', '1710'),
        Campo(2, 'NUM_DOC_INI'),
        Campo(3, 'NUM_DOC_FIN'),
    ]


class Registro1800(Registro):
    """
    DCTA - DEMONSTRATIVO DE CRÉDITO DO ICMS SOBRE TRANSPORTE AÉREO
    """
    campos = [
        CampoFixo(1, 'REG', '1800'),
        Campo(2, 'VL_CARGA'),
        Campo(3, 'VL_PASS'),
        Campo(4, 'VL_FAT'),
        Campo(5, 'IND_RAT'),
        Campo(6, 'VL_ICMS_ANT'),
        Campo(7, 'VL_BC_ICMS'),
        Campo(8, 'VL_ICMS_APUR'),
        Campo(9, 'VL_BC_ICMS_APUR'),
        Campo(10, 'VL_DIF'),
    ]


class Registro1900(Registro):
    """
    INDICADOR DE SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1900'),
        Campo(2, 'IND_APUR_ICMS'),
        Campo(3, 'DESCR_COMPL_OUT_APUR'),
    ]


class Registro1910(Registro):
    """
    PERÍODO DA SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1910'),
        Campo(2, 'DT_INI'),
        Campo(3, 'DT_FIN'),
    ]


class Registro1920(Registro):
    """
    SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1920'),
        Campo(2, 'VL_TOT_TRANSF_DEBITOS_OA'),
        Campo(3, 'VL_TOT_AJ_DEBITOS_OA'),
        Campo(4, 'VL_ESTORNOS_CRED_OA'),
        Campo(5, 'VL_TOT_TRANSF_CREDITOS_OA'),
        Campo(6, 'VL_TOT_AJ_CREDITOS_OA'),
        Campo(7, 'VL_ESTORNOS_DEB_OA'),
        Campo(8, 'VL_SLD_CREDOR_ANT_OA'),
        Campo(9, 'VL_SLD_APURADO_OA'),
        Campo(10, 'VL_TOT_DED'),
        Campo(11, 'VL_ICMS_RECOLHER_OA'),
        Campo(12, 'VL_SLD_CREDOR_TRANSP_OA'),
        Campo(13, 'DEB_ESP_OA'),
    ]


class Registro1921(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1921'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'VL_AJ_APUR'),
    ]


class Registro1922(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1922'),
        Campo(2, 'NUM_DA'),
        Campo(3, 'NUM_PROC'),
        Campo(4, 'IND_PROC'),
        Campo(5, 'PROC'),
        Campo(6, 'TXT_COMPL'),
    ]


class Registro1923(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA SUB-APURAÇÃO DO ICMS - IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', '1923'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        Campo(5, 'SUB'),
        Campo(6, 'NUM_DOC'),
        Campo(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        Campo(9, 'VL_AJ_ITEM'),
    ]


class Registro1925(Registro):
    """
    INFORMAÇÕES ADICIONAIS DA SUB-APURAÇÃO - VALORES DECLARATÓRIOS
    """
    campos = [
        CampoFixo(1, 'REG', '1925'),
        Campo(2, 'COD_INF_ADIC'),
        Campo(3, 'VL_INF_ADIC'),
        Campo(4, 'DESCR_COMPL_AJ'),
    ]


class Registro1926(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - OPERAÇÕES REFERENTES À SUB-APURAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1926'),
        Campo(2, 'COD_OR'),
        Campo(3, 'VL_OR'),
        Campo(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]


class Registro1990(Registro):
    """
    ENCERRAMENTO DO BLOCO 1
    """
    campos = [
        CampoFixo(1, 'REG', '1990'),
        Campo(2, 'QTD_LIN_1'),
    ]


class Registro9001(Registro):
    """
    ABERTURA DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9001'),
        Campo(2, 'IND_MOV'),
    ]


class Registro9900(Registro):
    """
    REGISTROS DO ARQUIVO
    """
    campos = [
        CampoFixo(1, 'REG', '9900'),
        Campo(2, 'REG_BLC'),
        Campo(3, 'QTD_REG_BLC'),
    ]


class Registro9990(Registro):
    """
    ENCERRAMENTO DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9990'),
        Campo(2, 'QTD_LIN_9'),
    ]


class Registro9999(Registro):
    """
    ENCERRAMENTO DO ARQUIVO DIGITAL
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        Campo(2, 'QTD_LIN'),
    ]

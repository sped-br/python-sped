# -*- coding: utf-8 -*-

from ...registros import Registro
from ...campos import Campo
from ...campos import CampoData
from ...campos import CampoFixo
from ...campos import CampoNumerico
from ...campos import CampoAlfanumerico
from ...campos import CampoRegex
from ...campos import CampoCNPJ
from ...campos import CampoCPF
from ...campos import CampoCPFouCNPJ
from ...campos import CampoChaveEletronica

class Registro0000(Registro):
    """
    ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA ENTIDADE
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        Campo(2, 'COD_VER'),
        Campo(3, 'COD_FIN'),
        CampoData(4, 'DT_INI'),
        CampoData(5, 'DT_FIN'),
        Campo(6, 'NOME'),
        CampoCNPJ(7, 'CNPJ'),
        CampoCPF(8, 'CPF'),
        Campo(9, 'UF'),
        Campo(10, 'IE'),
        CampoNumerico(11, 'COD_MUN'),
        Campo(12, 'IM'),
        Campo(13, 'SUFRAMA'),
        Campo(14, 'IND_PERFIL'),
        Campo(15, 'IND_ATIV'),
    ]

    nivel = 0

class Registro0001(Registro):
    """
    ABERTURA DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

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

    nivel = 2

class Registro0015(Registro):
    """
    DADOS DO CONTRIBUINTE SUBSTITUTO
    """
    campos = [
        CampoFixo(1, 'REG', '0015'),
        Campo(2, 'UF_ST'),
        Campo(3, 'IE_ST'),
    ]

    nivel = 2

class Registro0100(Registro):
    """
    DADOS DO CONTABILISTA
    """
    campos = [
        CampoFixo(1, 'REG', '0100'),
        Campo(2, 'NOME'),
        CampoCPF(3, 'CPF'),
        Campo(4, 'CRC'),
        CampoCNPJ(5, 'CNPJ'),
        Campo(6, 'CEP'),
        Campo(7, 'END'),
        Campo(8, 'NUM'),
        Campo(9, 'COMPL'),
        Campo(10, 'BAIRRO'),
        Campo(11, 'FONE'),
        Campo(12, 'FAX'),
        Campo(13, 'EMAIL'),
        CampoNumerico(14, 'COD_MUN'),
    ]

    nivel = 2

class Registro0150(Registro):
    """
    TABELA DE CADASTRO DO PARTICIPANTE
    """
    campos = [
        CampoFixo(1, 'REG', '0150'),
        Campo(2, 'COD_PART'),
        Campo(3, 'NOME'),
        Campo(4, 'COD_PAIS'),
        CampoCNPJ(5, 'CNPJ'),
        CampoCPF(6, 'CPF'),
        Campo(7, 'IE'),
        CampoNumerico(8, 'COD_MUN'),
        Campo(9, 'SUFRAMA'),
        Campo(10, 'END'),
        Campo(11, 'NUM'),
        Campo(12, 'COMPL'),
        Campo(13, 'BAIRRO'),
    ]

    nivel = 2

class Registro0175(Registro):
    """
    ALTERAÇÃO DA TABELA DE CADASTRO DE PARTICIPANTE
    """
    campos = [
        CampoFixo(1, 'REG', '0175'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'NR_CAMPO'),
        Campo(4, 'CONT_ANT'),
    ]

    nivel = 3

class Registro0190(Registro):
    """
    IDENTIFICAÇÃO DAS UNIDADES DE MEDIDA
    """
    campos = [
        CampoFixo(1, 'REG', '0190'),
        Campo(2, 'UNID'),
        Campo(3, 'DESCR'),
    ]

    nivel = 2

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
        CampoNumerico(12, 'ALIQ_ICMS'),
        Campo(13, 'CEST'),
    ]

    nivel = 2

class Registro0205(Registro):
    """
    ALTERAÇÃO DO ITEM
    """
    campos = [
        CampoFixo(1, 'REG', '0205'),
        Campo(2, 'DESCR_ANT_ITEM'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIM'),
        Campo(5, 'COD_ANT_ITEM'),
    ]

    nivel = 3

class Registro0206(Registro):
    """
    CÓDIGO DE PRODUTO CONFORME TABELA PUBLICADA PELA ANP (COMBUSTÍVEIS)
    """
    campos = [
        CampoFixo(1, 'REG', '0206'),
        Campo(2, 'COD_COMB'),
    ]
    
    nivel = 3

class Registro0210(Registro):
    """
    CONSUMO ESPECÍFICO PADRONIZADO
    """
    campos = [
        CampoFixo(1, 'REG', '0210'),
        Campo(2, 'COD_ITEM_COMP'),
        CampoNumerico(3, 'QTD_COMP'),
        CampoNumerico(4, 'PERDA'),
    ]

    nivel = 3

class Registro0220(Registro):
    """
    FATORES DE CONVERSÃO DE UNIDADES
    """
    campos = [
        CampoFixo(1, 'REG', '0220'),
        Campo(2, 'UNID_CONV'),
        Campo(3, 'FAT_CONV'),
    ]

    nivel = 3

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

    nivel = 2

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

    nivel = 3

class Registro0400(Registro):
    """
    TABELA DE NATUREZA DA OPERAÇÃO/PRESTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '0400'),
        Campo(2, 'COD_NAT'),
        Campo(3, 'DESCR_NAT'),
    ]

    nivel = 2

class Registro0450(Registro):
    """
    TABELA DE INFORMAÇÃO COMPLEMENTAR DO DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', '0450'),
        Campo(2, 'COD_INF'),
        Campo(3, 'TXT'),
    ]

    nivel = 2

class Registro0460(Registro):
    """
    TABELA DE OBSERVAÇÕES DO LANÇAMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', '0460'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT'),
    ]

    nivel = 2

class Registro0500(Registro):
    """
    PLANO DE CONTAS CONTÁBEIS
    """
    campos = [
        CampoFixo(1, 'REG', '0500'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_NAT_CC'),
        Campo(4, 'IND_CTA'),
        Campo(5, 'NÍVEL'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'NOME_CTA'),
    ]

    nivel = 2

class Registro0600(Registro):
    """
    CENTRO DE CUSTOS
    """
    campos = [
        CampoFixo(1, 'REG', '0600'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'CCUS'),
    ]

    nivel = 2

class Registro0990(Registro):
    """
    ENCERRAMENTO DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0990'),
        CampoNumerico(2, 'QTD_LIN_0'),
    ]

    nivel = 1

class RegistroB001(Registro):
    """
    ABERTURA DO BLOCO B
    """
    campos = [
        CampoFixo(1, 'REG', 'B001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroB020(Registro):
    """
    NOTA FISCAL (CÓDIGO 01), NOTA FISCAL DE SERVIÇOS (CÓDIGO 03), 
    NOTA FISCAL DE SERVIÇOS AVULSA (CÓDIGO 3B), NOTA FISCAL DE PRODUTOR
    (CÓDIGO 04), CONHECIMENTO DE TRANSPORTE RODOVIÁRIO DE CARGAS
    (CÓDIGO 08), NF-e (CÓDIGO 55) e NFC-e (CÓDIGO 65).
    """
    campos = [
        CampoFixo(1, 'REG', 'B020'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'NUM_DOC'),
        CampoChaveEletronica(9, 'CHV_NFE'),
        CampoData(10, 'DT_DOC'),
        CampoNumerico(11, 'COD_MUN_SERV'),
        CampoNumerico(12, 'VL_CONT'),
        CampoNumerico(13, 'VL_MAT_TERC'),
        CampoNumerico(14, 'VL_SUB'),
        CampoNumerico(15, 'VL_ISNT_ISS'),
        CampoNumerico(16, 'VL_DED_BC'),
        CampoNumerico(17, 'VL_BC_ISS'),
        CampoNumerico(18, 'VL_BC_ISS_RT'),
        CampoNumerico(19, 'VL_ISS_RT'),
        CampoNumerico(20, 'VL_ISS'),
        Campo(21, 'COD_INF_OBS'),
    ]

    nivel = 2

class RegistroB025(Registro):
    """
    DETALHAMENTO POR COMBINAÇÃO DE ALÍQUOTA E ITEM DA
    LISTA DE SERVIÇOS DA LC 116/2003)
    """
    campos = [
        CampoFixo(1, 'REG', 'B025'),
        CampoNumerico(2, 'VL_CONT_P'),
        CampoNumerico(3, 'VL_BC_ISS_P'),
        CampoNumerico(4, 'ALIQ_ISS'),
        CampoNumerico(5, 'VL_ISS_P'),
        CampoNumerico(6, 'VL_ISNT_ISS_P'),
        Campo(7, 'COD_SERV'),
    ]

    nivel = 3

class RegistroB030(Registro):
    """
     NOTA FISCAL DE SERVIÇOS SIMPLIFICADA (CÓDIGO 3A)
    """
    campos = [
        CampoFixo(1, 'REG', 'B030'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        CampoNumerico(4, 'NUM_DOC_INI'),
        CampoNumerico(5, 'NUM_DOC_FIN'),
        CampoData(6, 'DT_DOC'),
        CampoNumerico(7, 'QTD_CANC'),
        CampoNumerico(8, 'VL_CONT'),
        CampoNumerico(9, 'VL_ISNT_ISS'),
        CampoNumerico(10, 'VL_BC_ISS'),
        CampoNumerico(11, 'VL_ISS'),
        Campo(12, 'COD_INF_OBS'),
    ]

    nivel = 2

class RegistroB035(Registro):
    """
    DETALHAMENTO POR COMBINAÇÃO DE ALÍQUOTA E ITEM DA
    LISTA DE SERVIÇOS DA LC 116/2003)
    """
    campos = [
        CampoFixo(1, 'REG', 'B035'),
        CampoNumerico(2, 'VL_CONT_P'),
        CampoNumerico(3, 'VL_BC_ISS_P'),
        CampoNumerico(4, 'ALIQ_ISS'),
        CampoNumerico(5, 'VL_ISS_P'),
        CampoNumerico(6, 'VL_ISNT_ISS_P'),
        Campo(7, 'COD_SERV'),
    ]

    nivel = 1

class RegistroB350(Registro):
    """
    SERVIÇOS PRESTADOS POR INSTITUIÇÕES FINANCEIRAS
    """
    campos = [
        CampoFixo(1, 'REG', 'B350'),
        Campo(2, 'COD_CTD'),
        Campo(3, 'CTA_ISS'),
        Campo(4, 'CTA_COSIF'),
        CampoNumerico(5, 'QTD_OCOR'),
        Campo(6, 'COD_SERV'),
        CampoNumerico(7, 'VL_CONT'),
        CampoNumerico(8, 'VL_BC_ISS'),
        CampoNumerico(9, 'ALIQ_ISS'),
        CampoNumerico(10, 'VL_ISS'),
        Campo(11, 'COD_INF_OBS'),
    ]

    nivel = 2

class RegistroB420(Registro):
    """
    TOTALIZAÇÃO DOS VALORES DE SERVIÇOS PRESTADOS POR
    COMBINAÇÃO DE ALÍQUOTA E ITEM DA LISTA DE SERVIÇOS DA LC 116/200
    """
    campos = [
        CampoFixo(1, 'REG', 'B420'),
        CampoNumerico(2, 'VL_CONT'),
        CampoNumerico(3, 'VL_BC_ISS'),
        CampoNumerico(4, 'ALIQ_ISS'),
        CampoNumerico(5, 'VL_ISNT_ISS'),
        CampoNumerico(6, 'VL_ISS'),
        Campo(7, 'COD_SERV'),
    ]

    nivel = 2

class RegistroB440(Registro):
    """
    TOTALIZAÇÃO DOS VALORES RETIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'B440'),
        CampoNumerico(2, 'IND_OPER'),
        Campo(3, 'COD_PART'),
        CampoNumerico(4, 'VL_CONT_RT'),
        CampoNumerico(5, 'VL_BC_ISS_RT'),
        CampoNumerico(6, 'VL_ISS_RT')
    ]

    nivel = 2

class RegistroB460(Registro):
    """
    DEDUÇÕES DO ISS
    """
    campos = [
        CampoFixo(1, 'REG', 'B460'),
        Campo(2, 'IND_DED'),
        CampoNumerico(3, 'VL_DED'),
        Campo(4, 'NUM_PROC'),
        Campo(5, 'IND_PROC'),
        Campo(6, 'PROC'),
        Campo(7, 'COD_INF_OBS'),
        Campo(8, 'IND_OBR'),
    ]

    nivel = 2

class RegistroB470(Registro):
    """
    APURAÇÃO DO ISS
    """
    campos = [
        CampoFixo(1, 'REG', 'B470'),
        CampoNumerico(2, 'VL_CONT'),
        CampoNumerico(3, 'VL_MAT_TERC'),
        CampoNumerico(4, 'VL_MAT_PROP'),
        CampoNumerico(5, 'VL_SUB'),
        CampoNumerico(6, 'VL_ISNT'),
        CampoNumerico(7, 'VL_DED_BC'),
        CampoNumerico(8, 'VL_BC_ISS'),
        CampoNumerico(9, 'VL_BC_ISS_RT'),
        CampoNumerico(10, 'VL_ISS'),
        CampoNumerico(11, 'VL_ISS_RT'),
        CampoNumerico(12, 'VL_DED'),
        CampoNumerico(13, 'VL_ISS_REC'),
        CampoNumerico(14, 'VL_ISS_ST'),
        CampoNumerico(15, 'VL_ISS_REC_UNI'),
    ]

    nivel = 2

class RegistroB500(Registro):
    """
    APURAÇÃO DO ISS SOCIEDADE UNIPROFISSIONA
    """
    campos = [
        CampoFixo(1, 'REG', 'B500'),
        CampoNumerico(2, 'VL_REC'),
        CampoNumerico(3, 'QTD_PROF'),
        CampoNumerico(4, 'VL_OR'),
    ]

    nivel = 2

class RegistroB510(Registro):
    """
    UNIPROFISSIONAL - EMPREGADOS E SÓCIOS
    """
    campos = [
        CampoFixo(1, 'REG', 'B510'),
        Campo(2, 'IND_PROF'),
        Campo(3, 'IND_ESC'),
        Campo(4, 'IND_SOC'),
        CampoCPF(5, 'CPF'),
        Campo(6, 'NOME'),
    ]

    nivel = 3

class RegistroB990(Registro):
    """
    ENCERRAMENTO DO BLOCO B
    """
    campos = [
        CampoFixo(1, 'REG', 'B990'),
        CampoNumerico(2, 'QTD_LIN_B'),
    ]

    nivel = 1

class RegistroC001(Registro):
    """
    ABERTURA DO BLOCO C
    """
    campos = [
        CampoFixo(1, 'REG', 'C001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroC100(Registro):
    """
    DADOS NOTA FISCAL (CÓDIGO 01, 1B, 04, 55 E 65)
    """
    campos = [
        CampoFixo(1, 'REG', 'C100'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'NUM_DOC'),
        CampoChaveEletronica(9, 'CHV_NFE'),
        CampoData(10, 'DT_DOC'),
        CampoData(11, 'DT_E_S'),
        CampoNumerico(12, 'VL_DOC'),
        Campo(13, 'IND_PGTO'),
        CampoNumerico(14, 'VL_DESC'),
        CampoNumerico(15, 'VL_ABAT_NT'),
        CampoNumerico(16, 'VL_MERC'),
        Campo(17, 'IND_FRT'),
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

    nivel = 2

class RegistroC101(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DOS DOCUMENTOS FISCAIS
    QUANDO DAS OPERAÇÕES INTERESTADUAIS DESTINADAS A CONSUMIDOR FINAL
    NÃO CONTRIBUINTE EC 87/15 (CÓDIGO 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C101'),
        CampoNumerico(2, 'VL_FCP_UF_DEST'),
        CampoNumerico(3, 'VL_ICMS_UF_DEST'),
        CampoNumerico(4, 'VL_ICMS_UF_REM'),
    ]

    nivel = 3

class RegistroC105(Registro):
    """
    OPERAÇÕES COM ICMS ST RECOLHIDO PARA UF DIVERSA DO DESTINATÁRIO DO DOCUMENTO FISCAL (CÓDIGO 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C105'),
        Campo(2, 'OPER'),
        Campo(3, 'UF'),
    ]

    nivel = 3

class RegistroC110(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DA NOTA FISCAL (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C110'),
        Campo(2, 'COD_INF'),
        Campo(3, 'TXT_COMPL'),
    ]

    nivel = 3

class RegistroC111(Registro):
    """
    PROCESSO REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C111'),
        Campo(2, 'NUM_PROC'),
        Campo(3, 'IND_PROC'),
    ]

    nivel = 4

class RegistroC112(Registro):
    """
    DOCUMENTO DE ARRECADAÇÃO REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C112'),
        Campo(2, 'COD_DA'),
        Campo(3, 'UF'),
        Campo(4, 'NUM_DA'),
        Campo(5, 'COD_AUT'),
        CampoNumerico(6, 'VL_DA'),
        CampoData(7, 'DT_VCTO'),
        CampoData(8, 'DT_PGTO'),
    ]

    nivel = 4

class RegistroC113(Registro):
    """
    DOCUMENTO FISCAL REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C113'),
        Campo(2, 'IND_OPER'),
        Campo(3, 'IND_EMIT'),
        Campo(4, 'COD_PART'),
        Campo(5, 'COD_MOD'),
        Campo(6, 'SER'),
        CampoNumerico(7, 'SUB'),
        CampoNumerico(8, 'NUM_DOC'),
        CampoData(9, 'DT_DOC'),
        CampoChaveEletronica(10, 'CHV_DOCe'),
    ]

    nivel = 4

class RegistroC114(Registro):
    """
    CUPOM FISCAL REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C114'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'ECF_FAB'),
        Campo(4, 'ECF_CX'),
        CampoNumerico(5, 'NUM_DOC'),
        CampoData(6, 'DT_DOC'),
    ]

    nivel = 4

class RegistroC115(Registro):
    """
    LOCAL DA COLETA E/OU ENTREGA (CÓDIGO 01, 1B, 04)
    """
    campos = [
        CampoFixo(1, 'REG', 'C115'),
        Campo(2, 'IND_CARGA'),
        CampoCNPJ(3, 'CNPJ_COL'),
        Campo(4, 'IE_COL'),
        CampoCPF(5, 'CPF_COL'),
        CampoNumerico(6, 'COD_MUN_COL'),
        CampoCNPJ(7, 'CNPJ_ENTG'),
        Campo(8, 'IE_ENTG'),
        CampoCPF(9, 'CPF_ENTG'),
        CampoNumerico(10, 'COD_MUN_ENTG'),
    ]

    nivel = 4

class RegistroC116(Registro):
    """
    CUPOM FISCAL ELETRÔNICO REFERENCIADO
    """
    campos = [
        CampoFixo(1, 'REG', 'C116'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'NR_SAT'),
        CampoChaveEletronica(4, 'CHV_CFE'),
        CampoNumerico(5, 'NUM_CFE'),
        CampoData(6, 'DT_DOC'),
    ]

    nivel = 4

class RegistroC120(Registro):
    """
    COMPLEMENTO DE DOCUMENTO - OPERAÇÕES DE IMPORTAÇÃO 
    (CÓDIGOS 01 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C120'),
        Campo(2, 'COD_DOC_IMP'),
        Campo(3, 'NUM_DOC IMP'),
        CampoNumerico(4, 'PIS_IMP'),
        CampoNumerico(5, 'COFINS_IMP'),
        Campo(6, 'NUM_ACDRAW'),
    ]

    nivel = 3

class RegistroC130(Registro):
    """
    ISSQN, IRRF E PREVIDÊNCIA SOCIAL
    """
    campos = [
        CampoFixo(1, 'REG', 'C130'),
        CampoNumerico(2, 'VL_SERV_NT'),
        CampoNumerico(3, 'VL_BC_ISSQN'),
        CampoNumerico(4, 'VL_ISSQN'),
        CampoNumerico(5, 'VL_BC_IRRF'),
        CampoNumerico(6, 'VL_ IRRF'),
        CampoNumerico(7, 'VL_BC_PREV'),
        CampoNumerico(8, 'VL_ PREV'),
    ]

    nivel = 3

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
        CampoNumerico(6, 'QTD_PARC'),
        CampoNumerico(7, 'VL_TIT'),
    ]

    nivel = 3

class RegistroC141(Registro):
    """
    VENCIMENTO DA FATURA (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C141'),
        CampoNumerico(2, 'NUM_PARC'),
        CampoData(3, 'DT_VCTO'),
        CampoNumerico(4, 'VL_PARC'),
    ]

    nivel = 4

class RegistroC160(Registro):
    """
    VOLUMES TRANSPORTADOS (CÓDIGO 01 E 04) - EXCETO COMBUSTÍVEIS
    """
    campos = [
        CampoFixo(1, 'REG', 'C160'),
        Campo(2, 'COD_PART'),
        Campo(3, 'VEIC_ID'),
        CampoNumerico(4, 'QTD_VOL'),
        CampoNumerico(5, 'PESO_BRT'),
        CampoNumerico(6, 'PESO_LIQ'),
        Campo(7, 'UF_ID'),
    ]

    nivel = 3

class RegistroC165(Registro):
    """
    OPERAÇÕES COM COMBUSTÍVEIS (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C165'),
        Campo(2, 'COD_PART'),
        Campo(3, 'VEIC_ID'),
        Campo(4, 'COD_AUT'),
        Campo(5, 'NR_PASSE'),
        CampoNumerico(6, 'HORA'),
        CampoNumerico(7, 'TEMPER'),
        CampoNumerico(8, 'QTD_VOL'),
        CampoNumerico(9, 'PESO_BRT'),
        CampoNumerico(10, 'PESO_LIQ'),
        Campo(11, 'NOM_MOT'),
        CampoCPF(12, 'CPF'),
        Campo(13, 'UF_ID'),
    ]

    nivel = 3

class RegistroC170(Registro):
    """
    ITENS DO DOCUMENTO (CÓDIGO 01, 1B, 04 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C170'),
        CampoNumerico(2, 'NUM_ITEM', obrigatorio=True),
        Campo(3, 'COD_ITEM', obrigatorio=True),
        Campo(4, 'DESCR_COMPL'),
        CampoNumerico(5, 'QTD'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM', obrigatorio=True),
        CampoNumerico(8, 'VL_DESC'),
        Campo(9, 'IND_MOV'),
        CampoNumerico(10, 'CST_ICMS'),
        CampoNumerico(11, 'CFOP', obrigatorio=True),
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
        CampoNumerico(25, 'CST_PIS', obrigatorio=True),
        CampoNumerico(26, 'VL_BC_PIS'),
        CampoNumerico(27, 'ALIQ_PIS'),         # 27 ALIQ_PIS em percentual
        CampoNumerico(28, 'QUANT_BC_PIS'),
        CampoNumerico(29, 'ALIQ_PIS_REAIS'),   # 27 ALIQ_PIS em reais: escolher nome diferente do nome do campo 27
        CampoNumerico(30, 'VL_PIS'),
        CampoNumerico(31, 'CST_COFINS', obrigatorio=True),
        CampoNumerico(32, 'VL_BC_COFINS'),
        CampoNumerico(33, 'ALIQ_COFINS'),       # 33 ALIQ_COFINS em percentual
        CampoNumerico(34, 'QUANT_BC_COFINS'),
        CampoNumerico(35, 'ALIQ_COFINS_REAIS'), # 35 ALIQ_COFINS em reais: escolher nome diferente do nome do campo 33
        CampoNumerico(36, 'VL_COFINS'),
        Campo(37, 'COD_CTA'),
        CampoNumerico(38, 'VL_ABAT_NT'),
    ]

    nivel = 3

class RegistroC171(Registro):
    """
    ARMAZENAMENTO DE COMBUSTÍVEIS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C171'),
        Campo(2, 'NUM_TANQUE'),
        CampoNumerico(3, 'QTDE'),
    ]

    nivel = 4

class RegistroC172(Registro):
    """
    OPERAÇÕES COM ISSQN (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C172'),
        CampoNumerico(2, 'VL_BC_ISSQN'),
        CampoNumerico(3, 'ALIQ_ISSQN'),
        CampoNumerico(4, 'VL_ISSQN'),
    ]

    nivel = 4

class RegistroC173(Registro):
    """
    OPERAÇÕES COM MEDICAMENTOS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C173'),
        Campo(2, 'LOTE_MED'),
        CampoNumerico(3, 'QTD_ITEM'),
        CampoData(4, 'DT_FAB'),
        CampoData(5, 'DT_VAL'),
        Campo(6, 'IND_MED'),
        Campo(7, 'TP_PROD'),
        CampoNumerico(8, 'VL_TAB_MAX'),
    ]

    nivel = 4

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

    nivel = 4

class RegistroC175(Registro):
    """
    OPERAÇÕES COM VEÍCULOS NOVOS (CÓDIGO 01 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C175'),
        Campo(2, 'IND_VEIC_OPER'),
        CampoCNPJ(3, 'CNPJ'),
        Campo(4, 'UF'),
        Campo(5, 'CHASSI_VEIC'),
    ]

    nivel = 4

class RegistroC176(Registro):
    """
    RESSARCIMENTO DE ICMS E FUNDO DE COMBATE À POBREZA
    (FCP) EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C176'),
        Campo(2, 'COD_MOD_ULT_E'),
        CampoNumerico(3, 'NUM_DOC_ULT_E'),
        Campo(4, 'SER_ULT_E'),
        CampoData(5, 'DT_ULT_E'),
        Campo(6, 'COD_PART_ULT_E'),
        CampoNumerico(7, 'QUANT_ULT_E'),
        CampoNumerico(8, 'VL_UNIT_ULT_E'),
        CampoNumerico(9, 'VL_UNIT_BC_ST'),
        CampoChaveEletronica(10, 'CHAVE_NFE_ULT_E'),
        CampoNumerico(11, 'NUM_ITEM_ULT_E'),
        CampoNumerico(12, 'VL_UNIT_BC_ICMS_ULT_E'),
        CampoNumerico(13, 'ALIQ_ICMS_ULT_E'),
        CampoNumerico(14, 'VL_UNIT_LIMITE_BC_ICMS_ULT_E'),
        CampoNumerico(15, 'VL_UNIT_ICMS_ULT_E'),
        CampoNumerico(16, 'ALIQ_ST_ULT_E'),
        CampoNumerico(17, 'VL_UNIT_RES'),
        CampoNumerico(18, 'COD_RESP_RET'),
        CampoNumerico(19, 'COD_MOT_RES'),
        CampoChaveEletronica(20, 'CHAVE_NFE_RET'),
        Campo(21, 'COD_PART_NFE_RET'),
        Campo(22, 'SER_NFE_RET'),
        CampoNumerico(23, 'NUM_NFE_RET'),
        CampoNumerico(24, 'ITEM_NFE_RET'),
        Campo(25, 'COD_DA'),
        Campo(26, 'NUM_DA'),
        CampoNumerico(27, 'VL_UNIT_RES_FCP_ST'),
    ]

    nivel = 4

class RegistroC177(Registro):
    """
    OPERAÇÕES COM PRODUTOS SUJEITOS A SELO DE CONTROLE IPI (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C177'),
        Campo(2, 'COD_SELO_IPI'),
        Campo(3, 'QT_SELO_IPI'),
    ]
    
    nivel = 4

class RegistroC178(Registro):
    """
    OPERAÇÕES COM PRODUTOS SUJEITOS À TRIBUTAÇÃO DE IPI POR UNIDADE OU QUANTIDADE DE PRODUTO (CÓDIGO 01)
    """
    campos = [
        CampoFixo(1, 'REG', 'C178'),
        Campo(2, 'CL_ENQ'),
        CampoNumerico(3, 'VL_UNID'),
        Campo(4, 'QUANT_PAD'),
    ]

    nivel = 4

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

    nivel = 4

class RegistroC180(Registro):
    """
    INFORMAÇÕES COMPLEMENTARES DAS OPERAÇÕES DE ENTRADA
    DE MERCADORIAS SUJEITAS À SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 1B, 04 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C180'),
        CampoNumerico(2, 'COD_RESP_RET'),
        CampoNumerico(3, 'QUANT_CONV'),
        CampoNumerico(4, 'UNID'),
        CampoNumerico(5, 'VL_UNIT_CONV'),
        CampoNumerico(6, 'VL_UNIT_ICMS_OP_CONV'),
        CampoNumerico(7, 'VL_UNIT_BC_ICMS_ST_CONV'),
        CampoNumerico(8, 'VL_UNIT_ICMS_ST_CONV'),
        CampoNumerico(9, 'VL_UNIT_FCP_ST_CONV'),
        Campo(10, 'COD_DA'),
        Campo(11, 'NUM_DA'),
    ]

    nivel = 4

class RegistroC185(Registro):
    """
    INFORMAÇÕES COMPLEMENTARES DAS OPERAÇÕES DE SAÍDA DE
    MERCADORIAS SUJEITAS À SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 1B, 04, 55 e 65).
    """
    campos = [
        CampoFixo(1, 'REG', 'C185'),
        CampoNumerico(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'CST_ICMS'),
        CampoNumerico(5, 'CFOP'),
        Campo(6, 'COD_MOT_REST_COMPL'),
        CampoNumerico(7, 'QUANT_CONV'),
        CampoNumerico(8, 'UNID'),
        CampoNumerico(9, 'VL_UNIT_CONV'),
        CampoNumerico(10, 'VL_UNIT_ICMS_NA_OPERACAO_CONV'),
        CampoNumerico(11, 'VL_UNIT_ICMS_OP_CONV'),
        CampoNumerico(12, 'VL_UNIT_ICMS_OP_ESTOQUE_CONV'),
        CampoNumerico(13, 'VL_UNIT_ICMS_ST_ESTOQUE_CONV'),
        CampoNumerico(14, 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV'),
        CampoNumerico(15, 'VL_UNIT_ICMS_ST_CONV_REST'),
        CampoNumerico(16, 'VL_UNIT_FCP_ST_CONV_REST'),
        CampoNumerico(17, 'VL_UNIT_ICMS_ST_CONV_COMPL'),
        CampoNumerico(18, 'VL_UNIT_FCP_ST_CONV_COMPL'),
    ]

    nivel = 3

class RegistroC190(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO (CÓDIGO 01, 1B, 04 E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C190'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS_ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        CampoNumerico(11, 'VL_IPI'),
        Campo(12, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC191(Registro):
    """
    INFORMAÇÕES DO FUNDO DE COMBATE À POBREZA – FCP – NA NFe (CÓDIGO 55) E NA NFC-E (CÓDIGO 65)
    """
    campos = [
        CampoFixo(1, 'REG', 'C191'),
        CampoNumerico(2, 'VL_FCP_OP'),
        CampoNumerico(3, 'VL_FCP_ST'),
        CampoNumerico(4, 'VL_FCP_RET'),
    ]

    nivel = 4

class RegistroC195(Registro):
    """
    OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 01, 1B E 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'C195'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT_COMPL'),
    ]

    nivel = 3

class RegistroC197(Registro):
    """
    OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'C197'),
        Campo(2, 'COD_AJ'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'COD_ITEM'),
        CampoNumerico(5, 'VL_BC_ICMS'),
        CampoNumerico(6, 'ALIQ_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_OUTROS'),
    ]

    nivel = 4

class RegistroC300(Registro):
    """
    RESUMO DIÁRIO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C300'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        CampoNumerico(4, 'SUB'),
        CampoNumerico(5, 'NUM_DOC_INI'),
        CampoNumerico(6, 'NUM_DOC_FIN'),
        CampoData(7, 'DT_DOC'),
        CampoNumerico(8, 'VL_DOC'),
        CampoNumerico(9, 'VL_PIS'),
        CampoNumerico(10, 'VL_COFINS'),
        Campo(11, 'COD_CTA'),
    ]

    nivel = 2

class RegistroC310(Registro):
    """
    DOCUMENTOS CANCELADOS DE NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C310'),
        CampoNumerico(2, 'NUM_DOC_CANC'),
    ]

    nivel = 3

class RegistroC320(Registro):
    """
    REGISTRO ANALÍTICO DO RESUMO DIÁRIO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C320'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC321(Registro):
    """
    ITENS DO RESUMO DIÁRIO DOS DOCUMENTOS (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C321'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
        Campo(4, 'UNID'),
        CampoNumerico(5, 'VL_ITEM'),
        CampoNumerico(6, 'VL_DESC'),
        CampoNumerico(7, 'VL_BC_ICMS'),
        CampoNumerico(8, 'VL_ICMS'),
        CampoNumerico(9, 'VL_PIS'),
        CampoNumerico(10, 'VL_COFINS'),
    ]

    nivel = 4

class RegistroC350(Registro):
    """
    NOTA FISCAL DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C350'),
        Campo(2, 'SER'),
        Campo(3, 'SUB_SER'),
        CampoNumerico(4, 'NUM_DOC'),
        CampoData(5, 'DT_DOC'),
        CampoCPFouCNPJ(6, 'CNPJ_CPF'),
        CampoNumerico(7, 'VL_MERC'),
        CampoNumerico(8, 'VL_DOC'),
        CampoNumerico(9, 'VL_DESC'),
        CampoNumerico(10, 'VL_PIS'),
        CampoNumerico(11, 'VL_COFINS'),
    ]

    nivel = 2

class RegistroC370(Registro):
    """
    ITENS DO DOCUMENTO (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C370'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'UNID'),
        CampoNumerico(6, 'VL_ITEM'),
        CampoNumerico(7, 'VL_DESC'),
    ]

    nivel = 3

class RegistroC390(Registro):
    """
    REGISTRO ANALÍTICO DAS NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGO 02)
    """
    campos = [
        CampoFixo(1, 'REG', 'C390'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]

    nivel = 3

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

    nivel = 2

class RegistroC405(Registro):
    """
    REDUÇÃO Z (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C405'),
        CampoData(2, 'DT_DOC'),
        Campo(3, 'CRO'),
        Campo(4, 'CRZ'),
        Campo(5, 'NUM_COO_FIN'),
        Campo(6, 'GT_FIN'),
        CampoNumerico(7, 'VL_BRT'),
    ]

    nivel = 3

class RegistroC410(Registro):
    """
    PIS E COFINS TOTALIZADOS NO DIA (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C410'),
        CampoNumerico(2, 'VL_PIS'),
        CampoNumerico(3, 'VL_COFINS'),
    ]

    nivel = 4

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

    nivel = 4

class RegistroC425(Registro):
    """
    RESUMO DE ITENS DO MOVIMENTO DIÁRIO (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C425'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
        Campo(4, 'UNID'),
        CampoNumerico(5, 'VL_ITEM'),
        CampoNumerico(6, 'VL_PIS'),
        CampoNumerico(7, 'VL_COFINS'),
    ]

    nivel = 5

class RegistroC460(Registro):
    """
    DOCUMENTO FISCAL EMITIDO POR ECF (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C460'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'COD_SIT'),
        CampoNumerico(4, 'NUM_DOC'),
        CampoData(5, 'DT_DOC'),
        CampoNumerico(6, 'VL_DOC'),
        CampoNumerico(7, 'VL_PIS'),
        CampoNumerico(8, 'VL_COFINS'),
        Campo(9, 'CPF_CNPJ'),
        Campo(10, 'NOM_ADQ'),
    ]

    nivel = 4

class RegistroC465(Registro):
    """
    DOCUMENTO
    """
    campos = [
        CampoFixo(1, 'REG', 'C465'),
        CampoChaveEletronica(2, 'CHV_CFE'),
        Campo(3, 'NUM_CCF'),
    ]

    nivel = 5

class RegistroC470(Registro):
    """
    ITENS DO DOCUMENTO FISCAL EMITIDO POR ECF (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C470'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
        CampoNumerico(4, 'QTD_CANC'),
        Campo(5, 'UNID'),
        CampoNumerico(6, 'VL_ITEM'),
        CampoNumerico(7, 'CST_ICMS'),
        CampoNumerico(8, 'CFOP'),
        CampoNumerico(9, 'ALIQ_ICMS'),
        CampoNumerico(10, 'VL_PIS'),
        CampoNumerico(11, 'VL_COFINS'),
    ]

    nivel = 5

class RegistroC490(Registro):
    """
    REGISTRO ANALÍTICO DO MOVIMENTO DIÁRIO (CÓDIGO 02 e 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C490'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]

    nivel = 4

class RegistroC495(Registro):
    """
    RESUMO MENSAL DE ITENS DO ECF POR ESTABELECIMENTO (CÓDIGO 02 E 2D)
    """
    campos = [
        CampoFixo(1, 'REG', 'C495'),
        CampoNumerico(2, 'ALIQ_ICMS'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        CampoNumerico(5, 'QTD_CANC'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM'),
        CampoNumerico(8, 'VL_DESC'),
        CampoNumerico(9, 'VL_CANC'),
        CampoNumerico(10, 'VL_ACMO'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'VL_ICMS'),
        CampoNumerico(13, 'VL_ISEN'),
        CampoNumerico(14, 'VL_NT'),
        CampoNumerico(15, 'VL_ICMS_ST'),
    ]

    nivel = 2

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
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'SUB'),
        Campo(9, 'COD_CONS'),
        CampoNumerico(10, 'NUM_DOC'),
        CampoData(11, 'DT_DOC'),
        CampoData(12, 'DT_E_S'),
        CampoNumerico(13, 'VL_DOC'),
        CampoNumerico(14, 'VL_DESC'),
        CampoNumerico(15, 'VL_FORN'),
        CampoNumerico(16, 'VL_SERV_NT'),
        CampoNumerico(17, 'VL_TERC'),
        CampoNumerico(18, 'VL_DA'),
        CampoNumerico(19, 'VL_BC_ICMS'),
        CampoNumerico(20, 'VL_ICMS'),
        CampoNumerico(21, 'VL_BC_ICMS_ST'),
        CampoNumerico(22, 'VL_ICMS_ST'),
        Campo(23, 'COD_INF'),
        CampoNumerico(24, 'VL_PIS'),
        CampoNumerico(25, 'VL_COFINS'),
        Campo(26, 'TP_LIGACAO'),
        Campo(27, 'COD_GRUPO_TENSAO'),
    ]

    nivel = 2

class RegistroC510(Registro):
    """
    ITENS DO DOCUMENTO NOTA FISCAL/CONTA ENERGIA ELÉTRICA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS (CÓDIGO 06 E 28)
    """
    campos = [
        CampoFixo(1, 'REG', 'C510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        CampoNumerico(5, 'QTD'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM'),
        CampoNumerico(8, 'VL_DESC'),
        CampoNumerico(9, 'CST_ICMS'),
        CampoNumerico(10, 'CFOP'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'ALIQ_ICMS'),
        CampoNumerico(13, 'VL_ICMS'),
        CampoNumerico(14, 'VL_BC_ICMS_ST'),
        CampoNumerico(15, 'ALIQ_ST'),
        CampoNumerico(16, 'VL_ICMS_ST'),
        Campo(17, 'IND_REC'),
        Campo(18, 'COD_PART'),
        CampoNumerico(19, 'VL_PIS'),
        CampoNumerico(20, 'VL_COFINS'),
        Campo(21, 'COD_CTA'),
    ]

    nivel = 3

class RegistroC590(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO - NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA E NOTA FISCAL CONSUMO FORNECIMENTO DE GÁS
    (CÓDIGO 06 E 28)
    """
    campos = [
        CampoFixo(1, 'REG', 'C590'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS_ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC600(Registro):
    """
    CONSOLIDAÇÃO DIÁRIA DE NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE FORNECIMENTO DÁGUA CANALIZADA
    E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS (EMPRESAS NÃO OBRIGADAS AO CONVÊNIO ICMS 115/03) - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C600'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'COD_MUN'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        Campo(6, 'COD_CONS'),
        CampoNumerico(7, 'QTD_CONS'),
        CampoNumerico(8, 'QTD_CANC'),
        CampoData(9, 'DT_DOC'),
        CampoNumerico(10, 'VL_DOC'),
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
        CampoNumerico(21, 'VL_PIS'),
        CampoNumerico(22, 'VL_COFINS'),
    ]

    nivel = 2

class RegistroC601(Registro):
    """
    DOCUMENTOS CANCELADOS - CONSOLIDAÇÃO DIÁRIA DE NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE
    FORNECIMENTO DÁGUA CANALIZADA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C601'),
        CampoNumerico(2, 'NUM_DOC_CANC'),
    ]

    nivel = 3

class RegistroC610(Registro):
    """
    ITENS DO DOCUMENTO CONSOLIDADO, NOTA FISCAL/CONTA DE FORNECIMENTO DÁGUA CANALIZADA E NOTA FISCAL/CONTA DE
    FORNECIMENTO DE GÁS (EMPRESAS NÃO OBRIGADAS AO CONVÊNIO ICMS 115/03) - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C610'),
        Campo(2, 'COD_CLASS'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'UNID'),
        CampoNumerico(6, 'VL_ITEM'),
        CampoNumerico(7, 'VL_DESC'),
        CampoNumerico(8, 'CST_ICMS'),
        CampoNumerico(9, 'CFOP'),
        CampoNumerico(10, 'ALIQ_ICMS'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'VL_ICMS'),
        CampoNumerico(13, 'VL_BC_ICMS_ST'),
        CampoNumerico(14, 'VL_ICMS_ST'),
        CampoNumerico(15, 'VL_PIS'),
        CampoNumerico(16, 'VL_COFINS'),
        Campo(17, 'COD_CTA'),
    ]

    nivel = 3

class RegistroC690(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS NOTAS FISCAIS/CONTAS DE ENERGIA ELÉTRICA, NOTA FISCAL/CONTA DE FORNECIMENTO D’ÁGUA
    CANALIZADA E NOTA FISCAL/CONTA DE FORNECIMENTO DE GÁS - CÓDIGO 06, 29 E 28.
    """
    campos = [
        CampoFixo(1, 'REG', 'C690'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_RED_BC'),
        CampoNumerico(9, 'VL_BC_ICMS_ST'),
        CampoNumerico(10, 'VL_ICMS_ST'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

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
        CampoData(6, 'DT_DOC_INI'),
        CampoData(7, 'DT_DOC_FIN'),
        Campo(8, 'NOM_MEST'),
    ]

    nivel = 2

class RegistroC790(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS
    """
    campos = [
        CampoFixo(1, 'REG', 'C790'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS_ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC791(Registro):
    """
    REGISTRO DE INFORMAÇÕES DE ST POR UF
    """
    campos = [
        CampoFixo(1, 'REG', 'C791'),
        Campo(2, 'UF'),
        CampoNumerico(3, 'VL_BC_ICMS_ST'),
        CampoNumerico(4, 'VL_ICMS_ST'),
    ]

    nivel = 4

class RegistroC800(Registro):
    """
    CUPOM FISCAL ELETRÔNICO (CÓDIGO 59)
    """
    campos = [
        CampoFixo(1, 'REG', 'C800'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'COD_SIT'),
        CampoNumerico(4, 'NUM_CFE'),
        CampoData(5, 'DT_DOC'),
        CampoNumerico(6, 'VL_CFE'),
        CampoNumerico(7, 'VL_PIS'),
        CampoNumerico(8, 'VL_COFINS'),
        CampoCPFouCNPJ(9, 'CNPJ_CPF'),
        CampoNumerico(10, 'NR_SAT'),
        CampoChaveEletronica(11, 'CHV_CFE'),
        CampoNumerico(12, 'VL_DESC'),
        CampoNumerico(13, 'VL_MERC'),
        CampoNumerico(14, 'VL_OUT_DA'),
        CampoNumerico(15, 'VL_ICMS'),
        CampoNumerico(16, 'VL_PIS_ST'),
        CampoNumerico(17, 'VL_COFINS_ST'),
    ]

    nivel = 2

class RegistroC850(Registro):
    """
    REGISTRO ANALÍTICO DO CF-E (CODIGO 59)
    """
    campos = [
        CampoFixo(1, 'REG', 'C850'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC860(Registro):
    """
    IDENTIFICAÇÃO DO EQUIPAMENTO SAT-CF-E
    """
    campos = [
        CampoFixo(1, 'REG', 'C860'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'NR_SAT'),
        CampoData(4, 'DT_DOC'),
        Campo(5, 'DOC_INI'),
        Campo(6, 'DOC_FIM'),
    ]

    nivel = 2

class RegistroC890(Registro):
    """
    RESUMO DIÁRIO DO CF-E (CÓDIGO 59) POR EQUIPAMENTO SAT-CF-E
    """
    campos = [
        CampoFixo(1, 'REG', 'C890'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        Campo(8, 'COD_OBS'),
    ]

    nivel = 3

class RegistroC990(Registro):
    """
    ENCERRAMENTO DO BLOCO C
    """
    campos = [
        CampoFixo(1, 'REG', 'C990'),
        CampoNumerico(2, 'QTD_LIN_C'),
    ]

    nivel = 1

class RegistroD001(Registro):
    """
    ABERTURA DO BLOCO D
    """
    campos = [
        CampoFixo(1, 'REG', 'D001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

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
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'SUB'),
        CampoNumerico(9, 'NUM_DOC'),
        CampoChaveEletronica(10, 'CHV_CTE'),
        CampoData(11, 'DT_DOC'),
        CampoData(12, 'DT_A_P'),
        Campo(13, 'TP_CT-e'),
        CampoChaveEletronica(14, 'CHV_CTE_REF'),
        CampoNumerico(15, 'VL_DOC'),
        CampoNumerico(16, 'VL_DESC'),
        Campo(17, 'IND_FRT'),
        CampoNumerico(18, 'VL_SERV'),
        CampoNumerico(19, 'VL_BC_ICMS'),
        CampoNumerico(20, 'VL_ICMS'),
        CampoNumerico(21, 'VL_NT'),
        Campo(22, 'COD_INF'),
        Campo(23, 'COD_CTA'),
        CampoNumerico(24, 'COD_MUN_ORIG'),
        CampoNumerico(25, 'COD_MUN_DEST'),
    ]

    nivel = 2

class RegistroD101(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DOS DOCUMENTOS FISCAIS
    QUANDO DAS PRESTAÇÕES INTERESTADUAIS DESTINADAS A CONSUMIDOR FINAL
    NÃO CONTRIBUINTE EC 87/15 (CÓDIGOS 57, 63 e 67)
    """
    campos = [
        CampoFixo(1, 'REG', 'D101'),
        CampoNumerico(2, 'VL_FCP_UF_DEST'),
        CampoNumerico(3, 'VL_ICMS_UF_DEST'),
        CampoNumerico(4, 'VL_ICMS_UF_REM'),
    ]

    nivel = 3

class RegistroD110(Registro):
    """
    ITENS DO DOCUMENTO - NOTA FISCAL DE SERVIÇOS DE TRANSPORTE (CÓDIGO 07)
    """
    campos = [
        CampoFixo(1, 'REG', 'D110'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'VL_SERV'),
        CampoNumerico(5, 'VL_OUT'),
    ]

    nivel = 3

class RegistroD120(Registro):
    """
    COMPLEMENTO DA NOTA FISCAL DE SERVIÇOS DE TRANSPORTE (CÓDIGO 07)
    """
    campos = [
        CampoFixo(1, 'REG', 'D120'),
        CampoNumerico(2, 'COD_MUN_ORIG'),
        CampoNumerico(3, 'COD_MUN_DEST'),
        Campo(4, 'VEIC_ID'),
        Campo(5, 'UF_ID'),
    ]

    nivel = 4

class RegistroD130(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO RODOVIÁRIO DE CARGAS E DO CONHECIMENTO RODOVIÁRIO DE CARGAS AVULSO (CÓDIGO 08 E 08B)
    """
    campos = [
        CampoFixo(1, 'REG', 'D130'),
        Campo(2, 'COD_PART_CONSG'),
        Campo(3, 'COD_PART_RED'),
        Campo(4, 'IND_FRT_RED'),
        CampoNumerico(5, 'COD_MUN_ORIG'),
        CampoNumerico(6, 'COD_MUN_DEST'),
        Campo(7, 'VEIC_ID'),
        CampoNumerico(8, 'VL_LIQ_FRT'),
        CampoNumerico(9, 'VL_SEC_CAT'),
        CampoNumerico(10, 'VL_DESP'),
        CampoNumerico(11, 'VL_PEDG'),
        CampoNumerico(12, 'VL_OUT'),
        CampoNumerico(13, 'VL_FRT'),
        Campo(14, 'UF_ID'),
    ]

    nivel = 3

class RegistroD140(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO AQUAVIÁRIO DE CARGAS (CÓDIGO 09)
    """
    campos = [
        CampoFixo(1, 'REG', 'D140'),
        Campo(2, 'COD_PART_CONSG'),
        CampoNumerico(3, 'COD_MUN_ORIG'),
        CampoNumerico(4, 'COD_MUN_DEST'),
        Campo(5, 'IND_VEIC'),
        Campo(6, 'VEIC_ID'),
        Campo(7, 'IND_NAV'),
        Campo(8, 'VIAGEM'),
        CampoNumerico(9, 'VL_FRT_LIQ'),
        CampoNumerico(10, 'VL_DESP_PORT'),
        CampoNumerico(11, 'VL_DESP_CAR_DESC'),
        CampoNumerico(12, 'VL_OUT'),
        CampoNumerico(13, 'VL_FRT_BRT'),
        CampoNumerico(14, 'VL_FRT_MM'),
    ]

    nivel = 3

class RegistroD150(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO AÉREO (CÓDIGO 10)
    """
    campos = [
        CampoFixo(1, 'REG', 'D150'),
        CampoNumerico(2, 'COD_MUN_ORIG'),
        CampoNumerico(3, 'COD_MUN_DEST'),
        Campo(4, 'VEIC_ID'),
        Campo(5, 'VIAGEM'),
        Campo(6, 'IND_TFA'),
        CampoNumerico(7, 'VL_PESO_TX'),
        CampoNumerico(8, 'VL_TX_TERR'),
        CampoNumerico(9, 'VL_TX_RED'),
        CampoNumerico(10, 'VL_OUT'),
        CampoNumerico(11, 'VL_TX_ADV'),
    ]

    nivel = 3

class RegistroD160(Registro):
    """
    CARGA TRANSPORTADA (CÓDIGO 08, 8B, 09, 10, 11, 26 E 27)
    """
    campos = [
        CampoFixo(1, 'REG', 'D160'),
        Campo(2, 'DESPACHO'),
        CampoCPFouCNPJ(3, 'CNPJ_CPF_REM'),
        Campo(4, 'IE_REM'),
        CampoNumerico(5, 'COD_MUN_ORI'),
        CampoCPFouCNPJ(6, 'CNPJ_CPF_DEST'),
        Campo(7, 'IE_DEST'),
        CampoNumerico(8, 'COD_MUN_DEST'),
    ]

    nivel = 3

class RegistroD161(Registro):
    """
    LOCAL DA COLETA E ENTREGA (CÓDIGO 08, 8B, 09, 10, 11 E 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D161'),
        Campo(2, 'IND_CARGA'),
        CampoCPFouCNPJ(3, 'CNPJ_CPF_COL'),
        Campo(4, 'IE_COL'),
        CampoNumerico(5, 'COD_MUN_COL'),
        CampoCPFouCNPJ(6, 'CNPJ_CPF_ENTG'),
        Campo(7, 'IE_ENTG'),
        CampoNumerico(8, 'COD_MUN_ENTG'),
    ]

    nivel = 4

class RegistroD162(Registro):
    """
    IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS (CÓDIGOS 08, 8B, 09, 10, 11, 26 E 27)
    """
    campos = [
        CampoFixo(1, 'REG', 'D162'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        CampoNumerico(4, 'NUM_DOC'),
        CampoData(5, 'DT_DOC'),
        CampoNumerico(6, 'VL_DOC'),
        CampoNumerico(7, 'VL_MERC'),
        CampoNumerico(8, 'QTD_VOL'),
        CampoNumerico(9, 'PESO_BRT'),
        CampoNumerico(10, 'PESO_LIQ'),
    ]

    nivel = 4

class RegistroD170(Registro):
    """
    COMPLEMENTO DO CONHECIMENTO MULTIMODAL DE CARGAS (CÓDIGO 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D170'),
        Campo(2, 'COD_PART_CONSG'),
        Campo(3, 'COD_PART_RED'),
        CampoNumerico(4, 'COD_MUN_ORIG'),
        CampoNumerico(5, 'COD_MUN_DEST'),
        Campo(6, 'OTM'),
        Campo(7, 'IND_NAT_FRT'),
        CampoNumerico(8, 'VL_LIQ_FRT'),
        CampoNumerico(9, 'VL_GRIS'),
        CampoNumerico(10, 'VL_PDG'),
        CampoNumerico(11, 'VL_OUT'),
        CampoNumerico(12, 'VL_FRT'),
        Campo(13, 'VEIC_ID'),
        Campo(14, 'UF_ID'),
    ]

    nivel = 3

class RegistroD180(Registro):
    """
    MODAIS (CÓDIGO 26)
    """
    campos = [
        CampoFixo(1, 'REG', 'D180'),
        Campo(2, 'NUM_SEQ'),
        Campo(3, 'IND_EMIT'),
        CampoCPFouCNPJ(4, 'CNPJ_CPF_EMIT'),
        Campo(5, 'UF_EMIT'),
        Campo(6, 'IE_EMIT'),
        CampoNumerico(7, 'COD_MUN_ORIG'),
        CampoCPFouCNPJ(8, 'CNPJ_CPF_TOM'),
        Campo(9, 'UF_TOM'),
        Campo(10, 'IE_TOM'),
        CampoNumerico(11, 'COD_MUN_DEST'),
        Campo(12, 'COD_MOD'),
        Campo(13, 'SER'),
        CampoNumerico(14, 'SUB'),
        CampoNumerico(15, 'NUM_DOC'),
        CampoData(16, 'DT_DOC'),
        CampoNumerico(17, 'VL_DOC'),
    ]

    nivel = 3

class RegistroD190(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27 E 57)
    """
    campos = [
        CampoFixo(1, 'REG', 'D190'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_RED_BC'),
        Campo(9, 'COD_OBS'),
    ]
    
    nivel = 3

class RegistroD195(Registro):
    """
    OBSERVAÇOES DO LANÇAMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'D195'),
        Campo(2, 'COD_OBS'),
        Campo(3, 'TXT_COMPL'),
    ]

    nivel = 3

class RegistroD197(Registro):
    """
    OUTRAS OBRIGAÇÕES TRIBUTÁRIAS, AJUSTES E INFORMAÇÕES DE VALORES PROVENIENTES DE DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'D197'),
        Campo(2, 'COD_AJ'),
        Campo(3, 'DESCR_COMPL_AJ'),
        Campo(4, 'COD_ITEM'),
        CampoNumerico(5, 'VL_BC_ICMS'),
        CampoNumerico(6, 'ALIQ_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_OUTROS'),
    ]

    nivel = 4

class RegistroD300(Registro):
    """
    REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE PASSAGEM RODOVIÁRIO, DE PASSAGEM AQUAVIÁRIO, DE PASSAGEM E NOTA DE
    BAGAGEM E DE PASSAGEM FERROVIÁRIO (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D300'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        CampoNumerico(4, 'SUB'),
        CampoNumerico(5, 'NUM_DOC_INI'),
        CampoNumerico(6, 'NUM_DOC_FIN'),
        CampoNumerico(7, 'CST_ICMS'),
        CampoNumerico(8, 'CFOP'),
        CampoNumerico(9, 'ALIQ_ICMS'),
        CampoData(10, 'DT_DOC'),
        CampoNumerico(11, 'VL_OPR'),
        CampoNumerico(12, 'VL_DESC'),
        CampoNumerico(13, 'VL_SERV'),
        CampoNumerico(14, 'VL_SEG'),
        CampoNumerico(15, 'VL_OUT DESP'),
        CampoNumerico(16, 'VL_BC_ICMS'),
        CampoNumerico(17, 'VL_ICMS'),
        CampoNumerico(18, 'VL_RED_BC'),
        Campo(19, 'COD_OBS'),
        Campo(20, 'COD_CTA'),
    ]

    nivel = 2

class RegistroD301(Registro):
    """
    DOCUMENTOS CANCELADOS DOS BILHETES DE PASSAGEM RODOVIÁRIO, DE PASSAGEM AQUAVIÁRIO, DE PASSAGEM E NOTA DE BAGAGEM E
    DE PASSAGEM FERROVIÁRIO (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D301'),
        CampoNumerico(2, 'NUM_DOC_CANC'),
    ]

    nivel = 3

class RegistroD310(Registro):
    """
    COMPLEMENTO DOS BILHETES (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D310'),
        CampoNumerico(2, 'COD_MUN_ORIG'),
        CampoNumerico(3, 'VL_SERV'),
        CampoNumerico(4, 'VL_BC_ICMS'),
        CampoNumerico(5, 'VL_ICMS'),
    ]

    nivel = 3

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

    nivel = 2

class RegistroD355(Registro):
    """
    REDUÇÃO Z (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D355'),
        CampoData(2, 'DT_DOC'),
        Campo(3, 'CRO'),
        Campo(4, 'CRZ'),
        Campo(5, 'NUM_COO_FIN'),
        Campo(6, 'GT_FIN'),
        CampoNumerico(7, 'VL_BRT'),
    ]

    nivel = 3

class RegistroD360(Registro):
    """
    PIS E COFINS TOTALIZADOS NO DIA (CÓDIGOS 2E, 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D360'),
        CampoNumerico(2, 'VL_PIS'),
        CampoNumerico(3, 'VL_COFINS'),
    ]

    nivel = 4

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

    nivel = 4

class RegistroD370(Registro):
    """
    COMPLEMENTO DOS DOCUMENTOS INFORMADOS (CÓDIGOS 13, 14, 15 E 16 E 2E)
    """
    campos = [
        CampoFixo(1, 'REG', 'D370'),
        CampoNumerico(2, 'COD_MUN_ORIG'),
        CampoNumerico(3, 'VL_SERV'),
        CampoNumerico(4, 'QTD_BILH'),
        CampoNumerico(5, 'VL_BC_ICMS'),
        CampoNumerico(6, 'VL_ICMS'),
    ]

    nivel = 5

class RegistroD390(Registro):
    """
    REGISTRO ANALÍTICO DO MOVIMENTO DIÁRIO (CÓDIGOS 13, 14, 15, 16 E 2E)
    """
    campos = [
        CampoFixo(1, 'REG', 'D390'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ISSQN'),
        CampoNumerico(7, 'ALIQ_ISSQN'),
        CampoNumerico(8, 'VL_ISSQN'),
        CampoNumerico(9, 'VL_BC_ICMS'),
        CampoNumerico(10, 'VL_ICMS'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 4

class RegistroD400(Registro):
    """
    RESUMO DE MOVIMENTO DIÁRIO - RMD (CÓDIGO 18)
    """
    campos = [
        CampoFixo(1, 'REG', 'D400'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        CampoNumerico(4, 'COD_SIT'),
        Campo(5, 'SER'),
        CampoNumerico(6, 'SUB'),
        CampoNumerico(7, 'NUM_DOC'),
        CampoData(8, 'DT_DOC'),
        CampoNumerico(9, 'VL_DOC'),
        CampoNumerico(10, 'VL_DESC'),
        CampoNumerico(11, 'VL_SERV'),
        CampoNumerico(12, 'VL_BC_ICMS'),
        CampoNumerico(13, 'VL_ICMS'),
        CampoNumerico(14, 'VL_PIS'),
        CampoNumerico(15, 'VL_COFINS'),
        Campo(16, 'COD_CTA'),
    ]

    nivel = 2

class RegistroD410(Registro):
    """
    DOCUMENTOS INFORMADOS (CÓDIGOS 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D410'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SER'),
        CampoNumerico(4, 'SUB'),
        CampoNumerico(5, 'NUM_DOC_INI'),
        CampoNumerico(6, 'NUM_DOC_FIN'),
        CampoData(7, 'DT_DOC'),
        CampoNumerico(8, 'CST_ICMS'),
        CampoNumerico(9, 'CFOP'),
        CampoNumerico(10, 'ALIQ_ICMS'),
        CampoNumerico(11, 'VL_OPR'),
        CampoNumerico(12, 'VL_DESC'),
        CampoNumerico(13, 'VL_SERV'),
        CampoNumerico(14, 'VL_BC_ICMS'),
        CampoNumerico(15, 'VL_ICMS'),
    ]

    nivel = 3

class RegistroD411(Registro):
    """
    DOCUMENTOS CANCELADOS DOS DOCUMENTOS INFORMADOS (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D411'),
        CampoNumerico(2, 'NUM_DOC_CANC'),
    ]

    nivel = 4

class RegistroD420(Registro):
    """
    COMPLEMENTO DOS DOCUMENTOS INFORMADOS (CÓDIGO 13, 14, 15 E 16)
    """
    campos = [
        CampoFixo(1, 'REG', 'D420'),
        CampoNumerico(2, 'COD_MUN_ORIG'),
        CampoNumerico(3, 'VL_SERV'),
        CampoNumerico(4, 'VL_BC_ICMS'),
        CampoNumerico(5, 'VL_ICMS'),
    ]

    nivel = 3

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
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'SUB'),
        CampoNumerico(9, 'NUM_DOC'),
        CampoData(10, 'DT_DOC'),
        CampoData(11, 'DT_A_P'),
        CampoNumerico(12, 'VL_DOC'),
        CampoNumerico(13, 'VL_DESC'),
        CampoNumerico(14, 'VL_SERV'),
        CampoNumerico(15, 'VL_SERV_NT'),
        CampoNumerico(16, 'VL_TERC'),
        CampoNumerico(17, 'VL_DA'),
        CampoNumerico(18, 'VL_BC_ICMS'),
        CampoNumerico(19, 'VL_ICMS'),
        Campo(20, 'COD_INF'),
        CampoNumerico(21, 'VL_PIS'),
        CampoNumerico(22, 'VL_COFINS'),
        Campo(23, 'COD_CTA'),
        Campo(24, 'TP_ASSINANTE'),
    ]

    nivel = 2

class RegistroD510(Registro):
    """
    ITENS DO DOCUMENTO - NOTA FISCAL DE SERVIÇO DE COMUNICAÇÃO E SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        CampoNumerico(5, 'QTD'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM'),
        CampoNumerico(8, 'VL_DESC'),
        CampoNumerico(9, 'CST_ICMS'),
        CampoNumerico(10, 'CFOP'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'ALIQ_ICMS'),
        CampoNumerico(13, 'VL_ICMS'),
        CampoNumerico(14, 'VL_BC_ICMS_ST'),
        CampoNumerico(15, 'VL_ICMS_ST'),
        Campo(16, 'IND_REC'),
        Campo(17, 'COD_PART'),
        CampoNumerico(18, 'VL_PIS'),
        CampoNumerico(19, 'VL_COFINS'),
        Campo(20, 'COD_CTA'),
    ]

    nivel = 3

class RegistroD530(Registro):
    """
    TERMINAL FATURADO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D530'),
        Campo(2, 'IND_SERV'),
        CampoData(3, 'DT_INI_SERV'),
        CampoData(4, 'DT_FIN_SERV'),
        Campo(5, 'PER_FISCAL'),
        Campo(6, 'COD_AREA'),
        Campo(7, 'TERMINAL'),
    ]

    nivel = 3

class RegistroD590(Registro):
    """
    REGISTRO ANALÍTICO DO DOCUMENTO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D590'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS_ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

class RegistroD600(Registro):
    """
    CONSOLIDAÇÃO DA PRESTAÇÃO DE SERVIÇOS - NOTAS DE SERVIÇO DE COMUNICAÇÃO E DE SERVIÇO DE TELECOMUNICAÇÃO (CÓDIGO 21
    E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D600'),
        Campo(2, 'COD_MOD'),
        CampoNumerico(3, 'COD_MUN'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        Campo(6, 'COD_CONS'),
        CampoNumerico(7, 'QTD_CONS'),
        CampoData(8, 'DT_DOC'),
        CampoNumerico(9, 'VL_DOC'),
        CampoNumerico(10, 'VL_DESC'),
        CampoNumerico(11, 'VL_SERV'),
        CampoNumerico(12, 'VL_SERV_N T'),
        CampoNumerico(13, 'VL_TERC'),
        CampoNumerico(14, 'VL_DA'),
        CampoNumerico(15, 'VL_BC_ICMS'),
        CampoNumerico(16, 'VL_ICMS'),
        CampoNumerico(17, 'VL_PIS'),
        CampoNumerico(18, 'VL_COFINS'),
    ]

    nivel = 2

class RegistroD610(Registro):
    """
    ITENS DO DOCUMENTO CONSOLIDADO (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D610'),
        Campo(2, 'COD_CLASS'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'UNID'),
        CampoNumerico(6, 'VL_ITEM'),
        CampoNumerico(7, 'VL_DESC'),
        CampoNumerico(8, 'CST_ICMS'),
        CampoNumerico(9, 'CFOP'),
        CampoNumerico(10, 'ALIQ_ICMS'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'VL_ICMS'),
        CampoNumerico(13, 'VL_BC_ICMS _ST'),
        CampoNumerico(14, 'VL_ICMS_ST'),
        CampoNumerico(15, 'VL_RED_BC'),
        CampoNumerico(16, 'VL_PIS'),
        CampoNumerico(17, 'VL_COFINS'),
        Campo(18, 'COD_CTA'),
    ]

    nivel = 3

class RegistroD690(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D690'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS _ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

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
        CampoData(6, 'DT_DOC_INI'),
        CampoData(7, 'DT_DOC_FIN'),
        Campo(8, 'NOM_MEST'),
    ]

    nivel = 2

class RegistroD696(Registro):
    """
    REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 21 E 22)
    """
    campos = [
        CampoFixo(1, 'REG', 'D696'),
        CampoNumerico(2, 'CST_ICMS'),
        CampoNumerico(3, 'CFOP'),
        CampoNumerico(4, 'ALIQ_ICMS'),
        CampoNumerico(5, 'VL_OPR'),
        CampoNumerico(6, 'VL_BC_ICMS'),
        CampoNumerico(7, 'VL_ICMS'),
        CampoNumerico(8, 'VL_BC_ICMS_ST'),
        CampoNumerico(9, 'VL_ICMS_ST'),
        CampoNumerico(10, 'VL_RED_BC'),
        Campo(11, 'COD_OBS'),
    ]

    nivel = 3

class RegistroD697(Registro):
    """
    REGISTRO DE INFORMAÇÕES DE OUTRAS UFs, RELATIVAMENTE AOS SERVIÇOS “NÃO-MEDIDOS” DE TELEVISÃO POR ASSINATURA VIA
    SATÉLITE
    """
    campos = [
        CampoFixo(1, 'REG', 'D697'),
        Campo(2, 'UF'),
        CampoNumerico(3, 'VL_BC_ICMS'),
        CampoNumerico(4, 'VL_ICMS'),
    ]

    nivel = 4

class RegistroD990(Registro):
    """
    ENCERRAMENTO DO BLOCO D
    """
    campos = [
        CampoFixo(1, 'REG', 'D990'),
        CampoNumerico(2, 'QTD_LIN_D'),
    ]

    nivel = 1

class RegistroE001(Registro):
    """
    ABERTURA DO BLOCO E
    """
    campos = [
        CampoFixo(1, 'REG', 'E001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroE100(Registro):
    """
    PERÍODO DA APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', 'E100'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]

    nivel = 2

class RegistroE110(Registro):
    """
    APURAÇÃO DO ICMS - OPERAÇÕES PRÓPRIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'E110'),
        CampoNumerico(2, 'VL_TOT_DEBITOS'),
        CampoNumerico(3, 'VL_AJ_DEBITOS'),
        CampoNumerico(4, 'VL_TOT_AJ_DEBITOS'),
        CampoNumerico(5, 'VL_ESTORNOS_CRED'),
        CampoNumerico(6, 'VL_TOT_CREDITOS'),
        CampoNumerico(7, 'VL_AJ_CREDITOS'),
        CampoNumerico(8, 'VL_TOT_AJ_CREDITOS'),
        CampoNumerico(9, 'VL_ESTORNOS_DEB'),
        CampoNumerico(10, 'VL_SLD_CREDOR_ANT'),
        CampoNumerico(11, 'VL_SLD_APURADO'),
        CampoNumerico(12, 'VL_TOT_DED'),
        CampoNumerico(13, 'VL_ICMS_RECOLHER'),
        CampoNumerico(14, 'VL_SLD_CREDOR_TRANSPORTAR'),
        Campo(15, 'DEB_ESP'),
    ]

    nivel = 3

class RegistroE111(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', 'E111'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'DESCR_COMPL_AJ'),
        CampoNumerico(4, 'VL_AJ_APUR'),
    ]

    nivel = 4

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

    nivel = 5

class RegistroE113(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS - IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', 'E113'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC'),
        CampoData(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        CampoNumerico(9, 'VL_AJ_ITEM'),
    ]

    nivel = 5

class RegistroE115(Registro):
    """
    INFORMAÇÕES ADICIONAIS DA APURAÇÃO - VALORES DECLARATÓRIOS
    """
    campos = [
        CampoFixo(1, 'REG', 'E115'),
        Campo(2, 'COD_INF_ADIC'),
        CampoNumerico(3, 'VL_INF_ADIC'),
        Campo(4, 'DESCR_COMPL_AJ'),
    ]

    nivel = 4

class RegistroE116(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - OPERAÇÕES PRÓPRIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'E116'),
        Campo(2, 'COD_OR'),
        CampoNumerico(3, 'VL_OR'),
        CampoData(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]

    nivel = 4

class RegistroE200(Registro):
    """
    PERÍODO DA APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E200'),
        Campo(2, 'UF'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIN'),
    ]
    
    nivel = 2

class RegistroE210(Registro):
    """
    APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E210'),
        Campo(2, 'IND_MOV_ST'),
        CampoNumerico(3, 'VL_SLD_CRED_ANT_ST'),
        CampoNumerico(4, 'VL_DEVOL_ST'),
        CampoNumerico(5, 'VL_RESSARC_ST'),
        CampoNumerico(6, 'VL_OUT_CRED_ST'),
        CampoNumerico(7, 'VL_AJ_CREDITOS_ST'),
        CampoNumerico(8, 'VL_RETENÇAO_ST'),
        CampoNumerico(9, 'VL_OUT_DEB_ST'),
        CampoNumerico(10, 'VL_AJ_DEBITOS_ST'),
        CampoNumerico(11, 'VL_SLD_DEV_ANT_ST'),
        CampoNumerico(12, 'VL_DEDUÇÕES_ST'),
        CampoNumerico(13, 'VL_ICMS_RECOL_ST'),
        CampoNumerico(14, 'VL_SLD_CRED_ST_TRAN SPORTAR'),
        Campo(15, 'DEB_ESP_ST'),
    ]

    nivel = 3

class RegistroE220(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E220'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'DESCR_COMPL_AJ'),
        CampoNumerico(4, 'VL_AJ_APUR'),
    ]

    nivel = 4

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

    nivel = 5

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
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC'),
        CampoData(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        CampoNumerico(9, 'VL_AJ_ITEM'),
    ]

    nivel = 5

class RegistroE250(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - SUBSTITUIÇÃO TRIBUTÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', 'E250'),
        Campo(2, 'COD_OR'),
        CampoNumerico(3, 'VL_OR'),
        CampoData(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]

    nivel = 4

class RegistroE300(Registro):
    """
    PERÍODO DE APURAÇÃO DO FUNDO DE COMBATE À POBREZA E
    DO ICMS DIFERENCIAL DE ALÍQUOTA – UF ORIGEM/DESTINO EC 87/15
    """
    campos = [
        CampoFixo(1, 'REG', 'E300'),
        Campo(2, 'UF'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIN'),
    ]

    nivel = 2

class RegistroE310(Registro):
    """
    APURAÇÃO DO FUNDO DE COMBATE À POBREZA E DO ICMS
    DIFERENCIAL DE ALÍQUOTA – UF ORIGEM/DESTINO EC 87/15.
    (VÁLIDO A PARTIR DE 01/01/2017)
    """
    campos = [
        CampoFixo(1, 'REG', 'E310'),
        Campo(2, 'IND_MOV_FCP_DIFAL'),
        CampoNumerico(3, 'VL_SLD_CRED_ANT_DIFAL'),
        CampoNumerico(4, 'VL_TOT_DEBITOS_DIFAL'),
        CampoNumerico(5, 'VL_OUT_DEB_DIFAL'),
        CampoNumerico(6, 'VL_TOT_CREDITOS_DIFAL'),
        CampoNumerico(7, 'VL_OUT_CRED_DIFAL'),
        CampoNumerico(8, 'VL_SLD_DEV_ANT_DIFAL'),
        CampoNumerico(9, 'VL_DEDUCOES_DIFAL'),
        CampoNumerico(10, 'VL_RECOL_DIFAL'),
        CampoNumerico(11, 'VL_SLD_CRED_TRANSPORTAR_DIFAL'),
        Campo(12, 'DEB_ESP_DIFAL'),
        CampoNumerico(13, 'VL_SLD_CRED_ANT_FCP'),
        CampoNumerico(14, 'VL_TOT_DEB_FCP'),
        CampoNumerico(15, 'VL_OUT_DEB_FCP'),
        CampoNumerico(16, 'VL_TOT_CRED_FCP'),
        CampoNumerico(17, 'VL_OUT_CRED_FCP'),
        CampoNumerico(18, 'VL_SLD_DEV_ANT_FCP'),
        CampoNumerico(19, 'VL_DEDUCOES_FCP'),
        CampoNumerico(20, 'VL_RECOL_FCP'),
        CampoNumerico(21, 'VL_SLD_CRED_TRANSPORTAR_FCP'),
        Campo(22, 'DEB_ESP_FCP'),
    ]

    nivel = 3

class RegistroE311(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO FUNDO DE
    COMBATE À POBREZA E DO ICMS DIFERENCIAL DE ALÍQUOTA UF
    ORIGEM/DESTINO EC 87/15
    """
    campos = [
        CampoFixo(1, 'REG', 'E311'),
        Campo(2, 'COD_AJ_APUR'),
        Campo(3, 'DESCR_COMPL_AJ'),
        CampoNumerico(4, 'VL_AJ_APUR'),
    ]

    nivel = 4

class RegistroE312(Registro):
    """
    REGISTRO E312: INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO
    FUNDO DE COMBATE À POBREZA E DO ICMS DIFERENCIAL DE ALÍQUOTA UF
    ORIGEM/DESTINO EC 87/15
    """
    campos = [
        CampoFixo(1, 'REG', 'E312'),
        Campo(2, 'NUM_DA'),
        Campo(3, 'NUM_PROC'),
        Campo(4, 'IND_PROC'),
        Campo(5, 'PROC'),
        Campo(6, 'TXT_COMPL'),
    ]

    nivel = 5

class RegistroE313(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO
    FUNDO DE COMBATE À POBREZA E DO ICMS DIFERENCIAL DE ALÍQUOTA UF
    ORIGEM/DESTINO EC 87/15 - IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', 'E313'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC'),
        CampoChaveEletronica(7, 'CHV_DOCe'),
        CampoData(8, 'DT_DOC'),
        Campo(9, 'COD_ITEM'),
        CampoNumerico(10, 'VL_AJ_ITEM'),
    ]

    nivel = 5

class RegistroE316(Registro):
    """
    OBRIGAÇÕES RECOLHIDAS OU A RECOLHER – FUNDO DE
    COMBATE À POBREZA E ICMS DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO
    EC 87/15.
    """
    campos = [
        CampoFixo(1, 'REG', 'E316'),
        Campo(2, 'COD_OR'),
        CampoNumerico(3, 'VL_OR'),
        CampoData(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]

    nivel = 4

class RegistroE500(Registro):
    """
    PERÍODO DE APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E500'),
        Campo(2, 'IND_APUR'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIN'),
    ]

    nivel = 2

class RegistroE510(Registro):
    """
    CONSOLIDAÇÃO DOS VALORES DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E510'),
        CampoNumerico(2, 'CFOP'),
        Campo(3, 'CST_IPI'),
        CampoNumerico(4, 'VL_CONT_IPI'),
        CampoNumerico(5, 'VL_BC_IPI'),
        CampoNumerico(6, 'VL_IPI'),
    ]

    nivel = 3

class RegistroE520(Registro):
    """
    APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E520'),
        CampoNumerico(2, 'VL_SD_ANT_IPI'),
        CampoNumerico(3, 'VL_DEB_IPI'),
        CampoNumerico(4, 'VL_CRED_IPI'),
        CampoNumerico(5, 'VL_OD_IPI'),
        CampoNumerico(6, 'VL_OC_IPI'),
        CampoNumerico(7, 'VL_SC_IPI'),
        CampoNumerico(8, 'VL_SD_IPI'),
    ]

    nivel = 3

class RegistroE530(Registro):
    """
    AJUSTES DA APURAÇÃO DO IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'E530'),
        Campo(2, 'IND_AJ'),
        CampoNumerico(3, 'VL_AJ'),
        Campo(4, 'COD_AJ'),
        Campo(5, 'IND_DOC'),
        CampoNumerico(6, 'NUM_DOC'),
        Campo(7, 'DESCR_AJ'),
    ]

    nivel = 4

class RegistroE531(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO IPI –
    IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS (01 e 55)
    """
    campos = [
        CampoFixo(1, 'REG', 'E531'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC'),
        CampoData(7, 'DT_DOC'),
        CampoNumerico(8, 'COD_ITEM'),
        CampoNumerico(9, 'VL_AJ_ITEM'),
        CampoChaveEletronica(10, 'CHV_NFE'),
    ]

    nivel = 5

class RegistroE990(Registro):
    """
    ENCERRAMENTO DO BLOCO E
    """
    campos = [
        CampoFixo(1, 'REG', 'E990'),
        CampoNumerico(2, 'QTD_LIN_E'),
    ]

    nivel = 1

class RegistroG001(Registro):
    """
    ABERTURA DO BLOCO G
    """
    campos = [
        CampoFixo(1, 'REG', 'G001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroG110(Registro):
    """
    ICMS ATIVO PERMANENTE CIAP
    """
    campos = [
        CampoFixo(1, 'REG', 'G110'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        Campo(4, 'SALDO_IN_ICMS'),
        Campo(5, 'SOM_PARC'),
        CampoNumerico(6, 'VL_TRIB_EXP'),
        CampoNumerico(7, 'VL_TOTAL'),
        Campo(8, 'IND_PER_SAI'),
        Campo(9, 'ICMS_APROP'),
        Campo(10, 'SOM_ICMS_OC'),
    ]

    nivel = 2

class RegistroG125(Registro):
    """
    MOVIMENTAÇÃO DE BEM OU COMPONENTE DO ATIVO IMOBILIZADO
    """
    campos = [
        CampoFixo(1, 'REG', 'G125'),
        Campo(2, 'COD_IND_BEM'),
        CampoData(3, 'DT_MOV'),
        Campo(4, 'TIPO_MOV'),
        CampoNumerico(5, 'VL_IMOB_ICMS_OP'),
        CampoNumerico(6, 'VL_IMOB_ICMS_ST'),
        CampoNumerico(7, 'VL_IMOB_ICMS_FRT'),
        CampoNumerico(8, 'VL_IMOB_ICMS_DIF'),
        CampoNumerico(9, 'NUM_PARC'),
        CampoNumerico(10, 'VL_PARC_PASS'),
    ]

    nivel = 3

class RegistroG126(Registro):
    """
    OUTROS CRÉDITOS CIAP
    """
    campos = [
        CampoFixo(1, 'REG', 'G126'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        CampoNumerico(4, 'NUM_PARC'),
        CampoNumerico(5, 'VL_PARC_PASS'),
        CampoNumerico(6, 'VL_TRIB_OC'),
        CampoNumerico(7, 'VL_TOTAL'),
        Campo(8, 'IND_PER_SAI'),
        CampoNumerico(9, 'VL_PARC_APRO P'),
    ]

    nivel = 4

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
        CampoNumerico(6, 'NUM_DOC'),
        CampoChaveEletronica(7, 'CHV_NFE_CTE'),
        CampoData(8, 'DT_DOC'),
    ]

    nivel = 4

class RegistroG140(Registro):
    """
    IDENTIFICAÇÃO DO ITEM DO DOCUMENTO FISCAL
    """
    campos = [
        CampoFixo(1, 'REG', 'G140'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
    ]

    nivel = 5

class RegistroG990(Registro):
    """
    ENCERRAMENTO DO BLOCO G
    """
    campos = [
        CampoFixo(1, 'REG', 'G990'),
        CampoNumerico(2, 'QTD_LIN_G'),
    ]

    nivel = 1

class RegistroH001(Registro):
    """
    ABERTURA DO BLOCO H
    """
    campos = [
        CampoFixo(1, 'REG', 'H001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroH005(Registro):
    """
    TOTAIS DO INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H005'),
        CampoData(2, 'DT_INV'),
        CampoNumerico(3, 'VL_INV'),
        Campo(4, 'MOT_INV'),
    ]

    nivel = 2

class RegistroH010(Registro):
    """
    INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H010'),
        Campo(2, 'COD_ITEM'),
        Campo(3, 'UNID'),
        CampoNumerico(4, 'QTD'),
        CampoNumerico(5, 'VL_UNIT'),
        CampoNumerico(6, 'VL_ITEM'),
        Campo(7, 'IND_PROP'),
        Campo(8, 'COD_PART'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'COD_CTA'),
        CampoNumerico(11, 'VL_ITEM_IR'),
    ]

    nivel = 3

class RegistroH020(Registro):
    """
    INFORMAÇÃO COMPLEMENTAR DO INVENTÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'H020'),
        CampoNumerico(2, 'CST_ICMS'),
        Campo(3, 'BC_ICMS'),
        CampoNumerico(4, 'VL_ICMS'),
    ]

    nivel = 4

class RegistroH990(Registro):
    """
    ENCERRAMENTO DO BLOCO H
    """
    campos = [
        CampoFixo(1, 'REG', 'H990'),
        CampoNumerico(2, 'QTD_LIN_H'),
    ]

    nivel = 1

class RegistroK001(Registro):
    """
    ABERTURA DO BLOCO K
    """
    campos = [
        CampoFixo(1, 'REG', 'K001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class RegistroK100(Registro):
    """
    PERÍODO DE APURAÇÃO DO ICMS/IPI
    """
    campos = [
        CampoFixo(1, 'REG', 'K100'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]

    nivel = 2

class RegistroK200(Registro):
    """
    ESTOQUE ESCRITURADO
    """
    campos = [
        CampoFixo(1, 'REG', 'K200'),
        CampoData(2, 'DT_EST'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'IND_EST'),
        Campo(6, 'COD_PART'),
    ]

    nivel = 3

class RegistroK210(Registro):
    """
    DESMONTAGEM DE MERCADORIAS – ITEM DE ORIGE
    """
    campos = [
        CampoFixo(1, 'REG', 'K210'),
        CampoData(2, 'DT_INI_OS'),
        CampoData(3, 'DT_FIN_OS'),
        Campo(4, 'COD_DOC_OS'),
        Campo(5, 'COD_ITEM_ORI'),
        CampoNumerico(6, 'QTD_ORI'),
    ]

    nivel = 3

class RegistroK215(Registro):
    """
    DESMONTAGEM DE MERCADORIAS – ITENS DE DESTINO
    """
    campos = [
        CampoFixo(1, 'REG', 'K215'),
        Campo(2, 'COD_ITEM_DES'),
        CampoNumerico(3, 'QTD_DES'),
    ]

    nivel = 4

class RegistroK220(Registro):
    """
    OUTRAS MOVIMENTAÇÕES INTERNAS ENTRE MERCADORIAS
    """
    campos = [
        CampoFixo(1, 'REG', 'K220'),
        CampoData(2, 'DT_MOV'),
        Campo(3, 'COD_ITEM_ORI'),
        Campo(4, 'COD_ITEM_DEST'),
        CampoNumerico(5, 'QTD'),
    ]

    nivel = 3

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
        CampoNumerico(6, 'QTD_ENC'),
    ]

    nivel = 3

class RegistroK235(Registro):
    """
    INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K235'),
        CampoData(2, 'DT_SAIDA'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'COD_INS_SUBST'),
    ]

    nivel = 4

class RegistroK250(Registro):
    """
    INDUSTRIALIZAÇÃO EFETUADA POR TERCEIROS – ITENS PRODUZIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K250'),
        CampoData(2, 'DT_PROD'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
    ]

    nivel = 3

class RegistroK255(Registro):
    """
    INDUSTRIALIZAÇÃO EM TERCEIROS – INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K255'),
        CampoData(2, 'DT_CONS'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD'),
        Campo(5, 'COD_INS_SUBST'),
    ]

    nivel = 4

class RegistroK260(Registro):
    """
    REPROCESSAMENTO/REPARO DE PRODUTO/INSUMO
    """
    campos = [
        CampoFixo(1, 'REG', 'K260'),
        Campo(2, 'OD_OP_OS'),
        Campo(3, 'COD_ITEM'),
        CampoData(4, 'DT_SAIDA'),
        CampoNumerico(5, 'QTD_SAIDA'),
        CampoData(6, 'DT_RET'),
        CampoNumerico(7, 'QTD_RET'),
    ]

    nivel = 3

class RegistroK265(Registro):
    """
    REPROCESSAMENTO/REPARO – MERCADORIAS CONSUMIDAS E/OU
    RETORNADAS
    """
    campos = [
        CampoFixo(1, 'REG', 'K265'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD_CONS'),
        CampoNumerico(4, 'QTD_RET'),
    ]

    nivel = 4

class RegistroK270(Registro):
    """
    CORREÇÃO DE APONTAMENTO DOS REGISTROS K210, K220, K230,
    K250, K260, K291, K292, K301 E K302
    """
    campos = [
        CampoFixo(1, 'REG', 'K270'),
        CampoData(2, 'DT_INI_AP'),
        CampoData(3, 'DT_FIN_AP'),
        Campo(4, 'COD_OP_OS'),
        Campo(5, 'COD_ITEM'),
        CampoNumerico(6, 'QTD_COR_POS'),
        CampoNumerico(7, 'QTD_COR_NEG'),
        Campo(8, 'ORIGEM'),
    ]

    nivel = 3

class RegistroK275(Registro):
    """
    CORREÇÃO DE APONTAMENTO E RETORNO DE INSUMOS DOS
    REGISTROS K215, K220, K235, K255 E K265.
    """
    campos = [
        CampoFixo(1, 'REG', 'K275'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD_COR_POS'),
        CampoNumerico(4, 'QTD_COR_NEG'),
        Campo(5, 'COD_INS_SUBST'),
    ]

    nivel = 4

class RegistroK280(Registro):
    """
    CORREÇÃO DE APONTAMENTO – ESTOQUE ESCRITURADO
    """
    campos = [
        CampoFixo(1, 'REG', 'K280'),
        CampoData(2, 'DT_EST'),
        Campo(3, 'COD_ITEM'),
        CampoNumerico(4, 'QTD_COR_POS'),
        CampoNumerico(5, 'QTD_COR_NEG'),
        Campo(6, 'IND_EST'),
        Campo(7, 'COD_PART'),
    ]

    nivel = 3

class RegistroK290(Registro):
    """
    PRODUÇÃO CONJUNTA – ORDEM DE PRODUÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', 'K290'),
        CampoData(2, 'DT_INI_OP'),
        CampoData(3, 'DT_FIN_OP'),
        Campo(4, 'COD_DOC_OP'),
    ]

    nivel = 3

class RegistroK291(Registro):
    """
    PRODUÇÃO CONJUNTA – ITENS PRODUZIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K291'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
    ]

    nivel = 4

class RegistroK292(Registro):
    """
    PRODUÇÃO CONJUNTA – INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K292'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
    ]

    nivel = 4

class RegistroK300(Registro):
    """
    PRODUÇÃO CONJUNTA – INDUSTRIALIZAÇÃO EFETUADA POR
    TERCEIROS
    """
    campos = [
        CampoFixo(1, 'REG', 'K300'),
        CampoData(2, 'DT_PROD'),
    ]

    nivel = 3

class RegistroK301(Registro):
    """
    PRODUÇÃO CONJUNTA – INDUSTRIALIZAÇÃO EFETUADA POR
    TERCEIROS – ITENS PRODUZIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K301'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
    ]

    nivel = 4

class RegistroK302(Registro):
    """
    PRODUÇÃO CONJUNTA – INDUSTRIALIZAÇÃO EFETUADA POR
    TERCEIROS – INSUMOS CONSUMIDOS
    """
    campos = [
        CampoFixo(1, 'REG', 'K302'),
        Campo(2, 'COD_ITEM'),
        CampoNumerico(3, 'QTD'),
    ]

    nivel = 4

class RegistroK990(Registro):
    """
    ENCERRAMENTO DO BLOCO K
    """
    campos = [
        CampoFixo(1, 'REG', 'K990'),
        CampoNumerico(2, 'QTD_LIN_K'),
    ]

    nivel = 1

class Registro1001(Registro):
    """
    ABERTURA DO BLOCO 1
    """
    campos = [
        CampoFixo(1, 'REG', '1001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

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
        Campo(11, 'IND_GIAF1'),
        Campo(12, 'IND_GIAF3'),
        Campo(13, 'IND_GIAF4'),
    ]

    nivel = 2

class Registro1100(Registro):
    """
    REGISTRO DE INFORMAÇÕES SOBRE EXPORTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1100'),
        Campo(2, 'IND_DOC'),
        Campo(3, 'NRO_DE'),
        CampoData(4, 'DT_DE'),
        Campo(5, 'NAT_EXP'),
        Campo(6, 'NRO_RE'),
        CampoData(7, 'DT_RE'),
        Campo(8, 'CHC_EMB'),
        CampoData(9, 'DT_CHC'),
        CampoData(10, 'DT_AVB'),
        Campo(11, 'TP_CHC'),
        Campo(12, 'PAIS'),
    ]

    nivel = 2

class Registro1105(Registro):
    """
    DOCUMENTOS FISCAIS DE EXPORTAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1105'),
        Campo(2, 'COD_MOD'),
        Campo(3, 'SERIE'),
        CampoNumerico(4, 'NUM_DOC'),
        CampoChaveEletronica(5, 'CHV_NFE'),
        CampoData(6, 'DT_DOC'),
        Campo(7, 'COD_ITEM'),
    ]

    nivel = 3

class Registro1110(Registro):
    """
    OPERAÇÕES DE EXPORTAÇÃO INDIRETA DE PRODUTOS NÃO INDUSTRIALIZADOS PELO ESTABELECIMENTO EMITENTE
    """
    campos = [
        CampoFixo(1, 'REG', '1110'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'NUM_DOC'),
        CampoData(6, 'DT_DOC'),
        CampoChaveEletronica(7, 'CHV_NFE'),
        Campo(8, 'NR_ MEMO'),
        CampoNumerico(9, 'QTD'),
        Campo(10, 'UNID'),
    ]

    nivel = 4

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

    nivel = 2

class Registro1210(Registro):
    """
    UTILIZAÇÃO DE CRÉDITOS FISCAIS - ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1210'),
        Campo(2, 'TIPO_UTIL'),
        Campo(3, 'NR_DOC'),
    ]

    nivel = 3

class Registro1300(Registro):
    """
    MOVIMENTAÇÃO DIÁRIA DE COMBUSTÍVEIS
    """
    campos = [
        CampoFixo(1, 'REG', '1300'),
        Campo(2, 'COD_ITEM'),
        CampoData(3, 'DT_FECH'),
        Campo(4, 'ESTQ_ABERT'),
        Campo(5, 'VOL_ENTR'),
        Campo(6, 'VOL_DISP'),
        Campo(7, 'VOL_SAIDAS'),
        Campo(8, 'ESTQ_ESCR'),
        Campo(9, 'VAL_AJ_PERDA'),
        Campo(10, 'VAL_AJ_GANHO'),
        Campo(11, 'FECH_FISICO'),
    ]

    nivel = 2

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

    nivel = 3

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
        CampoCNPJ(6, 'CNPJ_INTERV'),
        Campo(7, 'CPF_INTERV'),
        Campo(8, 'VAL_FECHA'),
        Campo(9, 'VAL_ABERT'),
        Campo(10, 'VOL_AFERI'),
        Campo(11, 'VOL_VENDAS'),
    ]

    nivel = 4

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

    nivel = 2

class Registro1360(Registro):
    """
    LACRES DA BOMBA
    """
    campos = [
        CampoFixo(1, 'REG', '1360'),
        Campo(2, 'NUM_LACRE'),
        CampoData(3, 'DT_APLICACAO'),
    ]

    nivel = 3

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

    nivel = 3

class Registro1390(Registro):
    """
    CONTROLE DE PRODUÇÃO DE USINA
    """
    campos = [
        CampoFixo(1, 'REG', '1390'),
        Campo(2, 'COD_PROD'),
    ]

    nivel = 2

class Registro1391(Registro):
    """
    PRODUÇÃO DIÁRIA DA USINA
    """
    campos = [
        CampoFixo(1, 'REG', '1391'),
        CampoData(2, 'DT_REGISTRO'),
        CampoNumerico(3, 'QTD_MOID'),
        Campo(4, 'ESTQ_INI'),
        CampoNumerico(5, 'QTD_PRODUZ'),
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

    nivel = 3

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

    nivel = 2

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
        CampoNumerico(6, 'COD_SIT'),
        Campo(7, 'SER'),
        CampoNumerico(8, 'SUB'),
        Campo(9, 'COD_CONS'),
        CampoNumerico(10, 'NUM_DOC'),
        CampoData(11, 'DT_DOC'),
        CampoData(12, 'DT_E_S'),
        CampoNumerico(13, 'VL_DOC'),
        CampoNumerico(14, 'VL_DESC'),
        CampoNumerico(15, 'VL_FORN'),
        CampoNumerico(16, 'VL_SERV_NT'),
        CampoNumerico(17, 'VL_TERC'),
        CampoNumerico(18, 'VL_DA'),
        CampoNumerico(19, 'VL_BC_ICMS'),
        CampoNumerico(20, 'VL_ICMS'),
        CampoNumerico(21, 'VL_BC_ICMS_ST'),
        CampoNumerico(22, 'VL_ICMS_ST'),
        Campo(23, 'COD_INF'),
        CampoNumerico(24, 'VL_PIS'),
        CampoNumerico(25, 'VL_COFINS'),
        Campo(26, 'TP_LIGACAO'),
        Campo(27, 'COD_GRUPO_TENSAO'),
    ]

    nivel = 2

class Registro1510(Registro):
    """
    ITENS DO DOCUMENTO NOTA FISCAL/CONTA ENERGIA ELÉTRICA (CÓDIGO 06)
    """
    campos = [
        CampoFixo(1, 'REG', '1510'),
        Campo(2, 'NUM_ITEM'),
        Campo(3, 'COD_ITEM'),
        Campo(4, 'COD_CLASS'),
        CampoNumerico(5, 'QTD'),
        Campo(6, 'UNID'),
        CampoNumerico(7, 'VL_ITEM'),
        CampoNumerico(8, 'VL_DESC'),
        CampoNumerico(9, 'CST_ICMS'),
        CampoNumerico(10, 'CFOP'),
        CampoNumerico(11, 'VL_BC_ICMS'),
        CampoNumerico(12, 'ALIQ_ICMS'),
        CampoNumerico(13, 'VL_ICMS'),
        CampoNumerico(14, 'VL_BC_ICMS_ST'),
        CampoNumerico(15, 'ALIQ_ST'),
        CampoNumerico(16, 'VL_ICMS_ST'),
        Campo(17, 'IND_REC'),
        Campo(18, 'COD_PART'),
        CampoNumerico(19, 'VL_PIS'),
        CampoNumerico(20, 'VL_COFINS'),
        Campo(21, 'COD_CTA'),
    ]

    nivel = 3

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

    nivel = 2

class Registro1700(Registro):
    """
    DOCUMENTOS FISCAIS UTILIZADOS
    """
    campos = [
        CampoFixo(1, 'REG', '1700'),
        Campo(2, 'COD_DISP'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC_INI'),
        CampoNumerico(7, 'NUM_DOC_FIN'),
        Campo(8, 'NUM_AUT'),
    ]

    nivel = 2

class Registro1710(Registro):
    """
    DOCUMENTOS FISCAIS CANCELADOS/INUTILIZADOS
    """
    campos = [
        CampoFixo(1, 'REG', '1710'),
        CampoNumerico(2, 'NUM_DOC_INI'),
        CampoNumerico(3, 'NUM_DOC_FIN'),
    ]

    nivel = 3

class Registro1800(Registro):
    """
    DCTA - DEMONSTRATIVO DE CRÉDITO DO ICMS SOBRE TRANSPORTE AÉREO
    """
    campos = [
        CampoFixo(1, 'REG', '1800'),
        CampoNumerico(2, 'VL_CARGA'),
        CampoNumerico(3, 'VL_PASS'),
        CampoNumerico(4, 'VL_FAT'),
        Campo(5, 'IND_RAT'),
        CampoNumerico(6, 'VL_ICMS_ANT'),
        CampoNumerico(7, 'VL_BC_ICMS'),
        CampoNumerico(8, 'VL_ICMS_APUR'),
        CampoNumerico(9, 'VL_BC_ICMS_APUR'),
        CampoNumerico(10, 'VL_DIF'),
    ]

    nivel = 2

class Registro1900(Registro):
    """
    INDICADOR DE SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1900'),
        Campo(2, 'IND_APUR_ICMS'),
        Campo(3, 'DESCR_COMPL_OUT_APUR'),
    ]

    nivel = 2

class Registro1910(Registro):
    """
    PERÍODO DA SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1910'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]

    nivel = 3

class Registro1920(Registro):
    """
    SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1920'),
        CampoNumerico(2, 'VL_TOT_TRANSF_DEBITOS_OA'),
        CampoNumerico(3, 'VL_TOT_AJ_DEBITOS_OA'),
        CampoNumerico(4, 'VL_ESTORNOS_CRED_OA'),
        CampoNumerico(5, 'VL_TOT_TRANSF_CREDITOS_OA'),
        CampoNumerico(6, 'VL_TOT_AJ_CREDITOS_OA'),
        CampoNumerico(7, 'VL_ESTORNOS_DEB_OA'),
        CampoNumerico(8, 'VL_SLD_CREDOR_ANT_OA'),
        CampoNumerico(9, 'VL_SLD_APURADO_OA'),
        CampoNumerico(10, 'VL_TOT_DED'),
        CampoNumerico(11, 'VL_ICMS_RECOLHER_OA'),
        CampoNumerico(12, 'VL_SLD_CREDOR_TRANSP_OA'),
        Campo(13, 'DEB_ESP_OA'),
    ]

    nivel = 4

class Registro1921(Registro):
    """
    AJUSTE/BENEFÍCIO/INCENTIVO DA SUB-APURAÇÃO DO ICMS
    """
    campos = [
        CampoFixo(1, 'REG', '1921'),
        Campo(2, 'COD_AJ_APUR'),
        CampoNumerico(3, 'VL_AJ_APUR'),
    ]

    nivel = 5

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

    nivel = 6

class Registro1923(Registro):
    """
    INFORMAÇÕES ADICIONAIS DOS AJUSTES DA SUB-APURAÇÃO DO ICMS - IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS
    """
    campos = [
        CampoFixo(1, 'REG', '1923'),
        Campo(2, 'COD_PART'),
        Campo(3, 'COD_MOD'),
        Campo(4, 'SER'),
        CampoNumerico(5, 'SUB'),
        CampoNumerico(6, 'NUM_DOC'),
        CampoData(7, 'DT_DOC'),
        Campo(8, 'COD_ITEM'),
        CampoNumerico(9, 'VL_AJ_ITEM'),
    ]

    nivel = 6

class Registro1925(Registro):
    """
    INFORMAÇÕES ADICIONAIS DA SUB-APURAÇÃO - VALORES DECLARATÓRIOS
    """
    campos = [
        CampoFixo(1, 'REG', '1925'),
        Campo(2, 'COD_INF_ADIC'),
        CampoNumerico(3, 'VL_INF_ADIC'),
        Campo(4, 'DESCR_COMPL_AJ'),
    ]

    nivel = 5

class Registro1926(Registro):
    """
    OBRIGAÇÕES DO ICMS A RECOLHER - OPERAÇÕES REFERENTES À SUB-APURAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', '1926'),
        Campo(2, 'COD_OR'),
        CampoNumerico(3, 'VL_OR'),
        CampoData(4, 'DT_VCTO'),
        Campo(5, 'COD_REC'),
        Campo(6, 'NUM_PROC'),
        Campo(7, 'IND_PROC'),
        Campo(8, 'PROC'),
        Campo(9, 'TXT_COMPL'),
        Campo(10, 'MES_REF'),
    ]

    nivel = 5

class Registro1960(Registro):
    """
    GIAF 1 - GUIA DE INFORMAÇÃO E APURAÇÃO DE INCENTIVOS
    FISCAIS E FINANCEIROS: INDÚSTRIA (CRÉDITO PRESUMIDO)
    """
    campos = [
        CampoFixo(1, 'REG', '1960'),
        Campo(2, 'IND_AP'),
        CampoNumerico(3, 'G1_01'),
        CampoNumerico(4, 'G1_02'),
        CampoNumerico(5, 'G1_03'),
        CampoNumerico(6, 'G1_04'),
        CampoNumerico(7, 'G1_05'),
        CampoNumerico(8, 'G1_06'),
        CampoNumerico(9, 'G1_07'),
        CampoNumerico(10, 'G1_08'),
        CampoNumerico(11, 'G1_09'),
        CampoNumerico(12, 'G1_10'),
        CampoNumerico(13, 'G1_11'),
    ]

    nivel = 2

class Registro1970(Registro):
    """
    GIAF 3 - GUIA DE INFORMAÇÃO E APURAÇÃO DE INCENTIVOS
    FISCAIS E FINANCEIROS: IMPORTAÇÃO (DIFERIMENTO NA ENTRADA E CRÉDITO
    PRESUMIDO NA SAÍDA SUBSEQUENTE
    """
    campos = [
        CampoFixo(1, 'REG', '1970'),
        Campo(2, 'IND_AP'),
        CampoNumerico(3, 'G3_01'),
        CampoNumerico(4, 'G3_02'),
        CampoNumerico(5, 'G3_03'),
        CampoNumerico(6, 'G3_04'),
        CampoNumerico(7, 'G3_05'),
        CampoNumerico(8, 'G3_06'),
        CampoNumerico(9, 'G3_07'),
        CampoNumerico(10, 'G3_T'),
        CampoNumerico(11, 'G3_08'),
        CampoNumerico(12, 'G3_09'),
    ]

    nivel = 2

class Registro1975(Registro):
    """
    GIAF 3 - GUIA DE INFORMAÇÃO E APURAÇÃO DE INCENTIVOS
    FISCAIS E FINANCEIROS: IMPORTAÇÃO (SAÍDAS INTERNAS POR FAIXA DE
    ALÍQUOTA)
    """
    campos = [
        CampoFixo(1, 'REG', '1975'),
        CampoNumerico(2, 'ALIQ_IMP_BASE'),
        CampoNumerico(3, 'G3_10'),
        CampoNumerico(4, 'G3_11'),
        CampoNumerico(5, 'G3_12'),
    ]

    nivel = 3

class Registro1980(Registro):
    """
    GIAF 4 GUIA DE INFORMAÇÃO E APURAÇÃO DE INCENTIVOS
    FISCAIS E FINANCEIROS: CENTRAL DE DISTRIBUIÇÃO (ENTRADAS/SAÍDAS
    """
    campos = [
        CampoFixo(1, 'REG', '1980'),
        CampoNumerico(2, 'IND_AP'),
        CampoNumerico(3, 'G4_01'),
        CampoNumerico(4, 'G4_02'),
        CampoNumerico(5, 'G4_03'),
        CampoNumerico(6, 'G4_04'),
        CampoNumerico(7, 'G4_05'),
        CampoNumerico(8, 'G4_06'),
        CampoNumerico(9, 'G4_07'),
        CampoNumerico(10, 'G4_08'),
        CampoNumerico(11, 'G4_09'),
        CampoNumerico(12, 'G4_10'),
        CampoNumerico(13, 'G4_11'),
        CampoNumerico(14, 'G4_12'),
    ]

    nivel = 2

class Registro1990(Registro):
    """
    ENCERRAMENTO DO BLOCO 1
    """
    campos = [
        CampoFixo(1, 'REG', '1990'),
        CampoNumerico(2, 'QTD_LIN_1'),
    ]

    nivel = 1

class Registro9001(Registro):
    """
    ABERTURA DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9001'),
        Campo(2, 'IND_MOV'),
    ]

    nivel = 1

class Registro9900(Registro):
    """
    REGISTROS DO ARQUIVO
    """
    campos = [
        CampoFixo(1, 'REG', '9900'),
        Campo(2, 'REG_BLC'),
        CampoNumerico(3, 'QTD_REG_BLC'),
    ]

    nivel = 2

class Registro9990(Registro):
    """
    ENCERRAMENTO DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9990'),
        CampoNumerico(2, 'QTD_LIN_9'),
    ]

    nivel = 1

class Registro9999(Registro):
    """
    ENCERRAMENTO DO ARQUIVO DIGITAL
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        CampoNumerico(2, 'QTD_LIN'),
    ]

    nivel = 0

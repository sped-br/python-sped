# -*- coding: utf-8 -*-

from ..registros import Registro
from ..campos import Campo
from ..campos import CampoData
from ..campos import CampoFixo
from ..campos import CampoNumerico
from ..campos import CampoAlfanumerico


class Registro0000(Registro):
    """
    ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO EMPRESÁRIO OU DA SOCIEDADE EMPRESÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoFixo(2, 'LECD', 'LECD'),
        CampoData(3, 'DT_INI'),
        CampoData(4, 'DT_FIN'),
        Campo(5, 'NOME'),
        Campo(6, 'CNPJ'),
        Campo(7, 'UF'),
        Campo(8, 'IE'),
        CampoNumerico(9, 'COD_MUN'),
        Campo(10, 'IM'),
        Campo(11, 'IND_SIT_ESP'),
        Campo(12, 'IND_SIT_INI_PER'),
        Campo(13, 'IND_NIRE'),
        Campo(14, 'IND_FIN_ESC'),
        Campo(15, 'COD_HASH_SUB'),
        Campo(16, 'NIRE_SUBST'),
        Campo(17, 'IND_GRANDE_PORTE'),
        Campo(18, 'TIP_ECD'),
        Campo(19, 'COD_SCP'),
    ]


class Registro0001(Registro):
    """
    ABERTURA DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0001'),
        Campo(2, 'IND_DAD'),
    ]


class Registro0007(Registro):
    """
    OUTRAS INSCRIÇÕES CADASTRAIS DO EMPRESÁRIO OU SOCIEDADE EMPRESÁRIA
    """
    campos = [
        CampoFixo(1, 'REG', '0007'),
        Campo(2, 'COD_ENT_REF'),
        Campo(3, 'COD_INSCR'),
    ]


class Registro0020(Registro):
    """
    ESCRITURAÇÃO CONTÁBIL DESCENTRALIZADA
    """
    campos = [
        CampoFixo(1, 'REG', '0020'),
        Campo(2, 'IND_DEC'),
        Campo(3, 'CNPJ'),
        Campo(4, 'UF'),
        Campo(5, 'IE'),
        Campo(6, 'COD_MUN'),
        Campo(7, 'IM'),
        Campo(8, 'NIRE'),
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
        Campo(7, 'NIT'),
        Campo(8, 'UF'),
        Campo(9, 'IE'),
        Campo(10, 'IE_ST'),
        Campo(11, 'COD_MUN'),
        Campo(12, 'IM'),
        Campo(13, 'SUFRAMA'),
    ]


class Registro0180(Registro):
    """
    IDENTIFICAÇÃO DO RELACIONAMENTO COM O PARTICIPANTE
    """
    campos = [
        CampoFixo(1, 'REG', '0180'),
        Campo(2, 'COD_REL'),
        CampoData(3, 'DT_INI_REL'),
        CampoData(4, 'DT_FIN_REL'),
    ]


class Registro0990(Registro):
    """
    ENCERRAMENTO DO BLOCO 0
    """
    campos = [
        CampoFixo(1, 'REG', '0990'),
        CampoNumerico(2, 'QTD_LIN_0'),
    ]


class RegistroI001(Registro):
    """
    ABERTURA DO BLOCO I
    """
    campos = [
        CampoFixo(1, 'REG', 'I001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroI010(Registro):
    """
    IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL
    """
    campos = [
        CampoFixo(1, 'REG', 'I010'),
        Campo(2, 'IND_ESC'),
        Campo(3, 'COD_VER_LC'),
    ]


class RegistroI012(Registro):
    """
    LIVROS AUXILIARES AO DIÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'I012'),
        Campo(2, 'NUM_ORD'),
        Campo(3, 'NAT_LIVR'),
        Campo(4, 'TIPO'),
        Campo(5, 'COD_HASH_AUX'),
    ]


class RegistroI015(Registro):
    """
    IDENTIFICAÇÃO DAS CONTAS DA ESCRITURAÇÃO RESUMIDA A QUE SE REFERE A ESCRITURAÇÃO AUXILIAR
    """
    campos = [
        CampoFixo(1, 'REG', 'I015'),
        Campo(2, 'COD_CTA_RES'),
    ]


class RegistroI020(Registro):
    """
    CAMPOS ADICIONAIS
    """
    campos = [
        CampoFixo(1, 'REG', 'I020'),
        Campo(2, 'REG_COD'),
        Campo(3, 'NUM_AD'),
        Campo(4, 'CAMPO'),
        Campo(5, 'DESCRICAO'),
        Campo(6, 'TIPO'),
    ]


class RegistroI030(Registro):
    """
    TERMO DE ABERTURA DO LIVRO
    """
    campos = [
        CampoFixo(1, 'REG', 'I030'),
        Campo(2, 'DNRC_ABERT'),
        CampoNumerico(3, 'NUM_ORD'),
        Campo(4, 'NAT_LIVR'),
        CampoNumerico(5, 'QTD_LIN'),
        Campo(6, 'NOME'),
        Campo(7, 'NIRE'),
        Campo(8, 'CNPJ'),
        CampoData(9, 'DT_ARQ'),
        CampoData(10, 'DT_ARQ_CONV'),
        Campo(11, 'DESC_MUN'),
        CampoData(12, 'DT_EX_SOCIAL'),
    ]


class RegistroI050(Registro):
    """
    PLANO DE CONTAS
    """
    campos = [
        CampoFixo(1, 'REG', 'I050'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_NAT'),
        Campo(4, 'IND_CTA'),
        CampoNumerico(5, 'NIVEL'),
        Campo(6, 'COD_CTA'),
        Campo(7, 'COD_CTA_SUP'),
        Campo(8, 'CTA'),
    ]


class RegistroI051(Registro):
    """
    PLANO DE CONTAS REFERENCIAL
    """
    campos = [
        CampoFixo(1, 'REG', 'I051'),
        Campo(2, 'COD_ENT_REF'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'COD_CTA_REF'),
    ]


class RegistroI052(Registro):
    """
    INDICAÇÃO DOS CÓDIGOS DE AGLUTINAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', 'I052'),
        Campo(2, 'COD_CCUS'),
        Campo(3, 'COD_AGL'),
    ]


class RegistroI075(Registro):
    """
    TABELA DE HISTÓRICO PADRONIZADO
    """
    campos = [
        CampoFixo(1, 'REG', 'I075'),
        Campo(2, 'COD_HIST'),
        Campo(3, 'DESCR_HIST'),
    ]


class RegistroI100(Registro):
    """
    CENTRO DE CUSTOS
    """
    campos = [
        CampoFixo(1, 'REG', 'I100'),
        CampoData(2, 'DT_ALT'),
        Campo(3, 'COD_CCUS'),
        Campo(4, 'CCUS'),
    ]


class RegistroI150(Registro):
    """
    SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO
    """
    campos = [
        CampoFixo(1, 'REG', 'I150'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
    ]


class RegistroI155(Registro):
    """
    DETALHE DOS SALDOS PERIÓDICOS
    """
    campos = [
        CampoFixo(1, 'REG', 'I155'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_SLD_INI', precisao=2),
        Campo(5, 'IND_DC_INI'),
        CampoNumerico(6, 'VL_DEB', precisao=2),
        CampoNumerico(7, 'VL_CRED', precisao=2),
        CampoNumerico(8, 'VL_SLD_FIN', precisao=2),
        Campo(9, 'IND_DC_FIN'),
    ]


class RegistroI200(Registro):
    """
    LANÇAMENTO CONTÁBIL
    """
    campos = [
        CampoFixo(1, 'REG', 'I200'),
        Campo(2, 'NUM_LCTO'),
        CampoData(3, 'DT_LCTO'),
        CampoNumerico(4, 'VL_LCTO', precisao=2),
        Campo(5, 'IND_LCTO'),
    ]


class RegistroI250(Registro):
    """
    PARTIDAS DO LANÇAMENTO
    """
    campos = [
        CampoFixo(1, 'REG', 'I250'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_DC', precisao=2),
        Campo(5, 'IND_DC'),
        Campo(6, 'NUM_ARQ'),
        Campo(7, 'COD_HIST_PAD'),
        Campo(8, 'HIST'),
        Campo(9, 'COD_PART'),
    ]


class RegistroI300(Registro):
    """
    BALANCETES DIÁRIOS – IDENTIFICAÇÃO DA DATA
    """
    campos = [
        CampoFixo(1, 'REG', 'I300'),
        CampoData(2, 'DT_BCTE'),
    ]


class RegistroI310(Registro):
    """
    DETALHES DO BALANCETE DIÁRIO
    """
    campos = [
        CampoFixo(1, 'REG', 'I310'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VAL_DEBD', precisao=2),
        CampoNumerico(5, 'VAL_CREDD', precisao=2),
    ]


class RegistroI350(Registro):
    """
    SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO - IDENTIFICAÇÃO DA DATA
    """
    campos = [
        CampoFixo(1, 'REG', 'I350'),
        CampoData(2, 'DT_RES'),
    ]


class RegistroI355(Registro):
    """
    DETALHES DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO
    """
    campos = [
        CampoFixo(1, 'REG', 'I355'),
        Campo(2, 'COD_CTA'),
        Campo(3, 'COD_CCUS'),
        CampoNumerico(4, 'VL_CTA', precisao=2),
        Campo(5, 'IND_DC'),
    ]


class RegistroI500(Registro):
    """
    PARÂMETROS DE IMPRESSÃO E VISUALIZAÇÃO DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL
    """
    campos = [
        CampoFixo(1, 'REG', 'I500'),
        Campo(2, 'TAM_FONTE'),
    ]


class RegistroI510(Registro):
    """
    DEFINIÇÃO DE CAMPOS DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL
    """
    campos = [
        CampoFixo(1, 'REG', 'I510'),
        Campo(2, 'NM_CAMPO'),
        Campo(3, 'DESC_CAMPO'),
        Campo(4, 'TIPO_CAMPO'),
        Campo(5, 'TAM_CAMPO'),
        Campo(6, 'DEC_CAMPO'),
        Campo(7, 'COL_CAMPO'),
    ]


class RegistroI550(Registro):
    """
    DETALHES DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL
    """
    campos = [
        CampoFixo(1, 'REG', 'I550'),
        Campo(2, 'RZ_CONT'),
    ]


class RegistroI555(Registro):
    """
    TOTAIS NO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL
    """
    campos = [
        CampoFixo(1, 'REG', 'I555'),
        Campo(2, 'RZ_CONT_TOT'),
    ]


class RegistroI990(Registro):
    """
    ENCERRAMENTO DO BLOCO I
    """
    campos = [
        CampoFixo(1, 'REG', 'I990'),
        CampoNumerico(2, 'QTD_LIN_I'),
    ]


class RegistroJ001(Registro):
    """
    ABERTURA DO BLOCO J
    """
    campos = [
        CampoFixo(1, 'REG', 'J001'),
        Campo(2, 'IND_DAD'),
    ]


class RegistroJ005(Registro):
    """
    DEMONSTRAÇÕES CONTÁBEIS
    """
    campos = [
        CampoFixo(1, 'REG', 'J005'),
        CampoData(2, 'DT_INI'),
        CampoData(3, 'DT_FIN'),
        CampoNumerico(4, 'ID_DEM'),
        Campo(5, 'CAB_DEM'),
    ]


class RegistroJ100(Registro):
    """
    BALANÇO PATRIMONIAL
    """
    campos = [
        CampoFixo(1, 'REG', 'J100'),
        Campo(2, 'COD_AGL'),
        CampoNumerico(3, 'NIVEL_AGL'),
        Campo(4, 'IND_GRP_BAL'),
        Campo(5, 'DESCR_COD_AGL'),
        CampoNumerico(6, 'VL_CTA', precisao=2),
        Campo(7, 'IND_DC_BAL'),
        CampoNumerico(8, 'VL_CTA_INI', precisao=2),
        Campo(9, 'IND_DC_BAL_INI'),
    ]


class RegistroJ150(Registro):
    """
    DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO
    """
    campos = [
        CampoFixo(1, 'REG', 'J150'),
        Campo(2, 'COD_AGL'),
        CampoNumerico(3, 'NIVEL_AGL'),
        Campo(4, 'DESCR_COD_AGL'),
        CampoNumerico(5, 'VL_CTA', precisao=2),
        Campo(6, 'IND_VL'),
    ]


class RegistroJ800(Registro):
    """
    OUTRAS INFORMAÇÕES
    """
    campos = [
        CampoFixo(1, 'REG', 'J800'),
        Campo(2, 'ARQ_RTF'),
        Campo(3, 'IND_FIM_RTF'),
    ]


class RegistroJ900(Registro):
    """
    TERMO DE ENCERRAMENTO
    """
    campos = [
        CampoFixo(1, 'REG', 'J900'),
        Campo(2, 'DNRC_ENCER'),
        CampoNumerico(3, 'NUM_ORD'),
        Campo(4, 'NAT_LIVRO'),
        Campo(5, 'NOME'),
        CampoNumerico(6, 'QTD_LIN'),
        CampoData(7, 'DT_INI_ESCR'),
        CampoData(8, 'DT_FIN_ESCR'),
    ]


class RegistroJ930(Registro):
    """
    IDENTIFICAÇÃO DOS SIGNATÁRIOS DA ESCRITURAÇÃO
    """
    campos = [
        CampoFixo(1, 'REG', 'J930'),
        CampoAlfanumerico(2, 'IDENT_NOM'),
        CampoAlfanumerico(3, 'IDENT_CPF', tamanho=11),
        CampoAlfanumerico(4, 'IDENT_QUALIF'),
        CampoAlfanumerico(5, 'COD_ASSIN', tamanho=3),
        CampoAlfanumerico(6, 'IND_CRC'),
        CampoAlfanumerico(7, 'EMAIL'),
        CampoAlfanumerico(8, 'FONE'),
        CampoAlfanumerico(9, 'UF_CRC'),
        CampoAlfanumerico(10, 'NUM_SEQ_CRC'),
        CampoData(11, 'DT_CRC')
    ]


class RegistroJ990(Registro):
    """
    ENCERRAMENTO DO BLOCO J
    """
    campos = [
        CampoFixo(1, 'REG', 'J990'),
        CampoNumerico(2, 'QTD_LIN_J'),
    ]


class Registro9001(Registro):
    """
    ABERTURA DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9001'),
        Campo(2, 'IND_DAD'),
    ]


class Registro9900(Registro):
    """
    REGISTROS DO ARQUIVO
    """
    campos = [
        CampoFixo(1, 'REG', '9900'),
        Campo(2, 'REG_BLC'),
        CampoNumerico(3, 'QTD_REG_BLC'),
    ]


class Registro9990(Registro):
    """
    ENCERRAMENTO DO BLOCO 9
    """
    campos = [
        CampoFixo(1, 'REG', '9990'),
        CampoNumerico(2, 'QTD_LIN_9'),
    ]


class Registro9999(Registro):
    """
    ENCERRAMENTO DO ARQUIVO DIGITAL
    """
    campos = [
        CampoFixo(1, 'REG', '9999'),
        CampoNumerico(2, 'QTD_LIN'),
    ]

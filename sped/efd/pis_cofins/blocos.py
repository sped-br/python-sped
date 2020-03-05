# -*- coding: utf-8 -*-

from ...blocos import Bloco
from .registros import Registro0001
from .registros import Registro0990
from .registros import Registro1001
from .registros import Registro1990
from .registros import Registro9001
from .registros import Registro9990
from .registros import RegistroA001
from .registros import RegistroA990
from .registros import RegistroC001
from .registros import RegistroC990
from .registros import RegistroD001
from .registros import RegistroD990
from .registros import RegistroF001
from .registros import RegistroF990
from .registros import RegistroI001
from .registros import RegistroI990
from .registros import RegistroM001
from .registros import RegistroM990
from .registros import RegistroP001
from .registros import RegistroP990


class Bloco0(Bloco):
    """
    Abertura, Identificação e Referências
    """
    registro_abertura = Registro0001()
    registro_encerramento = Registro0990()


class BlocoA(Bloco):
    """
    Documentos Fiscais - Serviços (ISS)
    """
    registro_abertura = RegistroA001()
    registro_encerramento = RegistroA990()


class BlocoC(Bloco):
    """
    Documentos Fiscais I – Mercadorias (ICMS/IPI)
    """
    registro_abertura = RegistroC001()
    registro_encerramento = RegistroC990()


class BlocoD(Bloco):
    """
    Documentos Fiscais II – Serviços (ICMS)
    """
    registro_abertura = RegistroD001()
    registro_encerramento = RegistroD990()


class BlocoF(Bloco):
    """
    Demais Documentos e Operações
    """
    registro_abertura = RegistroF001()
    registro_encerramento = RegistroF990()


class BlocoI(Bloco):
    """
    Operações das Instituições Financeiras e Assemelhadas, Seguradoras, Entidades de Previdência Privada e Operadoras de Planos de Assistência à Saúde (*)
    """
    registro_abertura = RegistroI001()
    registro_encerramento = RegistroI990()


class BlocoM(Bloco):
    """
    Apuração da Contribuição e Crédito de PIS/PASEP e da COFINS
    """
    registro_abertura = RegistroM001()
    registro_encerramento = RegistroM990()


class BlocoP(Bloco):
    """
    Apuração da Contribuição Previdenciária sobre a Receita Bruta
    """
    registro_abertura = RegistroP001()
    registro_encerramento = RegistroP990()


class Bloco1(Bloco):
    """
    Complemento da Escrituração – Controle de Saldos de Créditos e de  Retenções, Operações Extemporâneas e Outras Informações
    """
    registro_abertura = Registro1001()
    registro_encerramento = Registro1990()


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro0001()
    registro_encerramento = Registro0990()

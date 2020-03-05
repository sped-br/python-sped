# -*- coding: utf-8 -*-

from ...blocos import Bloco
from .registros import Registro0001
from .registros import Registro0990
from .registros import RegistroB001
from .registros import RegistroB990
from .registros import RegistroC001
from .registros import RegistroC990
from .registros import RegistroD001
from .registros import RegistroD990
from .registros import RegistroE001
from .registros import RegistroE990
from .registros import RegistroG001
from .registros import RegistroG990
from .registros import RegistroH001
from .registros import RegistroH990
from .registros import RegistroK001
from .registros import RegistroK990
from .registros import Registro1001
from .registros import Registro1990
from .registros import Registro9001
from .registros import Registro9990


class Bloco0(Bloco):
    """
    Abertura, Identificação e Referências
    """
    registro_abertura = Registro0001()
    registro_encerramento = Registro0990()

    @property
    def fechamento(self):
        registro = self.__class__.registro_encerramento()
        # Define a quantidade de registros
        registro[2] = len(self._registros) + 3
        return registro


class BlocoB(Bloco):
    """
    Apuração de ISS – Mercadorias (ICMS/IPI)
    """
    registro_abertura = RegistroB001()
    registro_encerramento = RegistroB990()


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


class BlocoE(Bloco):
    """
    Apuração do ICMS e do IPI
    """
    registro_abertura = RegistroE001()
    registro_encerramento = RegistroE990()


class BlocoG(Bloco):
    """
    Controle do Crédito de ICMS do Ativo Permanente – CIAP
    """
    registro_abertura = RegistroG001()
    registro_encerramento = RegistroG990()


class BlocoH(Bloco):
    """
    Inventário Físico
    """
    registro_abertura = RegistroH001()
    registro_encerramento = RegistroH990()


class BlocoK(Bloco):
    """
    Controle da Produção e do Estoque
    """
    registro_abertura = RegistroK001()
    registro_encerramento = RegistroK990()


class Bloco1(Bloco):
    """
    Outras Informações
    """
    registro_abertura = Registro1001()
    registro_encerramento = Registro1990()


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001()
    registro_encerramento = Registro9990()

    @property
    def fechamento(self):
        registro = self.__class__.registro_encerramento()
        # Define a quantidade de registros
        registro[2] = len(self._registros) + 3
        return registro

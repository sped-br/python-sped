# -*- coding: utf-8 -*-

from ..blocos import Bloco
from .registros import Registro0001
from .registros import Registro0990
from .registros import RegistroC001
from .registros import RegistroC990
from .registros import RegistroE001
from .registros import RegistroE990
from .registros import RegistroJ001
from .registros import RegistroJ990
from .registros import RegistroK001
from .registros import RegistroK990
from .registros import RegistroL001
from .registros import RegistroL990
from .registros import RegistroM001
from .registros import RegistroM990
from .registros import RegistroN001
from .registros import RegistroN990
from .registros import RegistroP001
from .registros import RegistroP990
from .registros import RegistroQ001
from .registros import RegistroQ990
from .registros import RegistroT001
from .registros import RegistroT990
from .registros import RegistroU001
from .registros import RegistroU990
from .registros import RegistroX001
from .registros import RegistroX990
from .registros import RegistroY001
from .registros import RegistroY990
from .registros import Registro9001
from .registros import Registro9099


class Bloco0(Bloco):
    """
    Abertura e Identificação
    """
    registro_abertura = Registro0001
    registro_encerramento = Registro0990

    @property
    def fechamento(self):
        registro = Bloco.fechamento.fget(self)
        registro[2] += 1
        return registro


class BlocoC(Bloco):
    """
    Informações Recuperadas das ECD (bloco recuperado pelo sistema – não é importado)
    """
    registro_abertura = RegistroC001
    registro_encerramento = RegistroC990


class BlocoE(Bloco):
    """
    Informações Recuperadas da ECF Anterior e Cálculo Fiscal dos Dados Recuperados da ECD (Bloco recuperado pelo sistema – não é importado)
    """
    registro_abertura = RegistroE001
    registro_encerramento = RegistroE990


class BlocoJ(Bloco):
    """
    Plano de Contas e Mapeamento
    """
    registro_abertura = RegistroJ001
    registro_encerramento = RegistroJ990


class BlocoK(Bloco):
    """
    Saldos das Contas Contábeis e Referenciais
    """
    registro_abertura = RegistroK001
    registro_encerramento = RegistroK990


class BlocoL(Bloco):
    """
    Lucro Líquido
    """
    registro_abertura = RegistroL001
    registro_encerramento = RegistroL990


class BlocoM(Bloco):
    """
    e-LALUR e e-LACS
    """
    registro_abertura = RegistroM001
    registro_encerramento = RegistroM990


class BlocoN(Bloco):
    """
    Imposto de Renda e Contribuição Social (Lucro Real)
    """
    registro_abertura = RegistroN001
    registro_encerramento = RegistroN990


class BlocoP(Bloco):
    """
    Lucro Presumido
    """
    registro_abertura = RegistroP001
    registro_encerramento = RegistroP990


class BlocoQ(Bloco):
    """
    Livro Caixa
    """
    registro_abertura = RegistroQ001
    registro_encerramento = RegistroQ990


class BlocoT(Bloco):
    """
    Lucro Arbitrado
    """
    registro_abertura = RegistroT001
    registro_encerramento = RegistroT990


class BlocoU(Bloco):
    """
    Imunes ou Isentas
    """
    registro_abertura = RegistroU001
    registro_encerramento = RegistroU990


class BlocoX(Bloco):
    """
    Informações Econômicas
    """
    registro_abertura = RegistroX001
    registro_encerramento = RegistroX990


class BlocoY(Bloco):
    """
    Informações Gerais
    """
    registro_abertura = RegistroY001
    registro_encerramento = RegistroY990


class Bloco9(Bloco):
    """
    Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001
    registro_encerramento = Registro9099

    @property
    def fechamento(self):
        registro = super(Bloco9, self).fechamento
        registro[2] += 1
        return registro

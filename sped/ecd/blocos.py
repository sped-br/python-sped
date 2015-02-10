from ..blocos import Bloco
from .registros import Registro0001
from .registros import Registro0990
from .registros import Registro9001
from .registros import Registro9990


class Bloco0(Bloco):
    """
    Abertura, Identificação e Referências
    """
    registro_abertura = Registro0001
    registro_fechamento = Registro0990


class Bloco9(Bloco):
    """
    Controle e Encerramento do Arquivo Digital
    """
    registro_abertura = Registro9001
    registro_fechamento = Registro9990

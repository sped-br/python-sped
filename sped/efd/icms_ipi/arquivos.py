from ...arquivos import ArquivoDigital
from . import blocos
from . import registros
from .registros import Registro0000
from .registros import Registro9999


class ArquivoDigital(ArquivoDigital):
    registro_abertura = Registro0000
    registro_fechamento = Registro9999
    registros = registros
    blocos = blocos

    def __init__(self):
        super().__init__()

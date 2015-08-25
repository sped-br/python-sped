# -*- coding: utf-8 -*-


class RegistroError(Exception):
    def __init__(self, registro):
        self._registro = registro

    def __str__(self):
        return u'{0}'.format(self._registro)


class CampoError(RegistroError):
    def __init__(self, registro, campo):
        super(CampoError, self).__init__(registro)
        self._campo = campo

    def __str__(self):
        return u'{0} -> {1}'.format(self._registro.__class__.__name__, self._campo)


class CampoFixoError(CampoError):
    pass


class CampoInexistenteError(CampoError):
    pass


class CampoObrigatorioError(CampoError):
    pass


class FormatoInvalidoError(CampoError):
    pass


class UseValorError(CampoError):
    pass

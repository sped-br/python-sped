# -*- coding: utf-8 -*-

import os
import re

import sys

__all__ = ['PLANO_REFERENCIAL_PJ_RESUMIDO']

if sys.version_info[0] > 2:
    # py3k
    pass
else:
    # py2
    import codecs
    import warnings

    def open(file, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True, opener=None):
        if newline is not None:
            warnings.warn('newline is not supported in py2')
        if not closefd:
            warnings.warn('closefd is not supported in py2')
        if opener is not None:
            warnings.warn('opener is not supported in py2')
        return codecs.open(filename=file, mode=mode, encoding=encoding,
                    errors=errors, buffering=buffering)

PLANO_REFERENCIAL_PJ_RESUMIDO = []

path_tabelas = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tabelas')
# tabela = 'SPEDCONTABIL_DINAMICO_2014$SPEDECF_DINAMICA_P100$12$389'
tabela = 'SPEDCONTABIL_DINAMICO_2014$SPEDECF_DINAMICA_P150$3$398'
path_tabela = os.path.join(path_tabelas, tabela)

def carregar_tabela(caminho_tabela, encoding='cp1252'):
    with open(caminho_tabela, 'r', encoding=encoding) as file:
        header = re.match('versão=(?P<version>\\d+) (?P<columns>.+)$', file.readline())
        version = header.groupdict()['version']
        columns = header.groupdict()['columns'].split(', ')

        return [dict(zip(columns, line.split('|'))) for line in file.readlines()]

if not PLANO_REFERENCIAL_PJ_RESUMIDO:
    pj1 = carregar_tabela(os.path.join(path_tabelas, 'SPEDCONTABIL_DINAMICO_2014$SPEDECF_DINAMICA_P100$12$389'))
    pj2 = carregar_tabela(os.path.join(path_tabelas, 'SPEDCONTABIL_DINAMICO_2014$SPEDECF_DINAMICA_P150$3$398'))
    PLANO_REFERENCIAL_PJ_RESUMIDO = pj1 + pj2

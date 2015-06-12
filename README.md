# SPED para python

[![Build Status](https://travis-ci.org/sped-br/python-sped.svg "Build Status")](https://travis-ci.org/sped-br/python-sped)
[![Coverage Status](https://coveralls.io/repos/sped-br/python-sped/badge.svg)](https://coveralls.io/r/sped-br/python-sped)
[![Stories in Ready](https://badge.waffle.io/sped-br/python-sped.svg?label=ready&title=Ready)](http://waffle.io/sped-br/python-sped)
[![Supported Python versions](https://shields.io/py_versions/sped/badge.svg)](https://pypi.python.org/pypi/sped/)

Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python 3.4+.

> This software is coded and documented in portuguese only as it is intended to be used to generate the necessary files for the brazilian government regarding to digital bookkeeping.

## Requisitos

 * python 3.4+

## Como instalar

    $ pip install sped

## Objetivos do Projeto

A ideia inicial do projeto e unificar em uma única biblioteca módulos para facilitar a geração dos arquivos do SPED, diminuido o retrabalho necessário para isso e tentando ao máximo garantir que o arquivo gerado seja considerado válido pelo validador do SPED.

Não é objetivo deste projeto, remover a necessidade do programador em conhecer o SPED, bem como sua legislação e saber informar adequadamente todas as informações corretamente.

## Compatibilidade do Projeto

O projeto inicialmente suportará apenas Python 3.4+, devido a minha necessidade de integra-lo ao meu sistema ERP. Em breve e se houver tempo e necessidade, poderei auxiliar a portabilidade para Python 2.7 para facilitar seu uso no OpenERP. Pull requests que adicionem compatibilidade são bem vindos.

Outras linguagens de programação poderão ter versões especificas conforme minha disponibilidade de tempo.

## Contribuições para o Projeto

Contribuições são bem vindas ao projeto, exemplos de como você pode contribuir:
 * usando o projeto e [apontando bugs](https://github.com/sped-br/python-sped/issues)
 * [sugestões de melhoria](https://github.com/sped-br/python-sped/issues)
 * enviando [pull requests](https://github.com/sped-br/python-sped/pulls)
 * auxiliando na [documentação](https://github.com/sped-br/python-sped/wiki)

## Status do Projeto

O projeto está em fase inicial de desenvolvimento e **não deve** ser usado em produção.

| Módulo         |     Status    |
|----------------|:-------------:|
| ECD            |   Funcional   |
| ECF            |   Funcional   |
| EFD-PIS/COFINS |   Funcional   |
| EFD-ICMS/IPI   |   Funcional   |

### ECD

Este módulo está funcional, com todos seus registros codificados, porém muitos campos ainda não possuem uma validação
adequada, consultado tabelas externas por exemplo, ou validando corretamente todos os tamanhos de campos.

Ele pode ser usado para gerar um arquivo digital, com validações de abertura e fechamento de bloco automaticamente.

### ECF

Este módulo está funcional, com todos seus registros codificados, porém muitos campos ainda não possuem uma validação
adequada, consultado tabelas externas por exemplo, ou validando corretamente todos os tamanhos de campos.

Ele pode ser usado para gerar um arquivo digital, com validações de abertura e fechamento de bloco automaticamente.

### EFD-ICMS/IPI

Este módulo está funcional, com todos seus registros codificados, porém muitos campos ainda não possuem uma validação
adequada, consultado tabelas externas por exemplo, ou validando corretamente todos os tamanhos de campos.

Ele pode ser usado para gerar um arquivo digital, com validações de abertura e fechamento de bloco automaticamente.

### EFD-PIS/COFINS

Este módulo está funcional, com todos seus registros codificados, porém muitos campos ainda não possuem uma validação
adequada, consultado tabelas externas por exemplo, ou validando corretamente todos os tamanhos de campos.

Ele pode ser usado para gerar um arquivo digital, com validações de abertura e fechamento de bloco automaticamente.

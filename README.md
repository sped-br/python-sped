# SPED para python

[![Build Status](https://travis-ci.org/Trust-Code/python-sped.svg?branch=11.0)](https://travis-ci.org/Trust-Code/python-sped)
[![Coverage Status](https://coveralls.io/repos/github/Trust-Code/python-sped/badge.svg?branch=11.0)](https://coveralls.io/github/Trust-Code/python-sped?branch=11.0)

Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.

> This software is coded and documented in portuguese only as it is intended to be used to generate the necessary files for the brazilian government regarding to digital bookkeeping.

## Requisitos

  * python
  * six

## Como instalar

    $ pip install python-sped

## Objetivos do Projeto

A ideia inicial do projeto e unificar em uma única biblioteca módulos para facilitar a geração dos arquivos do SPED, diminuido o retrabalho necessário para isso e tentando ao máximo garantir que o arquivo gerado seja considerado válido pelo validador do SPED.

Não é objetivo deste projeto, remover a necessidade do programador em conhecer o SPED, bem como sua legislação e saber informar adequadamente todas as informações corretamente.

## Compatibilidade do Projeto

O projeto inicialmente suportará apenas Python 3.4+, o suporte para Python 2.7 está em desenvolvimento. Pull requests que melhorem a compatibilidade são bem vindos.

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
| FCI            |   Funcional   |

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

### FCI

Este módulo está funcional, com todos seus registros codificados, porém muitos campos ainda não possuem uma validação
adequada, validando corretamente todos os tamanhos de campos.

Ele pode ser usado para gerar um arquivo digital, com validações de abertura e fechamento de bloco automaticamente.

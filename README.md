# SPED para python

Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.

> This software is coded and documented in portuguese only as it is intended to be used to generate the necessary files for the brazilian government regarding to digital bookkeeping.

```
!!! Aviso importante !!!

O SPED necessita de atualizações constantes para continuar se adequando a legislação vigente e eu como desenvolvedor inicial desta biblioteca não consigo mais mante-la e portanto estou arquivando este repositório.

Nos anos que mantive este projeto público, o uso foi mínimo ou inexistente.

Comumente recebo emails, por ser o mantenedor dela, sempre de alguém procurando uma solução simples e barata para a geração dos arquivos do SPED, porém estes são muito mais complexos que os necessários a NF-e, a título de comparação.

Caso você possua recursos e disponibilidade para manter este projeto ou você faça uso dele e deseja assumir a administração da organização no GitHub e PyPI, você é bem vindo para tal desde que demostre real interesse nisso com contribuições (Pull Requests) a este repositório.

Ao termino de 1 ano deste comunicado, este repositório e os pacotes PyPI serão removidos de forma definitiva.

A licença de uso (MIT) permite que qualquer um use o código fonte aqui disponibilizado como bem queira, sem a necessidade de minha autorização para tal.
```

## Requisitos

- python
- six

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

- usando o projeto e [apontando bugs](https://github.com/sped-br/python-sped/issues)
- [sugestões de melhoria](https://github.com/sped-br/python-sped/issues)
- enviando [pull requests](https://github.com/sped-br/python-sped/pulls)
- auxiliando na [documentação](https://github.com/sped-br/python-sped/wiki)

## Status do Projeto

O projeto está em fase inicial de desenvolvimento e **não deve** ser usado em produção.

| Módulo         |  Status   |
| -------------- | :-------: |
| ECD            | Funcional |
| ECF            | Funcional |
| EFD-PIS/COFINS | Funcional |
| EFD-ICMS/IPI   | Funcional |
| FCI            | Funcional |

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

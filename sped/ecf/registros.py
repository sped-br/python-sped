from ..campos import *
from ..registros import Registro


class Registro0000(Registro):
    """
    Abertura do Arquivo Digital e Identificação da Pessoa Jurídica

    >>> r = Registro0000()
    >>> r.REG
    '0000'
    >>> r.NOME_ESC
    'LECF'
    >>> line='|0000|LECF|1.00|11111111000191|EMPRESA TESTE|0|0|||01012014|31122014|N||0||'
    >>> r = Registro0000(line)
    >>> r.as_line()
    '|0000|LECF|1.00|11111111000191|EMPRESA TESTE|0|0|||01012014|31122014|N||0||'
    >>> r.REG
    '0000'
    >>> r.NOME_ESC
    'LECF'
    >>> r.COD_VER
    '1.00'
    >>> r.CNPJ
    '11111111000191'
    >>> r.NOME
    'EMPRESA TESTE'
    >>> r.DT_INI
    datetime.date(2014, 1, 1)
    >>> r.NOME = 'EMPRESA DEMO'
    >>> r.NOME
    'EMPRESA DEMO'
    """
    campos = [
        CampoFixo(1, 'REG', '0000'),
        CampoFixo(2, 'NOME_ESC', 'LECF'),
        CampoAlfanumerico(3, 'COD_VER', obrigatorio=True, tamanho=4),
        CampoAlfanumerico(4, 'CNPJ', obrigatorio=True, tamanho=14),
        CampoAlfanumerico(5, 'NOME', obrigatorio=True),
        CampoRegex(6, 'IND_SIT_INI_PER', obrigatorio=True, regex='[0-4]'),
        CampoRegex(7, 'SIT_ESPECIAL', obrigatorio=True, regex='[0-9]'),
        CampoNumerico(8, 'PAT_REMAN_CIS', precisao=2, minimo=Decimal(0), maximo=Decimal(100)),
        CampoData(9, 'DT_SIT_ESP'),
        CampoData(10, 'DT_INI', obrigatorio=True),
        CampoData(11, 'DT_FIN', obrigatorio=True),
        CampoRegex(12, 'RETIFICADORA', obrigatorio=True, regex='[SN]'),
        CampoAlfanumerico(13, 'NUM_REC', tamanho=41),
        CampoRegex(14, 'TIP_ECF', obrigatorio=True, regex='[0-2]'),
        CampoAlfanumerico(15, 'COD_SCP', tamanho=14)
    ]


class Registro0001(Registro):
    """
    Abertura do Bloco 0
    """
    pass


class Registro0010(Registro):
    """
    Parâmetros de Tributação
    """
    pass


class Registro0020(Registro):
    """
    Parâmetros Complementares
    """
    pass


class Registro0030(Registro):
    """
    Dados Cadastrais
    """
    pass


class Registro0035(Registro):
    """
    Identificação das SCP
    """
    pass


class Registro0930(Registro):
    """
    Identificação dos Signatários da ECF
    """
    pass


class Registro0990(Registro):
    """
    Encerramento do Bloco 0
    """
    pass


class RegistroC001(Registro):
    """
    Abertura do Bloco C – Informações Recuperadas da ECD
    """
    pass


class RegistroC040(Registro):
    """
    Identificador da ECD
    """
    pass


class RegistroC050(Registro):
    """
    Plano de Contas da ECD
    """
    pass


class RegistroC051(Registro):
    """
    Plano de Contas Referencial
    """
    pass


class RegistroC053(Registro):
    """
    Subcontas Correlatas
    """
    pass


class RegistroC100(Registro):
    """
    Centro de Custos
    """
    pass


class RegistroC150(Registro):
    """
    Identificação do Período dos Saldos Periódicos das Contas Patrimoniais
    """
    pass


class RegistroC155(Registro):
    """
    Detalhes dos Saldos Contábeis das Contas Patrimoniais
    """
    pass


class RegistroC157(Registro):
    """
    Transferência de Saldos do Plano de Contas Anterior
    """
    pass


class RegistroC350(Registro):
    """
    Identificação da Data dos Saldos das Contas de Resultado Antes do Encerramento
    """
    pass


class RegistroC355(Registro):
    """
    Detalhes dos Saldos das Contas de Resultado Antes do Encerramento
    """
    pass


class RegistroC990(Registro):
    """
    Encerramento do Bloco C
    """
    pass


class RegistroE001(Registro):
    """
    Abertura do Bloco E – Informações Recuperadas da ECF Anterior e Cálculo Fiscal dos Dados Recuperados da ECD
    """
    pass


class RegistroE010(Registro):
    """
    Saldos Finais Recuperados da ECF Anterior
    """
    pass


class RegistroE015(Registro):
    """
    Contas Contábeis Mapeadas
    """
    pass


class RegistroE020(Registro):
    """
    Saldos Finais das Contas da Parte B do e-Lalur da ECF Imediatamente Anterior
    """
    pass


class RegistroE030(Registro):
    """
    Identificação do Período
    """
    pass


class RegistroE155(Registro):
    """
    Detalhes dos Saldos Contábeis Calculados com Base nas ECD
    """
    pass


class RegistroE355(Registro):
    """
    Detalhes dos Saldos das Contas de Resultado Antes do Encerramento
    """
    pass


class RegistroE990(Registro):
    """
    Encerramento do Bloco E
    """
    pass


class RegistroJ001(Registro):
    """
    Abertura do Bloco J – Plano de Contas e Mapeamento
    """
    pass


class RegistroJ050(Registro):
    """
    Plano de Contas do Contribuinte
    """
    pass


class RegistroJ051(Registro):
    """
    Plano de Contas Referencial
    """
    pass


class RegistroJ053(Registro):
    """
    Subcontas Correlatas
    """
    pass


class RegistroJ100(Registro):
    """
    Centro de Custos
    """
    pass


class RegistroJ990(Registro):
    """
    Encerramento do Bloco J
    """
    pass


class RegistroK001(Registro):
    """
    Abertura do Bloco K – Saldos das Contas Contábeis e Referenciais
    """
    pass


class RegistroK030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
    """
    pass


class RegistroK155(Registro):
    """
    Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)
    """
    pass


class RegistroK156(Registro):
    """
    Mapeamento Referencial do Saldo Final
    """
    pass


class RegistroK355(Registro):
    """
    Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
    """
    pass


class RegistroK356(Registro):
    """
    Mapeamento Referencial dos Saldos Finais das Contas de Resultado Antes do Encerramento
    """
    pass


class RegistroK990(Registro):
    """
    Encerramento do Bloco K
    """
    pass


class RegistroL001(Registro):
    """
    Abertura do Bloco L – Lucro Real
    """
    pass


class RegistroL030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
    """
    pass


class RegistroL100(Registro):
    """
    Balanço Patrimonial
    """
    pass


class RegistroL200(Registro):
    """
    Método de Avaliação do Estoque Final
    """
    pass


class RegistroL210(Registro):
    """
    Informativo da Composição de Custos
    """
    pass


class RegistroL300(Registro):
    """
    Demonstração do Resultado do Exercício
    """
    pass


class RegistroL990(Registro):
    """
    Encerramento do Bloco L
    """
    pass


class RegistroM001(Registro):
    """
    Abertura do Bloco M – Livro Eletrônico de
    Apuração do Lucro Real (e-Lalur) e Licro Eletrônico
    de Apuração da Base de Cálculo da CSLL (e-Lacs)
    """
    pass


class RegistroM010(Registro):
    """
    Identificação da Conta na Parte B e-Lalur e do e-Lacs
    """
    pass


class RegistroM030(Registro):
    """
    Identificação do Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Real
    """
    pass


class RegistroM300(Registro):
    """
    Lançamentos da Parte A do e-Lalur
    """
    pass


class RegistroM305(Registro):
    """
    Conta da Parte B do e-Lalur
    """
    pass


class RegistroM310(Registro):
    """
    Contas Contábeis Relacionadas ao Lançamento da
    Parte A do e-Lalur.
    """
    pass


class RegistroM312(Registro):
    """
    Números dos Lançamentos Relacionados à Conta Contábil
    """
    pass


class RegistroM315(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    pass


class RegistroM350(Registro):
    """
    Lançamentos da Parte A do e-Lacs
    """
    pass


class RegistroM355(Registro):
    """
    Conta da Parte B do e-Lacs
    """
    pass


class RegistroM360(Registro):
    """
    Contas Contábeis Relacionadas ao Lançamento da
    Parte A do e-Lacs.
    """
    pass


class RegistroM362(Registro):
    """
    Números dos Lançamentos Relacionados à Conta
    Contábil
    """
    pass


class RegistroM365(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    pass


class RegistroM410(Registro):
    """
    Lançamentos na Conta da Parte B do e-Lalur e do e-
    Lacs Sem Reflexo na Parte A
    """
    pass


class RegistroM415(Registro):
    """
    Identificação de Processos Judiciais e
    Administrativos Referentes ao Lançamento
    """
    pass


class RegistroM500(Registro):
    """
    Controle de Saldos das Contas da Parte B do e-Lalur
    e do e-Lacs
    """
    pass


class RegistroM990(Registro):
    """
    Encerramento do Bloco M
    """
    pass


class RegistroN001(Registro):
    """
    Abertura do bloco N – Cálculo do IRPJ e da CSLL
    """
    pass


class RegistroN030(Registro):
    """
    Identificação do Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Real
    """
    pass


class RegistroN500(Registro):
    """
    Base de Cálculo do IRPJ Sobre o Lucro Real Após
    as Compensações de Prejuízo
    """
    pass


class RegistroN600(Registro):
    """
    Demonstração do Lucro da Exploração
    """
    pass


class RegistroN610(Registro):
    """
    Cálculo da Isenção e Redução do Imposto sobre
    Lucro Real
    """
    pass


class RegistroN615(Registro):
    """
    Informações da Base de Cálculo de Incentivos Fiscais
    """
    pass


class RegistroN620(Registro):
    """
    Cálculo do IRPJ Mensal por Estimativa
    """
    pass


class RegistroN630(Registro):
    """
    Cálculo do IRPJ Com Base no Lucro Real
    """
    pass


class RegistroN650(Registro):
    """
    Base de Cálculo da CSLL Após Compensações das
    Bases de Cálculo Negativa
    """
    pass


class RegistroN660(Registro):
    """
    Cálculo da CSLL Mensal por Estimativa
    """
    pass


class RegistroN670(Registro):
    """
    Cálculo da CSLL Com Base no Lucro Real
    """
    pass


class RegistroN990(Registro):
    """
    Encerramento do Bloco N
    """
    pass


class RegistroP001(Registro):
    """
    Abertura do Bloco P – Lucro Presumido
    """
    pass


class RegistroP030(Registro):
    """
    Identificação dos Período e Forma de Apuração do
    IRPJ e da CSLL das Empresas Tributadas pelo
    Lucro Presumido
    """
    pass


class RegistroP100(Registro):
    """
    Balanço Patrimonial
    """
    pass


class RegistroP130(Registro):
    """
    Demonstração das Receitas Incentivadas do Lucro
    Presumido
    """
    pass


class RegistroP150(Registro):
    """
    Demonstração do Resultado
    """
    pass


class RegistroP200(Registro):
    """
    Apuração da Base de Cálculo do Lucro Presumido
    """
    pass


class RegistroP230(Registro):
    """
    Cálculo da Isenção e Redução do Lucro Presumido
    """
    pass


class RegistroP300(Registro):
    """
    Cálculo do IRPJ com Base no Lucro Presumido
    """
    pass


class RegistroP400(Registro):
    """
    Apuração da Base de Cálculo da CSLL com Base no
    Lucro Presumido
    """
    pass


class RegistroP500(Registro):
    """
    Cálculo da CSLL com Base no Lucro Líquido
    """
    pass


class RegistroP990(Registro):
    """
    Encerramento do Bloco P
    """
    pass


class RegistroT001(Registro):
    """
    Abertura do Bloco T – Lucro Arbitrado
    """
    pass


class RegistroT030(Registro):
    """
    Identificação dos Período e Forma de Apuração do
    IRPJ e CSLL das Empresas Tributadas pelo Lucro
    Arbitrado
    """
    pass


class RegistroT120(Registro):
    """
    Apuração da Base de Cálculo do IRPJ com Base no
    Lucro Arbitrado
    """
    pass


class RegistroT150(Registro):
    """
    Cálculo do Imposto de Renda com Base no Lucro
    Arbitrado
    """
    pass


class RegistroT170(Registro):
    """
    Apuração da Base de Cálculo da CSLL com Base no
    Lucro Arbitrado
    """
    pass


class RegistroT181(Registro):
    """
    Cálculo da CSLL com Base no Lucro Arbitrado
    """
    pass


class RegistroT990(Registro):
    """
    Encerramento do Bloco T
    """
    pass


class RegistroU001(Registro):
    """
    Abertura do Bloco U – Imunes e Isentas
    """
    pass


class RegistroU030(Registro):
    """
    Identificação dos Períodos e Formas de Apuração do
    IPRJ e da CSLL das Empressa Imunes e Isentas
    """
    pass


class RegistroU100(Registro):
    """
    Balanço Patrimonial
    """
    pass


class RegistroU150(Registro):
    """
    Demonstração do Resultado
    """
    pass


class RegistroU180(Registro):
    """
    Cálculo do IRPJ das Empresas Imunes ou Isentas
    """
    pass


class RegistroU182(Registro):
    """
    Cálculo da CSLL das Empresas Imunes ou Isentas
    """
    pass


class RegistroU990(Registro):
    """
    Encerramento do Bloco U
    """
    pass


class RegistroX001(Registro):
    """
    Abertura do Bloco X – Informações Econômicas
    """
    pass


class RegistroX280(Registro):
    """
    Atividades Incentivadas - PJ em Geral
    """
    pass


class RegistroX291(Registro):
    """
    Operações com o Exterior - Pessoa
    Vinculada/Interposta/País com Tributação
    Favorecida.
    """
    pass


class RegistroX292(Registro):
    """
    Operações com o Exterior - Pessoa Não Vinculada/
    Não Interposta/País sem Tributação Favorecida
    """
    pass


class RegistroX300(Registro):
    """
    Operações com o Exterior - Exportações (Entradas
    de Divisas)
    """
    pass


class RegistroX310(Registro):
    """
    Operações com o Exterior - Contratantes das
    Exportações
    """
    pass


class RegistroX320(Registro):
    """
    Operações com o Exterior - Importações (Saídas de Divisas)
    """
    pass


class RegistroX330(Registro):
    """
    Operações com o Exterior - Contratantes das
    Importações
    """
    pass


class RegistroX340(Registro):
    """
    Identificação da Participação no Exterior
    """
    pass


class RegistroX350(Registro):
    """
    Participações no Exterior - Resultado do Período de
    Apuração
    """
    pass


class RegistroX351(Registro):
    """
    Demonstrativo de Resultados e de Imposto a Pagar
    no Exterior
    """
    pass


class RegistroX352(Registro):
    """
    Demonstrativo de Resultados no Exterior de
    Coligadas em Regime de Caixa
    """
    pass


class RegistroX353(Registro):
    """
    Demonstrativo de Consolidação
    """
    pass


class RegistroX354(Registro):
    """
    Demonstrativo de Prejuízos Acumulados
    """
    pass


class RegistroX355(Registro):
    """
    Demonstrativo de Rendas Ativas e Passivas
    """
    pass


class RegistroX356(Registro):
    """
    Demonstrativo de Estrutura Societária
    """
    pass


class RegistroX366(Registro):
    """
    Demonstrativo de Imposto Pago no Exterior
    """
    pass


class RegistroX390(Registro):
    """
    Origem e Aplicação de Recursos - Imunes ou Isentas
    """
    pass


class RegistroX400(Registro):
    """
    Comércio Eletrônico e Tecnologia da Informação
    """
    pass


class RegistroX410(Registro):
    """
    Comércio Eletrônico
    """
    pass


class RegistroX420(Registro):
    """
    Royalties Recebidos ou Pagos a Beneficiários do
    Brasil e do Exterior
    """
    pass


class RegistroX430(Registro):
    """
    Rendimentos Relativos a Serviços, Juros e
    Dividendos Recebidos do Brasil e do Exterior
    """
    pass


class RegistroX450(Registro):
    """
    Pagamentos/Remessas Relativos a Serviços, Juros e
    Dividendos Recebidos do Brasil e do Exterior
    """
    pass


class RegistroX460(Registro):
    """
    Inovação Tecnológica e Desenvolvimento
    Tecnológico
    """
    pass


class RegistroX470(Registro):
    """
    Capacitação de Informática e Inclusão Digital
    """
    pass


class RegistroX480(Registro):
    """
    Repes, Recap, Padis, PATVD, Reidi, Repenec,
    Reicomp, Retaero, Recine, Resíduos Sólidos,
    Recopa, Copa do Mundo, Retid, REPNBL-Redes,
    Reif e Olimpíadas
    """
    pass


class RegistroX490(Registro):
    """
    Pólo Industrial de Manaus e Amazônia Ocidental
    """
    pass


class RegistroX500(Registro):
    """
    Zonas de Processamento de Exportação (ZPE)
    """
    pass


class RegistroX510(Registro):
    """
    Áreas de Livre Comércio (ALC)
    """
    pass


class RegistroX990(Registro):
    """
    Encerramento do Bloco X
    """
    pass


class RegistroY001(Registro):
    """
    Abertura do Bloco Y – Informações Gerais
    """
    pass


class RegistroX520(Registro):
    """
    Pagamentos/Recebimentos do Exterior ou de Não
    Residentes
    """
    pass


class RegistroX540(Registro):
    """
    Discriminação da Receita de Vendas dos
    Estabelecimentos por Atividade Econômica
    """
    pass


class RegistroY550(Registro):
    """
    Vendas a Comercial Exportadora com Fim
    Específico de Exportação
    """
    pass


class RegistroY560(Registro):
    """
    Detalhamento das Exportações da Comercial
    Exportadora
    """
    pass


class RegistroY570(Registro):
    """
    Demonstrativo do Imposto de Renda e CSLL
    Retidos na Fonte
    """
    pass


class RegistroY580(Registro):
    """
    Doações a Campanhas Eleitorais
    """
    pass


class RegistroY590(Registro):
    """
    Ativos no Exterior
    """
    pass


class RegistroY600(Registro):
    """
    Identificação de Sócios ou Titular
    """
    pass


class RegistroY611(Registro):
    """
    Rendimentos de Dirigentes, Conselheiros, Sócios ou
    Titular
    """
    pass


class RegistroY612(Registro):
    """
    Rendimentos de Dirigentes e Conselheiros - Imunes
    ou Isentas
    """
    pass


class RegistroY620(Registro):
    """
    Participação Avaliada pelo Método de Equivalência
    Patrimonial
    """
    pass


class RegistroY630(Registro):
    """
    Fundos/Clubes de Investimento
    """
    pass


class RegistroY640(Registro):
    """
    Participações em Consórcios de Empresas
    """
    pass


class RegistroY650(Registro):
    """
    Participantes do Consórcio
    """
    pass


class RegistroY660(Registro):
    """
    Dados de Sucessoras
    """
    pass


class RegistroY665(Registro):
    """
    Demonstrativo das Diferenças na Adoção Inicial
    """
    pass


class RegistroY671(Registro):
    """
    Outras Informações
    """
    pass


class RegistroY672(Registro):
    """
    Outras Informações (Lucro Presumido ou Lucro
    Arbitrado)
    """
    pass


class RegistroY680(Registro):
    """
    Mês das Informações de Optantes pelo Refis (Lucro
    Real, Presumido e Arbitrado)
    """
    pass


class RegistroY681(Registro):
    """
    Informações de Optantes pelo Refis (Lucro Real,
    Presumido e Arbitrado)
    """
    pass


class RegistroY682(Registro):
    """
    Informações de Optantes pelo Refis - Imunes ou
    Isentas
    """
    pass


class RegistroY690(Registro):
    """
    Informações de Optantes pelo Paes
    """
    pass


class RegistroY800(Registro):
    """
    Outras Informações
    """
    pass


class RegistroY990(Registro):
    """
    Encerramento do Bloco Y
    """
    pass


class Registro9001(Registro):
    """
    Abertura do Bloco 9
    """
    pass


class Registro9100(Registro):
    """
    Avisos da Escrituração
    """
    pass


class Registro9900(Registro):
    """
    Registros do Arquivo
    """
    pass


class Registro9099(Registro):
    """
    Encerramento do Bloco 9
    """
    pass


class Registro9999(Registro):
    """
    Encerramento do Arquivo Digital
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

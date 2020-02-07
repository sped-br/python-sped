#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '06 de Fevereiro de 2020 (início: 10 de Janeiro de 2020)'

class EFD_Tabelas:
	"""
	Tabelas utilizadas na EFD
	"""
	
	tabela_natureza_da_conta = {
		'01': 'Contas de ativo',
		'02': 'Contas de passivo',
		'03': 'Patrimônio líquido',
		'04': 'Contas de resultado',
		'05': 'Contas de compensação',
		'09': 'Outras',
	}
	
	# Tabela 4.3.7 - Tabela Código de Base de Cálculo do Crédito
	tabela_bc_do_credito = {
		'01': 'Aquisição de bens para revenda',
		'02': 'Aquisição de bens utilizados como insumo',
		'03': 'Aquisição de serviços utilizados como insumo',
		'04': 'Energia elétrica e térmica, inclusive sob a forma de vapor',
		'05': 'Aluguéis de prédios',
		'06': 'Aluguéis de máquinas e equipamentos',
		'07': 'Armazenagem de mercadoria e frete na operação de venda',
		'08': 'Contraprestações de arrendamento mercantil',
		'09': 'Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação)',
		'10': 'Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição)',
		'11': 'Amortização e Depreciação de edificações e benfeitorias em imóveis',
		'12': 'Devolução de Vendas Sujeitas à Incidência Não-Cumulativa',
		'13': 'Outras Operações com Direito a Crédito',
		'14': 'Atividade de Transporte de Cargas - Subcontratação',
		'15': 'Atividade Imobiliária - Custo Incorrido de Unidade Imobiliária',
		'16': 'Atividade Imobiliária - Custo Orçado de unidade não concluída',
		'17': 'Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção - vale-transporte, valerefeição ou vale-alimentação, fardamento ou uniforme',
		'18': 'Estoque de abertura de bens',
	}
	
	# 4.3.3 - CÓDIGO DA SITUAÇÃO TRIBUTÁRIA REFERENTE AO PIS/PASEP e COFINS
	tabela_cst = {
		'01': 'Operação Tributável com Alíquota Básica',
		'02': 'Operação Tributável com Alíquota Diferenciada',
		'03': 'Operação Tributável com Alíquota por Unidade de Medida de Produto',
		'04': 'Operação Tributável Monofásica - Revenda a Alíquota Zero',
		'05': 'Operação Tributável por Substituição Tributária',
		'06': 'Operação Tributável a Alíquota Zero',
		'07': 'Operação Isenta da Contribuição',
		'08': 'Operação sem Incidência da Contribuição',
		'09': 'Operação com Suspensão da Contribuição',
		'49': 'Outras Operações de Saída',
		'50': 'Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno',
		'51': 'Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno',
		'52': 'Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação',
		'53': 'Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno',
		'54': 'Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação',
		'55': 'Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação',
		'56': 'Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação',
		'60': 'Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno',
		'61': 'Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno',
		'62': 'Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação',
		'63': 'Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno',
		'64': 'Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação',
		'65': 'Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação',
		'66': 'Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação',
		'67': 'Crédito Presumido - Outras Operações',
		'70': 'Operação de Aquisição sem Direito a Crédito',
		'71': 'Operação de Aquisição com Isenção',
		'72': 'Operação de Aquisição com Suspensão',
		'73': 'Operação de Aquisição a Alíquota Zero',
		'74': 'Operação de Aquisição sem Incidência da Contribuição',
		'75': 'Operação de Aquisição por Substituição Tributária',
		'98': 'Outras Operações de Entrada',
		'99': 'Outras Operações',
	}

	tabela_tipo_do_item = {
		'00': 'Mercadoria para Revenda',
		'01': 'Matéria-Prima',
		'02': 'Embalagem',
		'03': 'Produto em Processo',
		'04': 'Produto Acabado',
		'05': 'Subproduto',
		'06': 'Produto Intermediário',
		'07': 'Material de Uso e Consumo',
		'08': 'Ativo Imobilizado',
		'09': 'Serviços',
		'10': 'Outros insumos',
		'99': 'Outras',
	}
	
	# 4.1.1- Tabela Modelos de Documentos Fiscais
	tabela_modelos_documentos_fiscais = {
		'01': 'Nota Fiscal',
		'1B': 'Nota Fiscal Avulsa',
		'02': 'Nota Fiscal de Venda a Consumidor',
		'2D': 'Cupom Fiscal emitido por ECF',
		'2E': 'Bilhete de Passagem emitido por ECF',
		'04': 'Nota Fiscal de Produtor',
		'06': 'Nota Fiscal / Conta de Energia Elétrica',
		'07': 'Nota Fiscal de Serviço de Transporte',
		'08': 'Conhecimento de Transporte Rodoviário de Cargas',
		'8B': 'Conhecimento de Transporte de Cargas Avulso',
		'09': 'Conhecimento de Transporte Aquaviário de Cargas',
		'10': 'Conhecimento Aéreo',
		'11': 'Conhecimento de Transporte Ferroviário de Cargas',
		'13': 'Bilhete de Passagem Rodoviário',
		'14': 'Bilhete de Passagem Aquaviário',
		'15': 'Bilhete de Passagem e Nota de Bagagem',
		'17': 'Despacho de Transporte',
		'16': 'Bilhete de Passagem Ferroviário',
		'18': 'Resumo de Movimento Diário',
		'20': 'Ordem de Coleta de Cargas',
		'21': 'Nota Fiscal de Serviço de Comunicação',
		'22': 'Nota Fiscal de Serviço de Telecomunicação',
		'23': 'GNRE',
		'24': 'Autorização de Carregamento e Transporte',
		'25': 'Manifesto de Carga',
		'26': 'Conhecimento de Transporte Multimodal de Cargas',
		'27': 'Nota Fiscal de Transporte Ferroviário de Cargas',
		'28': 'Nota Fiscal / Conta de Fornecimento de Gás Canalizado',
		'29': 'Nota Fiscal / Conta de Fornecimento de Água Canalizada',
		'30': 'Bilhete / Recibo do Passageiro',
		'55': 'Nota Fiscal Eletrônica: NF-e',
		'57': 'Conhecimento de Transporte Eletrônico: CT-e',
		'59': 'Cupom Fiscal Eletrônico: CF-e (CF-e-SAT)',
		'60': 'Cupom Fiscal Eletrônico: CF-e-ECF',
		'63': 'Bilhete de Passagem Eletrônico: BP-e',
		'65': 'Nota Fiscal Eletrônica ao Consumidor Final: NFC-e',
		'66': 'Nota Fiscal de Energia Elétrica Eletrônica: NF3e',
		'67': 'Conhecimento de Transporte Eletrônico para Outros Serviços: CT-e OS',
	}

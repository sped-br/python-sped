#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imprimir informações da SPED EFD Contribuições em um arquivo.csv
Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '23 de Janeiro de 2020 (início: 10 de Janeiro de 2020)'

import os, csv, sys, re
from datetime import datetime

# definir path necessário para os testes
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from sped.efd.pis_cofins.arquivos import ArquivoDigital
from sped.efd.pis_cofins.blocos import *
from sped.efd.pis_cofins.registros import *

verbose = False

# Altere o endereço e nome do arquivo EFD Contribuições
# file_path = './PISCOFINS_20150201_20150228_77744881000155_teste1.txt'
file_path = './PISCOFINS_20170101_20170131_55566871000169_teste2.txt'

arq = ArquivoDigital() # veja sped/arquivos.py

arq.readfile(file_path, codificacao='latin-1', verbose=True)

print() if verbose else 0

# Imprimir as informações desta coluna, nesta ordem
colunas = ['NOME', 'CNPJ', 'DT_INI', 'REG', 'COD_PART', 'COD_CTA', 'IND_OPER', 'NAT_BC_CRED', 'CFOP', 'CST_PIS', 'CST_COFINS', 'DT_DOC', 'Chave Eletrônica', 'NUM_DOC', 'NUM_ITEM', 'Valor do Item', 'Valor da Base de Cálculo', 'ALIQ_PIS', 'ALIQ_COFINS']

registros_de_valor = ['VL_DOC', 'VL_BRT', 'VL_OPER', 'VL_OPR', 'VL_OPER_DEP', 'VL_BC_CRED', 'VL_BC_EST', 'VL_TOT_REC', 'VL_REC_CAIXA', 'VL_REC_COMP', 'VL_REC', 'VL_ITEM'] # adicionado 'VL_OPR' para EFD ICMS_IPI

registros_de_chave_eletronica = ['CHV_NFE', 'CHV_CTE', 'CHV_NFSE', 'CHV_DOCe', 'CHV_CFE', 'CHV_NFE_CTE']

registros_de_codigo_cst = ['CST_PIS', 'CST_COFINS']

registros_de_base_de_calculo = ['VL_BC_PIS', 'VL_BC_COFINS']

def formatar_valor(nome,val):
	if nome in registros_de_chave_eletronica and len(val) == 44:
		chave = val
		# Manual de Orientação Contribuinte v 6.00 - NFe, quantidade de caracteres: 02 04 14 02 03 09 01 08 01
		return "%s.%s.%s.%s.%s.%s.%s.%s-%s" % (chave[0:2],chave[2:6],chave[6:20],chave[20:22],chave[22:25],chave[25:34],chave[34:35],chave[35:43],chave[43:44])
	# re.search: find something anywhere in the string and return a match object.
	if re.search('CNPJ', nome, flags=re.IGNORECASE): # em perl: if (cfop =~ /CNPJ/i)
		cnpj = val
		# https://wiki.python.org.br/Cnpj
		return "%s.%s.%s/%s-%s" % (cnpj[0:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:14])
	if nome in ['DT_INI', 'DT_FIN', 'DT_DOC', 'DT_E_S', 'DT_A_P'] and len(val) == 8:
		dt = datetime.strptime(val, "%d%m%Y") # ddmmaaaa
		#return dt.isoformat('T')
		return dt.strftime("%d/%m/%Y")
		#return dt.strftime('%x %X') # excel date format
	return val

def natureza_da_bc_dos_creditos(cfop):	
	"""
	http://sped.rfb.gov.br/arquivo/show/1681
	Tabela CFOP - Operações Geradoras de Créditos - Versão 1.0.0
	"""
	natureza_bc = None
	
	# Código 01 - CFOP de 'Aquisição de Bens para Revenda'
	if   cfop in ['1102','1113','1117','1118','1121','1251','1403','1652','2102','2113','2117','2118','2121','2251','2403','2652','3102','3251','3652']:
		natureza_bc = 1
	# Código 02 - CFOP de 'Aquisição de Bens Utilizados como Insumo'
	elif cfop in ['1101','1111','1116','1120','1122','1126','1128','1401','1407','1556','1651','1653','2101','2111','2116','2120','2122','2126','2128','2401','2407','2556','2651','2653','3101','3126','3128','3556','3651','3653']:
		natureza_bc = 2
	# Código 03 - CFOP de 'Aquisição de Serviços Utilizados como Insumos'
	elif cfop in ['1124','1125','1933','2124','2125','2933']:
		natureza_bc = 3
	# Código 12 - CFOP de 'Devolução de Vendas Sujeitas à Incidência Não-Cumulativa'
	elif cfop in ['1201','1202','1203','1204','1410','1411','1660','1661','1662','2201','2202','2410','2411','2660','2661','2662']:
		natureza_bc = 12
	# Código 13 - CFOP de 'Outras Operações com Direito a Crédito'
	elif cfop in ['1922','2922']:
		natureza_bc = 13
	
	return natureza_bc

info_de_abertura = {}

for registro in [arq._registro_abertura, arq._registro_encerramento]:
	REG = registro.valores[1]
	nivel = registro.nivel
	codigo_cst = ''
	valor_item = ''
	
	# https://www.geeksforgeeks.org/python-creating-multidimensional-dictionary/
	info_de_abertura.setdefault(nivel, {}).setdefault(codigo_cst, {}).setdefault(valor_item, {})['Nível Hierárquico'] = nivel
	
	if verbose:
		print(f'{registro.as_line() = } ; {REG = } ; {nivel = }')
		print(f'{info_de_abertura = }')
	
	for c in registro.campos:
			
		valor = formatar_valor(nome=c.nome, val=registro.valores[c.indice])
		
		if c.nome in colunas:
			info_de_abertura[nivel][codigo_cst][valor_item][c.nome] = valor			
		if verbose:
			print(f'{c.indice = :>2} ; {c.nome = :>22} ; {registro.valores[c.indice] = :<50} ; {valor = }')
	
	print() if verbose else 0

my_regex = "^[ABCDFI]" # Ler apenas os blocos A, B, C, D, F e I.

# Inicialmente apenas para teste
def imprimir_informacoes_linha_a_linha():
	# https://docs.python.org/3/library/csv.html
	with open('efd_contrib_todas_informacoes.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')
		writer.writerow(colunas) # imprimir nomes das colunas
		
		for key in arq._blocos.keys():
			
			match_bloco = re.search(my_regex, key, flags=re.IGNORECASE)
			if not match_bloco:
				continue
			
			bloco = arq._blocos[key]
			count = 1
			
			for registro in bloco.registros:
				
				REG = registro.valores[1]
				nivel = registro.nivel
				
				info = {}
				for coluna in colunas:
					info[coluna] = ''
					if coluna in info_de_abertura[0]['']['']:
						info[coluna] = info_de_abertura[0][''][''][coluna]
				
				for c in registro.campos:
					
					valor = formatar_valor(nome=c.nome, val=registro.valores[c.indice])
					
					if c.nome in colunas:
						info[c.nome] = valor
					if c.nome in registros_de_valor:
						info['Valor do Item'] = valor
					if c.nome in registros_de_chave_eletronica and registro.valores[c.indice] != '':
						info['Chave Eletrônica'] = valor
					if c.nome in registros_de_base_de_calculo:
						info['Valor da Base de Cálculo'] = valor
						
				writer.writerow( info.values() )
				
				# limitar tamanho do arquivo impresso
				# Imprimir apenas os 100 primeiros registro de cada Bloco
				if (count := count + 1) > 100:
					break

# imprimir_informacoes_linha_a_linha()

# https://docs.python.org/3/library/csv.html
with open('efd_contrib.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=';')
	writer.writerow(colunas) # imprimir nomes das colunas
	
	for key in arq._blocos.keys():
		
		match_bloco = re.search(my_regex, key, flags=re.IGNORECASE)
		if not match_bloco:
			continue
		
		bloco = arq._blocos[key]
		count = 1
		
		info = info_de_abertura
		nivel_anterior = 0
		nivel = 0
		
		for registro in bloco.registros:
			
			REG = registro.valores[1]
			codigo_cst = ''
			valor_item = ''
			
			nivel_anterior = nivel
			nivel = registro.nivel # nível atual	
			
			for c in registro.campos:
				if c.nome in registros_de_codigo_cst:
					codigo_cst = registro.valores[c.indice]
				if c.nome in registros_de_valor:
					valor_item = registro.valores[c.indice]
			
			if verbose:
				print(f'\n{count = :>2} ; {key = } ; {bloco = } ; {REG = } ; {nivel_anterior = } ; {nivel = } ; {codigo_cst = } ; {valor_item = }')
				print(f'{registro.as_line() = }')

			if nivel < nivel_anterior:
				
				if verbose:
					print(f'\n nivel atual: {nivel = } < {nivel_anterior = }; deletar informações em info a partir do nível {nivel} em diante:')
				# Delete items from dictionary while iterating: https://www.geeksforgeeks.org/python-delete-items-from-dictionary-while-iterating/
				
				for nv in list(info):
					if nv >= nivel:
						del info[nv]
						if verbose:
							print(f'\t *** deletar informações do nível {nv}: del info[{nv}] ***')
				
				print() if verbose else 0
			
			info.setdefault(nivel, {}).setdefault(codigo_cst, {}).setdefault(valor_item, {})['Nível Hierárquico'] = nivel
			
			for c in registro.campos:
				
				valor = formatar_valor(nome=c.nome, val=registro.valores[c.indice])
				
				if verbose:
					print(f'{c.indice = :>2} ; {c.nome = :>22} ; {registro.valores[c.indice] = :<50} ; {valor = }')
				
				if c.nome in colunas:
					info[nivel][codigo_cst][valor_item][c.nome] = valor
				if c.nome in registros_de_chave_eletronica and registro.valores[c.indice] != '':
					info[nivel][codigo_cst][valor_item]['Chave Eletrônica'] = valor
				if c.nome in registros_de_valor:
					info[nivel][codigo_cst][valor_item]['Valor do Item'] = valor
				if c.nome in registros_de_base_de_calculo:
					info[nivel][codigo_cst][valor_item][c.nome] = valor
					info[nivel][codigo_cst][valor_item]['Valor da Base de Cálculo'] = valor
			
			if verbose:
				print(f'\n-->{nivel = } ; {codigo_cst = } ; {valor_item = } ; {info[nivel][codigo_cst][valor_item] = }')
			
			if ('CST_PIS' in info[nivel][codigo_cst][valor_item] and 'CST_COFINS' in info[nivel][codigo_cst][valor_item]
				and info[nivel][codigo_cst][valor_item]['CST_PIS'] == info[nivel][codigo_cst][valor_item]['CST_COFINS'] 
				and info[nivel][codigo_cst][valor_item]['VL_BC_PIS'] == info[nivel][codigo_cst][valor_item]['VL_BC_COFINS']):
				
				flattened_info = {} # eliminar os diversos niveis e trazer todas as informações para um só nivel.
				
				for coluna in colunas:
					flattened_info[coluna] = '' # atribuir este valor inicial para todas as colunas
					
					if coluna in info[nivel][codigo_cst][valor_item]:
						flattened_info[coluna] = info[nivel][codigo_cst][valor_item][coluna]
						if verbose:
							print(f'{nivel = } ; {cst = :<4} ; {valor = :<12} ; {coluna = :>25} = {info[nivel][codigo_cst][valor_item][coluna]:<18} ; {info[nivel][codigo_cst][valor_item] = }')
						continue			
					for nv in range(0,nivel):   # nível em ordem crescente ; as informações obtidas do último nível prevalecerá.
						for cst in sorted(info[nv]):
							for valor in info[nv][cst]:	
								if coluna in info[nv][cst][valor]:
									flattened_info[coluna] = info[nv][cst][valor][coluna]
									if verbose:
										print(f'{nivel = } ; {nv = } ; {cst = :<4} ; {valor = :<12} ; {coluna = :>25} = {info[nv][cst][valor][coluna]:<18} ; {info[nv][cst][valor] = }')	
				
				print() if verbose else 0
				
				# adicionar informação de 'NAT_BC_CRED' para os créditos quando houver informação do CFOP.
				# re.search: find something anywhere in the string and return a match object.
				if len(flattened_info['NAT_BC_CRED']) == 0 and re.search('\d{4}', flattened_info['CFOP']) and re.search('\d{1,2}', flattened_info['CST_COFINS']): # em perl: if (cfop =~ /\d{4}/)
					cfop = flattened_info['CFOP']
					cst  = int(flattened_info['CST_COFINS'])
					if 50 <= cst <= 66:
						flattened_info['NAT_BC_CRED'] = natureza_da_bc_dos_creditos(cfop)
				
				writer.writerow( flattened_info.values() )
			
			# Limitar tamanho do arquivo impresso
			# Imprimir apenas os 20 primeiros registro de cada Bloco
			if False and (count := count + 1) > 20:
				break

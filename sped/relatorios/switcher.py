# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '01 de Março de 2020 (início: 10 de Janeiro de 2020)'

import sys, re
from datetime import datetime
from sped.campos import (CampoData, CampoCNPJ, CampoCPF, CampoNCM,
                        CampoCPFouCNPJ, CampoChaveEletronica)

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

class My_Switch:
	"""
	Definir, apenas uma vez, um dicionário ao invés de utilizar vários 'if/then/else' a cada
	execução de formatar_valor():
	dict[key] = funtion_key(value)
	Ao escolher uma chave, o dicionário aplica uma função (que depende da chave) sobre o valor
	Esta construção possui Ordem O(1).
	Caso fossem utilizados vários if/then/else (ou switch) a ordem seria O(N), que é mais lento!
	"""

	@staticmethod
	def funcao_identidade(chave):
		return chave

	@staticmethod
	def formatar_linhas(numero):
		return f'{int(numero):09d}'

	@staticmethod
	def formatar_mes(mes_num):
		try:
			mes_num = f'{int(mes_num):02d}'
			return f'{EFD_Tabelas.tabela_mes_nominal[mes_num]}'
		except:
			return mes_num
	
	@staticmethod
	def formatar_registro(registro):
		try:
			return f'{registro} - {EFD_Tabelas.tabela_info_do_registro[registro]}'
		except:
			reg = registro[0]
			return f'{registro} - {EFD_Tabelas.tabela_info_do_registro[reg]}'
	
	@staticmethod
	def formatar_cfop(cfop):
		try:
			cfop = f'{int(cfop):04d}'
			return f'{cfop} - {EFD_Tabelas.tabela_cfop_descricao[cfop]}'
		except:
			return cfop
	
	@staticmethod
	def formatar_cst_contrib(codigo_cst):
		try:
			codigo_cst = f'{int(codigo_cst):02d}'
			return f'{codigo_cst} - {EFD_Tabelas.tabela_cst_contrib[codigo_cst]}'
		except:
			return codigo_cst

	@staticmethod
	def formatar_cst_icms(codigo_cst):
		try:
			codigo_cst = f'{int(codigo_cst):03d}'
			return f'{codigo_cst} - {EFD_Tabelas.tabela_cst_icms[codigo_cst]}'
		except:
			return codigo_cst
	
	@staticmethod
	def formatar_nbc(natureza_bc):
		try:
			natureza_bc = f'{int(natureza_bc):02d}'
			return f'{natureza_bc} - {EFD_Tabelas.tabela_bc_do_credito[natureza_bc]}'
		except:
			return natureza_bc
	
	@staticmethod
	def formatar_tipo(tipo_do_item):
		try:
			tipo_do_item = f'{int(tipo_do_item):02d}'
			return f'{tipo_do_item} - {EFD_Tabelas.tabela_tipo_do_item[tipo_do_item]}'
		except:
			return tipo_do_item
	
	@staticmethod
	def formatar_mod(doc_fiscal):
		try:
			return f'{doc_fiscal} - {EFD_Tabelas.tabela_modelos_documentos_fiscais[doc_fiscal]}'
		except:
			return doc_fiscal

	@staticmethod
	def formatar_valores_reais(valor):
		try:
			return float(valor)
		except:
			valor = valor.replace( '.', ''  ) # 4.218.239,19 --> 4218239,19
			valor = valor.replace( ',', '.' ) #   4218239,19 --> 4218239.19
			return float(valor)
	
	@staticmethod
	def formatar_datas(data):
		date_time = datetime.strptime(data, "%d/%m/%Y") # dd/mm/aaaa
		return date_time
	
	# initialize the attributes of the class
	
	def __init__(self, lista_de_colunas, verbose=False):
		self.lista_de_colunas = lista_de_colunas
		self.verbose = verbose
		self.dicionario = {}
	
	def formatar_colunas_do_arquivo_csv(self):

		for nome_da_coluna in self.lista_de_colunas:
			
			match_linha = re.search(r'^Linhas', nome_da_coluna, flags=re.IGNORECASE)
			match_mes   = re.search(r'^Mês do Período', nome_da_coluna, flags=re.IGNORECASE)
			match_reg   = re.search(r'^REG', nome_da_coluna, flags=re.IGNORECASE)
			match_cfop  = re.search(r'^CFOP', nome_da_coluna, flags=re.IGNORECASE)
			match_nbc   = re.search(r'NAT_BC_CRED', nome_da_coluna, flags=re.IGNORECASE)
			match_tipo  = re.search(r'TIPO_ITEM', nome_da_coluna, flags=re.IGNORECASE)
			match_mod   = re.search(r'COD_MOD', nome_da_coluna, flags=re.IGNORECASE)
			match_data  = re.search(r'^DT_|Data', nome_da_coluna, flags=re.IGNORECASE)
			match_chave = re.search(r'^CHV_|Chave Eletrônica', nome_da_coluna, flags=re.IGNORECASE)
			match_ncm   = re.search(r'COD_NCM', nome_da_coluna, flags=re.IGNORECASE)
			match_cnpj  = re.search(r'CNPJ', nome_da_coluna, flags=re.IGNORECASE)
			match_cpf   = re.search(r'CPF',  nome_da_coluna, flags=re.IGNORECASE)

			match_cst_contib = re.search(r'^CST_(PIS|COFINS)|CST_PIS_COFINS', nome_da_coluna, flags=re.IGNORECASE)
			match_cst_icms   = re.search(r'^CST_ICMS', nome_da_coluna, flags=re.IGNORECASE)

			# https://www.geeksforgeeks.org/switch-case-in-python-replacement/
			# Ao invés de usar vários 'if/elif/elif/elif/.../else', usar o dict switcher[chave] = valor, 
			# tal que switcher.get(True, 'default value') retorna o valor da última chave True.
			# bool(match_linha) retorna True ou False.
			switcher = {
				bool(match_linha):      self.formatar_linhas,
				bool(match_mes):        self.formatar_mes,
				bool(match_reg):        self.formatar_registro,
				bool(match_cfop):       self.formatar_cfop,
				bool(match_nbc):        self.formatar_nbc,
				bool(match_tipo):       self.formatar_tipo,
				bool(match_mod):        self.formatar_mod,
				bool(match_cst_contib): self.formatar_cst_contrib,
				bool(match_cst_icms):   self.formatar_cst_icms,
				bool(match_data):       CampoData.formatar,
				bool(match_chave):      CampoChaveEletronica.formatar,
				bool(match_ncm):        CampoNCM.formatar,
				bool(match_cnpj):       CampoCNPJ.formatar,
				bool(match_cpf):        CampoCPF.formatar,
				bool(match_cnpj and match_cpf): CampoCPFouCNPJ.formatar,
			}

			# Caso não ocorra nenhum match, retornar default value = self.funcao_identidade
			self.dicionario[nome_da_coluna] = switcher.get(True, self.funcao_identidade)

			#print(f'{switcher = } ; {nome_da_coluna = } ; {bool(match_data) = } ; {self.dicionario[nome_da_coluna] = } \n')
			#sleep(0.5)
		
		if self.verbose:
			for idx, key in enumerate(sorted(self.dicionario.keys()),1):
				print(f'{key:>40}: [{idx:>2}] {self.dicionario[key]}')
	
	def formatar_valores_das_colunas(self):

		for nome_da_coluna in self.lista_de_colunas:

			match_n_center = re.search(r'Linha|NUM_ITEM', nome_da_coluna, flags=re.IGNORECASE)
			match_n_right  = re.search(r'NUM_DOC', nome_da_coluna, flags=re.IGNORECASE)
			match_valor    = re.search(r'VL|Valor', nome_da_coluna, flags=re.IGNORECASE)
			match_aliquota = re.search(r'Aliq', nome_da_coluna, flags=re.IGNORECASE)
			match_data     = re.search(r'Data|DT_', nome_da_coluna, flags=re.IGNORECASE)

			self.dicionario[nome_da_coluna] = self.funcao_identidade
			
			# Estes vários if/elif/elif/... são executados apenas uma vez na execução do método/função.
			if match_n_center or match_n_right or match_valor or match_aliquota:
				self.dicionario[nome_da_coluna] = self.formatar_valores_reais
			elif match_data:
				self.dicionario[nome_da_coluna] = self.formatar_datas
	
	def formatar_colunas_do_arquivo_excel(self,workbook):

		format_default  = workbook.add_format()
		format_n_center = workbook.add_format({'num_format': '0', 'align':'center'})
		format_n_right  = workbook.add_format({'num_format': '0', 'align':'right'})
		format_valor    = workbook.add_format({'num_format': '#,##0.00', 'align':'right'})
		format_aliquota = workbook.add_format({'num_format': '#,##0.0000', 'align':'center'})
		format_data     = workbook.add_format({'num_format': 'dd/mm/yyyy', 'align':'center'})
		format_center   = workbook.add_format({'align':'center'})

		for nome_da_coluna in self.lista_de_colunas:

			match_n_center = re.search(r'Linha|NUM_ITEM', nome_da_coluna, flags=re.IGNORECASE)
			match_n_right  = re.search(r'NUM_DOC', nome_da_coluna, flags=re.IGNORECASE)
			match_valor    = re.search(r'VL|Valor', nome_da_coluna, flags=re.IGNORECASE)
			match_aliquota = re.search(r'Aliq', nome_da_coluna, flags=re.IGNORECASE)
			match_data     = re.search(r'Data|DT_', nome_da_coluna, flags=re.IGNORECASE)
			match_center   = re.search(r'Período|Operação', nome_da_coluna, flags=re.IGNORECASE)

			switcher = {
				bool(match_n_center):  format_n_center,
				bool(match_n_right):   format_n_right,
				bool(match_valor):     format_valor,
				bool(match_aliquota):  format_aliquota,
				bool(match_data):      format_data,
				bool(match_center):    format_center,
			}

			# Caso não ocorra nenhum match, retornar default value = format_default
			self.dicionario[nome_da_coluna] = switcher.get(True, format_default)

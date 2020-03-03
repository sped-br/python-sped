# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '01 de Março de 2020 (início: 10 de Janeiro de 2020)'

import sys, csv
import xlsxwriter # pip install xlsxwriter
from sped.relatorios.switcher import My_Switch
from sped.relatorios.print_csv_file import SPED_EFD_Info

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

# Python OOP: Atributos e Métodos (def, funções)
class CSV_to_Excel:
	"""
	converter arquivo de formato .csv para .xlsx do excel
	"""

	# initialize the attributes of the class
	
	def __init__(self, arquivo_csv, arquivo_excel, verbose=False):
		self.imput_csv = arquivo_csv
		self.output_excel = arquivo_excel
		self.verbose = verbose

	@property
	def convert_csv_to_xlsx(self):

		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook(self.output_excel)
		worksheet = workbook.add_worksheet('Itens de Docs Fiscais')
		workbook.set_properties({'comments': 'Created with Python and XlsxWriter'})
		
		# definindo a altura da primeira coluna, row_index == 0
		worksheet.set_row(0, 30)

		# Freeze pane on the top row.
		worksheet.freeze_panes(1, 0)

		# Set up some formatting
		header_format = workbook.add_format({
						'align':'center', 'valign':'vcenter', 
						'bg_color':'#C5D9F1', 'text_wrap':True, 
						'font_size':10})
		
		select_value = My_Switch(SPED_EFD_Info.registros_totais,verbose=self.verbose)
		select_value.formatar_valores_das_colunas()
		myValue = select_value.dicionario

		select_format = My_Switch(SPED_EFD_Info.registros_totais,verbose=self.verbose)
		select_format.formatar_colunas_do_arquivo_excel(workbook)
		myFormat = select_format.dicionario

		# First we find the length of the header column 
		largura_max = [len(c) for c in SPED_EFD_Info.colunas_selecionadas]
        
		with open(self.imput_csv, 'r', encoding='utf-8', errors='ignore') as file:
        
			reader = csv.reader(file, delimiter=';')
			for row_index, row in enumerate(reader):

				# nomes das colunas
				if row_index == 0:
					worksheet.write_row(row_index, 0, tuple(SPED_EFD_Info.colunas_selecionadas), header_format)
					continue

				for column_index, cell in enumerate(row):

					# reter largura máxima
					if len(cell) > largura_max[column_index]:
						largura_max[column_index] = len(cell)
					
					column_name = SPED_EFD_Info.colunas_selecionadas[column_index]

					if len(cell) > 0:
						worksheet.write(row_index, column_index, myValue[column_name](cell), myFormat[column_name])
					else:
						# Write cell with row/column notation.
						worksheet.write(row_index, column_index, cell)
		
		# Ajustar largura das colunas com os valores máximos
		largura_min = 4
		for i, width in enumerate(largura_max):
			if width > 120: # largura máxima
				width = 120
			worksheet.set_column(i, i, width + largura_min)
		
		# Set the autofilter( $first_row, $first_col, $last_row, $last_col )
		worksheet.autofilter(0, 0, 0, len(largura_max) - 1)

		workbook.close()

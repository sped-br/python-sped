#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '03 de Março de 2020 (início: 29 de Janeiro de 2020)'
Home  = 'https://github.com/claudiofsr/python-sped'

# Instruções (no Linux):
# Para obter uma cópia, na linha de comando, execute:
# > git clone git@github.com:claudiofsr/python-sped.git

# Em seguida, vá ao diretório python-sped:
# > cd python-sped

# Para instalar o módulo do SPED em seu sistema execute, como superusuário:
# > python setup.py install

# Em um diretório que contenha arquivos de SPED EFD, 
# execute no terminal o camando:
# > efd_relatorios

import sys, os, re
from time import time, sleep
from sped import __version__
from sped.relatorios.find_efd_files import ReadFiles, Total_Execution_Time
from sped.relatorios.print_csv_file import SPED_EFD_Info
from sped.relatorios.convert_csv_to_xlsx import CSV_to_Excel

import psutil
from multiprocessing import Pool # take advantage of multiple cores

num_cpus = psutil.cpu_count(logical=True)

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

def make_csv_file(sped_file_path, numero_do_arquivo, lista_de_arquivos):

	tipo_da_efd = lista_de_arquivos.informations[sped_file_path]['tipo']
	codificacao = lista_de_arquivos.informations[sped_file_path]['codificação']

	filename = os.path.splitext(sped_file_path)[0] # ('/home/user/file', '.txt')
	arquivo_csv   = filename + '.csv'
	
	csv_file = SPED_EFD_Info(sped_file_path, numero_do_arquivo, encoding=codificacao, efd_tipo=tipo_da_efd, verbose=False)
	csv_file.imprimir_arquivo_csv

	return {numero_do_arquivo: arquivo_csv}

def main():

	print(f'\n Python Sped - versão: {__version__}\n')
	
	dir_path = os.getcwd() # CurrentDirectory
	extensao = 'txt'
	
	lista_de_arquivos = ReadFiles(root_path = dir_path, extension = extensao)
	
	arquivos_efd_contrib  = list(lista_de_arquivos.find_all_efd_contrib) # SPED EFD Contrib
	arquivos_efd_icms_ipi = list(lista_de_arquivos.find_all_efd_icmsipi) # SPED EFD ICMS_IPI
	
	arquivos_sped_efd = arquivos_efd_contrib + arquivos_efd_icms_ipi

	if len(arquivos_sped_efd) == 0:
		print(f"\tDiretório atual: '{dir_path}'.")
		print(f"\tNenhum arquivo SPED EFD foi encontrado neste diretório.\n")
		exit()
	
	print(" Arquivo(s) de SPED EFD encontrado(s) neste diretório:\n")
	
	for index,file_path in enumerate(arquivos_sped_efd,1):
		print( f"{index:>6}: {file_path}")
		for attribute, value in lista_de_arquivos.get_file_info(file_path).items():
			print(f'{attribute:>25}: {value}')

	# argumentos: sys.argv: argv[0], argv[1], argv[2], ...
	command_line = sys.argv[1:]
	
	if len(command_line) == 0:
		print("\n Selecione os arquivos pelos números correspondentes.")
		print(" Use dois pontos .. para indicar intervalo.")
		print(" Modos de uso:\n")
		print("\tExemplo A (selecionar apenas o arquivo 4): \n\tefd_relatorios 4 \n")
		print("\tExemplo B (selecionar os arquivos de 1 a 6): \n\tefd_relatorios 1 2 3 4 5 6 \n")
		print("\tExemplo C (selecionar os arquivos de 1 a 6): \n\tefd_relatorios 1..6 \n")
		print("\tExemplo D (selecionar os arquivos 2, 4 e 8): \n\tefd_relatorios 2 4 8 \n")
		print("\tExemplo E (selecionar os arquivos de 1 a 5, 7, 9, 12 a 15 e 18): \n\tefd_relatorios 1..5 7 9 12..15 18 \n")
		exit()
	else:
		# concatenate item in list to strings
		opcoes = ' '.join(command_line)
		comando_inicial = opcoes
		# remover todos os caracteres, exceto dígitos, pontos e espaços em branco
		opcoes = re.sub(r'[^\d\.\s]', '', opcoes)
		# substituir dois ou mais espaços em branco por apenas um.
		opcoes = re.sub(r'\s{2,}', ' ', opcoes)
		# remover os possíveis espaços em branco do início e do final da variável
		opcoes = opcoes.strip()
		# remover possíveis espaços: '32 ..  41' --> '32..41' ou também '32... ..  41' --> '32..41'
		opcoes = re.sub(r'(?<=\d)[\.\s]*\.[\.\s]*(?=\d)', '..', opcoes)
		# string.split(separator, maxsplit): maxsplit -1 split "all occurrences"
		# command_line = opcoes.split(r' ', -1)
		# split string based on regex
		command_line = re.split(r'\s+', opcoes)
	
	arquivos_escolhidos = {} # usar dicionário para evitar repetição

	for indice in command_line: # exemplo: ('5', '17', '32..41')

		apenas_um_digito = re.search(r'^(\d+)$', indice)
		intervalo_digito = re.search(r'^(\d+)\.{2}(\d+)$', indice)

		if apenas_um_digito: # exemplo: '17'
			value_1 = int(apenas_um_digito.group(1)) # group(1) will return the 1st capture.
			if value_1 > len(arquivos_sped_efd) or value_1 <= 0:
				print(f"\nArquivo número {value_1} não encontrado!\n")
				exit()
			sped_file = arquivos_sped_efd[value_1 - 1]
			arquivos_escolhidos[sped_file] = value_1

		elif intervalo_digito: # exemplo: '32..41'
			value_1 = int(intervalo_digito.group(1)) # 32
			value_2 = int(intervalo_digito.group(2)) # 41
			if value_1 > len(arquivos_sped_efd) or value_1 <= 0:
				print(f"\nArquivo número {value_1} não encontrado!\n")
				exit()
			if value_2 > len(arquivos_sped_efd) or value_2 <= 0:
				print(f"\nArquivo número {value_2} não encontrado!\n")
				exit()
			if value_1 > value_2:
				print(f"\n{value_1}..{value_2}: o primeiro número deve ser menor ou igual ao segundo!\n")
				exit()
			for index in range(value_1 - 1, value_2):
				sped_file = arquivos_sped_efd[index]
				arquivos_escolhidos[sped_file] = index + 1
		else:
			print(f"\nOpção {indice} inválida!\n")
			exit()
	
	print(f"\nArquivo(s) selecionado(s) '{comando_inicial}' -> {list(arquivos_escolhidos.values())}:\n")
	for sped_file in arquivos_escolhidos:
		print(f'\t{sped_file}')
	print()

	start = time()

	# https://sebastianraschka.com/Articles/2014_multiprocessing.html
	# https://stackoverflow.com/questions/26068819/how-to-kill-all-pool-workers-in-multiprocess
	# https://www.programcreek.com/python/index/175/multiprocessing
	pool    = Pool( processes = int(max(1, num_cpus - 2)) )
	results = [ pool.apply_async(make_csv_file, args=(k,v,lista_de_arquivos)) for (k,v) in arquivos_escolhidos.items() ]
	output  = [ p.get() for p in results ] # output = [{num: csv_file_path}]
	pool.close()

	num_total_de_arquivos = len(output)
	if num_total_de_arquivos > 1:
		print(f"\nForam gerados {num_total_de_arquivos} arquivos csv temporários.\n")
	else:
		print(f"\nFoi gerado {num_total_de_arquivos} arquivo csv temporário.\n")

	# https://stackoverflow.com/questions/5236296/how-to-convert-list-of-dict-to-dict
	new_dict = { key: dicts[key] for dicts in output for key in dicts } # dict Comprehensions
	#print(f'{new_dict = } ; {new_dict.values() = }')

	data_ini = {}
	data_fim = {}

	for value in new_dict.values():
		# PISCOFINS_20150701_20150731_12345678912345_...csv
		# 12345678912345-123456789123-20170101-20170131-1-...-SPED-EFD.csv
		data01 = re.search(r'PISCOFINS_(\d{8})_(\d{8})', value, flags=re.IGNORECASE)
		data02 = re.search(r'\d{14}.\d+.(\d{8}).(\d{8}).*SPED-EFD', value, flags=re.IGNORECASE)

		if data01:
			data_ini[ data01.group(1) ] = 1
			data_fim[ data01.group(2) ] = 1
		if data02:
			data_ini[ data02.group(1) ] = 1
			data_fim[ data02.group(2) ] = 1
	
	#print(f'{data_ini = } ; {data_fim = }')
	
	ini = list(sorted(data_ini.keys()))[0]
	fim = list(sorted(data_fim.keys()))[-1]
	
	target = f'Info do Contribuinte - SPED EFD - {ini} a {fim}'

	final_file_csv   = target + ".csv"
	final_file_excel = target + ".xlsx"

	# unificar todos os arquivos csv no arquivo final_file_csv
	with open(final_file_csv, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
		# imprimir nomes das colunas apenas uma vez na primeira linha
		nomes_das_colunas = ';'.join(SPED_EFD_Info.colunas_selecionadas)
		csvfile.write( nomes_das_colunas + '\n' )

		# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
		for num,csv_file_path in sorted(new_dict.items()):
			print(f"arquivo[{num:2d}]: '{csv_file_path}'.")
			with open(csv_file_path, mode='r', encoding='utf-8', errors='ignore') as f:
				csvfile.write(f.read()) # read all lines at once
			if os.path.exists(csv_file_path):
				os.remove(csv_file_path)

	excel_file = CSV_to_Excel(final_file_csv, final_file_excel, verbose=False)
	excel_file.convert_csv_to_xlsx

	if os.path.exists(final_file_csv):
		os.remove(final_file_csv)
	
	print(f"\nFinalmente, foi gerado o arquivo xlsx do Excel -> '{final_file_excel}'.\n")

	end = time()

	print(f'Total Execution Time: {Total_Execution_Time(start,end)}\n')

if __name__ == '__main__':
	main()

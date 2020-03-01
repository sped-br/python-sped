#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '01 de Março de 2020 (início: 29 de Janeiro de 2020)'

# Instruções (no Linux):
# Digite em seu web brawser o endereço abaixo:

# Escolha a opção A ou B:
# A: https://github.com/claudiofsr
# Selecione o projeto 'python-sped'.
# Em seguida selecione o Branch 'relatorios'.
# B: https://github.com/claudiofsr/python-sped/tree/relatorios

# Execute os passos 1 ou 2:
# 1. Na linha de comando execute:
# > git clone -b relatorios git@github.com:claudiofsr/python-sped.git
# Em seguida, vá ao diretório python-sped:
# > cd python-sped
# 2. Em 'Clone ou download' clique em 'Download ZIP':
# Em seguida, descompacte o arquivo copiado:
# > unzip python-sped-relatorios.zip
# > cd python-sped-relatorios

# Para instalar o módulo do SPED em seu sistema execute, como superusuário:
# > python setup.py install
# Em um diretório que contenha arquivos de EFD Contribuições, 
# execute no terminal o camando:
# > efd_relatorios

import sys, os
from time import time, sleep
from sped import __version__
from sped.relatorios.find_efd_files import ReadFiles, Total_Execution_Time
from sped.relatorios.print_csv_file import SPED_EFD_Info
from sped.relatorios.convert_csv_to_xlsx import CSV_to_Excel

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

def main():

	print(f'\n\tPython Sped - versão: {__version__}\n')
	
	dir_path = os.getcwd() # CurrentDirectory
	extensao = 'txt'
	
	lista_de_arquivos = ReadFiles(root_path = dir_path, extension = extensao)
	
	arquivos_efd_contrib  = list(lista_de_arquivos.find_all_efd_contrib) # SPED EFD Contrib
	arquivos_efd_icms_ipi = list(lista_de_arquivos.find_all_efd_icmsipi) # SPED EFD ICMS_IPI
	
	arquivos_sped_efd = arquivos_efd_contrib + arquivos_efd_icms_ipi
	
	for index,file_path in enumerate(arquivos_sped_efd,1):
		print( f"{index:>6}: {file_path}")
		for attribute, value in lista_de_arquivos.get_file_info(file_path).items():
			print(f'{attribute:>25}: {value}')
	
	indice_do_arquivo = None
	
	if len(arquivos_sped_efd) > 1:
		while indice_do_arquivo is None:
			my_input = input(f"\nFavor, digite o número do arquivo SPED EFD (1 a {len(arquivos_sped_efd)}): ")
			try:
				my_input = int(my_input)
				if 1 <= my_input <= len(arquivos_sped_efd):
					indice_do_arquivo = my_input - 1
			except:
				print(f"-->Opção incorreta: '{my_input}'.")
				print(f"-->Digite um número inteiro entre 1 e {len(arquivos_sped_efd)}.")
	elif len(arquivos_sped_efd) == 1:
		indice_do_arquivo = 0
	else:
		print(f"\tDiretório atual: '{dir_path}'.")
		print(f"\tNenhum arquivo SPED EFD foi encontrado neste diretório.\n")
		exit()

	# arquivo SPED EFD
	file_path   = arquivos_sped_efd[indice_do_arquivo]
	tipo_da_efd = lista_de_arquivos.informations[file_path]['tipo']
	codificacao = lista_de_arquivos.informations[file_path]['codificação']

	filename = os.path.splitext(file_path)[0] # ('./efd_info', '.py')
	arquivo_csv   = filename + '.csv'
	arquivo_excel = filename + '.xlsx'
	
	print(f"\nSelecionado o arquivo {indice_do_arquivo + 1}: '{file_path}'.\n")
	input("Tecle Enter para gerar arquivo Excel .xlsx com informações da SPED EFD.")
	print()
	
	start = time()
	
	csv_file = SPED_EFD_Info(file_path, encoding=codificacao, efd_tipo = tipo_da_efd, verbose=False)
	
	csv_file.imprimir_arquivo_csv

	excel_file = CSV_to_Excel(arquivo_csv, arquivo_excel, verbose=False)

	excel_file.convert_csv_to_xlsx

	if os.path.exists(arquivo_csv):
		os.remove(arquivo_csv)

	end = time()
	
	print(f'\nTotal Execution Time: {Total_Execution_Time(start,end)}\n')

if __name__ == '__main__':
	main()

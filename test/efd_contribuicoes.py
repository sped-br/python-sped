#!/usr/bin/env python3

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '06 de Fevereiro de 2020 (início: 29 de Janeiro de 2020)'

import sys

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

from time import time, sleep
from efd_read_dir import ReadFiles, Total_Execution_Time
from efd_print_info import EFD_Contrib_Info

if __name__ == '__main__':
	
	dir_path = '.' # Exemplo: '/home/claudio/Documents/PISCOFINS_20150201_20150228_77744881000155_teste1.txt'
	extensao = 'txt'
	
	lista_de_arquivos = ReadFiles(root_path = dir_path, extension = extensao)
	
	arquivos_efd_contrib = list(lista_de_arquivos.find_all_efd_contrib) # SPED EFD Contrib
	
	for index,file_path in enumerate(arquivos_efd_contrib,1):
		print( f"{index:>6}: {file_path}")
		for attribute, value in lista_de_arquivos.get_file_info(file_path).items():
			print(f'{attribute:>25}: {value}')
	
	indice_do_arquivo = None
	
	if len(arquivos_efd_contrib) > 1:
		while indice_do_arquivo is None:
			my_input = input(f"\nFavor, digite o número do arquivo da EFD Contribuições (1 a {len(arquivos_efd_contrib)}): ")
			try:
				my_input = int(my_input)
				if 1 <= my_input <= len(arquivos_efd_contrib):
					indice_do_arquivo = my_input - 1
			except:
				print(f"-->Opção incorreta: '{my_input}'.")
				print(f"-->Digite um número inteiro entre 1 e {len(arquivos_efd_contrib)}.")
	elif len(arquivos_efd_contrib) == 1:
		indice_do_arquivo = 0
	else:
		print(f"\nNenhum arquivo de EFD Contribuções foi encontrado em '{dir_path}' com a extensao = {extensao}.\n")
		exit()

	# arquivo EFD Contribuições
	file_path = arquivos_efd_contrib[indice_do_arquivo]
	codif = lista_de_arquivos.informations[file_path]['codificação']
	
	print(f"\nFoi selecionado o arquivo {indice_do_arquivo + 1}: '{file_path}'\n")
	input("Tecle Enter para gerar arquivo .csv com informações da EFD ")
	print()
	
	start = time()
	
	efd = EFD_Contrib_Info(file_path, encoding=codif, verbose=False)
	
	efd.imprimir_informacoes

	end = time()
	print(f'\nTotal Execution Time: {Total_Execution_Time(start,end)} \n')


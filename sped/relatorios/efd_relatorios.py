#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '29 de Fevereiro de 2020 (início: 29 de Janeiro de 2020)'

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
from sped.relatorios.efd_read_dir import ReadFiles, Total_Execution_Time
from sped.relatorios.efd_info import SPED_EFD_Info

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

def main():

	print(f'\nPython Sped - versão: {__version__}\n')
	
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
		# https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
		basename = os.path.basename(__file__) # 'efd_relatorios'
		file_ext = os.path.splitext(__file__)[-1] # ('./efd_relatorios', '.py')
		executavel = basename.replace(file_ext, '')
		
		print(f"Execute este programa no diretório que contenha os arquivos SPED EFD.")
		print(f"Na linha de comando, digite:\n")
		print(f"\t{executavel}\n")
		exit()

	# arquivo SPED EFD
	file_path   = arquivos_sped_efd[indice_do_arquivo]
	tipo_da_efd = lista_de_arquivos.informations[file_path]['tipo']
	codificacao = lista_de_arquivos.informations[file_path]['codificação']
	
	print(f"\nFoi selecionado o arquivo {indice_do_arquivo + 1}: '{file_path}'\n")
	input("Tecle Enter para gerar arquivo .csv com informações da EFD ")
	print()
	
	start = time()
	
	efd = SPED_EFD_Info(file_path, encoding=codificacao, efd_tipo = tipo_da_efd, verbose=False)
	
	efd.imprimir_informacoes

	end = time()
	
	print(f'\nTotal Execution Time: {Total_Execution_Time(start,end)} \n')

if __name__ == '__main__':
	main()

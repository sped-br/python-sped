#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, os, glob, sys
import cchardet as chardet # pip3 install cchardet

Autor = 'Claudio Fernandes de Souza Rodrigues (claudiofsr@yahoo.com)'
Data  = '06 de Fevereiro de 2020 (início: 15 de Dezembro de 2020)'

# Versão mínima exigida: python 3.6.0
python_version = sys.version_info
if python_version < (3,6,0):
	print('versão mínima exigida do python é 3.6.0')
	print('versão atual', "%s.%s.%s" % (python_version[0],python_version[1],python_version[2]))
	exit()

# Python OOP: Atributos e Métodos (def, funções)
class ReadFiles:
	"""Retorna um dicionário com informações dos arquivos encontrados no diretório"""
	recursive = True
	current_dir = os.getcwd()
	seen_file = set() # evitar duplicidade: Is there a more Pythonic way to prevent adding a duplicate to a list?
	
	def __init__(self, root_path = None, extension = None, pattern = None):
		if root_path is None:
			self.root_path = self.current_dir
		else:
			self.root_path = root_path
		if extension is None:
			self.extension = '*'
		else:
			self.extension = extension.strip('.')
		if pattern is None:
			self.pattern = '.'
		else:
			self.pattern = pattern
		self.informations = {}  # instance attributes, dict
	
	def __repr__(self):
		return f'{self.__class__.__name__}(root_path = {self.root_path!r}, extension = {self.extension!r}, pattern = {self.pattern!r})'

	def get_file_extension(self,file_path):
		# https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
		_, file_extension = os.path.splitext(file_path)
		return file_extension

	def get_filename(self,file_path):
		# https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
		filename = os.path.basename(file_path)
		return filename
	
	# https://stackoverflow.com/questions/9629179/python-counting-lines-in-a-huge-10gb-file-as-fast-as-possible
	def count_number_of_lines(self,file_path):
		lines = 0
		try:
			with open(file_path, mode='r', encoding="utf-8", errors='ignore') as filename:
				for _ in filename: 
					lines += 1
		except FileNotFoundError:
			print('O Arquivo não existe!')
		return f'{lines:,}'.replace(',','.')
	
	# https://stackoverflow.com/questions/436220/how-to-determine-the-encoding-of-text
	# https://chardet.readthedocs.io/en/latest/usage.html
	# https://github.com/PyYoshi/cChardet
	# iconv -f WINDOWS-1252 -t UTF-8 filename.txt # iconv - convert text from one character encoding to another
	def predict_encoding(self,file_path):
		'''Predict a file's encoding using cchardet'''
		# import cchardet as chardet
		lines = []
		my_regex = rb"^\|9999\|\d+\|"  # descartar informações após a linha que contém |9999| seguido por dígitos ; b'': binary mode
		with open(file_path, mode='rb') as filename: # mode 'rb': open the file as binary data
			for line in filename:
				match_object = re.search(my_regex, line, flags=re.IGNORECASE)
				if len(lines) > 2**8 or match_object:
					#print(f'{file_path = } ; {line = }')
					break
				lines.append(line)
		rawdata = b''.join(lines)
		info = chardet.detect(rawdata) # {'encoding': 'UTF-8', 'confidence': 0.9900000095367432}
		encoding = info['encoding']
		if encoding is None or not re.search('UTF-8', encoding, flags=re.IGNORECASE):
			encoding = 'Latin-1'
		return encoding
	
	@property
	def find_all_files(self):
		# https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
		# https://docs.python.org/3/library/glob.html
		files = [f for f in glob.glob(self.root_path + '/' + f"**/*.{self.extension}", recursive = self.recursive)]
		# How to use a variable inside a regular expression?
		my_regex = f"{self.pattern}" # Literal String Interpolation, "f-strings".
		for file_path in files:
			# path.isfile: The easiest way to check if both a file exists and if it is a file.
			# seen_file:   Is there a more Pythonic way to prevent adding a duplicate to a list?
			if not os.path.isfile(file_path) or file_path.casefold() in self.seen_file:
				continue
			match_pattern = re.search(my_regex, str(file_path), flags=re.IGNORECASE)
			if match_pattern:
				self.seen_file.add(file_path.casefold())
				self.informations.setdefault(file_path, {})['tipo'] = 'Arquivo'
		return self.informations
	
	@property
	def find_all_efd_contrib(self):
		indice = 0
		# Calling one method from another within same class in Python
		return self.find_all_efd(indice)
	
	@property
	def find_all_efd_icmsipi(self):
		indice = 1
		# Calling one method from another within same class in Python
		return self.find_all_efd(indice)
	
	def find_all_efd(self,indice=0):
		if not self.informations:  # How do I check if a list/dict is empty?
			self.find_all_files  # Calling one method from another within same class in Python
		regex_efd = ["PISCOFINS", "SPED-EFD"]
		efd_type = ['EFD Contribuições', 'EFD ICMS_IPI']
		idx_nome = [8,6]
		idx_data = [6,4]
		idx_cnpj = [9,7]
		for file_path in self.informations:
			encode_info = None
			if not re.search(regex_efd[indice], file_path, flags=re.IGNORECASE):
				continue
			# Ler apenas a primeira linha para obter encode_info
			with open(file_path, mode='rb') as filename: # mode 'rb': open the file as binary data
				for line in filename:
					info = chardet.detect(line) # {'encoding': 'UTF-8', 'confidence': 0.9900000095367432}
					encode_info = info['encoding']
					#print(f'{file_path = } ; {encode_info = } ; {info = }')
					break
			# Ler apenas a primeira linha para obter informações do registro de abertura '0000'.
			with open(file_path, mode='r', encoding=encode_info, errors='ignore') as filename: # encoding='latin-1','UTF-8'
				for line in filename:
					campos = line.strip().split('|')
					if len(campos) <= 10:
						break
					campo_registro = campos[1] # A primeira linha deve conter o registro '0000'
					campo_nome = campos[ idx_nome[indice] ]
					campo_data = campos[ idx_data[indice] ]
					campo_cnpj = campos[ idx_cnpj[indice] ] # o campo CNPJ deve conter 14 dígitos
					match_regi = re.search(  '0000', campo_registro)
					match_cnpj = re.search(r'(\D|^)\d{14}(\D|$)', campo_cnpj)
					match_data = re.search(r'(\D|^)\d{8}(\D|$)', campo_data)
					if match_regi and match_cnpj and match_data:
						self.informations[file_path]['tipo'] = efd_type[indice]
						self.informations[file_path]['NOME'] = campo_nome
						self.informations[file_path]['CNPJ'] = "%s.%s.%s/%s-%s" % (campo_cnpj[0:2],campo_cnpj[2:5],campo_cnpj[5:8],campo_cnpj[8:12],campo_cnpj[12:14])
						self.informations[file_path]['DT_INI'] = "%s/%s/%s" % (campo_data[0:2],campo_data[2:4],campo_data[4:8])
					break
		# Filter a Dictionary by values in Python using dict comprehension
		return {key: value for (key, value) in sorted(self.informations.items()) if value['tipo'] == efd_type[indice]}
		
	def get_file_info(self,file_path):
		self.informations[file_path]['extensão'        ] = self.get_file_extension(file_path)
		self.informations[file_path]['codificação'     ] = self.predict_encoding(file_path)
		self.informations[file_path]['número de linhas'] = self.count_number_of_lines(file_path)
		return self.informations[file_path]

from time import time, sleep

def Total_Execution_Time(start,end=None):
	'''
	How to format elapsed time from seconds to hours, minutes, seconds and milliseconds in Python?
	https://stackoverflow.com/questions/27779677/how-to-format-elapsed-time-from-seconds-to-hours-minutes-seconds-and-milliseco
	https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module/46544199
	https://blog.softhints.com/python-test-performance-and-measure-time-elapsed-in-seconds/
	'''
	if end is None:
		end = time()
	hours, rem = divmod(end-start, 3600)
	minutes, seconds = divmod(rem, 60)
	return f"{int(hours):02d}h:{int(minutes):02d}m:{seconds:07.4f}s"


if __name__ == '__main__':

	start = time()

	#print(f'\n{ReadFiles.__dict__ = } \n')

	lista_de_arquivos0 = ReadFiles(root_path = '.')
	lista_de_arquivos1 = ReadFiles(root_path = 'EFD Contribuicoes', extension = 'txt', pattern = 'PISCOFINS')
	lista_de_arquivos2 = ReadFiles(root_path = 'EFD ICMS_IPI-ADM',  extension = 'txt', pattern = 'SPED-EFD' )
	
	arquivos_da_efd = [lista_de_arquivos0, lista_de_arquivos1, lista_de_arquivos2]

	for lista_de_arquivos in arquivos_da_efd:
		print(f'\nlista_de_arquivos = {lista_de_arquivos}:\n')
		
		print(f'lista_de_arquivos.find_all_files = {lista_de_arquivos.find_all_files} ; len(lista_de_arquivos.informations) = {len(lista_de_arquivos.informations)}\n')
		
		# SPED EFD Contrib:
		for index,file_path in enumerate(lista_de_arquivos.find_all_efd_contrib,1):
			print( f"{index:>6}: {file_path} ; tipo = {lista_de_arquivos.informations[file_path]['tipo']}" )
			#continue
			for attribute, value in lista_de_arquivos.get_file_info(file_path).items():
				print(f'{attribute:>30}: {value}')
		
		# SPED EFD ICMS_IPI:
		for index,file_path in enumerate(lista_de_arquivos.find_all_efd_icmsipi,1):
			print( f"{index:>6}: {file_path} ; tipo = {lista_de_arquivos.informations[file_path]['tipo']}" )
			#continue
			for attribute, value in lista_de_arquivos.get_file_info(file_path).items():
				print(f'{attribute:>30}: {value}')

	end = time()
	print(f'\nTotal Execution Time: {Total_Execution_Time(start,end)} \n')


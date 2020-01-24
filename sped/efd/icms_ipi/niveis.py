#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Object that acts like a dictionary

class NiveisDosRegistros:
	"""
	Turns a dictionary into a class
	O arquivo digital da EFD-Contribuições ou da EFD-ICMS_IPI está organizado em Blocos.
	Cada um dos Blocos é composto de acordo com a Tabela de Registros e 
	de obrigatoriedade de apresentação.
	Segue o número do nível de cada registro dos blocos.    
	"""
	
	def __init__(self, efd = None):
		
		self.nivel_do_registro = {}
		
		if efd is None or efd == 'efd_contrib':
			self.nivel_do_registro = self.efd_contrib()  # Calling one method from another within same class in Python
		elif efd == 'efd_icms_ipi':
			self.nivel_do_registro = self.efd_icms_ipi()
	
	def efd_contrib(self):
		
		nivel = {}

		nivel['0000'] = 0
		nivel['0001'] = 1
		nivel['0035'] = 2
		nivel['0100'] = 2
		nivel['0110'] = 2
		nivel['0111'] = 3
		nivel['0120'] = 2
		nivel['0140'] = 2
		nivel['0145'] = 3
		nivel['0150'] = 3
		nivel['0190'] = 3
		nivel['0200'] = 3
		nivel['0205'] = 4
		nivel['0206'] = 4
		nivel['0208'] = 4
		nivel['0400'] = 3
		nivel['0450'] = 3
		nivel['0500'] = 2
		nivel['0600'] = 2
		nivel['0900'] = 2
		nivel['0990'] = 1

		nivel['A001'] = 1
		nivel['A010'] = 2
		nivel['A100'] = 3
		nivel['A110'] = 4
		nivel['A111'] = 4
		nivel['A120'] = 4
		nivel['A170'] = 4
		nivel['A990'] = 1

		nivel['B001'] = 1
		nivel['B020'] = 2
		nivel['B025'] = 3
		nivel['B030'] = 2
		nivel['B035'] = 2
		nivel['B350'] = 2
		nivel['B420'] = 2
		nivel['B440'] = 2
		nivel['B460'] = 2
		nivel['B470'] = 2
		nivel['B500'] = 2
		nivel['B510'] = 3
		nivel['B990'] = 1

		nivel['C001'] = 1
		nivel['C010'] = 2
		nivel['C100'] = 3
		nivel['C110'] = 4
		nivel['C111'] = 4
		nivel['C120'] = 4
		nivel['C170'] = 4
		nivel['C175'] = 4
		nivel['C180'] = 3
		nivel['C181'] = 4
		nivel['C185'] = 4
		nivel['C188'] = 4
		nivel['C190'] = 3
		nivel['C191'] = 4
		nivel['C195'] = 4
		nivel['C198'] = 4
		nivel['C199'] = 4
		nivel['C380'] = 3
		nivel['C381'] = 4
		nivel['C385'] = 4
		nivel['C395'] = 3
		nivel['C396'] = 4
		nivel['C400'] = 3
		nivel['C405'] = 4
		nivel['C481'] = 5
		nivel['C485'] = 5
		nivel['C489'] = 4
		nivel['C490'] = 3
		nivel['C491'] = 4
		nivel['C495'] = 4
		nivel['C499'] = 4
		nivel['C500'] = 3
		nivel['C501'] = 4
		nivel['C505'] = 4
		nivel['C509'] = 4
		nivel['C600'] = 3
		nivel['C601'] = 4
		nivel['C605'] = 4
		nivel['C609'] = 4
		nivel['C800'] = 3
		nivel['C810'] = 4
		nivel['C820'] = 4
		nivel['C830'] = 4
		nivel['C860'] = 3
		nivel['C870'] = 4
		nivel['C880'] = 4
		nivel['C890'] = 4
		nivel['C990'] = 1

		nivel['D001'] = 1
		nivel['D010'] = 2
		nivel['D100'] = 3
		nivel['D101'] = 4
		nivel['D105'] = 4
		nivel['D111'] = 4
		nivel['D200'] = 3
		nivel['D201'] = 4
		nivel['D205'] = 4
		nivel['D209'] = 4
		nivel['D300'] = 3
		nivel['D309'] = 4
		nivel['D350'] = 3
		nivel['D359'] = 4
		nivel['D500'] = 3
		nivel['D501'] = 4
		nivel['D505'] = 4
		nivel['D509'] = 4
		nivel['D600'] = 3
		nivel['D601'] = 4
		nivel['D605'] = 4
		nivel['D609'] = 4
		nivel['D990'] = 1

		nivel['F001'] = 1
		nivel['F010'] = 2
		nivel['F100'] = 3
		nivel['F111'] = 4
		nivel['F120'] = 3
		nivel['F129'] = 4
		nivel['F130'] = 3
		nivel['F139'] = 4
		nivel['F150'] = 3
		nivel['F200'] = 3
		nivel['F205'] = 4
		nivel['F210'] = 4
		nivel['F211'] = 4
		nivel['F500'] = 3
		nivel['F509'] = 4
		nivel['F510'] = 3
		nivel['F519'] = 4
		nivel['F525'] = 3
		nivel['F550'] = 3
		nivel['F559'] = 4
		nivel['F560'] = 3
		nivel['F569'] = 4
		nivel['F600'] = 3
		nivel['F700'] = 3
		nivel['F800'] = 3
		nivel['F990'] = 1

		nivel['I001'] = 1
		nivel['I010'] = 2
		nivel['I100'] = 3
		nivel['I199'] = 4
		nivel['I200'] = 4
		nivel['I299'] = 5
		nivel['I300'] = 5
		nivel['I399'] = 6
		nivel['I990'] = 1

		nivel['M001'] = 1
		nivel['M100'] = 2
		nivel['M105'] = 3
		nivel['M110'] = 3
		nivel['M115'] = 4
		nivel['M200'] = 2
		nivel['M205'] = 3
		nivel['M210'] = 3
		nivel['M211'] = 4
		nivel['M220'] = 4
		nivel['M225'] = 5
		nivel['M230'] = 4
		nivel['M300'] = 2
		nivel['M350'] = 2
		nivel['M400'] = 2
		nivel['M410'] = 3
		nivel['M500'] = 2
		nivel['M505'] = 3
		nivel['M510'] = 3
		nivel['M515'] = 4
		nivel['M600'] = 2
		nivel['M605'] = 3
		nivel['M610'] = 3
		nivel['M611'] = 4
		nivel['M620'] = 4
		nivel['M625'] = 5
		nivel['M630'] = 4
		nivel['M700'] = 2
		nivel['M800'] = 2
		nivel['M810'] = 3
		nivel['M990'] = 1

		nivel['P001'] = 1
		nivel['P010'] = 2
		nivel['P100'] = 3
		nivel['P110'] = 4
		nivel['P199'] = 4
		nivel['P200'] = 2
		nivel['P210'] = 3
		nivel['P990'] = 1

		nivel['1001'] = 1
		nivel['1010'] = 2
		nivel['1011'] = 3
		nivel['1020'] = 2
		nivel['1100'] = 2
		nivel['1101'] = 3
		nivel['1102'] = 4
		nivel['1200'] = 2
		nivel['1210'] = 3
		nivel['1220'] = 3
		nivel['1300'] = 2
		nivel['1500'] = 2
		nivel['1501'] = 3
		nivel['1502'] = 4
		nivel['1600'] = 2
		nivel['1610'] = 3
		nivel['1620'] = 3
		nivel['1700'] = 2
		nivel['1800'] = 2
		nivel['1809'] = 3
		nivel['1900'] = 2
		nivel['1990'] = 1

		nivel['9001'] = 1
		nivel['9900'] = 2
		nivel['9990'] = 1
		nivel['9999'] = 0
		
		return nivel
	
	
	def efd_icms_ipi(self):
		
		nivel = {}
		
		nivel['0000'] = 0
		nivel['0001'] = 1
		nivel['0005'] = 2
		nivel['0015'] = 2
		nivel['0100'] = 2
		nivel['0150'] = 2
		nivel['0175'] = 3
		nivel['0190'] = 2
		nivel['0200'] = 2
		nivel['0205'] = 3
		nivel['0206'] = 3
		nivel['0210'] = 3
		nivel['0220'] = 3
		nivel['0300'] = 2
		nivel['0305'] = 3
		nivel['0400'] = 2
		nivel['0450'] = 2
		nivel['0460'] = 2
		nivel['0500'] = 2
		nivel['0600'] = 2
		nivel['0990'] = 1

		nivel['B001'] = 1
		nivel['B020'] = 2
		nivel['B025'] = 3
		nivel['B030'] = 2
		nivel['B035'] = 1
		nivel['B350'] = 2
		nivel['B420'] = 2
		nivel['B440'] = 2
		nivel['B460'] = 2
		nivel['B470'] = 2
		nivel['B500'] = 2
		nivel['B510'] = 3
		nivel['B990'] = 1

		nivel['C001'] = 1
		nivel['C100'] = 2
		nivel['C101'] = 3
		nivel['C105'] = 3
		nivel['C110'] = 3
		nivel['C111'] = 4
		nivel['C112'] = 4
		nivel['C113'] = 4
		nivel['C114'] = 4
		nivel['C115'] = 4
		nivel['C116'] = 4
		nivel['C120'] = 3
		nivel['C130'] = 3
		nivel['C140'] = 3
		nivel['C141'] = 4
		nivel['C160'] = 3
		nivel['C165'] = 3
		nivel['C170'] = 3
		nivel['C171'] = 4
		nivel['C172'] = 4
		nivel['C173'] = 4
		nivel['C174'] = 4
		nivel['C175'] = 4
		nivel['C176'] = 4
		nivel['C177'] = 4
		nivel['C178'] = 4
		nivel['C179'] = 4
		nivel['C190'] = 3
		nivel['C191'] = 4
		nivel['C195'] = 3
		nivel['C197'] = 4
		nivel['C300'] = 2
		nivel['C310'] = 3
		nivel['C320'] = 3
		nivel['C321'] = 4
		nivel['C350'] = 2

		nivel['C370'] = 3
		nivel['C390'] = 3
		nivel['C400'] = 2
		nivel['C405'] = 3
		nivel['C410'] = 4
		nivel['C420'] = 4
		nivel['C425'] = 5
		nivel['C460'] = 4
		nivel['C465'] = 5
		nivel['C470'] = 5
		nivel['C490'] = 4
		nivel['C495'] = 2
		nivel['C500'] = 2
		nivel['C510'] = 3
		nivel['C590'] = 3
		nivel['C600'] = 2
		nivel['C601'] = 3
		nivel['C610'] = 3
		nivel['C690'] = 3
		nivel['C700'] = 2
		nivel['C790'] = 3
		nivel['C791'] = 4
		nivel['C800'] = 2
		nivel['C850'] = 3
		nivel['C860'] = 2
		nivel['C890'] = 3
		nivel['C990'] = 1

		nivel['D001'] = 1
		nivel['D100'] = 2
		nivel['D101'] = 3
		nivel['D110'] = 3
		nivel['D120'] = 4
		nivel['D130'] = 3
		nivel['D140'] = 3
		nivel['D150'] = 3
		nivel['D160'] = 3
		nivel['D161'] = 4
		nivel['D162'] = 4
		nivel['D170'] = 3
		nivel['D180'] = 3
		nivel['D190'] = 3
		nivel['D195'] = 3
		nivel['D197'] = 4
		nivel['D300'] = 2
		nivel['D301'] = 3
		nivel['D310'] = 3
		nivel['D350'] = 2
		nivel['D355'] = 3
		nivel['D360'] = 4
		nivel['D365'] = 4
		nivel['D370'] = 5
		nivel['D390'] = 4
		nivel['D400'] = 2
		nivel['D410'] = 3
		nivel['D411'] = 4
		nivel['D420'] = 3
		nivel['D500'] = 2
		nivel['D510'] = 3
		nivel['D530'] = 3
		nivel['D590'] = 3
		nivel['D600'] = 2
		nivel['D610'] = 3

		nivel['D690'] = 3
		nivel['D695'] = 2
		nivel['D696'] = 3
		nivel['D697'] = 4
		nivel['D990'] = 1

		nivel['E001'] = 1
		nivel['E100'] = 2
		nivel['E110'] = 3
		nivel['E111'] = 4
		nivel['E112'] = 5
		nivel['E113'] = 5
		nivel['E115'] = 4
		nivel['E116'] = 4
		nivel['E200'] = 2
		nivel['E210'] = 3
		nivel['E220'] = 4
		nivel['E230'] = 5
		nivel['E240'] = 5
		nivel['E250'] = 4
		nivel['E300'] = 2
		nivel['E310'] = 3
		nivel['E311'] = 4
		nivel['E312'] = 5
		nivel['E313'] = 5
		nivel['E316'] = 4
		nivel['E500'] = 2
		nivel['E510'] = 3
		nivel['E520'] = 3
		nivel['E530'] = 4
		nivel['E531'] = 5
		nivel['E990'] = 1

		nivel['G001'] = 1
		nivel['G110'] = 2

		nivel['G125'] = 3
		nivel['G126'] = 4
		nivel['G130'] = 4
		nivel['G140'] = 5
		nivel['G990'] = 1

		nivel['H001'] = 1
		nivel['H005'] = 2
		nivel['H010'] = 3
		nivel['H020'] = 4
		nivel['H990'] = 1

		nivel['K001'] = 1
		nivel['K100'] = 2
		nivel['K200'] = 3
		nivel['K210'] = 3
		nivel['K215'] = 4
		nivel['K220'] = 3
		nivel['K230'] = 3
		nivel['K235'] = 4
		nivel['K250'] = 3
		nivel['K255'] = 4
		nivel['K260'] = 3
		nivel['K265'] = 4
		nivel['K270'] = 3
		nivel['K275'] = 4
		nivel['K280'] = 3
		nivel['K290'] = 3
		nivel['K291'] = 4
		nivel['K292'] = 4
		nivel['K300'] = 3
		nivel['K301'] = 4
		nivel['K302'] = 4
		nivel['K990'] = 1

		nivel['1001'] = 1
		nivel['1010'] = 2
		nivel['1100'] = 2
		nivel['1105'] = 3

		nivel['1110'] = 4
		nivel['1200'] = 2
		nivel['1210'] = 3
		nivel['1300'] = 2
		nivel['1310'] = 3
		nivel['1320'] = 4
		nivel['1350'] = 2
		nivel['1360'] = 3
		nivel['1370'] = 3
		nivel['1390'] = 2
		nivel['1391'] = 3
		nivel['1400'] = 2
		nivel['1500'] = 2
		nivel['1510'] = 3
		nivel['1600'] = 2
		nivel['1700'] = 2
		nivel['1710'] = 3
		nivel['1800'] = 2
		nivel['1900'] = 2
		nivel['1910'] = 3
		nivel['1920'] = 4
		nivel['1921'] = 5
		nivel['1922'] = 6
		nivel['1923'] = 6
		nivel['1925'] = 5
		nivel['1926'] = 5
		nivel['1960'] = 2
		nivel['1970'] = 2
		nivel['1975'] = 3
		nivel['1980'] = 2
		nivel['1990'] = 1

		nivel['9001'] = 1
		nivel['9900'] = 2
		nivel['9990'] = 1
		nivel['9999'] = 0

		return nivel

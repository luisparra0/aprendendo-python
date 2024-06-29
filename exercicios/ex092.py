'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
ctps = int(input('Carteira de trabalho (0 não tem): '))
dados['ctps'] = ctps
if ctps != 0:
    dados['contratada'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    idade_aposenta = 35 - (datetime.now().year - dados['contratada']) + dados['idade']
    dados['aposentadoria'] = idade_aposenta


for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


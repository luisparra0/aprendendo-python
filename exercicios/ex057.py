'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o sexo[M/F] da pessoa: ')).strip()[0]

while sexo not in 'MmFf':
    sexo = str(input('Comando inválido.\nTente novamente: ')).strip[0]
print(f'Pessoa do sexo {sexo.upper()} registrada com sucesso. ')

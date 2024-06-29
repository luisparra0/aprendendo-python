
'''Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {'nome':'','média': 0,'situação': ''}

nom = str(input('Nome: '))
aluno['nome'] = nom
med = float(input(f'Média de {nom}: '))
aluno['média'] = med

if med >= 7.0:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'


print('-=' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

'''print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["média"]}')
print(f'Situação é igual a {aluno["situação"]}')'''
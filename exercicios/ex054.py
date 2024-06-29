'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import datetime
#datetime.now().year

cont = 0

for c in range(1,8):
    idade = int(input(f'Digite o {c}º ano de nascimento: '))
    if datetime.now().year - idade < 18:
        cont +=1

print(f'Ao todo, {cont} pessoas são menores de idade')


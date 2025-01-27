'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime
nasc = int(input('Em que ano nasceu? '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nasc
if idade == 18:
    print(f'Você tem 18 anos! Hora de se alistar')
elif idade < 18:
    print(f'Você tem {idade} anos! Ainda não está na hora. Apenas no ano que for completar 18.')
else:
    print(f'Você tem {idade} ! Já passou da hora!')
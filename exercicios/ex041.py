'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import datetime

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.now().year - ano

if idade <= 9:
    print(f'Idade {idade} anos. Categoria MIRIM')
elif idade <=14 :
    print(f'Idade {idade} anos. Categoria INFTANTIL')
elif idade <=19:
    print(f'Idade {idade} anos. Categoria JÚNIOR')
elif idade <=25:
    print(f'Idade {idade} anos. Categoria SÊNIOR')
else:
    print(f'Idade {idade}. Categoria MASTER')
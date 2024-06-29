'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

resultado = {'Jogador1': randint(1,6),
             'Jogador2': randint(1,6),
             'Jogador3': randint(1,6),
             'Jogador4': randint(1,6),
             }

ranking = list()

print('Valores sorteados:')
for k, v in resultado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.4)
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True) #itemgetter(0) em ordem de chave
                                                                     #itemgetter(1) em ordem de valor


for i, v in enumerate(ranking): #i = indice da lista, v = valor
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')





#for k, v in resultado.items():
    
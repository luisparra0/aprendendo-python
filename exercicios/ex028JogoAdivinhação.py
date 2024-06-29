#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

print('-' + '=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' + '=--'*20)

numpc = random.randint(0,5) # Faz o computador 'pensar'

print(numpc)
num = int(input('Em que número eu pensei? ')) # Usuário tenta adivinhar
print('PROCESSANDO...')
time.sleep(3)

if num == numpc:
    print('Parabéns! Você ganhou ! ! !')

else:
    print('GANHEEEEI! Pensei no número {} e não no {}!'.format(numpc,num))



#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
op = int(input('Qual é sua jogada? '))
sleep(0.7)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.3)

pc = randint(0,2)

if op == 0 and pc == 1:
    print('Computador jogou PAPEL')
    print('Você jogou PEDRA')
    print('COMPUTADOR VENCEU')

elif op == 0 and pc == 2:
    print('Computador jogou TESOURA')
    print('Você jogou PEDRA')
    print('VOCÊ VENCEU')
    
elif op == 1 and pc == 0:
    print('Computador jogou PEDRA')
    print('Você jogou PAPEL')
    print('VOCÊ VENCEU')
    
elif op == 1 and pc == 2:
    print('Computador jogou TESOURA')
    print('Você jogou PAPEL')
    print('COMPUTADOR VENCEU')

elif op == 2 and pc == 0:
    print('Computador jogou PEDRA')
    print('Você jogou TESOURA')
    print('Computador VENCEU')

elif op == 2 and pc == 1:
    print('Computador jogou PAPEL')
    print('Você jogou TESOURA')
    print('VOCÊ VENCEU')
    

    
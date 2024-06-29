#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
op = int(input('Qual é sua jogada? '))
sleep(0.7)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.3)

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[op]}')

if computador == 0: #computador jogou Pedra
    if op == 0:
        print('EMPATE')
    
    elif op == 1:
        print('JOGADOR VENCE')
    
    elif op == 2:
        print('COMPUTADOR VENCE')
        
    else:
        print('JOGADA INVÁLIDA')
        
if computador == 1: #computador jogou Papel
    if op == 0:
        print('COMPUTADOR VENCE')
    
    elif op == 1:
        print('EMPATE')
    
    elif op == 2:
        print('JOGADOR VENCE')
        
    else:
        print('JOGADA INVÁLIDA')
if computador == 2: #computador jogou Tesoura
    if op == 0:
        print('JOGADOR VENCE')
    
    elif op == 1:
        print('COMPUTADOR VENCE')
    
    elif op == 2:
        print('EMPATE')
        
    else:
        print('JOGADA INVÁLIDA')
'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''

term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = term + (10-1)*raz

for c in range (term, decimo, raz):
    print(c)
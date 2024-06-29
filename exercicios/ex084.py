'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                              
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

pessoas = [] # lista para colocar os dados nome e peso
cont = 0 #contador para a quantidade de pessoas
mais = menos = 0 #mais e menos pesadas

while True:
    nome = str(input('Nome: '))
    cont += 1
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    
    
    if cont == 1:
        mais = menos = peso
    else:
        if peso > mais:
            mais = peso
        elif peso < menos:
            menos = peso
            
    
    continua = str(input('Continua? '))
    if continua in 'Nn':
        break
    
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi: {mais}kg')
for maior in pessoas:
    if maior[1] == mais:
        print(f'{maior[0]}')
print(f'O menor peso foi: {menos}kg')
for menor in pessoas:
    if menor[1] == menos:
        print(f'{menor[0]}')



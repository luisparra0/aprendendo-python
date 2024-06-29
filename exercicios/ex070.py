'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = mil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ').strip())
    cont +=1
    preco = float(input('Preço: R$'))
    total += preco
    if preco >= 1000:
        mil +=1
    
    if cont == 1:
        menor = preco
        barato = nome
    elif preco < menor:
        menor = preco
        barato = nome
    
    continua = ''
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]').strip().upper()[0])
        if continua == 'N':
            break
    
    
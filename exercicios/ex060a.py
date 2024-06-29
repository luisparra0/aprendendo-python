#Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

num = int(input('Digite um número para calcular sua fatorial: '))

f = factorial(num)

print(f'A fatorial de {num} é {f}')
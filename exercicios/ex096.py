''' Faça um programa que tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.'''




def area (b, h):
    print(f'A área é igual a: {b*h}m²')

base = float(input('Digite a base do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area(base,altura)
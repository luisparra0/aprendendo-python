#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow
cat1 = float(input('Comprimento cateto oporto: '))
cat2 = float(input('Comprimento cateto oporto: '))

hipo = sqrt(pow(cat1,2) + pow(cat2,2))

print('A hipotenusa vai medir: {:.2f}'.format(hipo))


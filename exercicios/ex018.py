#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse ângulo.

import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'. format(ang, seno))

cosseno = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(ang, cosseno))

tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o TANGENTE de {:.2f}'. format(ang, tangente))
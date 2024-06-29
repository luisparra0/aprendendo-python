#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numpc = randint(0,10)
print(numpc)
usuario = int(input('Tente adivinhar o número que estou pensando: '))

while numpc != usuario:
    if numpc > usuario:
        usuario = int(input('Erroooooou! O número que pensei é menor. Tente novamente: '))

    else:
        usuario = int(input('Erroooooou! O número que pensei é menor. Tente novamente: '))
        

print('AAAA EU PERDI!')
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano para saber se é ou não bissexto: '))
if ano % 4 ==0 and ano % 100 !=0 or ano % 400 == 0:
    print('É bissexto!')
else:
    print('Não é :(')
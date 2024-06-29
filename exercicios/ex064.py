''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final,mostre quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag)'''

n = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = n
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    cont += 1

print(f'A soma dos {cont} números digitados é {soma - 999}')
    
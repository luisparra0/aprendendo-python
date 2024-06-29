#Faça um programa que leia um número inteiro e diga 
# se ele é ou não um número primo.

num = int(input('Digite um número para saber se é Primo: '))
tot = 0
for c in range(1, num+1):
    if num%c==0:
        tot +=1

if tot ==2:
    print('é primo')
else:
    print('Não é primo')
                
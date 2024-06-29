'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

maior = 0
homem = 0
mulher = 0

while True:
    nome = str(input('Digite o nome: ').strip())
    sexo = str(input('Digite o sexo: [M/F]').strip().upper()[0])
    idade = int(input('Idade: '))
    if idade < 20 and sexo =='F':
        mulher+=1
        if idade > 18:
            maior+=1
    elif idade >= 18:
        maior +=1
    elif sexo =='M':
        homem +=1
    
    continua = str(input('Deseja continuar? [S/N]').strip().upper()[0])
    while continua not in 'SN':
        continua = str(input('Resposta inválida. Deseja continuar? [S/N]').strip().upper()[0])
    if continua == 'N':
        break
    
print(f'{maior} pessoas maior de idade; {homem} homens cadastrados; {mulher} mulheres tem menos de 20 anos.')
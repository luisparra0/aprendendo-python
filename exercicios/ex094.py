'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres  
D) Uma lista de pessoas com idade acima da média'''


dicio = {}
lista = []
media = 0
mulher = []
acima_media = []

while True:
    nome = str(input('Nome: '))
    dicio['nome'] = nome   
    sexo = str(input('Sexo: [M/F]'))
    while sexo not in 'MmFf':
        print('ERRO! Responda apenas com M ou F')
        sexo = str(input('Sexo: [M/F]'))
    dicio['sexo'] = sexo
    if sexo in 'Ff':
        mulher.append(nome)
        
       
    idade = int(input('Idade: '))
    dicio['idade'] = idade
    media += idade # no final divide por len(lista) e tem a média
    
    lista.append(dicio.copy())
    continua = str(input('Quer continuar? [S/N]').strip().lower()[0])
    while continua not in 'sn':
        print('ERRO! Responda apenas com S ou N')
        continua = str(input('Quer continuar? [S/N]').strip().lower()[0])
    if continua == 'n':
        break

print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas. ')
print(f'B) A média de idade é de {media/len(lista)} anos.')
print(f'C) As mulheres cadastradas foram: ')
for c in mulher:
    print(c , end=' ,')

print(f'\nLista de pessoas que estão acima da média: ')
for pessoa in lista:
    if pessoa['idade'] > (media / len(lista)):
        acima_media.append(pessoa)
for pessoa in acima_media:
    print(f"Nome: {pessoa['nome']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}")

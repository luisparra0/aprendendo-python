
''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome 
do homem mais velho e quantas mulheres têm menos de 20 anos.'''
velho = 0
nomehomem = 0
mulher = 0

for c in range(1,5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo [M/F] da {c}ª pessoa: ')).strip()
    
    idade+= idade
    
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        mulher+= 1

print(f'A média de idade do grupo é {idade/3}')
print(nomehomem)
print(mulher)
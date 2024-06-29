'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares 
e ímpares em ordem crescente.'''

numeros = [[], []]

for c in range(1,8):
    num = int(input(f'Valor {c} : '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
        
print(f'Números separados em duas listas: \n{numeros}')
print('-'*30) 

numeros[0].sort()
numeros[1].sort()

print(f'Pares: {numeros[0]}')

print('-'*30) 

print(f'Ímpares: {numeros[1]}')
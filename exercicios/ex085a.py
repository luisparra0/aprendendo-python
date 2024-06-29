
'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares 
e ímpares em ordem crescente.'''

valores = list()
par = list()
impar = list()


for c in range (0,7):
    num = int(input(f'Valor {c + 1}: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

valores.append(par[:])
valores.append(impar[:])

print(valores)
print('-'*30)
par.sort()
print(par)
print('-'*30)
impar.sort()
print(impar)
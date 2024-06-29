'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                               
A) Quantos números foram digitados.                                                                                                                   
B) A lista de valores, ordenada de forma decrescente.                                                                                         
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []


while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continua = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if continua == 'N':
        break
    

if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('Não foi digitado o valor 5.')

print(f'A lista abaixo contém {len(lista)} elementos')

lista.sort(reverse=True)
print(lista)

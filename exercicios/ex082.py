'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter 
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
par = []
impar = []
while True:
    num = int(input('Digite um valor para colocar na lista: '))
    lista.append(num)
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num)
    continua = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    
    if continua == 'N':
        break
   
print(lista)
print(par)
print(impar)
   
   
   
   
   
   
   
   
   
   # par = lista [:]
   # impar = lista[:]
    
    
    
    
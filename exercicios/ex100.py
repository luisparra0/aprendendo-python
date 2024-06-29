'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda  
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior'''




from random import randint


numeros = []
def sorteia():
    print('Sorteando 5 valores: ', end='')
    for c in range(0,5):
       num = randint(1,10)
       print(num, end=' ')
       numeros.append(num)
   
    
def somaPar():
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma+=v
    print(f'\nSomando os valores pares de {numeros}, temos {soma}')
    
sorteia()
somaPar()



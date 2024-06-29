

'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                  
a) de 1 até 10, de 1 em 1          
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada
'''


def maior(*num):
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
    print(f' foram informados {len(num)} ao todo')
    #print(f'O maior número é informado é o {max(num)}')
    print('-='*20)

print('-='*20)   
maior(12,3,4,1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()



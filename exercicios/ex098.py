
'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, 
fim e passo. Seu programa tem que realizar três contagens através da função criada:    
a) de 1 até 10, de 1 em 1                                                                 
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada
'''



from time import sleep

def contador(ini, fim, passo):
    if passo <0:
        passo *= -1
        
    if passo == 0:
        passo = 1
        
    print('-='*20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    
    
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += passo
            sleep(0.5)
        print("FIM!")
    
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo        
            sleep(0.5)
        print("FIM!")
    
        
    print('FIM!')
    print('-='*20)
contador(1,10,1)
contador(10,0,2)

print('AGORA É SUA VEZ!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

    


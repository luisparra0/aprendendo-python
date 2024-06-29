'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

#An = A1 + raz(N-1)

term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
rep = 0
total = 0
mais = 10
while mais !=0:
    total+=mais
    while rep <= total :
        print(f'{term}')
        term += raz
        rep += 1

    mais = int(input('Mais quantos termos você quer mostrar??'))
    
print(f'Progressão finalizada com {total} termos')

        

#if x != 0:
    




'''while x != 0:
    print(f'{term}')
    term += raz
    rep ==x
    '''
        
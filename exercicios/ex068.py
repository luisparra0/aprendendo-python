
from random import randint


cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

while True:
    val = int(input('Digite um valor: '))
    pc = randint(0,11)
    soma = val+pc
    
    jogada = str(input('Par ou ímpar? [P/I]').strip().upper()[0])
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I]').strip().upper()[0])
        
    if jogada =='P':
        if soma % 2 == 0:
            print(f'Você ganhou! Eu joguei {pc} e você {val}')
            cont+=1
        else:
            print(f'Você perdeu :C . Eu joguei {pc} e você {val}')
            break
            
            
    if jogada =='I':
        if soma%2 ==1:
            print(f'Você ganhou! Eu joguei {pc} e você {val}')
            cont+=1
        else:
            print(f'Você perdeu :( . Eu joguei {pc} e você {val}')
            break

print(f'Você me venceu {cont} vezes !')
        
    

    
    
    
    
    
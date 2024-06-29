'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opc = 1
while opc <= 5 and opc >= 1:
    opc = int(input(f'''\n Certo. Números digitados: {num1} e {num2} .
                Agora digite:
                 
                [ 1 ] somar

                [ 2 ] multiplicar

                [ 3 ] maior

                [ 4 ] novos números

                [ 5 ] sair do programa 
                
                Qual sua opção: ''' ))
    if opc == 1:
        print(f'\nVocê escolheu soma. A soma entre {num1} e {num2} é : {num1+num2}')
    elif opc == 2:
        print(f'\nVocê escolheu multiplicar. A multiplicação entre {num1} e {num2} é : {num1*num2}')
    elif opc == 3:
        print(f'\nVocê escolheu saber quem é o maior.')
        if num1 > num2:
            print(f'O maior é {num1}.')
        else:
            print(f'O maior é {num2}')
    elif opc == 4:
        num1 = int(input('Novo valor 1: '))
        num2 = int(input('Novo valor 2: '))
    elif opc == 5:
        print('Obrigado pela participação!')
        print('Fim')
        break
    else:
        print('Opção inválida.')
        
    print('Fim!')
    
    

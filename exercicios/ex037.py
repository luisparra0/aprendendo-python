'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
escolha =str(input('Número escolhido foi {}. Agora digite 1 para conversão em binário, 2 para octal ou 3 para hexadecimal'.format(num)))
if escolha == '1':
    print('Vc escolheu conversão para binário')
elif escolha == '2':
    print('Vc escolheu conversão para octal')
elif escolha == 'e':
    print('Vc escolheu conversão para hexadecimal')
    
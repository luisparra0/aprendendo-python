'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2 :
    print(f'O {num1} é maior que o {num2}')
elif num2 > num1 :
    print(f'O {num2} é maior que o {num1}')
else:
    print(f'O {num1} e o {num2} são iguais')

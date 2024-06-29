'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

from time import sleep
valor = float(input('Digite o valor da compra: '))

print('''Digite 1 para pagamento à vista em dinheiro com 10% de desconto\n
Digite 2 para pagamento à vista no cartão com 5% de desconto \n
Digite 3 para pagamento em 2x sem juros no cartão\n
Digite 4 para pagamento em 3x ou mais, com 20% de juros no cartão''')
op = int(input())

print('PROCESSANDO...')
sleep(3)

if op == 1:    
    valor -= valor*0.1
    print(f'O valor da compra será de R${valor :.2f} à vista em dinheiro!')
elif op ==2:
    valor -= valor*0.05
    print(f'O valor da compra será de R${valor :.2f} à vista no cartão!')
elif op == 3:
    parcela = valor/2
    print(f'O valor da compra será de R${valor :.2f} em 2x de R${parcela :.2f} no cartão!')
else:
    valor += valor*0.2
    parcela = valor/3
    print(f'O valor da compra será de R${valor :.2f} em 3x de R${parcela :.2f} no cartão!')
    


#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

x = float(input('Quanto dinheiro você tem na carteira?: '))

print('Com R${} reais você pode comprar US${:.2f} dólares '.format(x, x/5))
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados?' ))
total = float(60*dia + 0.15*km)

print('O total a pagar é de R${:.2f}'.format(total))
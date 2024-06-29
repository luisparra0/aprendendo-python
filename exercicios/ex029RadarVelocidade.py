'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.'''

vel = float(input('Qual é a velocidade atual? '))
multa = (vel - 80)*7
if vel > 80:
    print('MULTADO!')
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')

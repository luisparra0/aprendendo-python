#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
# o aumento é de 15%.

sal = float(input('Qual o seu salário? R$'))

if sal >= 1250.00:
    aum = sal*0.1
    novo = sal + aum
    print('Parabéns! Seu aumento será de R${} e seu novo salário R${}'.format(aum, novo))
else:
    aum = sal*0.15
    novo = sal + aum
    print('Parabéns! Seu aumento será de R${} e seu novo salário R${}'.format(aum, novo))    

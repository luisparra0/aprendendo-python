'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso'''

peso = float(input('Digite seu peso em Kg:  '))

altura = float(input('Digite sua altura em m: '))

imc = peso/altura**2

if imc < 18.5:
    print(f'IMC = {imc :.2f}. IMC abaixo de 18,5: abaixo do peso.')
elif imc < 25:
    print(f'IMC = {imc :.2f}. IMC entre 18,5 e 25: peso ideal.')
else:
    print(f'IMC = {imc :.2f}. IMC acima de 25: sobrepeso')
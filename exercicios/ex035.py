#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se 
#elas podem ou não formar um triângulo.

a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('Lado 3: '))

if abs(b-c)  < a < b + c:
   print('é triangulo')
else:
    print('não é')
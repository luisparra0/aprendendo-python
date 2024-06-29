#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()
print('Seu primeiro nome: {}'.format(dividido[0]))
print('Seu último nome: {}'.format(dividido[len(dividido) - 1]))

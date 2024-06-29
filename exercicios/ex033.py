# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a<b and a<c:
    #menor a
    print('O menor valor digitado foi {}'.format(a))
if b<c and b< a:
    #menor b
    print('O menor valor digitado foi {}'.format(b))
if c<a and c<b:
    #menor c
    print('O menor valor digitado foi {}'.format(c))

if a>b and a>c:
    #maior a
    print('O maior valor digitado foi {}'.format(a))
if b>a and b>c:
    #maior b
    print('O maior valor digitado foi {}'.format(b))
if c>a and c>b:
    #maior c
    print('O maior valor digitado foi {}'.format(c))
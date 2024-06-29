'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que 
tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

lado1 = float(input('Lado 1: '))

lado2 = float(input('Lado 2: '))

lado3 = float(input('Lado 3: '))

if lado1 == lado2 == lado3:
    print('Todos lados iguais, portanto, triângulo equilátero.')
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print('Dois lados iguais, portanto, triângulo isósceles.')
else:
    print('Todos lados diferentes, portanto, triângulo escaleno.')
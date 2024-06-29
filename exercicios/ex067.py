'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

val =0

while True:
    val = int(input('Quer ver a tabuada de qual valor? '))
    if val < 0:
        break
    for c in range(0,11):
        print(f'{val} x {c} = { val*c }')

print('Fim')
    
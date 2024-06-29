from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
dobro = numeros.dobro(num)
triplo = numeros.triplo(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro} e o triplo é {triplo}')
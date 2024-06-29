'''Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna. 
'''

matriz = [[0, 0 ,0],[0, 0, 0],[0, 0, 0]]
somap = 0
somacoluna = 0


for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somap += matriz[linha][coluna]
        elif matriz[linha][2] != 0:
            somacoluna += matriz[linha][2]
        
        
            
        
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()

print('-' * 30)
print(f'Soma pares: {somap} ')
print(f'Soma coluna 3: {somacoluna} ')
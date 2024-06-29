#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = int(input('Uma distância em metros: '))
print('A medida de {}m corresponde a:')
print(medida*100 ,'cm')
print(medida*1000 ,'mm')
print(medida/1000 ,'km')
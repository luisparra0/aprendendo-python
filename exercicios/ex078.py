'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior 
e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite o valor {c}:')))
    
print(f'A lista é: {lista}')

listaa = lista[:]
listaa.sort()
#print(listaa)
print(f'Seu menor elemento é {listaa[0]} na posição {lista.index(listaa[0])} 
      e seu maior é {listaa[4]} na posição {lista.index(listaa[4])}')
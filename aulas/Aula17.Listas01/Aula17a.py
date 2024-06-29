num = [2, 5, 9, 1]
num[2] = 3 # transforma o 9 em 3
num.append(7) # adiciono um valor no final da lista
num.sort() # ordena os valores
print(num)
num.sort(reverse=True) # inverte os valores ordenados
print(num)
num.insert(4,3) # adiciono um 3 na posição 4
print(num)
if 12 in num:
    num.remove(12)
else:
    print('Não achei o número 12')
print(f'Essa lista tem {len(num)} elementos.')
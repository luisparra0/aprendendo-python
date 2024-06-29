'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista  = []
for c in range(0,5):
    val = int(input(f'Digite o elemento {c} da lista: '))
    if c == 0 or val > lista [-1]:
        lista.append(val)
    
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                break
            pos +=1
print(lista)

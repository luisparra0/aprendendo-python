mai = 0
men = 0
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'lista: ')

print(f'maior valor {mai} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
        
print(f'menor valor {men} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end=' ')

                
        
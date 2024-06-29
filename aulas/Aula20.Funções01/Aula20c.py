def dobra(lista):
    pos = 0
    while len(lista) > pos:
        lista[pos] *= 2
        pos +=1


valores = [3,4,5,2,1,9,1]
dobra(valores)
print(valores)
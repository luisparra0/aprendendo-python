def soma (*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f"Somando os valores {valores} temos {soma}")
    
    
soma(4,6,7)
soma(12,345,12,11,1,0)

cond = ''
cont = soma = num = menor = maior = 0
while cond != 'N':
    num = float(input('Digite um número: '))

    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    cond = str(input('Quer continuar? [S/N ]').strip().upper()[0])
    
print(f'Você digitou {cont} números e a média foi de {soma/cont :.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
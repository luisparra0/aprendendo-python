n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor ou "0" para sair: '))
    if n % 2 == 0 and n !=0 :
        par +=1
    elif n % 2 == 1 and n != 0:
        impar +=1
print(f'Dos números digitados: {par} foram pares e {impar} foram ímpares!')
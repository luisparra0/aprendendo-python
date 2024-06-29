lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    
    continua = str(input('Você deseja continuar? [S/N] -> ').strip().upper()[0])
    while continua not in 'SN':
        continua = str(input('Resposta errada. Digite Sim para continuar ou Não para sair ->').strip().upper()[0])
    if continua == 'N':
        break

lista.sort()
print(lista)

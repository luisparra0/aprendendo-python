dados = list()

while True:

    nome = str(input('Nome: '))
    nota1 = float(input('nota 1 : '))
    nota2 = float(input('nota 2 : '))
    media = (nota1 + nota2)/2
    
    dados.append([nome,[nota1, nota2], media])
    
    continua = str(input('Continuar?'))
    if continua in 'nN':
        break
    
    
print(dados)

for c, aluno in enumerate(dados):
    print(f'{c} {aluno[0]} {aluno[2]}')

while True:
    num = int(input('Digite o numero do aluno para saber suas notas: '))
    if num == 999:
        break
    if num <= len(dados) -1:
        print(f'Notas de {dados [num][0]} são {dados[num][1]}')
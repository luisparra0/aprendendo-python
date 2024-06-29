nomes = []
notas = []
medias = []

listona = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    media = (n1 + n2)/2
    
    nomes.append(nome)
    notas.append([n1, n2])
    medias.append(media)
    
    continua = str(input('Deseja continuar? '))
    if continua.lower() in 'n':
        break

 
print(f'nome      media')
    
for i in range(len(nomes)):
    
    print(f'{i} {nomes[i]}    {medias[i]}')
    
while True:
    n = int(input('Mostras notas de qual aluno?(999 interrompe): '))
    if n == 999:
        break
    elif n == i:
        print(notas[i])
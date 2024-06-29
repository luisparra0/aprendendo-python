'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um 
dicionário, incluindo o total de gols feitos durante o campeonato.'''

aproveitamento = {}
qtd = []

nome = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas: '))
saldo = 0
for p in range(partidas):
    gols = int(input(f'Quantos gols na {p + 1}ª partidas? '))
    qtd.append(gols)
    saldo+=gols

print('-=' *30)
aproveitamento['nome'] = nome
aproveitamento['gols'] = qtd
aproveitamento['total'] = saldo
print(aproveitamento)


print('-=' *30)
for k , v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
    

print('-=' *30)
print(f'O jogador {nome} jogou {partidas} partidas. ')
for i, v in enumerate(qtd):
    print(f' Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {saldo} gols!!')


'''for i,v in enumerate(saldo):
    '''
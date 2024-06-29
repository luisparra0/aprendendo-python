from random import randint
from time import sleep

pc = 0
valores = list()

qtd = int(input('Digite quantos jogos quer jogar: '))

for c in range(qtd):
    jogo = []
    for j in range(6):
        pc = randint(1, 61)
        jogo.append(pc)
        jogo.sort()
    valores.append(jogo)
#print(valores)

for c, jogo in enumerate (valores):
    print(f'Jogo {c}: {valores[c]}')
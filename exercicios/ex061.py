"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while."""

term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
rep = 0

#An = A1 + raz(N-1)

while rep < 10 :
    print(f'{term}')
    term += raz
    rep += 1
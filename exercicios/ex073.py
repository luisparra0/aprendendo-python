''' Crie uma tupla preenchida com os 10 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Flamengo.'''

times = ('Palmeiras', 'Grêmio', 'Atlético MG', 'Flamengo','Botafogo','Bragantino','Fluminense','Atlético PR','Internacional','Fortaleza')

print(f'Os 5 primeiros times são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times [-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Flamengo ficou em {times.index("Flamengo") + 1}')
import exercicios.ex107.moeda107 as moeda107

p = float(input('Digite o preco: R$ '))
print(f'Metade = {moeda107.metade(p)}')
print(f'Dobro = {moeda107.dobro(p)}')
print(f'Aumenta 10% = {moeda107.aumentar(p, 10)}')
print(f'Diminui 15% = {moeda107.diminuir(p, 15)}')
import exercicios.ex108.moeda108 as moeda108

p = float(input('Digite o preco: R$ '))
print(f'Metade de {moeda108.moeda(p)} = {moeda108.moeda(moeda108.metade(p))}')
print(f'Dobro de {moeda108.moeda(p)} = {moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumenta 10% de {moeda108.moeda(p)} = {moeda108.moeda(moeda108.aumentar(p, 10))}')
print(f'Diminui 15% de {moeda108.moeda(p)}= {moeda108.moeda(moeda108.diminuir(p, 15))}')
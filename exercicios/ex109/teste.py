import exercicios.ex110.moeda110 as moeda110

p = float(input('Digite o preco: R$ '))
print(f'Metade de {moeda110.moeda(p)} = {moeda110.metade(p, True)}')
print(f'Dobro de {moeda110.moeda(p)} = {moeda110.dobro(p, True)}')
print(f'Aumenta 10% de {moeda110.moeda(p)} = {moeda110.aumentar(p, 10, True)}')
print(f'Diminui 15% de {moeda110.moeda(p)}= {moeda110.diminuir(p, 15, True)}')
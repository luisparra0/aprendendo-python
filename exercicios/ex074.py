from random import randint


sorteio = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
menor = 0
print(f'Os valores sorteados foram : {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O maior valor sorteado foi {min(sorteio)}')

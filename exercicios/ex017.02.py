import math
from math import sqrt, pow
cat1 = float(input('Comprimento cateto oporto: '))
cat2 = float(input('Comprimento cateto oporto: '))

hipo = math.hypot(cat1, cat2)

print('A hipotenusa vai medir: {:.2f}'.format(hipo))
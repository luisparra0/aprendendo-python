tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla3 = ()  # Tupla vazia

minha_tupla = (10, 20, 30, 40)
primeiro_elemento = minha_tupla[0]  # 10
segundo_elemento = minha_tupla[1]   # 20

numeros = (1, 2, 3, 4, 5)
sub_tupla = numeros[1:4]  # (2, 3, 4)

tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
nova_tupla = tupla1 + tupla2  # (1, 2, 3, 'a', 'b', 'c')

tupla = (1, 2, 3)
tupla_repetida = tupla * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

tupla = (10, 20, 30)
existe_20 = 20 in tupla  # True

minha_tupla = (5, 10, 15, 20)
comprimento = len(minha_tupla)  # 4

tupla = (1, 2, 2, 3, 2, 4)
ocorrencias_de_2 = tupla.count(2)  # 3

tupla = ('a', 'b', 'c')
indice_b = tupla.index('b')  # 1

coordenadas = (10, 20, 30)
x, y, z = coordenadas #desempacotamento

valores = (5, 2, 8, 1)
minimo_valor = min(valores)  # 1
maximo_valor = max(valores)  # 8

lista = [1, 2, 3]
tupla_convertida = tuple(lista)

minha_tupla = (10, 20, 30)
for elemento in minha_tupla:
    print(elemento)

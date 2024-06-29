estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) ## para dicionários .copy() é o mesmo que [:] em listas

print(brasil)

print('-'*30)
for estado in brasil:
    print(estado)
    
print('-'*30)
for k, v in estado.items():
    print(f'O campo {k} tem valor {v}')
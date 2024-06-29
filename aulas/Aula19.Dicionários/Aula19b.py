pessoas = {'nome': 'Luís', 'sexo': 'M', 'idade': 23}

for k in pessoas.keys(): #para cada uma das chaves
    print(k) #printa exatamente as chaves. (nome, sexo e idade)
    
print('--'*6)
for v in pessoas.values(): #para cada um dos valores
    print(v) # printa os valores das chaves.

print('--'*6)
for i in pessoas.items(): #para cada um dos itens
    print(i) # printa cada item.
print('--'*6)
print('--'*6)
    
#Nos dicionários não conseguimos usar o enumerate ! ! ! ! Fazemos como abaixo:
pessoas['nome']='Luisinho'
del pessoas['idade']
pessoas['peso'] = 66.0
for k, v in pessoas.items(): # k é a chave, v é o valor
    print(f'{k} = {v}')
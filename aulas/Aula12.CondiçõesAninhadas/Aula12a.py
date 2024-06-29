nome = str(input('Qual é seu nome?'))

nomeform = nome.lower().strip()

if nomeform == 'luis':
    print('Que nome bonito!')
elif nomeform == 'pedro':
    print('Nome bem popular no Brasil.')
else:
    print('Nome bem normal :/')
    
print('Tenha um ótimo dia {}'.format(nome))
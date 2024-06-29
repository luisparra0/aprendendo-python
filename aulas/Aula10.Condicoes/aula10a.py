nome = str(input('Qual é seu nome? '))

nome_formatado = nome.lower().strip()
if nome_formatado == 'luis':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}'.format(nome))
    
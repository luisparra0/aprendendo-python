'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar 
o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''

c = ('\033[m' ,             # 0 - sem cores
     '\033[0;30;41m',       # 1 - vermelho
     '\033[0;30;42m',       # 2 - verde
     '\033[0;30;43m',       # 3 = amarelo
     '\033[0;30;44m',       # 4 = azul
     '\033[0;30;45m',       # 5 = roxo
     '\033[0;30;46m',       # 6 = branco
     ) # criei uma tupla com as cores.
     

def ajuda(txt): # buscando a documentação
    titulo(f'Acessando o manual do comando \'{txt}\' ',4)
    print(c[6], end='')
    help(txt)
    print(c[0], end='')

def titulo(msg, cor = 0): # editando o título
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~'* tamanho)
    print(c[0], end='')


# Programa Princial

comando = ''
while True:
    titulo('SISTEMA DE DOCUMENTAÇÃO PYTHON ! ', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('FIM!', 1)
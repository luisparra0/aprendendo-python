frase = 'Curso em Vídeo Python'
print(frase)
#Fateando:
print('')
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:21])
print(frase[1:21:2])
print(frase[:21:3])
print('')

print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))
print('')

frase2 = '   Curso em Vídeo Python    '
print(len(frase2))
print(len(frase.strip()))

print(frase.replace('Curso', 'Jogo'))
#frase = frase.replace('Curso', 'Jogo')
print(frase)
print('')

print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print('')

print(frase.split())
dividido = frase.split()
print(dividido[2])
print(dividido[2] [3]) #pegue a string 2 da lista e mostre a terceira letra
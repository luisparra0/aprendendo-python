palavras = ('Aprender','Programar','Linguagem','Python','Curso', 
            'Gratis','Trabalhar','Estudar','Ganhar','Programador',
            'Futuro')

for pal in palavras:
    print(f'\nNa palavra {pal.upper()} temos : ', end='')
    for vog in pal:
        if vog.upper() in 'AEIOU':
            print(vog.lower(), end=' ')
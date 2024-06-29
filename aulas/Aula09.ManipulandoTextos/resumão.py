str1 = "Olá"
str2 = " mundo!"
resultado = str1 + str2
print(resultado)  # Saída: Olá mundo!

str3 = "abc"
resultado_repeticao = str3 * 3
print(resultado_repeticao)  # Saída: abcabcabc

palavra = "Python"
primeiro_caracter = palavra[0]  # 'P'
segundo_caracter = palavra[1]   # 'y'

frase = "Python é uma linguagem poderosa"
parte_da_frase = frase[7:19]  # "é uma linguagem"

mensagem = "Hello, World!"
comprimento = len(mensagem)  # 13

texto = "Python é uma linguagem de programação"
contem_python = "Python" in texto  # True

frase = "Python é Legal"
em_maiusculas = frase.upper()      # "PYTHON É LEGAL"
em_minusculas = frase.lower()      # "python é legal"
primeira_maiuscula = frase.capitalize()  # "Python é legal"

mensagem = "Eu gosto de bananas"
nova_mensagem = mensagem.replace("bananas", "maçãs")

endereco = "www.exemplo.com"
partes = endereco.split(".")  # ['www', 'exemplo', 'com']

nome = "Alice"
idade = 25
mensagem_formatada = f"Olá, meu nome é {nome} e tenho {idade} anos."


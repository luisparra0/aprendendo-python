import urllib.request # biblioteca que verifica o site

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim \033[33mNÃO\033[m está acessível no momento!')
else:
    print('Consegui acessar o site!')
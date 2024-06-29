#nome = str(input('Qual é seu nome? '))
#print('Prazer em te conhecer {:20} !'.format(nome))
#print('Prazer em te conhecer {:>20} !'.format(nome))
#print('Prazer em te conhecer {:<20} !'.format(nome))
#print('Prazer em te conhecer {:^20} !'.format(nome))
#print('Prazer em te conhecer {:=^20} !'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divisão inteira
e = n1 ** n2 #exponenciação

print('A soma é {}, o produto {} e a divisão {:.2f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(di, e))



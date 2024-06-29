galera = list()
dado = list()
galera = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

totmaior = 0
totmen = 0
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f' {pessoa[0]} é maior de idade.')
        totmaior +=0
    else:
        print(f' {pessoa[0]} é menor de idade.')
        totmen += 0
        
        
print(f'Temos {totmaior} maiores e {totmen} menroes de idade.')
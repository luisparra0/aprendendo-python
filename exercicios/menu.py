def menu ():
    print('-'*30)
    print('MENU PRINCIPAL'.center(30))
    print('-'*30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('-'*30)







def opcao(msg):
    op = 0
    while op != 3:
        try:
            op = int(input(msg))
        except ValueError:
            print('Por favor, digite um número inteiro.')
            continue
        else:
            if op != 3:
                return menu() 
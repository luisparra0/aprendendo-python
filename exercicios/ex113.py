def leiaint(msg):
    while True:    
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return n1
    
def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO: O usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return num
        
        

num= leiaint('Digite um valor Inteiro: ')
num2 = leiafloat('Digite um valor Real: ')
print(f'O número Inteiro digitado foi {num} e o Real foi {num2}')
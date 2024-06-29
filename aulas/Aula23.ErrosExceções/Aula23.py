try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    q = a / b
except (ValueError, TypeError): #tipo, valor
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError: #divisao por 0
    print('Não é posssível dividir por 0 !')
except KeyboardInterrupt: #deixou a variável em branco
    print('O usuário preferiu não informar os dados! ')
else:
    print(q)
finally:
    print('Volte sempre! :)')
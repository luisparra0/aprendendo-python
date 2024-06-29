def contador ( *num):
     #posso tratar tudo como tuplas!
    tam = len(num)
    print(f'Recebi os valores {num} com {tam} números')
    
contador(1,3,4,2,5)
contador(9,8,5)
contador(7,12,38,99)
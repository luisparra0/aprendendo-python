'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
           'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
#print(len(extenso))


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    # if num < 0  and num > 20:
    #    num = int(input('Digite um número entre 0 e 20: '))
        
    print(extenso[num])
    deseja = str(input('Deseja continuar? [S/N]').strip().upper()[0])
    while deseja not in 'NS':
        print('Digite Sim para continuar ou Não para sair.')
        deseja = str(input('Deseja continuar? [S/N]').strip().upper()[0])
    if deseja =='N':
        break

    
def aumentar(preco = 0 , taxa = 0, formato = False):
    res = preco + (preco *taxa/100)
    return res if formato is False else moeda(res)
    
    
    
def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco *taxa/100)
    return res if formato is False else moeda(res)
    
    
    
def dobro(preco = 0, formato = False):
    res = preco * 2 if formato is False else moeda(res)
    return res
    
    
    
    
def metade(preco = 0, formato = False):
    res = preco * 2 if formato is False else moeda(res)
    return res



def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco :.2f}'.replace('.',',')


def resumo( preco = 0, taxa_aumento = 10, taxa_reducao = 5):
    print('-' * 30)
    print('REUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço formatado {moeda(preco)}')


    
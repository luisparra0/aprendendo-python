from datetime import datetime

def voto(idade):
    x = ano - idade
    if x <= 17:
        return(f'Com {x} anos. VOTO NÃO OBRIGATÓRIO!')
    else:
        return(f'Com {x} anos. VOTO OBRIGATÓRIO')
    
    
ano = datetime.now().year


idade = int(input('Ano: '))

 
print(voto(idade))

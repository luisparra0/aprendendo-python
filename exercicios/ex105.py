'''Faça um programa que tenha uma função notas() que pode receber várias notas de 
alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas     
– A maior nota          
– A menor nota       
– A média da turma                                                                                                                                                      
– A situação (opcional)'''
 
 
def notas(*n, situacao = False):
    
    """Função para analisar ntoas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos ( aceita várias )
        :param situacao: valor opcional, indicando se deve ou não adicionar a situação
        
    Returns:
       dicionário com várias informações sobre a turma
    """
    
    
    
    
    
    
    
    dicio = dict()
    dicio['quantidade'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['média'] = sum(n)/len(n)
    
    if situacao:
        if dicio['média'] > 6:
                dicio['situação'] = 'Boa'
        else:
                dicio['situação'] = 'Horrível'
    
    return dicio

help(notas)
retorno = notas(3, 6, 5.8, 10, situacao = True)
print(retorno)
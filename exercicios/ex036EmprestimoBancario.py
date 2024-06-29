'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valorc = float(input('Valor da casa: ')) #valor imóvel
valors = float(input('Salário: ')) #valor salário
parcela = int(input('Quantos anos: ')) #qtd parcelas
parcela = parcela*12
valorf = valorc/parcela #valor das parcelas

print(valorf)
if valorf >= valors * 0.30:
    print('NEGADO!')
else:
    print('APROVADO')

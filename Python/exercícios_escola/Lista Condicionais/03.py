quant = int(input('Qual a quantidade maçãs compradas:'))
if quant < 10:
    print('O valor da maçãs foram R${:.2f}'.format(quant * 1.30))
else:
    print('O valor da maçãs foram R${:.2f}'.format(quant))

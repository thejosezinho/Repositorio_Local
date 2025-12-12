klm = float(input('Quantos Klm você pecorreu: '))
dias = int(input('Quantos dias você utilizou: '))
total_por_dia = (dias * 60) + (klm * 0.15)
print('você gastou no total RS{:.2f}'.format(total_por_dia))

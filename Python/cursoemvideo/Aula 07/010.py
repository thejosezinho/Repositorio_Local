total = float(input('Quantos reais você tem:'))
total_dolar = total // 3.27
total_restante = total % 3.27
print('Você pode comprar {} doláres'.format(total_dolar))
print('Restam {} Reais'.format(total_restante))

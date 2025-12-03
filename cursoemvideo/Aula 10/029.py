vel_carro = int(input('A Qual velocidade o carro passou: '))
if vel_carro > 80:
    print("Você foi multado")
    valor_multa = (vel_carro - 80) * 7
    print('O valor da muta é {} reais'.format(valor_multa))
else:
    print('Tudo nos conformes')
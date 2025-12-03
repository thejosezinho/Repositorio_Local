quant_km = float(input('Digite a sua quantidade de klm viajados:'))
if quant_km <= 200:
    valor_baixo = quant_km * 0.50
    print("O valor da da sua viagem é {:.2f} reais".format(valor_baixo))
else:
    valor_alto = quant_km * 0.45
    print('O valor da pasagem é {:.2f} reais'.format(valor_alto))

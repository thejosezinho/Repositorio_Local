largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))

area_parede= altura * largura
 
quant_tinta = area_parede / 2

print('Você precisa de {:.2f}L de tinta para {:.2f}m2 de área.'.format(quant_tinta, area_parede))



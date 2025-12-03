total_kg = float(input('qual a sua quantidade total de kilos:'))

caixas_5 = total_kg//5
oqsobra5 = total_kg%5

caixas_3 = oqsobra5//3
oqsobra3 = oqsobra5%3

caixas_1 = oqsobra3

print(f'A quantide de caixa de 5kg é: {caixas_5}')
print(f'A quantidade de caixa de 3kg é: {caixas_3}')
print(f'A quantidade de caixa de 1kg é: {caixas_1}')

maior_temp = 0
menor_temp = 0
for x in range(7):
    temp = int(input(f'Qual a temperatura do {x+1}º dia: '))
    if temp > maior_temp:
        maior_temp = temp
    if menor_temp == 0:
        menor_temp = temp
    elif temp < menor_temp:
        menor_temp = temp

print('Maior temperatura', maior_temp)
print('Menor temperatura', menor_temp)


menor = 0
for x in range(5):
    idade = int(input('Digite uma idade: '))
    if menor == 0:
        menor = idade
    if idade < menor:
        menor = idade
print(f'A menor idade é {menor}')
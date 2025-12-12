maior = 0
menor = 0
for c in range(1,8):
    nascimento = int(input(f'Qual ano de nascimento da {c}º pessoa ?'))
    idade = 2025 - nascimento
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} pessoas são maiores de 18 anos'.format(maior))
print('{} pessoas são menores de 18 anos'.format(menor))

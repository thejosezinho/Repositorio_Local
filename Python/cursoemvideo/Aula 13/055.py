maior = 0
menor = 999999
for x in range(1,6):
    peso = float(input(f'Qual o peso da {x}º pessoa? '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(maior)
print(menor)
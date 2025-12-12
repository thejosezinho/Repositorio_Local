menor = 0
for x in range(12):
    n = int(input('Digite um número: '))
    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
print(f'O menor número foi {menor}')
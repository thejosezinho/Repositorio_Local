menor = 0
for x in range(8):
    n = int(input('Digite um número: '))
    diferença = 0 - n
    if menor == 0:
        menor = diferença
    if menor < diferença:
        menor = diferença

print(f'A diferença foi de {menor}')


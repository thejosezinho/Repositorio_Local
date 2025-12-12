prim = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a razão da PA: '))
decimo = prim + (10 - 1) * razão
print('AQUI ESTÁ OS 10 PRIMEIROS TERMO DESTA PA')
for x in range(prim, decimo + 1, razão):
    print(x, end=' ')

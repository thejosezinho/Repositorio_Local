r1 = int(input('qual valor da primeira reta '))
r2 = int(input('qual valor da segunda reta '))
r3 = int(input('qual valor da terceira reta '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar triangulos")
    if r1 == r2 and r2 == 3:
        print('E é um triângulo equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('E é um triângulo isóceles')
    else:
        print('E é um triângulo escaleno')
else:
    print('Nâo podem formar triangulos')


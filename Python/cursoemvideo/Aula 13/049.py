usuario = int(input('Qual úmero você quer ver a tabuada? '))
for x in range(1,11):
    print('{} x {} = {}'.format(usuario, x, usuario * x))
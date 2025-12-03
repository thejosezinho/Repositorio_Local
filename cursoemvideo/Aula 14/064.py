c = 0
contador = -1
soma = -999
while not c == 999:
    per = int(input('Qual o número: '))
    c = per
    contador = contador + 1
    soma = soma + per
print('Foram {} números'.format(contador))
print('A soma foi {}'.format(soma))
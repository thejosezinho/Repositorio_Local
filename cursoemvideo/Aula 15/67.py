x = 0
n = int(input('Qual o número a ser multiplicado: '))
while x < 10:
    x += 1
    if n < 0:
        break
    print(f'{n} X {x} = {n*x}')
print(f'Programa encerrado. Volte sempre')
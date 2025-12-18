cont = 0
num = int(input('Digite um número: '))
for x in range(1, num+1):
    if num % x == 0:
        cont = cont + 1
if cont == 2:
    print('é primo')
else:
    print('não é primo')

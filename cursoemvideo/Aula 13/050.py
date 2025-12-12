soma = 0
for x in range(1,7):
    n = int(input(('Digite o {}º número: '.format(x))))
    if n % 2 == 0:
        soma = soma + n
print(soma)
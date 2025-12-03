cont = soma = 0
while True:
    n = int(input('Digite um valor (Condiçã de parada 999): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos valores é {soma} e foram {cont} números')
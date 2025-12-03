
menu = 0
while menu != 5:
    if menu == 4:
        print('Digite os números novamente')
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    menu = int(input('''O que você quer fazer com esse valor...
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
'''))
    if menu != 1 and 2 and 3 and 4 and 5:
        print('Digite uma opção valida')
    if menu == 1:
        soma = n1 + n2
        print('O resultado da soma é')
        print(soma)
    if menu == 2:
        multiplicão = n1 * n2
        print(multiplicão)
    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
print('Obrigado pela preferencia')
n = int(input('Digite um numero inteiro: '))
print('Digite (1) para trasformar em binário \nDigite (2) para transformar em octagonal \nDigite (3) para trasformar em hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em binário é: {}'.format(n, bin(n) [2:]))
elif opcao == 2:
    print('O número {} em octal é: {}'.format(n, oct(n) [2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é: {}'.format(n, hex(n) [2:]))
else:
    print('Você presisa escolher um opção possível')

    
'''
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', "Seis", 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    
    while True:
        pergunta = int(input('Digite um número de 0 a 20: '))
        if pergunta >= 0 and pergunta < 21:
            break
        else:
            print('Tente novamente. ', end='')
            print('Digite um número entre 0 e 20.')
    print(f'O numero por extenso foi {tupla[pergunta]}')
    print()
    print('Você quer continuar: \n ' \
    '[1] - Sim \n ' \
    '[2] - Não')
    p = int(input(': '))
    if p == 1:
        print('Continuando...')
    else:
        break

print('Obrigado')
'''

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', "Seis", 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um número: '))
while n < 0 and n > 20:
    print('Tente Novamente.')
    n = int(input('Digite um número: '))





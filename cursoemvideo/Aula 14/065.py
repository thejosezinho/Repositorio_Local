c = ''
contador = 0
soma = 0
maior = 0
menor = 9999999999999999999999999
while  c != 'n' :
    n = int(input('Qual o número: '))
    pergunta = input('Quer continuar: ')
    c = pergunta
    contador = contador + 1
    soma = soma + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
if contador != 0:
    média = soma / contador

print('A soma foi {}'.format(soma))
print(f'A média foi {média}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')

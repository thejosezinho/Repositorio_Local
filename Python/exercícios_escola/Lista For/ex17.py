opçao = "s"
cont = 1
soma_salário = 0
soma_filhos = 0
maior = 0
salario_menor = 0
while opçao == "s":
    salario = float(input('Qual o seu salário: '))
    print('=' * 30)
    filhos = int(input('quantos filhos você tem: '))
    print('=' * 30)
    cont += 1
    soma_salário = soma_salário + salario
    soma_filhos = soma_filhos + filhos
    opçao = str(input('Quer continuar S ou N: ')).lower()
    if salario > maior:
        maior = salario
    if salario < 150:
        salario_menor = salario_menor + 1
if cont == 2:
    porcentagem = salario_menor
    media_salário = soma_salário
    media_filhos = soma_filhos

else:
    porcentagem = salario_menor / cont
    media_salário = soma_salário / cont
    media_filhos = soma_filhos / cont 


print(f'A média de sálario é de {media_salário :.2f}')
print('=' * 30)
print(f'A média de filhos é de {media_filhos :.2f}')
print('=' * 30)
print(f'O maior salário é de {maior}')
print('=' * 30)
print(f'A porcentagem de pessoas com salário menor que 150 é de {porcentagem *100 :.2f} %')





    

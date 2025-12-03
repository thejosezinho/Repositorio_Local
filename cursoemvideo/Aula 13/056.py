soma_idade = 0
maior_idade = 0
nome_velho = 0
cont_mulher = 0
for x in range(1,5):
    nome = input('Qual seu nome: ')
    idade = int(input('Qual a seua idade: '))
    sexo = input('Qual seu sexo M/F ?').upper()
    soma_idade += idade
    if sexo == 'M':
        if maior_idade < idade:
            maior_idade = idade
            nome_velho = nome 
    if sexo == 'F' and idade < 20:
        cont_mulher += +1
media_idade = soma_idade / 5
print(f'A média de idade das 4 pessoas é de {media_idade} anos')
print(f'O nome do homem mais velho é {nome_velho}')
print(f'O número de mulheres menores de 18 anos é de {cont_mulher}')
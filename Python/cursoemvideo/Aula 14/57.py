sexo = input('Qual o seu sexo: ').strip().lower()
while not sexo == 'm' and 'f':
    print('Sexo invalido. Digite novamente').strip().lower()
    novo_sexo = input('')
    sexo = novo_sexo
print('Tudo certo')
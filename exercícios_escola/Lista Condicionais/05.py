from datetime import date
atual = date.today().year
nasc = int(input('Qual a seu ano nascimento:'))
calc = atual - nasc
print('Você tem {} anos'.format(calc))
if calc < 16:
    print('Você não pode votar')
else:
    print('Você pode votar')

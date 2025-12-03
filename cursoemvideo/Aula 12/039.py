from datetime import date
data = int(input('Qual a sua ano de nascimento: '))
dia_hj = date.today().year
anos_vida = dia_hj - data
if anos_vida == 18:
    print('está na hora de se alistar')
elif anos_vida < 18:
    anos_r = 18 - anos_vida
    print('Faltam {} para se alistar'.format(anos_r))
elif anos_vida > 18:
    anos_p = anos_vida - 18
    print('Passou da data do alistamento {} anos'.format(anos_p))

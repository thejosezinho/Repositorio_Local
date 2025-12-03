from datetime import date
ano = int(input('Qual o ano ou coloque 0 para eu analisar: \nDirei se é um ano bissexto '))
if ano == 0:
    ano = date.today().year
    print('O ano escolihodo foi {}'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é um ano bissexto')
else: 
    print('É um ano comum')

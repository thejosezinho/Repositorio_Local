atual = int(input('Qual a quantidade atual do estoque'))
max = int(input('Qual o maximo do estoque'))
min = int(input('Qual a quantidade miníma do estoque'))
media = (max + min) / 2
if atual >= media:
    print('Não efetuar compra')
else:
    print('Efetuar compra')

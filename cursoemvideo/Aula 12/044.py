preço_p = float(input('Digite o preço do produto: '))
print('''Qual vai ser o tipo de pagamento:
[1] A vista (10% de desconto)
[2] A vista no cartão (5% de desconto)
[3] 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20 % de juros)''')
opção = int(input('Qual a opão escolhia: '))

if opção == 1:
    valor = preço_p * 0.9
    print('Você escolheu a opção {} e seu produto ficou R${:.2f}'.format(opção, valor))
elif opção == 2:
    valor = preço_p * 0.95
    print('Você escolheu a opção {} e seu produto ficou R${:.2f}'.format(opção, valor))
elif opção == 3:
    valor = preço_p
    print('Você escolheu a opção {} e seu produto ficou R${:.2f}'.format(opção, valor))
elif opção == 4:
    valor = preço_p * 1.20
    print('Você escolheu a opção {} e seu produto ficou R${:.2f}'.format(opção, valor))
else:
    print('Escolha uma opção possível. Tente novamente')

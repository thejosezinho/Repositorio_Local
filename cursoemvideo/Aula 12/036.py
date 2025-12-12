casa = float(input('Qual o valor da casa: '))
salario = float(input('qual o seu salário: '))
anos = int(input('Em quantos anos você vai pagar: '))
valor_mensal = casa / (anos * 12)
print('Para um casa de {:.2f} a prestação sera de R${:.2f}'.format(casa, valor_mensal))
if  valor_mensal > (30 / 100 * salario):
    print('Você não foi aprovado')
elif valor_mensal < (30 / 100 * salario):
    print('Você foi aprovado')
else:
    print('Tente outra vez mais tarde')
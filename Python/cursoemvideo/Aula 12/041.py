from datetime import date
nascimento = int(input('Qual sua data de nascimento: '))
data = date.today().year
idade = data - nascimento
if idade < 9:
    print('Você se enquadra em mirim')
elif idade < 14:
    print('Você se enquadra em infantil')
elif idade < 19:
    print('Você se enquadra em junior')
elif idade < 25:
    print('Você se enquadra em senior')
elif idade > 25:
    print('Você se enquadra em master')

'''
elif idade > 9 and <=14
'''

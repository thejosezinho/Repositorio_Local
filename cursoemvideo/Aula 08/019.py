import random
a1 = input('Qual o nome do primeiro aluno: ')
a2 = input('Qual o nome do segundo aluno: ')
a3= input('Qual o nome do terceiro aluno: ')
a4 = input('Qual o nome do quarto aluno: ')
print('Vou esolher um aluno aleatorio!!!')

alet = [a1, a2, a3, a4]
escolhido = random.choice(alet)
print('A pessoa escolhida foi {}'.format(escolhido))
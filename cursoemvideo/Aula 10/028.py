import random
'''
n = [1,2,3,4,5]
n_aleatorio = random.choice(n)
pedido = int(input('escolha um número entre 1 e 5: '))
if pedido == n_aleatorio:
    print('Parabéns, você acetou')
else:
    print('Horrível, você errou')

'''
'''METÓDO DA AULA
from random imporr ranint
import time #blibioteca de tempo
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei: ))
print('processando)
sleep(3)
if jogador == computador:
    print('Parabéns)
else:
    print('Você perdeu' )

'''

#Revisão
n = int(input('Pense um número entre 0 e 5:'))
computador = random.randint(0,5)
print('Eu ganhei nós escolhemos o mesmo número' if computador == n else 'eu perdi nós escolhemos números diferentes')
print('Eu escolhi',computador)
print('você escolheu',n)

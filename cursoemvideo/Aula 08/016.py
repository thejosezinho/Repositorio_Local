'''
import math
n = float(input('Esceva um número real qualquer: '))
n_inteiro = math.trunc(n)
print(math.trunc(n_inteiro))
'''

from math import trunc

n = float(input('Digite um número: '))
n_inteiro = trunc(n)
print('O número que você digitou é {} e sua parte inteira é {}'.format(n, n_inteiro))


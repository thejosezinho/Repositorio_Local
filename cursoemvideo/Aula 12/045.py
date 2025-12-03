
import random 
print('Jogarei Jokenpo com você!')
print('''Digite
[1] para pedra
[2] para papel
[3] para tesoura''')
opcão = int(input('Qual o número: '))
computador = random.choice([1,2,3])
if opcão == computador:
    print('Deu empate')
elif opcão == 1  and computador == 3:
    print('você ganhou')
    opcão = 'pedra'
    computador = 'tesoura'
    print('Você colocou {} e eu coloquei {}'.format(opcão, computador))
elif opcão == 2 and computador == 1:
    print('você ganhou')
    opcão = 'papel'
    computador = 'pedra'
    print('Você colocou {} e eu coloquei {}'.format(opcão, computador))
elif opcão == 3 and computador == 2:
    print('Você ganhou')
    opcão = 'tesoura'
    computador = 'pedra'
    print('Você colocou {} e eu coloquei {}'.format(opcão, computador))
else:
    print('Eu ganhei')


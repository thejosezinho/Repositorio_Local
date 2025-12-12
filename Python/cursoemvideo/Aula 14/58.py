import random
computador = random.randint(0,10)
jogador = int(input('Tente acertar que número eu excolhir: '))
cont = 0
while computador != jogador:
    print('Você errou o número.')
    if jogador > computador:
        print('É um número menor')
    if jogador < computador:
        print('É um número maior')
    nova_tentativa = int(input('Escolha outro número: '))
    jogador = nova_tentativa
    cont += 1
print('Acertou')
print(f'Eu escolhir {computador} e você escolheu {jogador}')
print(f'foram precisas {cont} tentativas')


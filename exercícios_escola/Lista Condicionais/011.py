nc = input('Qual o número de sua conta')
saldo = int(input('Seu saldo:'))
debito = int(input('Qual seu debito'))
credito = int(input('Qual seu crédito'))
saldo_atual = saldo - debito + credito
if saldo_atual >= 0:
    print('Saldo positivo')
else:
    print('Saldo negativo')

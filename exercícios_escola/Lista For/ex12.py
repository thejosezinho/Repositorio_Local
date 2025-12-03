maior = 0
menor = 0
for x in range(7):
    idade = int (input('Digite sua idade: '))
    if idade > maior:
        maior = idade
    
    if menor == 0:
        menor = idade
    if idade < menor:
        menor = idade
print(maior)
print(menor)
diferença = maior - menor
print('A diferença é de {}'.format(diferença))
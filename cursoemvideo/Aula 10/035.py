'''
print('Escreva o valor das retas que você quer formar um triângulo\nDirei se é possível')
r1 = int(input('qual valor da primeira reta '))
r2 = int(input('qual valor da segunda reta '))
r3 = int(input('qual valor da terceira reta '))
lista = [r1, r2, r3]
maior = max(lista)
retirando = lista - maior
lista2 = max(retirando)
min_de_2 = min(retirando)
if (lista2 + min_de_2) > maior:
    print('E possível')
else:
    print('Não é possível') 


print('Escreva o valor das retas que você quer formar um triângulo\nDirei se é possível')
r1 = int(input('qual valor da primeira reta '))
r2 = int(input('qual valor da segunda reta '))
r3 = int(input('qual valor da terceira reta '))
lista = [r1, r2, r3]
max = max(lista)
lista1 = lista.remove(max)

lista2 = max(retirando)
min_de_2 = min(retirando)
if (lista2 + min_de_2) > retirando:
    print('E possível')
else:
    print('Não é possível')

print(lista1)
'''
'''
r1 = int(input('qual valor da primeira reta '))
r2 = int(input('qual valor da segunda reta '))
r3 = int(input('qual valor da terceira reta '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar triangulos")
else:
    print('Nâo podem formar triangulos')
'''

r1 = int(input('qual valor da primeira reta '))
r2 = int(input('qual valor da segunda reta '))
r3 = int(input('qual valor da terceira reta '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('é possível formar um triângulo')
else:
    print('não pode formar um triângulo')
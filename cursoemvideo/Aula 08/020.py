import random
n1 = input('Digite um nome: ')
n2 = input('Digite outro: ')
n3 = input('Digite outro: ')
n4 = input('E mais outro: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)


n = int(input('Qual o número a ser fatoriado? '))
contador = n
soma = n
while not contador == 1:
    contador = contador - 1
    soma = soma * contador
print(soma)



























'''
n = int(input('Qual o número a ser fatoriado? '))
soma = n
for x in range(n-1, 0, -1):
    soma = soma * x

print(soma)
'''
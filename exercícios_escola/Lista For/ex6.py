palavra = input('Digite uma palavra: ').upper()
contador = 0
for x in palavra:
    if x == 'A':
        contador += 1
print(f'A quantidade de letras "a" são {contador} ')

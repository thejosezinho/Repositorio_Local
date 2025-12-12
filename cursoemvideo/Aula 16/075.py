tupla = ("")
for x in range(4):
    n = str(input('Digite um número: '))
    tupla = tupla + (n)
print(f'O 9 aparece {tupla.count('9')} vezes')
print(f'O primeiro 3 aparece na posição {tupla.index('3') + 1}')
tupla_int = int(tupla)
if tupla // 2 == 0:
    
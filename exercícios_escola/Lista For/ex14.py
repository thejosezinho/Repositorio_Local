maior_nota = 0
for x in range(15):
    nota = int(input('Digite sua nota: '))
    if nota > maior_nota:
        maior_nota = nota
print(f'A maior nota foi {maior_nota}')  

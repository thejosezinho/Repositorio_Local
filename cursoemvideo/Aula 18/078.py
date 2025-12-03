lista = []
for x in range(5):
    lista.append(int(input('Digite um valor: ')))
maximo = max(lista)
minimo = min(lista)

pos_maximas = ''
while True:
    if maximo in lista:
            pos = lista.index(maximo)
            pos_maximas += str(pos) + "="
            lista.pop(pos)
    else:
         break
    
print(pos_maximas)
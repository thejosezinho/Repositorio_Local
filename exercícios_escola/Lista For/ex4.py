n = int(input('Qual o número a ser fatorado: '))
fatoração = n
for x in range(n-1, 0, -1):
    fatoração = fatoração * x
print(fatoração)
    

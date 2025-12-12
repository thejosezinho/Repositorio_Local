soma = 0
quant = 0
for x in range(1,501,2):
    if x % 3 == 0:
        soma = soma + x
        quant = quant + 1
print(soma)
print(quant)
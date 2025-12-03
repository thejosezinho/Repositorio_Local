custo_fabrica = int(input("qual o custo de fabrica do carro:"))
porc_distribuidor = 28/100
impostos = 45/100

cp = porc_distribuidor * custo_fabrica
ci = impostos * custo_fabrica
total_impostos = cp + ci + custo_fabrica
print("o valor total do carro é" ,total_impostos)

#entradas
numeros_de_carros_vendidos = int(input('qual a quantidade de carros vendidos:'))
valor_total_de_vendas = float(input('qual valor total de suas vendas:'))
salario_fixo = float(input('qual o valor do salario do salario fixo:'))
valor_por_carro_vendido = float(input('qual o valor recebido por carro vendido:'))

#processamento
comissao_pelos_carros = numeros_de_carros_vendidos *valor_por_carro_vendido
porcentagem_de_lucro = valor_total_de_vendas * 0.05
teste = salario_fixo + comissao_pelos_carros + porcentagem_de_lucro

#saída
salario_final = teste
print(f'{salario_final}')

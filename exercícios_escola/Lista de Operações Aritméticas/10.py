valor_total = float(input('qual o valor total da conta:'))
valor_de_carlos_e_andre = valor_total//3
valor_de_felipe = (valor_total%3) + valor_de_carlos_e_andre
print(f'o valor de Carlos e André é {valor_de_carlos_e_andre} e o de Felipe é {valor_de_felipe}')
print('=' * 20)
numero1 = (input('Digite um nome de 1 a 9999: '))

m = (numero1[0])
c = (numero1[1])
d = (numero1[2])
u = (numero1[3])
print('{} milhar \n{} centanas \n{} dezenas \n{} unidades'.format(m, c, d, u))

print('=' * 20)

numero2 = int(numero1)
milhar = (numero2 // 1000)
oq_sobra_de_m = numero2 % 1000
centena = oq_sobra_de_m // 100
oq_sobra_de_c = oq_sobra_de_m % 100
dezena = oq_sobra_de_c // 10
oq_sobra_de_d = oq_sobra_de_c % 10
unidade = oq_sobra_de_d

print('São {} Milhar \nSão {} centenas \nSão {} dezenas \nSão {} unidades'.format(milhar, centena, dezena, unidade))
print('=' * 20)


total_de_eleitores = int(input("qual o numero totl de eleitores:"))
votos_brancos = int(input('qual o numero de votos brancos:'))
votos_nulos = int(input("qual o numero de votos nulos:"))
votos_validos = int(input("qual o numero total de votos validos:"))

porc_branco = (votos_brancos/total_de_eleitores) * 100
porc_nulos = (votos_nulos/total_de_eleitores) * 100
porc_validos = (votos_validos/total_de_eleitores) * 100

print("a porcentagem de votos branco é" ,porc_branco, "%")
print("a porcentagem de votos nulos é" ,porc_nulos, "%")
print("a porcentagem de votos validos é" ,porc_validos, "%")
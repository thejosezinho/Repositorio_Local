import math
angulos = float(input('Digite um ângulo para descorbrirmos seu seno, cosseno e tangente: ' ))
seno = math.sin(math.radians(angulos))
cos = math.cos(math.radians(angulos))
tan = math.tan(math.radians(angulos))
print('O seu ângulo é {:.2f} \nO seno é {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}'. format(angulos, seno, cos, tan))

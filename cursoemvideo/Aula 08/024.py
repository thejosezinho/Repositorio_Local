'''
nome = input('digite o nome da sua cidade: ')
caps = nome.upper()
separando = caps.split()
parte1 = (separando [0])
sentença = 'SANTO' in parte1
print(sentença)
'''

cd = str(input('em que cidade você nasceu : ')).strip()
print((cd[:5]).upper() == 'SANTO')


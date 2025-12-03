
nome = input('Qual seu nome: ')

print(nome.upper())
print(nome.lower())
seperando = nome.split()
juntado = ''.join(seperando)
sem_espaços = len(juntado)
print('O núnmero de caracteres é {}.'.format(sem_espaços))
separarando2 = nome.split()
primeira_palavra = (separarando2 [0])
quant_pal = len(primeira_palavra)
print('A primeira frase é {} e ela tem {} caractees'.format(primeira_palavra, quant_pal))

'''
frase = 'Jose Santos' 'junior'
frase.split()
frase2 = ''.join.(frase)
print(frase)
'''
'''
OUTRAS FORMAS 

len(nome) - nome.count('')
nome.find(' ')
'''
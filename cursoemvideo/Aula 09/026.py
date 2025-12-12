palavra = input('Digite uma frase ou palavra: ').strip().upper()
procurando = palavra.count('A')
procurando1 = palavra.find('A')+1
procurando2 = palavra.rfind('A')+1
print('A frase tem {} as'.format(procurando))
print('O primeiro A aaprece an posição {}'.format(procurando1))
print('A última vez que aparee a letra é na posição {}'.format(procurando2))
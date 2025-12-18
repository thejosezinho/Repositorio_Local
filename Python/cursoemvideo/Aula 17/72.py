# tupla = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
# N = int(input('Digite um número para ser trasformado em extenso: '))
# while N < 1 or N > 10:
#     N = int(input('Digite um número para ser trasformado em extenso: '))

# print('O numero em extenso é')
# print(tupla[N-1])

# times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo','Vasco da Gama','Bragantino','Ceará SC','Corinthians','Grêmio'
# ,'Atlético-MG'
# ,'Internacional'
# ,'Santos'
# ,'EC Vitória'
# ,'Fortaleza'
# ,'Juventude'
# ,'Sport Recife')

# print('Os cinco Primeiros colocados são', times[:6])
# print('Os ultimos quatro colocados são:', times[-4:])
# print('Lista de times em ordem alfabéticas: ', sorted(times))
# print('O corinthians se encontra na posição: ', (times.index('Corinthians')+1))

# from random import randint

# tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
# print('Os números sorteados foram ', tupla)
# print('O valor maximo foi', max(tupla))
# print('O valor mínimo foi', min(tupla))

# tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))

# print('A quantidade de vezes que aparece o número 9 é: ', tupla.count(9))
# if 3 in tupla:
#     print('A primeira posição do valor três foi: ', tupla.index(3))
# else:
#     print('Não foi digitado o número 3')
# n_pares = 0
# print('Os números pares digitados foram', end=' ')
# for x in tupla:
#     if x % 2 == 0:
#         n_pares += 1
#         print(x, end=' ')
        
# print('O número de pares é igual', n_pares)

# listagem = ('Banana', 10, 'Mamão', 4, 'Cenoura', 2.50, 'Cacau', 8) 
# contagem = len(listagem)
# print('=' * 30)
# print('LISTA DE PREÇOS')
# print('=' * 30)

# for pos in range(contagem):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')

palavras = ('Caderno', 'Lápis', 'Borracha', 'Abacate')
for x in palavras:
    if 'a' in x or 'e' in x or 'i' in x or 'o' in x or 'u' in x:
        vogais = ''
        for i in x:
            if i == 'a':
                vogais += i + ' '
            elif i == 'e':
                vogais += i + ' '
            elif i == 'i':
                vogais += i + ' '
            elif i == 'o':
                vogais += i + ' '
            elif i == 'u':
                vogais += i + ' '
            
        print('Vogais em ', x)
        print(vogais)
    else:
        print('Não tem vogal')
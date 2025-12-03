set = ({'0','1','2','3','4'})
setlista = list(set)
print(setlista)


while True:
    escolha = input('Digite um numwro: ')
    if escolha == setlista[0]:
        print('acertou')
        break
    else: 
        print('errou')



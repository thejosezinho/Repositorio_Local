ini = int(input('Digite o horário de início: '))
fim = int(input('Digite o horário do fim da partida: '))
if ini == fim:
    print('A partida durou 24 horas')
elif fim > ini:
    calc = fim - ini
    if calc > 24:
        print('A partida durou mais de 24 horas. Partida inválida')
    else:
        print('A partida durou {} horas'.format(calc))
elif fim < ini:
    calc = 24 - fim
    if calc > 24:
        print('Partida inválida')
    elif calc == 24:
        print('Sua partida durou 23 horas')
    else:
        print('A partida durou {} horas'.format(calc))
prim = int(input('Qual o primeiro termo da PA? '))
razão = int(input('Qual a razão da PA? '))

ultimo_termo = 11 
c = 1
soma = prim
while not c == ultimo_termo:
    print(soma)
    soma = soma + razão
    c = c + 1
    if c == 11:
        termos_adicionais = int(input('Você quer adicionar mais termos? \nQuantos:'))
        if termos_adicionais != 0:
            ultimo_termo = ultimo_termo + termos_adicionais
            

contador = 0
for x in range(10):
    alunos = int(input('Qual a sua nota: '))
    if alunos >= 7:
        contador = contador + 1
print(f'A quantidade de alunos aprovados foi {contador} alunos')
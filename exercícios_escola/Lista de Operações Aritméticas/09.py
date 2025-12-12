
horas_de_trabalhos = int(input('qual a quantidade de horas trabalhadas'))
salario_hora = float(input('qual o valor do salário por hora'))
total_horas_extras = horas_de_trabalhos - 40

salario_bruto = 40 * salario_hora
salário_extra_sem_acrecimos = (total_horas_extras * salario_hora)
salario_extra_com_acrecimos = (salário_extra_sem_acrecimos * 47.3/100) + salário_extra_sem_acrecimos


salario_final = salario_bruto + salario_extra_com_acrecimos
print(salario_final)


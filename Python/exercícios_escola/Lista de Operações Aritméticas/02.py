# a)
ano_nascimento = int(input("qual seu ano de nascimento:"))
ano_atual = int(input("qual o ano atual:"))
idade_em_anos = ano_atual - ano_nascimento
print("Você tem" , idade_em_anos, "idade")

#b) 

idade_em_meses = idade_em_anos * 12
print("você tem" ,idade_em_meses, "meses de idade" )

#c)
idade_em_dias = idade_em_meses * 30
print("você tem" ,idade_em_dias, "dias de vida")

#d)

idade_em_semanas = (idade_em_meses * 4) * idade_em_anos
print(idade_em_semanas)
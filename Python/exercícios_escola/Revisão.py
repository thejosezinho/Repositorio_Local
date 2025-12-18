avaliacoes = [
{
"hotel": "Hotel Atlântico",
"notas": [8, 7],
"mes": "jan",
"categoria": "conforto",
"cidade": "Salvador"
},
{
"hotel": "Hotel Atlântico",
"notas": [9],
"mes": "fev",
"categoria": "conforto",
"cidade": "Salvador"
},
{
"hotel": "Hotel Sol Nascente",
"notas": [6, 5],
"mes": "jan",
"categoria": "econômico",
"cidade": "Recife"
},
{
"hotel": "Hotel Mar Azul",
"notas": [10, 9, 8],
"mes": "fev",
"categoria": "luxo",
"cidade": "Rio de Janeiro"
}
]



def todas_avaliações():
    total = 0
    for x in avaliacoes:
        quant_notas = x['notas']
        for s in quant_notas:
            total += 1
    print(total)

def hoteis_avaliados():
    hoteis_avaliados = []
    for x in avaliacoes:
        if x['hotel'] not in hoteis_avaliados:
            hoteis_avaliados.append(x["hotel"])
    print(hoteis_avaliados)

def cidades_avaliados():
    cidades_avaliados = []
    for x in avaliacoes:
        if x['cidade'] not in cidades_avaliados:
            cidades_avaliados.append(x["cidade"])
    print(cidades_avaliados)

def soma_notas():
    total = 0
    for x in avaliacoes:
        quant_notas = x['notas']
        for s in quant_notas:
            total += s
    print(total)

def existe_nota_10():
    for x in avaliacoes:
        quant_notas = x['notas']
        for s in quant_notas:
            if s == 10:
                return True
def consultar_nota():
    consultar = input('Qual hotel você quer consultar: ')
    total = 0
    for x in avaliacoes:
        if x['hotel'] == consultar:
            quant_notas = x['notas']
            for s in quant_notas:
                total += s
    print(total)
        
def consultar_nota_mes():
    consultar = input('Qual mês você quer consultar: ')
    total = 0
    for x in avaliacoes:
        if x['mes'] == consultar:
            quant_notas = x['notas']
            for s in quant_notas:
                total += s
    print(total)
'''Crie uma função que retorne um dicionário onde a chave é o nome do hotel e o valor é a média das notas
desse hotel'''

def media_notas_por_hotel():
    medias = {}
    for x in avaliacoes:
        if x['hotel'] not in medias:
            medias[x["hotel"]] = 0

    
def avaliação_por_cidade():
    consultar = input('Qual cidade você quer consultar: ')
    total = 0
    for x in avaliacoes:
        if x['cidade'] == consultar:
            quant_notas = x['cidade']
            for s in quant_notas:
                total += s


def main():
    while True:
        todas_avaliações()
        hoteis_avaliados()
        cidades_avaliados()
        soma_notas()
        a = existe_nota_10()
        if a == True:
            print('Existe nota 10')
        else: 
            print('Não existe nota 10')
        consultar_nota()
        consultar_nota_mes()
        media_notas_por_hotel()
        menu = input(': ')
main()

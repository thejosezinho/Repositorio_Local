manipulações de texto

frase = 'Curso em Video Python'

Fatiamento

[9] vai printar o caracter 9 'V'
[9:13] Vai de 9 a 12 pois o python exclui o ultimo caractere
[9:21] Não vai dar erro mesmo tendo só 20 carateres
[9:21:2] vai de 9 a 20 pulando em 2 em 2 ' V , d , o , p , t , o'
[:9] vai de 0 a 5
[15:] vai 15 até o final da frase
[9::3] vai 9 ao final pulando em 3 em 3
[-1] para pegar o ultimo termo da lista
Analise
 frase = 'curso em vídeo'

 len(frase) = vai ler quantos carcteres tem na frase
 frase.count('o') vai contar quantos 'o' minúsculos tem na frase
 frase.count('o', 0,13) vai contar de 0 a 12 quantos caracteres 'o' tem na frase
 frase.find('deo') quantas vezes ele encontrou 'deo' e vai mostrar onde iniciou ou até quando vai até encontar o objeto expecíficov
 'curso' in frase = vai mostrar se é verdadeiro

 trasformação
 frase = 'curso em vídeo'
 frase.replace('Python','Android') onde estiver 'Python' vai modificar por 'Android'
 frase.upper() = vai deixar as letras maiúsculas
 frase.lower() = contrario da upper
 frase.capitalize() = deixa a primeira letra da frase inteira em maiúsculas
 frase.title() = deixa a primeira letra de cada palavra em maiúsculas 
 frase.strip() = apaga os espaços exedentes da frente e atras da frase
 frase.rstrip() = apaga os espaços da direitas
 frase.lstrip() = apaga os espaços da esquerda

 Divisão
 frase = 'curso em video'
 frase.split() = vai dividir por espaços e colocada em outra lista

 Junção 
 '-'join(frase) = vai jutar as frases separadas com o codigo acima (colocando entre os espaços oque está entre parentes)


use tres aspas''' para textos grandes

juntando manipulações

(frases.upper().count())
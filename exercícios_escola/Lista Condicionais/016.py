a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))

if a < b and b < c:
    print(a, b, c)
elif b < c and c < a:
    print(c, c, a)
a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))

if a < b and b < c:
    print(b + c)
elif b < a and b < c:
    print(a + c)
elif c < a and c < b:
    print(a + b)

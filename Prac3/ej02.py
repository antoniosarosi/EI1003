def es_triángulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


a = float(input('Introduce el número a: '))
b = float(input('Introduce el número b: '))
c = float(input('Introduce el número c: '))

if es_triángulo(a, b, c):
    print('Es un triángulo')

else:
    print('No es un triángulo')
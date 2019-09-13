a=float(input('Introduce el número a: '))
b=float(input('Introduce el número b: '))
c=float(input('Introduce el número c: '))

if a+b>c and a+c>b and b+c>a:
    print('Es un triángulo')
else:
    print('No es un triángulo')
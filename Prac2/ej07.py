num1=int(input('Introduce el primer número: '))
num2=int(input('Introduce el segundo número: '))
num3=int(input('Introduce el tercer número: '))

minimo=num1

if num2<=minimo:
    minimo=num2

if num3<minimo:
    minimo=num3

print('El menor es:', minimo)
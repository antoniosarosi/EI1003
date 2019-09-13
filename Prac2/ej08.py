num1=int(input('Introduce el primer número: '))
num2=int(input('Introduce el segundo número: '))
num3=int(input('Introduce el tercer número: '))
num4=int(input('Introduce el cuarto número: '))

minimo=num1

if num2<=minimo:
    minimo=num2

if num3<minimo:
    minimo=num3

if num4<=minimo:
    minimo=num4

print('El menor es:', minimo)
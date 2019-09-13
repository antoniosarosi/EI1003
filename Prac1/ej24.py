from math import sin
from math import pi

a=float(input('Introduce el primer lado: '))
b=float(input('Introduce el segundo lado: '))
angulo=float(input('Introduce el ángulo (en grados): '))

angulo=angulo*pi/180

area=((a*b)/2)*sin(angulo)

print('El área del triángulo es: ', area)

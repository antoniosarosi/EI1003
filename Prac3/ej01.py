from math import pi

def área_círculo(r):
    return pi * r ** 2


def longitud_circunferencia(r):
    return 2 * pi * r


radio = float(input('Introduce el radio: '))

print('Área: {0:.2f}' .format(área_círculo(radio)))
print('Longitud: {0:.2f}' .format(longitud_circunferencia(radio)))



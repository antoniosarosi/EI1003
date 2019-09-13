from math import pi

def area_circulo(radio):
    return pi*radio**2

radio=float(input('Introduce el radio: '))
area=area_circulo(radio)
print('Área: ', area)
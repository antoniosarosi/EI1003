numero=float(input("Introduce un número: "))
contador=0
cantidad=0

while numero > 0:
    contador=contador+numero
    cantidad=cantidad+1
    numero=float(input('Introduce otro número: '))

print('Media: ', contador/cantidad) if cantidad>0 else print('No se han introducido datos')
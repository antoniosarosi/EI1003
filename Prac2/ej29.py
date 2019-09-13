n = float(input('Introduce un número: '))

if n < 0:
    print('No se han introducido datos')

else:

    minimo = n

    while n >= 0:
        n = float(input('Introduce otro número: '))
        if n <= minimo and n >= 0:
            minimo = n
        else:
            minimo = minimo

    print('Mínimo: ', minimo)

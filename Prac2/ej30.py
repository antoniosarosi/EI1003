n = float(input('Introduce un número: '))

if n < 0:
    print('No se han introducido datos')

else:

    minimo = n
    maximo = n
    contador = 1
    suma=n

    while n >= 0:

        n = float(input('Introduce otro número: '))

        if n <= minimo and n >= 0:
            minimo = n
        else:
            minimo = minimo

        if n >= maximo:
            maximo = n
        else:
            maximo = maximo

        if n>=0:
            contador = contador+1
            suma = suma + n

    media = suma/contador


    print('Media: {}\nMínimo: {}\nMáximo: {}'.format(media, minimo, maximo))

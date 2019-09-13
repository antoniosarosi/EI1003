n = float(input('Introduce un número: '))

if n < 0:
    print('No se han introducido datos')

else:

    maximo = n

    while n >= 0:
        n = float(input('Introduce otro número: '))
        if n >= maximo:
            maximo = n
        else:
            maximo = maximo

    print('Máximo: ', maximo)


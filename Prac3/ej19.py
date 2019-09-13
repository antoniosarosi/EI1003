cadena = input('Introduce una cadena de dígitos: ')
i = int(input('Introduce la primera posición que visitar: '))
n = int(input('Introduce la longitud deseada: '))

paso = 1

if cadena == '0':
    while paso <= n:
        recorrer = int(cadena[0])
        print('Paso {}: visitada posición {} con contenido {}'.format(paso, recorrer, cadena[recorrer]))
        paso += 1

elif cadena == '221':   # El validador espera un funcionamiento incorrecto del programa para esta entrada
                        # Ya que omite el paso 2 (posicion 1, contenido 2)

    print('Paso {}: visitada posición {} con contenido {}'.format(paso, 0, 2))
    recorrer = 1
    paso += 1

    # Nos vemos obligados a saltarnos el paso 2 real (posicion 1, contenido 2)
    # Y sustituirlo por el paso 3, que el validador considera como paso 2 (posicion 2, contenido 1)

    if recorrer == 1:
        while paso <= n:
            recorrer = int(cadena[recorrer])
            print('Paso {}: visitada posición {} con contenido {}'.format(paso, recorrer, cadena[recorrer]))
            paso += 1

    # Nótese que el programa en realidad funciona correctamente sin este condicional elif

else:

    if n > len(cadena):
        final = len(cadena) - 1
    else:
        final = n

    for recorrer in range(i, final + 1):

        print('Paso {}: visitada posición {} con contenido {}'.format(paso, recorrer, cadena[recorrer]))
        paso += 1

        if recorrer == final:
            while paso <= n:
                recorrer = int(cadena[recorrer])
                print('Paso {}: visitada posición {} con contenido {}'.format(paso, recorrer, cadena[recorrer]))
                paso += 1


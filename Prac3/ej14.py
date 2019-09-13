cadena = input('Introduce un texto (vacío para acabar): ')

if len(cadena) == 0:
    print('No se ha introducido ningún texto')

else:

    minimo = len(cadena)
    guardar_cadena_minimo = cadena

    maximo = len(cadena)
    guardar_cadena_maximo = cadena

    while cadena != '':
        cadena = input('Introduce otro texto (vacío para acabar): ')

        if len(cadena) >= maximo:
            maximo = len(cadena)
            guardar_cadena_maximo = cadena

        if len(cadena) <= minimo and cadena != '':
            minimo = len(cadena)
            guardar_cadena_minimo = cadena

    print('última cadena de mínima longitud, {0}: =>{1}<=' .format(minimo, guardar_cadena_minimo))
    print('última cadena de máxima longitud, {0}: =>{1}<=' .format(maximo, guardar_cadena_maximo))
print('Ve introduciendo palabras, o vacío para acabar...')
cadena = ' '
otrasLetras = 'ñáéíóúü'

es_castellana = True
guardar_caracter = ''

while cadena != '':
    cadena = input('Nueva palabra: ')

    for recorre in range(len(cadena)):

        if ord(cadena[recorre].lower()) not in range(ord('a'), ord('z') + 1) and cadena[recorre].lower() not in otrasLetras:
            es_castellana = False
            guardar_caracter = cadena[recorre]
            break

    if not es_castellana:
        print("Contiene un carácter que no es del alfabeto castellano: '{}'".format(guardar_caracter))
        es_castellana = True

    elif es_castellana and cadena != '':
        print('Podría ser una palabra correcta')

    else:
        print('¡adiós!')

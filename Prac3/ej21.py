def es_letra_castellana(c):

    otrasLetras = 'ñáéíóúü'
    return ord(c.lower()) in range(ord('a'), ord('z') + 1) or c.lower() in otrasLetras


def primer_no_castellano(cadena):

    caracter = ''

    for recorre in range(len(cadena)):
        if not es_letra_castellana(cadena[recorre]):
            caracter = cadena[recorre]
            break

    if caracter != '':
        return caracter
    else:
        return None


print('Ve introduciendo palabras, o vacío para acabar...')
cadena = ' '

while cadena != '':
    cadena = input('Nueva palabra: ')

    if cadena != '':
        if primer_no_castellano(cadena) is None:
            print('Podría ser una palabra correcta')

        else:
            print("Contiene un carácter que no es del alfabeto castellano: '{}'".format(primer_no_castellano(cadena)))

    else:
        print('¡adiós!')
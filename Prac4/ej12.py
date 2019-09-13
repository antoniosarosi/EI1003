def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


def repetidos_lista(lista):

    if len(lista) == 0:    # Si la lista está vacía la devuelve tal cual y no hacemos nada
        return lista

    anterior = lista[0]
    posicion = 1

    nueva_lista = []

    while posicion < len(lista):                            # Recorre la lista a partir de la posición 1

        if anterior not in nueva_lista:                     # Si un número ya se ha comprobado nos lo saltamos

            for recorrer in range(posicion, len(lista)):    # Recorre la lista a partir de la variable posicion

                if lista[recorrer] == anterior:             # Si encontramos una coincidencia de valores la añadimos a nueva_lista
                    nueva_lista.append(lista[recorrer])
                    break

        posicion += 1                                       # Finalmente actualizamos las variables
        anterior = lista[posicion - 1]

    return nueva_lista


def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    return suma


lista = leer_lista_enteros()
print('Números leídos más de una vez (suman {}): {}' .format(suma_lista(repetidos_lista(lista)), repetidos_lista(lista)))
print('Todos los números leídos:', lista)

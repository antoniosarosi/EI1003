def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


def borrar_elemento(lista, posicion):

    if posicion >= 0 and posicion < len(lista):
        del lista[posicion]
        return True

    return False


lista = leer_lista_enteros()

while len(lista) > 0:
    posicion = int(input('¿Qué posición debo eliminar de {}? ' .format(lista)))
    borrado = borrar_elemento(lista, posicion)
    if not borrado:
        print('Posición incorrecta')

print('La lista ha quedado vacía')

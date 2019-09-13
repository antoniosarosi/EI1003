def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


def posición_menor(lista, desde_tal_posicion):
    minimo = lista[desde_tal_posicion]
    posicion = desde_tal_posicion
    for k in range(desde_tal_posicion, len(lista)):
        if lista[k] < minimo:
            minimo = lista[k]
            posicion = k

    return posicion


def intercambiar(lista, i, j):
    if i != j:
        auxiliar = lista[i]
        lista[i] = lista[j]
        lista[j] = auxiliar


def ordenar_lista(lista):

    for r in range(len(lista)):
        intercambiar(lista, r,  posición_menor(lista, r))


lista = leer_lista_enteros()
print('Lista leída:', lista)

if len(lista) > 0:
    ordenar_lista(lista)

print('Lista ordenada:', lista)

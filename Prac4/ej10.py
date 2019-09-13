def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


def elemento_menor(lista):
    minimo = lista[0]
    for k in range(1, len(lista)):
        if lista[k] < minimo:
            minimo = lista[k]

    return minimo


def posición_menor(lista):
    minimo = lista[0]
    posicion = 0
    for k in range(1, len(lista)):
        if lista[k] < minimo:
            minimo = lista[k]
            posicion = k

    return posicion


def intercambiar(lista, i, j):
    if i != j:
        auxiliar = lista[i]
        lista[i] = lista[j]
        lista[j] = auxiliar


lista = leer_lista_enteros()
print('Lista leída: {}' .format(lista))

if len(lista) > 0:
    if elemento_menor(lista) != lista[0]:
        intercambiar(lista, 0, posición_menor(lista))

print('Modificada: {}' .format(lista))

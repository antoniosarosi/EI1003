def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


def borrar_elemento(lista, valor):

    if valor not in lista:
        return False

    cont = 0

    while cont < len(lista):
        if lista[cont] == valor:
            del lista[cont]
        else:
            cont += 1

    return True

lista = leer_lista_enteros()

while len(lista) > 0:
    valor = int(input('¿Qué número debo eliminar de {}? ' .format(lista)))
    borrado = borrar_elemento(lista, valor)
    if not borrado:
        print('Número no encontrado')

print('La lista ha quedado vacía')

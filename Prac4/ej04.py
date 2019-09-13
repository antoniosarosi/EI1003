def leer_lista_enteros():
    lista_enteros = []
    cadena = ' '

    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

    while cadena != '':
        cadena = input('Nuevo número: ')
        if cadena != '':
            lista_enteros.append(int(cadena))

    return lista_enteros


lista = leer_lista_enteros()
lista_cuadrado = []

for cont in range(len(lista)):
    lista_cuadrado.append(lista[cont] ** 2)

print('Cuadrados de los números leídos: {}' .format(lista_cuadrado))
print('Números leídos: {}' .format(lista))

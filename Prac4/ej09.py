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
print('Lista leída: {}' .format(lista))
print('Ve contestando con números enteros, o con una cadena vacía para acabar...')

suma = ' '
suma = input('¿Qué suma he de buscar en dos posiciones consecutivas? ')

while suma != '':

    for i in range(1, len(lista)):
        if lista[i] + lista[i - 1] == int(suma):
            print('{} + {} = {}' .format(lista[i - 1], lista[i], int(suma)))

    suma = input('¿Qué suma he de buscar en dos posiciones consecutivas? ')

print('¡Adiós!')

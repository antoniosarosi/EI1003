def leer_alturas():

    alturas = []
    print('Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...')

    altura = ' '
    punto = 0

    while altura != '':
        altura = input('Altura en metros en el punto kilométrico {}: ' .format(punto))
        if altura != '':
            alturas.append(int(altura))
        punto += 1

    return alturas


def mostrar_tramo(tramo, inicio, longitud, desnivel):
    print('Tramo de subida número {}:' .format(tramo))
    print('\tEntre los puntos kilométricos {} y {}' .format(inicio, inicio + longitud))
    print('\tLongitud de {} km' .format(longitud))
    print('\tDesnivel de {} m' .format(desnivel))


def mostrar_tramos_subida(lista):

    lista_de_tramos = []
    lista_de_desniveles = []
    lista_de_longitudes = []

    i = 1
    while i < len(lista):

        if lista[i] > lista [i - 1]:
            inicio = i - 1
            fin = i

            while fin < len(lista) and lista[fin] > lista[fin - 1]:
                fin += 1

            lista_de_tramos.append(inicio)

            total = 0
            for sumar in range(inicio + 1, fin):
                total += lista[sumar] - lista[sumar - 1]

            lista_de_desniveles.append(total)
            lista_de_longitudes.append(fin - i)

            i = fin

        i += 1

    if len(lista_de_tramos) == 0:
        print('ningún kilómetro es de subida')

    else:
        for tramo in range(len(lista_de_tramos)):
            mostrar_tramo(tramo + 1, lista_de_tramos[tramo], lista_de_longitudes[tramo], lista_de_desniveles[tramo])


# PROGRAMA PRINCIPAL

lista = leer_alturas()

if len(lista) > 2:
    print('Lista de alturas:', lista)
    mostrar_tramos_subida(lista)
    
else:
    print('Recorrido no válido, con menos de dos puntos')

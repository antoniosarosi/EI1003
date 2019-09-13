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


def calcular_desniveles(lista_de_alturas):

    lista_desniveles = []

    restar = 0
    for numero in range(1, len(lista_de_alturas)):
        lista_desniveles.append(lista_de_alturas[numero] - lista_de_alturas[restar])
        restar += 1

    return lista_desniveles


def posición_máximo(lista):

    maximo = lista[0]
    posicion = 0

    for c in range(1, len(lista)):
        if lista[c] >= maximo:
            maximo = lista[c]
            posicion = c

    return posicion


# PROGRAMA PRINCIPAL

lista = leer_alturas()

if len(lista) < 2:
    print('Recorrido no válido, con menos de dos puntos')

else:
    desniveles = calcular_desniveles(lista)
    posicion_max = posición_máximo(desniveles)

    print('Lista de alturas:', lista)
    print('Lista de desniveles:', desniveles)

    if desniveles[posicion_max] <= 0:
        print('Ningún kilómetro es de subida')

    else:
        print('Kilómetro con mayor desnivel de subida:')
        print('\tEntre los puntos kilométricos {} y {}' .format(posicion_max, posicion_max + 1))
        print('Desnivel de {} m' .format(desniveles[posicion_max]))

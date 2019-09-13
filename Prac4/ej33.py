from moduloimagen import leerImagen, mostrarImagen


def nueva_matriz(filas, columnas, valor):
    matriz = []
    for i in range(filas):
        a = [valor] * columnas
        matriz.append(a)

    return matriz


def reflejar_vertical(imagen):

    recorrer_al_reves = -1

    for i in range(len(imagen) // 2):
        aux = imagen[recorrer_al_reves]
        imagen[recorrer_al_reves] = imagen[i]
        imagen[i] = aux
        recorrer_al_reves -= 1


'''
Para girar la matriz 90º hacía la izquierda primero calculamos su traspuesta, después aprovechando el procedimiento
reflejar_vertical del ej30.py le damos la vuelta, de forma que queda girada en sentido antihorario. Por ejemplo: 

                                [1, 2, 3]       [1, 4, 7]       [3, 6, 9]
                                [4, 5, 6]   >>  [2, 5, 8]   >>  [2, 5, 8]
                                [7, 8, 9]       [3, 6, 9]       [1, 4, 7]
'''


def girada_izquierda(imagen):

    filas = len(imagen[0])      # La traspuesta tendrá el mismo número de filas que columnas de la original
    columnas = len(imagen)      # Y el mismo número de columnas que filas de la original
    girada = nueva_matriz(filas, columnas, 0)

    for i in range(filas):
        for j in range(columnas):
            girada[i][j] = imagen[j][i]

    reflejar_vertical(girada)

    return girada


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
girar = girada_izquierda(matriz)
mostrarImagen(girar)

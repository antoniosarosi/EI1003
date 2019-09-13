from moduloimagen import leerImagen, mostrarImagen


def nueva_matriz(filas, columnas, valor):
    matriz = []
    for i in range(filas):
        a = [valor] * columnas
        matriz.append(a)

    return matriz


def promedio_entorno(matriz, fila, columna):

    suma = 0

    for buscar_fila in range(fila - 1, fila + 2):
        for buscar_columna in range(columna - 1, columna + 2):
            suma += matriz[buscar_fila][buscar_columna]

    promedio = suma / 9
    return promedio


def difuminada(imagen, entero):

    filas = len(imagen)
    columnas = len(imagen[0])

    matriz = nueva_matriz(filas, columnas, entero)

    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            matriz[i][j] = round(promedio_entorno(imagen, i, j), 0)

    return matriz


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
borde = int(input("Introduce el valor del borde: "))
imagen_difuminada = difuminada(matriz, borde)
mostrarImagen(imagen_difuminada)


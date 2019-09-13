from moduloimagen import leerImagen, mostrarImagen


def nueva_matriz(filas, columnas, valor):
    matriz = []
    for i in range(filas):
        a = [valor] * columnas
        matriz.append(a)

    return matriz


def binarizada(matriz, numero):

    matriz_umbral = nueva_matriz(len(matriz), len(matriz[0]), numero)
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            if matriz[i][k] <= matriz_umbral[i][k]:
                matriz_umbral[i][k] = 0
            else:
                matriz_umbral[i][k] = 255

    return matriz_umbral


nombreFichero = input("Introduce el nombre de la imagen: ")
umbral = int(input('Introduce el umbral: '))
matriz = leerImagen(nombreFichero)
matriz_binarizada = binarizada(matriz, umbral)
mostrarImagen(matriz_binarizada)

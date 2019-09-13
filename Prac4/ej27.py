from moduloimagen import leerImagen, mostrarImagen


def aplicar_filtro_negativo(imagen):
    for i in range(len(imagen)):
        for k in range(len(imagen[0])):
            imagen[i][k] = 255 - imagen[i][k]


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
aplicar_filtro_negativo(matriz)
mostrarImagen(matriz)

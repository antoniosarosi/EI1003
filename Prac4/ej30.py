from moduloimagen import leerImagen, mostrarImagen


def reflejar_vertical(imagen):

    recorrer_al_reves = -1

    for i in range(len(imagen) // 2):
        aux = imagen[recorrer_al_reves]
        imagen[recorrer_al_reves] = imagen[i]
        imagen[i] = aux
        recorrer_al_reves -= 1


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
reflejar_vertical(matriz)
mostrarImagen(matriz)

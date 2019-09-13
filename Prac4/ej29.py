from moduloimagen import leerImagen, mostrarImagen


def invertir_fila(fila):

    recorrer_al_reves = -1

    # Si la lista es par nos detenemos a la mitad, si es impar nos detenemos antes del número que está justo en medio
    for i in range(len(fila) // 2):
        aux = fila[recorrer_al_reves]
        fila[recorrer_al_reves] = fila[i]
        fila[i] = aux
        recorrer_al_reves -= 1


def reflejar_horizontal(imagen):

    for i in range(len(imagen)):
        invertir_fila(imagen[i])


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
reflejar_horizontal(matriz)
mostrarImagen(matriz)

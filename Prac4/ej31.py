from moduloimagen import leerImagen


def promedio_entorno(matriz, fila, columna):

    suma = 0

    for buscar_fila in range(fila - 1, fila + 2):                # Incluimos la fila posterior y anterior a la dada
        for buscar_columna in range(columna - 1, columna + 2):   # Incluimos la columna posterior y anterior a la dada
            suma += matriz[buscar_fila][buscar_columna]          # Sumamos los 3 elementos de una misma fila

    promedio = suma / 9
    return promedio


nombreFichero = input("Introduce el nombre de la imagen: ")
matriz = leerImagen(nombreFichero)
fila = int(input("Introduce un número de fila: "))
columna = int(input("Introduce un número de columna: "))

print("El promedio en el entorno del punto ({0},{1}) es" .format(fila, columna), end=" ")
print("{0:.2f}" .format(promedio_entorno(matriz, fila, columna)))

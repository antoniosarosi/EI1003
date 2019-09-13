def ordenar_lista(lista):
    for r in range(len(lista)):
        intercambiar(lista, r,  posición_menor(lista, r))


def posición_menor(lista, desde_tal_posicion):
    minimo = lista[desde_tal_posicion]
    posicion = desde_tal_posicion
    for k in range(desde_tal_posicion, len(lista)):
        if lista[k] < minimo:
            minimo = lista[k]
            posicion = k

    return posicion


def intercambiar(lista, i, j):
    if i != j:
        auxiliar = lista[i]
        lista[i] = lista[j]
        lista[j] = auxiliar


# ------------------------------- PROGRAMA PRINCIPAL -------------------------------

nombre = input('Introduce el nombre de un fichero de test: ')

lista_dni = []

with open(nombre, 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        cadena = linea.split('#')
        lista_dni.append(cadena[0])

del lista_dni[0]
ordenar_lista(lista_dni)

for dni in lista_dni:
    print(dni)

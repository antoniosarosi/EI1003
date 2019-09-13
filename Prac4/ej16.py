def es_dígito(caracter):
    return caracter.isdigit()


def secuencias_dígitos(cadena):

    lista = []
    caracter_aux = ''
    añadir = False

    i = 0
    while i < len(cadena):
        while i < len(cadena) and es_dígito(cadena[i]):
            caracter_aux += cadena[i]
            i += 1
            añadir = True

        if añadir:
            lista.append(caracter_aux)
            caracter_aux = ''
            añadir = False
            i -= 1

        i += 1

    return lista


cadena = input('Introduce una cadena: ')
print('La lista de secuencias obtenida es', secuencias_dígitos(cadena))

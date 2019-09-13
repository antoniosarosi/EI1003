def es_triángulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


def tipo_triángulo(a, b, c):

    if es_triángulo(a, b, c):

        if a == b and a == c:
            return 'equilátero'

        elif a == b or a == c or b == c:
            return 'isósceles'

        else:
            return 'escaleno'

    else:
        return None


parar_bucle = False

while not parar_bucle:

    a = float(input('Introduce el lado a: '))
    b = float(input('Introduce el lado b: '))
    c = float(input('Introduce el lado c: '))

    if tipo_triángulo(a, b, c) is not None:
        print('Es {}' .format(tipo_triángulo(a, b, c)))
        parar_bucle = True

    else:
        print('No es un triángulo')
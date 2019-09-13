es_un_triangulo = False

while not es_un_triangulo:
    a=float(input('Introduce el lado a: '))
    b=float(input('Introduce el lado b: '))
    c=float(input('Introduce el lado c: '))

    if a+b>c and a+c>b and b+c>a:
        if a == b and a == c:
            print('Es equilátero\n')
        elif a == b or a == c or b == c:
            print('Es isósceles\n')

        else:
            print('Es escaleno\n')

        es_un_triangulo = True

    else:
        print('No es un triángulo\n')


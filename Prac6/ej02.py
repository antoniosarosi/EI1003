nombre = input('Introduce el nombre de un fichero de test: ')

with open(nombre, 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        if '#' in linea:
            cadena = linea.split('#')
            print('El alumno con DNI {} ha respondido {}' .format(cadena[0], cadena[1]), end='')

with open(nombre, 'r', encoding='utf-8') as fichero:
    print('Un alumno perfecto habría respondido {}' .format(fichero.readline()))

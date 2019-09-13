def evaluación_test(plantilla, respuestas):

    if len(plantilla) != len(respuestas):
        return None

    lista = []

    correctas = 0
    incorrectas = 0
    no_contestadas = 0

    for r in range(len(respuestas)):

        if respuestas[r] == plantilla[r]:
            correctas += 1

        elif respuestas[r] == '*':
            no_contestadas += 1

        else:
            incorrectas += 1

    lista.append(correctas)
    lista.append(incorrectas)
    lista.append(no_contestadas)

    return lista


# ------------------------------------ PROGRAMA PRINCIPAL  -----------------------------------------

nombre = input('Introduce el nombre de un fichero de test: ')

texto = ''      # Lo usaremos para escribir todas las notas

with open(nombre, 'r', encoding='utf-8') as fichero:

    # Leemos la plantilla del fichero

    leer_plantilla = fichero.readline()

    # Creamos una plantilla que no contiene el caracter de salto de linea

    plantilla = ''
    for r in leer_plantilla:
        if r != '\n':
            plantilla += r

    for linea in fichero:
        if '#' in linea:
            cadena = linea.split('#')

    # Hacemos lo mismo para las respuestas

            respuestas = ''
            for r in cadena[1]:
                if r != '\n':
                    respuestas += r


            respuestas_alumno = evaluación_test(plantilla, respuestas)
            nota = 10 * (respuestas_alumno[0] - respuestas_alumno[1]) / len(plantilla)

            if nota < 5:
                texto += 'DNI: {} NOTA: {}\n' .format(cadena[0], 'NO APTO')

            else:
                texto += 'DNI: {0} NOTA: APTO ({1:5.2f})\n' .format(cadena[0], nota)

# Finalmente escribimos en el fichero el resultado

with open('notas.txt', 'w', encoding='utf-8') as fichero_notas:
    fichero_notas.write(texto)

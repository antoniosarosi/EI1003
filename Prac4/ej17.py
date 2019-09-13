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


plantilla = input('Introduce la plantilla de respuestas correctas: ')
print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')

respuestas = ' '
alum_corregidos = 0

while respuestas != '':
    respuestas = input('Nuevas respuestas: ')
    resultados = evaluación_test(plantilla, respuestas)

    if len(respuestas) != 0:
        if resultados is None:
            print('La cadena introducida es de longitud {} (se esperaba {})' .format(len(respuestas), len(plantilla)))

        else:
            print('Resultados: {} BIEN; {} MAL; {} NS/NC' .format(resultados[0], resultados[1], resultados[2]))
            alum_corregidos += 1

print('Alumnos corregidos: {}' .format(alum_corregidos))

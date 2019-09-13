plantilla = input('Introduce la plantilla de respuestas correctas: ')
print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')

respuestas = ' '
no_contestadas = 0
bien = 0
mal = 0
alum_corregidos = 0

while respuestas != '':
    respuestas = input('Nuevas respuestas: ')

    if len(respuestas) != len(plantilla) and len(respuestas) != 0:
        print('La cadena introducida es de longitud {} (se esperaba {})' .format(len(respuestas), len(plantilla)))

    else:

        if len(respuestas) != 0:

            for r in range(len(respuestas)):
                if respuestas[r] == '*':
                    no_contestadas += 1

                elif respuestas[r] == plantilla[r]:
                    bien += 1

                else:
                    mal += 1

            alum_corregidos += 1

            print('Resultados: {} BIEN; {} MAL; {} NS/NC' .format(bien, mal, no_contestadas))
            no_contestadas = 0
            bien = 0
            mal = 0
print('Alumnos corregidos: {}' .format(alum_corregidos))
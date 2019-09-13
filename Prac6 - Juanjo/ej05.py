def evaluación_test(pcorrecta, respuesta):
    if len(pcorrecta) != len(respuesta):
        lista_respuestas=None
        return lista_respuestas
    else:
        lista_respuestas=[0, 0, 0]
        for i in range(len(pcorrecta)):
            if respuesta[i] == "*":
                lista_respuestas[2] += 1
            elif respuesta[i] == pcorrecta[i]:
                lista_respuestas[0] += 1
            elif respuesta[i] != pcorrecta[i]:
                lista_respuestas[1] += 1
        return lista_respuestas

nombre=input("Introduce el nombre de un fichero de test: ")
fichero=open(nombre, "r", encoding="utf-8")
texto=""
for linea in fichero:
    lista = linea.split("#")
    if "#" in linea:
        lista_respuestas=evaluación_test(pcorrecta, lista[1])
        nota=10*((lista_respuestas[0]-1)-lista_respuestas[1]) / (len(pcorrecta)-1)
        if nota < 5:
            texto+=("DNI: {0} NOTA: NO APTO\n".format(lista[0]))
        else:
            texto+=("DNI: {0} NOTA: APTO ({1:5.2f})\n".format(lista[0], nota))
    else:
        pcorrecta=lista[0]

fichero.close()
fichero_notas=open("notas.txt", "w", encoding="utf-8")
fichero_notas.write(texto)
fichero_notas.close()

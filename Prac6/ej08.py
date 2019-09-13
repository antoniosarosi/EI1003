def buscar_palabra_mas_larga(lista):
    max = ''
    for palabra in lista:
        longitud = len(palabra)

        if longitud > len(max): 
            max = palabra

    return max


nombre = input('Introduce el nombre de un fichero: ')

lista_completa = []     # Esta lista contendrá todas las palabras del fichero

with open(nombre, 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        palabras = linea.split()   # Palabras es una lista que contiene las palabras de una sola linea

        for añadir in palabras:
            lista_completa.append(añadir)

print('Su secuencia de caracteres sin espacios más larga es "{}".' .format(buscar_palabra_mas_larga(lista_completa)))

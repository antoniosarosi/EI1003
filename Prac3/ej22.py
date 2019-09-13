cadena = input('Introduce una cadena de caracteres: ')

todo_guiones_espacios = True

for r in range(len(cadena)):
    if cadena[r] != ' ' and cadena[r] != '-':
        todo_guiones_espacios = False
        break

if todo_guiones_espacios:
    print('Cadena limpiada: =><=')
    print('Cadena original: =>{}<=' .format(cadena))

else:
    for i in range(len(cadena)):
        if cadena[i] != ' ' and cadena[i] != '-':
            posicion_inicial = i
            break

    for i in range(-1, -len(cadena), -1):
        if cadena[i] != ' ' and cadena[i] != '-':
            posicion_final = i
            break

    cadena_limpia = cadena[posicion_inicial: len(cadena) + posicion_final + 1]

    print('Cadena limpiada: =>{}<=' .format(cadena_limpia))
    print('Cadena original: =>{}<=' .format(cadena))

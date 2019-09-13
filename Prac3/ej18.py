cadena = input('Introduce una cadena de caracteres: ')

todo_son_digitos = True
sumatorio = 0

for i in range(len(cadena)):

    if not cadena[i].isdigit():
        todo_son_digitos = False
        print('primer "no dígito": \'{}\' en posición {}' .format(cadena[i], i))
        break

    sumatorio += int(cadena[i])

if todo_son_digitos:
    print('todos los caracteres son dígitos')
    print('¿Cuántos dígitos?', len(cadena))
    print('¿Suma de dígitos?', sumatorio)
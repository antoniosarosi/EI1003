cadena = input('Introduce una cadena de caracteres: ')

todo_son_digitos = True

for i in range(len(cadena)):
    if not cadena[i].isdigit():
        todo_son_digitos = False
        print('No todos los caracteres son dígitos')
        break

if todo_son_digitos:
    print('todos los caracteres son dígitos')
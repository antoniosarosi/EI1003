def todos_dígitos(cadena):

    todo_son_digitos = True

    for i in range(len(cadena)):
        if not cadena[i].isdigit():
            todo_son_digitos = False
            break

    return todo_son_digitos


cadena = input('Introduce una cadena de caracteres: ')

print('todos los caracteres son dígitos') if todos_dígitos(cadena) else print('no todos los caracteres son dígitos')
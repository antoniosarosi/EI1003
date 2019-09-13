def todos_dígitos(cadena):
    for i in range(len(cadena)):
        if not cadena[i].isdigit():
            return False

    return True


nombre = input('Introduce el nombre de un fichero: ')

lista_digitos = []

with open(nombre, 'r', encoding='utf-8') as fichero:
    for linea in fichero:
        lista_cadenas = linea.split()

        for comprobar in lista_cadenas:
            if todos_dígitos(comprobar):
                lista_digitos.append(comprobar)

for i in lista_digitos:
    print(i)

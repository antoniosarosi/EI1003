print("ve introduciendo cadenas de caracteres, o vacío para acabar...")

lista = []

cadena = ' '

while cadena != '':
    cadena = input('Nueva cadena: ')
    if cadena != '':
        lista.append(cadena)

print('Cadenas leídas (desde la última hasta la primera): ')

for cont in range(-1, -len(lista) - 1, -1):
    print('Cadena de longitud {}: =>{}<=' .format(len(lista[cont]), lista[cont]))

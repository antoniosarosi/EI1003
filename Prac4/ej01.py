print("ve introduciendo cadenas de caracteres, o vacío para acabar...")

lista = []

cadena = ' '

while cadena != '':
    cadena = input('Nueva cadena: ')
    if cadena != '':
        lista.append(cadena)

print('Cadenas leídas: ')

for cont in range(len(lista)):
    print('Cadena de longitud {}: =>{}<=' .format(len(lista[cont]), lista[cont]))

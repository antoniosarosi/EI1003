listapar = []
listaimpar = []

print('Ve introduciendo números enteros positivos, o un número negativo para acabar...')

numero = 0

while numero >= 0:
    numero = int(input('Nuevo número: '))
    if numero >= 0:
        if numero % 2 == 0:
            listapar.append(numero)
        else:
            listaimpar.append(numero)

print('Números pares: {}' .format(listapar))
print('Números impares: {}' .format(listaimpar))

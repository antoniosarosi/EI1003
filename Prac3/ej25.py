print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')
cadena = input('Nueva cadena: ')

while cadena != '':
    cambios = 0
    anterior = ' '

    for caracter in cadena:
        if ord(caracter) in range(ord('0'), ord('9') + 1) and ord(anterior) not in range(ord('0'), ord('9') + 1):
            cambios += 1
        anterior = caracter

    print('Secuencias de dígitos encontradas:', cambios)

    cadena = input('Nueva cadena: ')

print('¡Adiós!')

def contar_secuencias_dígitos(cadena):

    cambios = 0
    anterior = ' '

    for caracter in cadena:
        if ord(caracter) in range(ord('0'), ord('9') + 1) and ord(anterior) not in range(ord('0'), ord('9') + 1):
            cambios += 1
        anterior = caracter

    return cambios


print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')
c = input('Nueva cadena: ')

while c != '':
    print('Secuencias de dígitos encontradas:', contar_secuencias_dígitos(c))
    c = input('Nueva cadena: ')

print('¡Adiós!')

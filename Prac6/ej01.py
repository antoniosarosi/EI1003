fichero = input("Introduce el nombre de un fichero: ")
fichero = open(fichero, 'r', encoding='utf-8')

digitos = 0
caracteres = 0

for linea in fichero:
    for recorre in linea:
        if recorre >= '0' and recorre <= '9':
            digitos += 1
        elif recorre.lower() >= 'a' and recorre.lower() <= 'z':
            caracteres += 1

fichero.close()

print('Dígitos decimales:', digitos)
print('letras del inglés:', caracteres)

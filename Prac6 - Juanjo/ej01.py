nombre = input("Introduce el nombre de un fichero: ")
fichero = open(nombre, 'r', encoding='utf-8')

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
print('Letras del inglés:', caracteres)

#mount directorio para montar una unidad externa como usb cd-rom etc


nombre=input("Introduce el nombre de un fichero: ")
fichero=open(nombre, "r", encoding="utf-8")

max = ""
len_linea = 0
lista = []

for linea in fichero:
    lista += linea.split()

for i in range (len(lista)):
    len_linea = len(lista[i])

    if len_linea > len(max):
        max = lista[i]

print('Su secuencia de caracteres sin espacios más larga es "{0}".'.format(max))
fichero.close()

def leer_lista_enteros():
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista=[]
    n=input("Nuevo número: ")
    while n!="":
        n=int(n)
        lista.append(n)
        n=input("Nuevo número: ")
    return lista
def posición_menor(lista, i):
    if len(lista)>0:
        menor=lista[i]
        pos_menor=i
        for o in range (i, len(lista)):
            if menor > lista[o]:
                menor=lista[o]
                pos_menor=o
        return pos_menor
    else:
        return 0
def intercambiar(lista, i, j):
    intermedio=lista[i]
    lista[i]=lista[j]
    lista[j]=intermedio
def ordenar_lista(lista):
    for i in range (len(lista)):
        j=posición_menor(lista, i)
        intercambiar(lista, i, j)

nombre=input("Introduce el nombre de un fichero de test: ")
fichero=open(nombre, "r", encoding="utf-8")
lista_dni=[]
lista=[]
for dni in fichero:
    lista=dni.split("#")
    if "#" in dni:
        lista_dni.append(lista[0])
fichero.close()
ordenar_lista(lista_dni)
texto=""
fichero_ordenado=open("dni.txt", "w", encoding="utf-8")
for i in range(len(lista_dni)):
    texto+=(lista_dni[i] + "\n")
fichero_ordenado.write(texto)
fichero_ordenado.close()
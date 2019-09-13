def todos_dígitos(x):
    b=len(x)
    for i in range(0, b, 1):
        if x[i].isdigit()==False:
            return False
    return True

nombre=input("Introduce el nombre de un fichero: ")
fichero=open(nombre, "r", encoding="utf-8")
max=""
len_linea=0
lista=[]
lista_digitos=[]
for linea in fichero:
    lista+=linea.split()
for j in range (len(lista)):
    if todos_dígitos(lista[j]) is True:
        lista_digitos.append(lista[j])
for i in range (len(lista_digitos)):
    print(lista_digitos[i])
fichero.close()

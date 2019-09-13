nombre=input("Introduce el nombre de un fichero de test: ")
fichero=open(nombre, "r", encoding="utf-8")

lista=[]
laquequieras=False

for linea in fichero:
    if laquequieras is True:
        lista=linea.split('#')
        print("El alumno con DNI {0} ha respondido {1}".format(lista[0], lista[1]), end="")
    else:
        plantilla=linea
    laquequieras=True
print("Un alumno perfecto habría respondido {0}".format(plantilla))

fichero.close()
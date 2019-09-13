from modulomatrices import leerMatrizEnteros

class Coche():

    def __init__(self):
        self.tiempo = 0
        self.distancia = 0
        self.velocidad = 0

    def acelerar(self, aceleración):
        self.velocidad += aceleración

    def decelerar(self, deceleración):
        self.velocidad -= deceleración

    def actualizar(self, tiempo):
        self.tiempo += tiempo
        self.distancia += self.velocidad * tiempo

    def consultar_tiempo(self):
        return self.tiempo

    def consultar_distancia(self):
        return self.distancia

    def consultar_velocidad_actual(self):
        return self.velocidad

    def consultar_velocidad_media(self):
        if self.tiempo == 0:
            return None
        else:
            return self.distancia / self.tiempo

objetivo_carrera = int(input("Introduce el objetivo de la carrera en km: "))
velocidad_inicial = int(input("Introduce la velocidad inicial en km/h: "))
nombreFichero = input("Introduce el nombre del fichero de planes de carrera: ")
matriz = leerMatrizEnteros(nombreFichero)

print("")
columnas = 0
max = 0
lista_participantes = []

for i in range (len(matriz)):
    coche = Coche()
    lista_participantes.append(coche)
    lista_participantes[i].acelerar(velocidad_inicial)

horas = 1

while columnas < len(matriz[0]):

    print("Resultados tras {0} h:".format(horas))
    ncoche = 0

    for filas in range (len(matriz)):
        lista_participantes[filas].acelerar(matriz[filas][columnas])
        lista_participantes[filas].actualizar(1)
        distancia = lista_participantes[filas].consultar_distancia()
        
        print("Coche {0}: alcanza el km {1} a {2} km/h".format(ncoche, distancia, lista_participantes[filas].consultar_velocidad_actual()))

        if distancia > max:
            max = distancia

        ncoche += 1

    print("")
    columnas += 1

    if columnas == len(matriz[0]):
        columnas = 0
    if max >= objetivo_carrera:
        break
    horas += 1

print("Coches ganadores: ", end="")
for recorrer_km in range (len(lista_participantes)):
    km_recorridos = lista_participantes[recorrer_km].consultar_distancia()
    if km_recorridos == max:
        print("{0}".format(recorrer_km), end=" ")

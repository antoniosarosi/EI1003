from modulomatrices import leerMatrizEnteros


class Coche:

    def __init__(self):
        self.tiempo = 0
        self.distancia = 0
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def decelerar(self, decremento):
        self.velocidad -= decremento

    def actualizar(self, cantidad_tiempo):
        self.tiempo += cantidad_tiempo
        self.distancia += self.velocidad * cantidad_tiempo

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


objetivo = int(input("Introduce el objetivo de la carrera en km: "))
velocidad = int(input("Introduce la velocidad inicial en km/h: "))
fichero = input("Introduce el nombre del fichero de planes de carrera: ")

planes = leerMatrizEnteros(fichero)

coches = []

for filas in range(len(planes)):  # Creamos la lista de coches
    coche = Coche()
    coches.append(coche)
    coches[filas].acelerar(velocidad)

horas = 0
tenemos_ganador = False

while not tenemos_ganador:

    for columnas in range(len(planes[0])):
        for filas in range(len(planes)):
            if horas >= 1:
                coches[filas].actualizar(1)
                print("Coche {}: alcanza el km {} a {} km/h".format(filas, coches[filas].consultar_distancia(),
                                                                    coches[filas].consultar_velocidad_actual()))

            coches[filas].acelerar(planes[filas][columnas])

        # Si algun coche llega al objetivo paramos todos los bucles

        for comprobar in range(len(coches)):
            if coches[comprobar].consultar_distancia() >= objetivo:
                tenemos_ganador = True
                break

        if tenemos_ganador:
            break

        # Mientras ningún coche alcance el objetivo seguimos mostrando resultados

        print("\n")
        print("Resultados tras {} h:".format(horas + 1))
        horas += 1

# Una vez acaba el bucle principal mostramos los ganadores:

lista_distancias = []  # Las distancias recorridas por cada coche al final de la carrera (cuando tenemos_ganador = True)

for i in range(len(coches)):
    lista_distancias.append(coches[i].consultar_distancia())

ganadores = []  # Número del coche o coches que hayan ganado (recorrido más distancia al final de la carrera)

for i in range(len(lista_distancias)):
    if lista_distancias[i] == max(lista_distancias):
        ganadores.append(i)

print("Coches ganadores:", end=" ")
for i in range(len(ganadores)):
    print(ganadores[i], end=" ")

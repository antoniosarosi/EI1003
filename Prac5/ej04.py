class Coche:

    def __init__(self):
        self.tiempo = 0.00
        self.distancia = 0.00
        self.velocidad = 0.00

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
        if self.tiempo == 0.00:
             return None
        else:
            return self.distancia / self.tiempo


print("Tu coche está inicialmente parado\n")
coche = Coche()

opcion = 1

while opcion < 5 and opcion > 0:

    print("1. Acelerar\n2. Decelerar\n3. Actualizar\n4. Consultar\n5. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        aceleracion = float(input("Introduce cuántos km/h quieres acelerar: "))
        coche.acelerar(aceleracion)

    elif opcion == 2:
        decelerar = float(input("Introduce cuántos km/h quieres decelerar: "))
        coche.decelerar(decelerar)

    elif opcion == 3:
        horas = float(input("Introduce cuántas horas han pasado: "))
        coche.actualizar(horas)

    elif opcion == 4:
        print("El tiempo trascurrido es {0:.2f} h" .format(coche.consultar_tiempo()))
        print("La distancia recorrida es {0:.2f} km" .format(coche.consultar_distancia()))
        print("La velocidad actual es {0:.2f} km/h" .format(coche.consultar_velocidad_actual()))

        if coche.consultar_velocidad_media() is None:
            print("No puedo calcular la velocidad media si no ha trascurrido tiempo")
        else:
            print("La velocidad media es {0:.2f} km/h" .format(coche.consultar_velocidad_media()))

    else:
        print("¡adiós!")

    print("\n")

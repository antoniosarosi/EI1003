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


coche = Coche()

coche.acelerar(100)
coche.actualizar(1.5)

coche.decelerar(40.1)
coche.actualizar(0.5)

print("Tiempo: {0}".format(coche.consultar_tiempo()))
print("Distancia: {0}".format(coche.consultar_distancia()))
print("Velocidad actual: {0}".format(coche.consultar_velocidad_actual()))
print("Velocidad media: {0}".format(coche.consultar_velocidad_media()))

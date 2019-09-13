class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, importe):
        self.saldo += importe

    def reintegrar(self, importe):
        self.saldo -= importe

    def consultar_saldo(self):
        return self.saldo


saldo_inicial = float(input("Introduce cuántos euros quieres como saldo inicial de tu cuenta: "))
print("\n")
cuenta = Cuenta(saldo_inicial)

opcion = 1

while opcion < 4 and opcion > 0:
    print("1. Hacer un ingreso\n2. Pedir un reintegro\n3. Consultar el saldo\n4. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        ingreso = float(input("Introduce cuántos euros quieres ingresar: "))
        cuenta.ingresar(ingreso)

    elif opcion == 2:
        reintegro = float(input("Introduce cuántos euros quieres que se te reintegren: "))
        cuenta.reintegrar(reintegro)

    elif opcion == 3:
        print("El saldo actual es {0:.2f} euros" .format(cuenta.consultar_saldo()))

    else:
        print("¡adiós!")
    print("\n")

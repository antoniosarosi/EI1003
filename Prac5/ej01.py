class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, importe):
        self.saldo += importe

    def reintegrar(self, importe):
        self.saldo -= importe

    def consultar_saldo(self):
        return self.saldo


cuenta1 = Cuenta(0)
cuenta2 = Cuenta(1000)

cuenta1.ingresar(100)
cuenta2.reintegrar(20)

print("Saldos: {0} y {1}".format(cuenta1.consultar_saldo(), cuenta2.consultar_saldo()))

class Cuenta:

    def __init__(self ,nombre ,numero ,saldo):
        self.nombre = nombre
        self.numero = numero
        self.saldo = saldo

    def depositar (self, monto):
        saldo = self.saldo + monto
        return saldo
    def retirar(self, monto):
        saldo = self.saldo - monto
        return saldo


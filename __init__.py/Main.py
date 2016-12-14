class Cliente:
    def __init__(self, nombre , saldo ):
        self.nombre = nombre
        self.saldo = saldo

    def retirar (self, cantidad):
        if cantidad > self.saldo:
            raise RuntimeError('cantidad mayor que saldo disponible.')
        self.saldo -= cantidad
        return  self.saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

if __name__ == '__main__':
    abdel = Cliente ('Abdel martinez' , 1000.0)
    oliver = Cliente ('Oliver arauz' , 2500.0)
    abdel.depositar(50.0)
    oliver.retirar(500.0)
    print("el saldo de " + abdel.nombre + " es " + str(abdel.saldo))

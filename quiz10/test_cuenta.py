from unittest import TestCase
from Cuenta import Cuenta

class TestCuenta(TestCase):
    def test_depositar(self):
        C = Cuenta("Mayorquin", "0", 0.0)
        self.assertEqual(C.depositar(5000), 5000)

    def test_retirar(self):
        C= Cuenta("mayorquin", "0", 500.00)
        self.assertEqual(C.retirar(200), 300)







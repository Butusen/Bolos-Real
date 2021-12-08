import unittest
from Bolos import Bolos

class MyTestCase(unittest.TestCase):
    def crearPartida(self):
        partida = Bolos()
    def test_suma_0(self):
        partida = Bolos()
        ronda = "--------------------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(0, suma)

    def test_suma_5(self):
        partida = Bolos()
        ronda = "113-----------------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(5, suma)






if __name__ == '__main__':
    unittest.main()

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

    def test_suma_19(self):
        partida = Bolos()
        ronda = "113563--------------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(19, suma)

    def test_suma_40(self):
        partida = Bolos()
        ronda = "44358---35--8-------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(40, suma)

    def test_strike(self):
        partida = Bolos()
        ronda = "113-x-43------------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(5+17+7, suma)

    def test_spare(self):
        partida = Bolos()
        ronda = "1/3---43------------"
        suma = partida.calcularPuntos(ronda)
        self.assertEqual(13+7, suma)






if __name__ == '__main__':
    unittest.main()

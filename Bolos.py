class Bolos:

    def calcularPuntos(self,ronda):
        suma = 0
        for i, numero in enumerate(ronda):
            if numero == "x":
                suma = suma + 10 + int(ronda[i+2]) + int(ronda[i+3])
            elif numero != "-":
                suma = suma + int(numero)
        return suma
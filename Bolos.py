class Bolos:

    def calcularPuntos(self,ronda):
        suma =0
        for i, numero in enumerate(ronda):
            if numero == "-":
                return suma
            elif numero != "-":
                suma = suma + int(numero)
        return suma
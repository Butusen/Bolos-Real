class Bolos:

    def calcularPuntos(self,ronda):
        suma = 0
        for i, numero in enumerate(ronda):
            if numero == "x":
                if ronda[i+2] == "/":
                    suma = suma + 10 + 10
                elif ronda[i+2] != "/":
                    suma = suma + 10 + int(ronda[i+1]) + int(ronda[i+2])
            elif numero == "/":
                if ronda[i+1] == "x":
                    suma = suma - int(ronda[i-1]) + 10 + 10
                elif ronda[i+1] != "x":
                    suma = suma - int(ronda[i-1]) + 10 + int(ronda[i+1])
            elif numero != "-":
                suma = suma + int(numero)
        return suma
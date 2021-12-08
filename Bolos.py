class Bolos:

    def calcularPuntos(self,ronda):
        suma = 0
        for i, numero in enumerate(ronda):
            if numero == "x" and (i %2==0):
                suma = suma + 10 + int(ronda[i+2]) + int(ronda[i+3])
            elif numero == "/" and (i%2 !=0):
                suma = suma - int(ronda[i-1]) + 10 + int(ronda[i+1])
            elif numero != "-":
                suma = suma + int(numero)
        return suma
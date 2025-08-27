import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        m = self.promedio()
        return math.sqrt(sum((x - m)**2 for x in self.datos) / (len(self.datos) - 1))

numeros = list(map(float, input("ingrese 10 numeros:").split()))
estad = Estadistica(numeros)
print(f"el promedio es {estad.promedio():.5f}")
print(f"la desviacion estandar es {estad.desviacion():.5f}")

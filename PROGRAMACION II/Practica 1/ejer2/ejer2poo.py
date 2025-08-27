import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return self.b**2 - 4*self.a*self.c

    def get_raices(self):
        d = self.get_discriminante()
        if d > 0:
            r1 = (-self.b + math.sqrt(d)) / (2*self.a)
            r2 = (-self.b - math.sqrt(d)) / (2*self.a)
            return [r1, r2]
        elif d == 0:
            return [-self.b / (2*self.a)]
        else:
            return []
a, b, c = map(float, input("ingrese a, b, c:").split())
ecuacion = EcuacionCuadratica(a, b, c)
raices = ecuacion.get_raices()

if len(raices) == 2:
    print(f"la ecuacion tiene dos raices {raices[0]:.6f} y {raices[1]:.6f}")
elif len(raices) == 1:
    print(f"la ecuacion tiene una raiz {raices[0]:.6f}")
else:
    print("la ecuacion no tiene raices reales")

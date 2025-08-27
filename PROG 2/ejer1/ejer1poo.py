class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tiene_solucion(self):
        return (self.a * self.d - self.b * self.c) != 0

    def get_x(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)

    def get_y(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)

a, b, c, d, e, f = map(float, input("ingrese a, b, c, d, e, f:").split())
ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tiene_solucion():
    print("x :", ecuacion.get_x())
    print("y :", ecuacion.get_y())
else:
    print("la ecuación no tiene solucion")

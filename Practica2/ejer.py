import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, b):
        return AlgebraVectorial(self.x + b.x, self.y + b.y, self.z + b.z)

    def __sub__(self, b):
        return AlgebraVectorial(self.x - b.x, self.y - b.y, self.z - b.z)

    def __mul__(self, b):
        if isinstance(b, AlgebraVectorial):
            return self.x*b.x + self.y*b.y + self.z*b.z
        else:
            return AlgebraVectorial(self.x*b, self.y*b, self.z*b)

    def proyeccionSobre(self, b):
        escalar = self * b / (b.magnitud()**2)
        return AlgebraVectorial(b.x*escalar, b.y*escalar, b.z*escalar)

    def componenteEn(self, b):
        return (self * b) / b.magnitud()

if __name__ == "__main__":
    a = AlgebraVectorial(3, 4, 0)
    b = AlgebraVectorial(1, 2, 0)

    print("Vec a:", a)
    print("Vec b:", b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("Proyeccion de a_sobre_b:", a.proyeccionSobre(b))
    print("Componente de_a_en b:", a.componenteEn(b))
    print("|a| =", a.magnitud())



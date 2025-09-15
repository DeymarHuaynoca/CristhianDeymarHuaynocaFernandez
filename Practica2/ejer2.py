import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("Multiplicación solo soporta un escalar.")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector cero")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("2 * a =", 2 * a)
    print("a * 2 =", a * 2)
    print("a == b?", a == b)
    print("a • b =", a.dot(b))
    print("a × b =", a.cross(b))
    print("|a| =", a.magnitude())
    print("Vec unitario de a =", a.normalize())

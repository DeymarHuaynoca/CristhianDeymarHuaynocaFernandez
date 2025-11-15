class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"{self.tipo} - {self.material}"

class Ropero:
    def __init__(self, material):
        self.material = material
        self.ropas = []
        self.nroRopas = 0

    def adicionarPrenda(self, prenda):
        if self.nroRopas < 20:
            self.ropas.append(prenda)
            self.nroRopas += 1
        else:
            print("No se pueden agregar mas prendas (maximo 20).")

    def eliminarPorMaterial(self, matX):
        self.ropas = [r for r in self.ropas if r.material != matX]
        self.nroRopas = len(self.ropas)

    def eliminarPorTipo(self, tipoX):
        self.ropas = [r for r in self.ropas if r.tipo != tipoX]
        self.nroRopas = len(self.ropas)

    def mostrarPorMaterial(self, matX):
        print(f"\nPrendas de material '{matX}':")
        for r in self.ropas:
            if r.material == matX:
                print("  ", r)

    def mostrarPorTipo(self, tipoX):
        print(f"\nPrendas de tipo '{tipoX}':")
        for r in self.ropas:
            if r.tipo == tipoX:
                print("  ", r)

    def mostrarTodo(self):
        print("\n--- Contenido del Ropero ---")
        if not self.ropas:
            print("  (vacío)")
        for r in self.ropas:
            print("  ", r)

ropero = Ropero("Madera")

ropero.adicionarPrenda(Ropa("Polera", "Algodon"))
ropero.adicionarPrenda(Ropa("Pantalon", "Jean"))
ropero.adicionarPrenda(Ropa("Camisa", "Seda"))
ropero.adicionarPrenda(Ropa("Chaqueta", "Cuero"))
ropero.adicionarPrenda(Ropa("Short", "Algodon"))

print("\n Ropero inicial con 5 prendas:")
ropero.mostrarTodo()

print("\n Eliminando prendas de material 'Algodon'...")
ropero.eliminarPorMaterial("Algodon")
ropero.mostrarTodo()

print("\n Eliminando prendas de tipo 'Camisa'...")
ropero.eliminarPorTipo("Camisa")
ropero.mostrarTodo()

ropero.mostrarPorMaterial("Cuero")

ropero.mostrarPorTipo("Pantalon")

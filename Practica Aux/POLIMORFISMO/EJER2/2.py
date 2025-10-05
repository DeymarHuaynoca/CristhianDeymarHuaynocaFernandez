class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Desconocida", cantidad_jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = cantidad_jugadores

    @classmethod
    def solo_nombre(cls, nombre):
        return cls(nombre=nombre)

    @classmethod
    def nombre_y_plataforma(cls, nombre, plataforma):
        return cls(nombre=nombre, plataforma=plataforma)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de jugadores: {self.cantidad_jugadores}")

    def agregarJugadores(self, cantidad=None):
        if cantidad is None:
            self.cantidad_jugadores += 1
            print(f"Se agrego 1 jugador. Total: {self.cantidad_jugadores}")
        else:
            self.cantidad_jugadores += cantidad
            print(f"Se agregaron {cantidad} jugadores. Total: {self.cantidad_jugadores}")

v1 = Videojuego("League of Legends", "PC", 10)
v2 = Videojuego.nombre_y_plataforma("God of War", "PlayStation 5")

print("=== Videojuego 1 ===")
v1.mostrar_info()
print("\n=== Videojuego 2 ===")
v2.mostrar_info()

print("\n Agregando jugadores ")
v1.agregarJugadores()      
v2.agregarJugadores(3)   

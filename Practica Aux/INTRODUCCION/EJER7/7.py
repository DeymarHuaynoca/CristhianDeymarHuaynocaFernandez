class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def alimentar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} ha comido... Energia actual: {self.energia}")

    def jugar(self):
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
        print(f"{self.nombre} ha jugado... Energia actual: {self.energia}")

m1 = Mascota("Firulais", "Perro", 50)
m2 = Mascota("Misu", "Gato", 30)

m1.alimentar()
m1.jugar()
m1.jugar()

m2.alimentar()
m2.alimentar()
m2.jugar()

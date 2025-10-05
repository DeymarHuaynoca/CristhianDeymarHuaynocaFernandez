class Pasajero:
    def __init__(self, nombre="", edad=0, genero=""):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __pos__(self):
        self.nombre = input("Nombre del pasajero: ")
        self.edad = int(input("Edad: "))
        self.genero = input("Genero (M/F): ")
        return self

    def __neg__(self):
        print(f"Pasajero: {self.nombre} | Edad: {self.edad} | Genero: {self.genero}")


class Crucero:
    def __init__(self, nombre="", paisOrigen="", paisDestino=""):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.nroPasajeros = 0

        self.pasajeros = [[""] * 100 for _ in range(3)]

    def __pos__(self):
        self.nombre = input("Nombre del crucero: ")
        self.paisOrigen = input("Pais de origen: ")
        self.paisDestino = input("Pais de destino: ")

        n = int(input("Numero de pasajeros a ingresar: "))
        for _ in range(n):
            nombre = input("Nombre pasajero: ")
            hab = input("Numero habitacion: ")
            costo = input("Costo pasaje: ")

            i = self.nroPasajeros
            self.pasajeros[0][i] = nombre
            self.pasajeros[1][i] = hab
            self.pasajeros[2][i] = costo
            self.nroPasajeros += 1
        return self

    def __neg__(self):
        print(f"\nCrucero: {self.nombre}")
        print(f"Origen: {self.paisOrigen}  → Destino: {self.paisDestino}")
        print(f"Nro pasajeros: {self.nroPasajeros}")
        print("Lista de pasajeros:")
        for i in range(self.nroPasajeros):
            print(f"  {self.pasajeros[0][i]} | Hab: {self.pasajeros[1][i]} | Costo: {self.pasajeros[2][i]}")

    def __eq__(self, other):
        total_self = sum(int(self.pasajeros[2][i]) for i in range(self.nroPasajeros))
        total_other = sum(int(other.pasajeros[2][i]) for i in range(other.nroPasajeros))
        print(f"Suma total de pasajes Crucero 1: {total_self}")
        print(f"Suma total de pasajes Crucero 2: {total_other}")
        return total_self == total_other

    def __add__(self, other):
        if self.nroPasajeros == other.nroPasajeros:
            print("Ambos cruceros tienen la MISMA cantidad de pasajeros.")
        else:
            print("Los cruceros tienen DIFERENTE cantidad de pasajeros.")

    def __sub__(self, pasajeros_lista):
        hombres = sum(1 for p in pasajeros_lista if p.genero.upper() == "M")
        mujeres = sum(1 for p in pasajeros_lista if p.genero.upper() == "F")
        print(f"En el crucero hay {hombres} hombres y {mujeres} mujeres.")
        return (hombres, mujeres)

if __name__ == "__main__":
    c1 = Crucero("Caribe Star", "Panamá", "Cuba")
    c2 = Crucero("Pacific Queen", "Chile", "México")

    p1 = Pasajero("Juan Vargas", 34, "M")
    p2 = Pasajero("Martina Vasques", 28, "F")
    p3 = Pasajero("Wilmer Montero", 41, "M")
    p4 = Pasajero("Ana Flores", 25, "F")
    p5 = Pasajero("Carlos Ruiz", 50, "M")

    pasajeros = [p1, p2, p3, p4, p5]

    -c1    
    -p1   

    c1.pasajeros[0][0], c1.pasajeros[1][0], c1.pasajeros[2][0] = "Juan Vargas", "502", "500"
    c1.pasajeros[0][1], c1.pasajeros[1][1], c1.pasajeros[2][1] = "Martina Vasques", "603", "1000"
    c1.nroPasajeros = 2

    c2.pasajeros[0][0], c2.pasajeros[1][0], c2.pasajeros[2][0] = "Wilmer Montero", "401", "925"
    c2.nroPasajeros = 1

    c1 == c2

    c1 + c2

    c1 - pasajeros

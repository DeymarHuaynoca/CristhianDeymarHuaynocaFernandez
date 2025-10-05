class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"CI: {self.ci}")

    def mayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
            return True
        else:
            print(f"{self.nombre} es menor de edad.")
            return False

    def modificarEdad(self, nuevo):
        self.edad = nuevo
        print(f"La nueva edad de {self.nombre} es {self.edad}.")
persona1 = Persona("Carlos", "Pérez", "Gómez", 20, "1234567")
persona2 = Persona("Ana", "Pérez", "López", 16, "7654321")

persona1.mostrarDatos()
persona2.mostrarDatos()

persona1.mayorDeEdad()
persona2.mayorDeEdad()

persona2.modificarEdad(18)

if persona1.paterno == persona2.paterno:
    print(f"{persona1.nombre} y {persona2.nombre} tienen el mismo apellido paterno.")
else:
    print(f"{persona1.nombre} y {persona2.nombre} NO tienen el mismo apellido paterno.")

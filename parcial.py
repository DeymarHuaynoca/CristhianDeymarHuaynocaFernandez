class Persona:
    def _init_(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

class Cabina:
    def _init_(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []

    def agregarPersona(self, persona):
        if len(self.personasAbordo) >= 10:
            return False
        peso_actual = sum(p.peso for p in self.personasAbordo)
        if peso_actual + persona.peso > 850:
            return False
        self.personasAbordo.append(persona)
        return True

    def totalIngresos(self):
        total = 0
        for p in self.personasAbordo:
            if p.edad < 5:
                total += 0
            elif 5 <= p.edad <= 25:
                total += 2
            elif p.edad > 60:
                total += 1.5
            else:
                total += 3
        return total

class Linea:
    def _init_(self, color):
        self.color = color
        self.cabinas = []

    def agregarCabina(self, cab):
        self.cabinas.append(cab)

    def agregarPersona(self, persona, nroCabina):
        for cab in self.cabinas:
            if cab.nroCabina == nroCabina:
                return cab.agregarPersona(persona)
        return False

    def verificarReglas(self):
        errores = []
        for cab in self.cabinas:
            if len(cab.personasAbordo) > 10:
                errores.append(True)
            peso_total = sum(p.peso for p in cab.personasAbordo)
            if peso_total > 850:
                errores.append(True)
        return errores

    def ingresoTotal(self):
        return sum(c.totalIngresos() for c in self.cabinas)

class MiTeleferico:
    def _init_(self):
        self.lineas = []
        self.cantidadIngresos = 0.0

    def agregarLinea(self, linea):
        self.lineas.append(linea)

    def agregarPersonaALinea(self, persona, colorLinea, nroCabina):
        for linea in self.lineas:
            if linea.color == colorLinea:
                return linea.agregarPersona(persona, nroCabina)
        return False

    def verificarTodo(self):
        problemas = []
        for linea in self.lineas:
            problemas += linea.verificarReglas()
        return problemas

    def calcularIngresoTotal(self):
        self.cantidadIngresos = sum(l.ingresoTotal() for l in self.lineas)
        return self.cantidadIngresos

    def imprimirResumen(self):
        print("==== MI TELEFÉRICO ====")
        for linea in self.lineas:
            print(f"Línea {linea.color} - Ingreso: {linea.ingresoTotal()} Bs")
        print("=======================")

teleferico = MiTeleferico()

l1 = Linea("Rojo")
l2 = Linea("Amarillo")
l3 = Linea("Verde")

for i in range(1, 6):
    l1.agregarCabina(Cabina(i))
    l2.agregarCabina(Cabina(i))
    l3.agregarCabina(Cabina(i))

teleferico.agregarLinea(l1)
teleferico.agregarLinea(l2)
teleferico.agregarLinea(l3)

def menu():
    while True:
        print("\n=== MENU MI TELEFÉRICO ===")
        print("1. Agregar persona a una cabina")
        print("2. Verificar reglas")
        print("3. Calcular ingreso total")
        print("4. Mostrar resumen")
        print("5. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso: "))
            persona = Persona(nombre, edad, peso)

            linea = input("Línea (Rojo/Amarillo/Verde): ")
            cabina = int(input("Número de cabina: "))

            r = teleferico.agregarPersonaALinea(persona, linea, cabina)
            if r:
                print("Persona agregada.")
            else:
                print("No se pudo agregar.")

        elif op == "2":
            problemas = teleferico.verificarTodo()
            if len(problemas) == 0:
                print("Todo correcto.")
            else:
                print("Hay problemas en las cabinas.")

        elif op == "3":
            print("Ingreso total:", teleferico.calcularIngresoTotal(), "Bs")

        elif op == "4":
            teleferico.imprimirResumen()

        elif op == "5":
            break

menu()
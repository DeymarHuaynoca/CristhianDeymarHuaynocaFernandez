class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.nombre} - {self.cargo} - ${self.sueldo}"

class Departamento:
    def __init__(self, nombre, area, empleados=None):
        self.nombre = nombre
        self.area = area
        self.empleados = empleados if empleados else []

    def mostrarEmpleados(self):
        print(f"\nDepartamento: {self.nombre} ({self.area})")
        if not self.empleados:
            print("  No hay empleados.")
            return
        for emp in self.empleados:
            print("  ", emp)

    def cambioSalario(self, nuevo_sueldo):
        for emp in self.empleados:
            emp.sueldo = nuevo_sueldo

empleados_dep1 = [
    Empleado("Ana", "Analista", 4000),
    Empleado("Luis", "Programador", 3500),
    Empleado("Maria", "Diseñadora", 3800),
    Empleado("Carlos", "Tester", 3200),
    Empleado("Jose", "DevOps", 4500)
]

departamento1 = Departamento("TI", "Tecnologia", empleados_dep1)
departamento2 = Departamento("RRHH", "Recursos Humanos")  

print("=== Empleados Departamento 1 ===")
departamento1.mostrarEmpleados()

print("=== Empleados Departamento 2 ===")
departamento2.mostrarEmpleados()

print("\nAplicando aumento de sueldo a TODOS en departamento 1...")
departamento1.cambioSalario(5000)

print("\n=== Departamento 1 (sueldos actualizados) ===")
departamento1.mostrarEmpleados()

def verificarEmpleado(dep_origen, dep_destino):
    for emp in dep_origen.empleados:
        if emp in dep_destino.empleados:
            return True
    return False

print("\n¿Algún empleado de dep1 pertenece tambien a dep2?:",
      verificarEmpleado(departamento1, departamento2))

print("\nMoviendo empleados del departamento 1 al departamento 2...")

departamento2.empleados.extend(departamento1.empleados)
departamento1.empleados.clear()

print("\n=== Departamento 1 (ahora vacio) ===")
departamento1.mostrarEmpleados()

print("=== Departamento 2 (ahora con empleados) ===")
departamento2.mostrarEmpleados()

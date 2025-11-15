class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []   

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empresa(self):
        print(f"\nEmpresa: {self.nombre}")
        print("Empleados:")
        if not self.empleados:
            print("  No hay empleados registrados.")
        else:
            for emp in self.empleados:
                print("  - " + emp.mostrar_info())

    def buscar_empleado(self, nombre):
        for emp in self.empleados:
            if emp.nombre == nombre:
                return emp
        return None

    def eliminar_empleado(self, nombre):
        emp = self.buscar_empleado(nombre)
        if emp:
            self.empleados.remove(emp)
            print(f"Empleado '{nombre}' eliminado correctamente.")
        else:
            print(f"Empleado '{nombre}' no encontrado.")

    def promedio_salarial(self):
        if not self.empleados:
            print("No hay empleados para calcular el promedio.")
            return
        promedio = sum(emp.salario for emp in self.empleados) / len(self.empleados)
        print(f"Promedio salarial: {promedio}")

    def empleados_con_salario_mayor(self, valor):
        print(f"\nEmpleados con salario mayor a {valor}:")
        filtrados = [emp for emp in self.empleados if emp.salario > valor]
        if filtrados:
            for emp in filtrados:
                print("  - " + emp.mostrar_info())
        else:
            print("  Ningun empleado supera ese salario.")

empresa1 = Empresa("TechWorld")

empresa1.agregar_empleado(Empleado("Carlos", "Programador", 5000))
empresa1.agregar_empleado(Empleado("Ana", "Diseñadora", 4500))
empresa1.agregar_empleado(Empleado("Luis", "Gerente", 7000))

empresa1.mostrar_empresa()

print("\nBUSCAR EMPLEADO:")
emp = empresa1.buscar_empleado("Ana")
if emp:
    print(emp.mostrar_info())
else:
    print("Empleado no encontrado.")

print("\nELIMINAR EMPLEADO:")
empresa1.eliminar_empleado("Carlos")
empresa1.mostrar_empresa()

print("\nPROMEDIO SALARIAL:")
empresa1.promedio_salarial()

empresa1.empleados_con_salario_mayor(4600)

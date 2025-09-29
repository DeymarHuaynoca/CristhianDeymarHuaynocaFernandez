from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Empleado : {self.nombre}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self) -> float:
        return self.salario_anual / 12

    def __str__(self) -> str:
        return f"{super().__str__()} | tipo: tiempo completo | salario anual: {self.salario_anual}"

class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario_mensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_hora

    def __str__(self) -> str:
        return (f"{super().__str__()} | tipo: tiempo horario | "
                f"Horas: {self.horas_trabajadas} | tarifa por hora: {self.tarifa_hora}")

def main():
    empleados = []

    for i in range(3):
        print(f"\nEmpleado tiempo completo {i+1}")
        nombre = input("Ingresar nombre... ")
        salario = float(input("Ingresa salario anual... "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salario))

    for i in range(2):
        print(f"\nEmpleado tiempo horario {i+1}")
        nombre = input("Ingresar nombre... ")
        horas = float(input("Ingrese horas trabajadas... "))
        tarifa = float(input("Ingrese tarifa por hora..."))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    print("\nLista de empleados")
    for emp in empleados:
        print(emp, "| salario mensual:", emp.calcular_salario_mensual())

if __name__ == "__main__":
    main()

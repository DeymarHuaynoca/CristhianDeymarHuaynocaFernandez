class Bus:
    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        self.pasajeros_actuales = 0
        self.costo_pasaje = 1.50

    def subir_pasajeros(self, cantidad):
        if self.pasajeros_actuales + cantidad <= self.capacidad_total:
            self.pasajeros_actuales += cantidad
            print(f"{cantidad} pasajeros subieron al bus.")
        else:
            disponibles = self.capacidad_total - self.pasajeros_actuales
            print(f"Solo pueden subir {disponibles} pasajeros, el resto no entra.")
            self.pasajeros_actuales = self.capacidad_total

    def cobrar_pasaje(self):
        total = self.pasajeros_actuales * self.costo_pasaje
        print(f"Se recaudo Bs. {total:.2f} en pasajes.")
        return total

    def mostrar_asientos_disponibles(self):
        disponibles = self.capacidad_total - self.pasajeros_actuales
        print(f"Asientos disponibles: {disponibles}")


mi_bus = Bus(30)  

mi_bus.subir_pasajeros(15)
mi_bus.mostrar_asientos_disponibles()
mi_bus.cobrar_pasaje()

mi_bus.subir_pasajeros(20) 
mi_bus.mostrar_asientos_disponibles()
mi_bus.cobrar_pasaje()

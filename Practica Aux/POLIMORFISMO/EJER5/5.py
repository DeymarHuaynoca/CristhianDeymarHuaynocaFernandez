class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio  
        self.ram = ram          
        self.nroApp = nroApp

    def mostrar(self):
        print(f"Dueño: {self.dueño}")
        print(f"Nro Tel: {self.nroTel}")
        print(f"Espacio: {self.espacio} GB")
        print(f"RAM: {self.ram} GB")
        print(f"Nro de Apps: {self.nroApp}")
        print("")

    def __add__(self, otro):
        nuevo = Celular(self.nroTel, self.dueño, self.espacio, self.ram, self.nroApp + 10)
        return nuevo

    def __sub__(self, otro):
        nuevo = Celular(self.nroTel, self.dueño, self.espacio - 5, self.ram, self.nroApp)
        return nuevo

cel = Celular("76543210", "Kayn Doomfury", 128, 8, 25)

print(" Datos iniciales ")
cel.mostrar()

cel_mas = cel + 1    
cel_menos = cel - 1  

print("Despues del operador ++ ")
cel_mas.mostrar()

print("Despues del operador -- ")
cel_menos.mostrar()

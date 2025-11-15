class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []  

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def mostrar_doctores(self):
        print(f"\nDoctores del Hospital {self.nombre}:")
        if not self.doctores:
            print("  No hay doctores asignados.")
        else:
            for d in self.doctores:
                print(" -", d)

d1 = Doctor("Carlos Perez", "Cardiologia")
d2 = Doctor("Ana Gomez", "Pediatria")
d3 = Doctor("Luis Vargas", "Traumatologia")

h1 = Hospital("Hospital Central")
h2 = Hospital("Clinica Los Andes")

h1.agregar_doctor(d1)
h1.agregar_doctor(d2)

h2.agregar_doctor(d2)  
h2.agregar_doctor(d3)

h1.mostrar_doctores()
h2.mostrar_doctores()

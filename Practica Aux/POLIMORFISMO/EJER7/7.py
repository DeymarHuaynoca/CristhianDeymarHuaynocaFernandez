class Parada:
    def __init__(self, nombreP="Sin nombre"):
        self.admins = [""] * 10            
        self.autos = [[""] * 3 for _ in range(10)]  
        self.nombreP = nombreP

        self.nroAdmins = 0
        self.nroAutos = 0

    @classmethod
    def crear_con_datos(cls):
        nombre = input("Ingrese el nombre de la parada: ")
        parada = cls(nombre)

        cant_admins = int(input("Ingrese numero de admins: "))
        for _ in range(cant_admins):
            admin = input("Ingrese nombre de admin: ")
            parada.adicionar_admin(admin)

        cant_autos = int(input("Ingrese numero de autos: "))
        for _ in range(cant_autos):
            modelo = input("Modelo: ")
            conductor = input("Conductor: ")
            placa = input("Placa: ")
            parada.adicionar_auto(modelo, conductor, placa)

        return parada

    def mostrar(self):
        print(f"\nParada: {self.nombreP}")
        print("Administradores:")
        for i in range(self.nroAdmins):
            print(f"  - {self.admins[i]}")

        print("\nAutos:")
        for i in range(self.nroAutos):
            modelo, conductor, placa = self.autos[i]
            print(f"  Modelo: {modelo}, Conductor: {conductor}, Placa: {placa}")

    def adicionar_admin(self, admin):
        if self.nroAdmins < 10:
            self.admins[self.nroAdmins] = admin
            self.nroAdmins += 1
            print(f"Admin '{admin}' agregado correctamente.")
        else:
            print("No se pueden agregar más admins (limite alcanzado).")

    def adicionar_auto(self, modelo, conductor, placa):
        if self.nroAutos < 10:
            self.autos[self.nroAutos][0] = modelo
            self.autos[self.nroAutos][1] = conductor
            self.autos[self.nroAutos][2] = placa
            self.nroAutos += 1
            print(f"Auto '{modelo}' agregado correctamente.")
        else:
            print("No se pueden agregar más autos (limite alcanzado).")

if __name__ == "__main__":
    p1 = Parada()
    p1.adicionar_admin("Carlos")
    p1.adicionar_auto("Toyota", "Luis", "ABC-123")
    p1.mostrar()
class Cliente:
    def __init__(self, nombre, mesa):
        self.__nombre = nombre
        self.__mesa = mesa
        print(f"Cliente {self.__nombre} creado.")

    def __del__(self):
        print(f"Cliente {self.__nombre} eliminado.")

    def get_nombre(self):
        return self.__nombre

    def get_mesa(self):
        return self.__mesa

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_mesa(self, mesa):
        self.__mesa = mesa

    def mostrar(self):
        print(f"Cliente: {self.__nombre}, Mesa: {self.__mesa}")

class Pedido:
    def __init__(self, producto, estado):
        self.__producto = producto
        self.__estado = estado
        print(f"Pedido de {self.__producto} creado.")

    def __del__(self):
        print(f"Pedido de {self.__producto} eliminado.")

    def get_producto(self):
        return self.__producto

    def get_estado(self):
        return self.__estado

    def set_producto(self, producto):
        self.__producto = producto

    def set_estado(self, estado):
        self.__estado = estado

    def mostrar(self):
        print(f"Pedido: {self.__producto}, Estado: {self.__estado}")

cliente1 = Cliente("Ana", 5)
pedido1 = Pedido("Cafe Latte", "Registrado")

cliente1.mostrar()
pedido1.mostrar()

cliente1.set_mesa(10)
pedido1.set_estado("Entregado")

print("\nDespues de modificar:")
cliente1.mostrar()
pedido1.mostrar()

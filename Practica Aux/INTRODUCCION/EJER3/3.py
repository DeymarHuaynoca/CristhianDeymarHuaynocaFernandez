class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = cantidad * self.precio
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")
            print(f"Total a pagar: Bs. {total:.2f}")
        else:
            print(f"No hay suficiente stock. Solo quedan {self.stock} unidades.")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}.")
        print(f"Stock actual: {self.stock}")
p1 = Producto("Gaseosa", 8.5, 20)

p1.vender(5)
p1.vender(30)

p1.reabastecer(50)
p1.vender(10)

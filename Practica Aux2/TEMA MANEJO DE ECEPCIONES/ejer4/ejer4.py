class ProductoNoEncontradoException(Exception):
    def __init__(self, mensaje="El producto no fue encontrado en el inventario"):
        super().__init__(mensaje)

class StockInsuficienteException(Exception):
    def __init__(self, mensaje="No hay suficiente stock para realizar la venta"):
        super().__init__(mensaje)

class ProductoExistenteException(Exception):
    def __init__(self, mensaje="El producto con ese código ya existe"):
        super().__init__(mensaje)

class DatosInvalidosException(Exception):
    def __init__(self, mensaje="El precio o stock no pueden ser negativos"):
        super().__init__(mensaje)

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                raise ProductoExistenteException()
        if producto.precio < 0 or producto.stock < 0:
            raise DatosInvalidosException()
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado correctamente.")

    def buscarProducto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontradoException()

    def venderProducto(self, codigo, cantidad):
        producto = self.buscarProducto(codigo)
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            print(f"Venta realizada. Stock restante de {producto.nombre}: {producto.stock}")
        else:
            raise StockInsuficienteException()

if __name__ == "__main__":
    inventario = Inventario()

    try:
        p1 = Producto("001", "Laptop", 1500, 10)
        p2 = Producto("002", "Mouse", 25, 50)
        p3 = Producto("003", "Teclado", 40, 20)

        inventario.agregarProducto(p1)
        inventario.agregarProducto(p2)
        inventario.agregarProducto(p3)
        
        inventario.agregarProducto(Producto("001", "Monitor", 300, 5))
    except Exception as e:
        print("Error:", e)

    try:

        inventario.venderProducto("001", 5)  
        inventario.venderProducto("002", 60) 
    except Exception as e:
        print("Error:", e)

    try:
        producto = inventario.buscarProducto("999")
    except Exception as e:
        print("Error:", e)

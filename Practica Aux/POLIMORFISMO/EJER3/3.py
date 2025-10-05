class Matriz:
    def __init__(self, matriz=None):
        if matriz is None:
            self.matriz = [[1.0 if i == j else 0.0 for j in range(10)] for i in range(10)]
        else:
            self.matriz = matriz

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

    def sumar(self, otra):
        resultado = [[self.matriz[i][j] + otra.matriz[i][j] for j in range(10)] for i in range(10)]
        return Matriz(resultado)

    def restar(self, otra):
        resultado = [[self.matriz[i][j] - otra.matriz[i][j] for j in range(10)] for i in range(10)]
        return Matriz(resultado)

    def igual(self, otra):
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != otra.matriz[i][j]:
                    return False
        return True

print(" Matriz identidad (por defecto) ")
m1 = Matriz()  
m1.mostrar()

print("\n Matriz personalizada ")
m2 = Matriz([[float(i + j) for j in range(10)] for i in range(10)])
m2.mostrar()

print("\n Suma de matrices ")
m3 = m1.sumar(m2)
m3.mostrar()

print("\n Resta de matrices ")
m4 = m2.restar(m1)
m4.mostrar()

print("\n¿m1 es igual a m2?:", m1.igual(m2))
print("¿m1 es igual a m1?:", m1.igual(m1))

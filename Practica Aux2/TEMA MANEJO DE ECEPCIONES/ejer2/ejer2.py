class NumeroInvalidoException(Exception):
    def __init__(self, mensaje="El valor ingresado no es un numero entero válido"):
        super().__init__(mensaje)

class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ArithmeticError("Error: No se puede dividir entre cero.")
        return a / b

    @staticmethod
    def convertir_entero(texto):
        try:
            return int(texto)
        except ValueError:
            raise NumeroInvalidoException(f"'{texto}' no es un numero entero valido.")

if __name__ == "__main__":
    
    print("=== PRUEBAS CALCULADORA ===\n")

    try:
        print("Suma:", Calculadora.sumar(10, 5))
        print("Resta:", Calculadora.restar(10, 5))
        print("Multiplicacion:", Calculadora.multiplicar(10, 5))
        print("Division:", Calculadora.dividir(10, 2))
    except Exception as e:
        print("Error:", str(e))

    print("\n=== PRUEBA DE DIVISION POR CERO ===")
    try:
        print(Calculadora.dividir(10, 0))
    except Exception as e:
        print("Ocurrio un error:", e)

    print("\n=== PRUEBA CONVERSION STRING A ENTERO ===")
    try:
        num = Calculadora.convertir_entero("123")
        print("Número convertido:", num)
    except NumeroInvalidoException as e:
        print("Error:", e)

    print("\n=== PRUEBA CON ERROR EN CONVERSION ===")
    try:
        num = Calculadora.convertir_entero("abc")
        print("Numero convertido:", num)
    except NumeroInvalidoException as e:
        print("Error:", e)

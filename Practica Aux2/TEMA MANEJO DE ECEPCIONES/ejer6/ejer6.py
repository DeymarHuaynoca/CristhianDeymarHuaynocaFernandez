class FondosInsuficientesException(Exception):
    def __init__(self, mensaje="Fondos insuficientes para realizar la operacion"):
        super().__init__(mensaje)


class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise FondosInsuficientesException(
                f"No se puede retirar {monto}. Saldo disponible: {self.saldo}"
            )
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def mostrarInfo(self):
        print("=== Informacion de la Cuenta ===")
        print(f"Numero de cuenta: {self.numeroCuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print("===============================")

if __name__ == "__main__":
    cuenta = CuentaBancaria("12345", "Juan Perez", 1000)
    cuenta.mostrarInfo()

    try:
        cuenta.depositar(500)
    except Exception as e:
        print(f"Error en deposito: {e}")

    try:
        cuenta.depositar(-200)
    except Exception as e:
        print(f"Error en deposito: {e}")

    try:
        cuenta.retirar(300)
    except Exception as e:
        print(f"Error en retiro: {e}")

    try:
        cuenta.retirar(2000)
    except Exception as e:
        print(f"Error en retiro: {e}")

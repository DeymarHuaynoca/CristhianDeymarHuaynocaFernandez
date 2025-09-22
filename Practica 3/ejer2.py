import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
        self.vidas_restantes = numeroDeVidas

    def reiniciaPartida(self):
        self.vidas_restantes = self.numeroDeVidas

    def actualizaRecord(self):
        self.record += 1

    def quitaVida(self):
        self.vidas_restantes -= 1
        return self.vidas_restantes > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = None

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("\n juego adivina numero ")
        print("adivina el numero entre 0 y 10")

        while True:
            try:
                intento = int(input("introduce tu numero: "))
            except ValueError:
                print("ingresa un numero valido")
                continue

            if not self.validaNumero(intento):
                print("numero fuera de rango (0-10).intenta de nuevo.")
                continue

            if intento == self.numeroAAdivinar:
                print("¡acertaste!")
                self.actualizaRecord()
                break
            else:
                if intento < self.numeroAAdivinar:
                    print("el numero es mayor.")
                else:
                    print("el numero es menor.")

                if self.quitaVida():
                    print(f"te quedan {self.vidas_restantes} vidas.")
                else:
                    print(f"no te quedan vidas.el numero era {self.numeroAAdivinar}.")
                    break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 == 0:
                return True
            else:
                print("el numero no es par.intenta de nuevo.")
                return False
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 == 1:
                return True
            else:
                print("el numero no es impar.intenta de nuevo.")
                return False
        return False

class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]

        for juego in juegos:
            juego.juega()
            print(f"record actual: {juego.record}")
if __name__ == "__main__":
    Aplicacion.main()

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

    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.randint(0, 10)

        print("adivina el numero entre 0 y 10")
        while True:
            try:
                intento = int(input("introduce tu numero: "))
            except ValueError:
                print("ingresa un numero valido")
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
                    print(f"te quedan {self.vidas_restantes} vidas.intenta de nuevo.")
                else:
                    print(f"no te quedan vidas...el numero era {self.numeroAAdivinar}.")
                    break
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
        print(f"record de partidas ganadas:{juego.record}")
if __name__ == "__main__":
    Aplicacion.main()

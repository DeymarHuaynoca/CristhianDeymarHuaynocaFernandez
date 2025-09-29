import random
from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str = "sin color"):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def __str__(self):
        return f"figura de color: {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "azul"):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def como_colorear(self) -> str:
        return "colorear los 4 lados"

    def __str__(self):
        return f"cuadro --- lado: {self.lado}  color: {self.color}"

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "rojo"):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return 3.1416 * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return f"circulo ---  radio: {self.radio} | color: {self.color}"

def main():
    figuras = []

    for _ in range(5):
        tipo = random.randint(1, 2)  
        if tipo == 1:
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado))
        else:
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio))

    print("\nFiguras")
    for fig in figuras:
        print(fig)
        print("area:", fig.area())
        print("perimetro:", fig.perimetro())
        if isinstance(fig, Coloreado):
            print("como colorear:", fig.como_colorear())
        print()

if __name__ == "__main__":
    main()


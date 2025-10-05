class Fruta:
    def __init__(self, nombre, tipo, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.vitaminas = vitaminas
        self.nroVitaminas = len(vitaminas)

    def mostrar_vitaminas(self):
        print(f"Vitaminas de {self.nombre}: {', '.join(self.vitaminas)}")


f1 = Fruta("Kiwi", "Subtropical", ["K", "C", "E"])
f2 = Fruta("Naranja", "Cítrica", ["C", "A"])
f3 = Fruta("Banana", "Tropical", ["B6", "C"])

frutas = [f1, f2, f3]

mas_vitaminas = max(frutas, key=lambda f: f.nroVitaminas)
print(f"La fruta con más vitaminas es: {mas_vitaminas.nombre} ({mas_vitaminas.nroVitaminas})")

nombre_buscar = input("Ingrese el nombre de la fruta para ver sus vitaminas: ")
encontrada = False
for f in frutas:
    if f.nombre.lower() == nombre_buscar.lower():
        f.mostrar_vitaminas()
        encontrada = True
if not encontrada:
    print("No se encontró esa fruta.")

citricas = [f for f in frutas if f.tipo.lower() == "citrica"]
print(f"Cantidad de frutas citricas: {len(citricas)}")

ordenadas = sorted(frutas, key=lambda f: f.vitaminas)
print("\nFrutas ordenadas alfabeticamente por el nombre de sus vitaminas:")
for f in ordenadas:
    print(f"{f.nombre}: {', '.join(f.vitaminas)}")

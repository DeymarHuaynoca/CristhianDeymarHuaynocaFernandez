class Facultad:
    def __init__(self, nombre, sigla):
        self.nombre = nombre
        self.sigla = sigla
        self.estudiantes = []

class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.miembros = []

class Participante:
    def __init__(self, nombre, edad, ci, facultad, fraternidad):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
        self.facultad = facultad
        self.fraternidad = fraternidad

class SistemaEntrada:
    def __init__(self):
        self.participantes = []
        self.fraternidades = []
        self.facultades = []

    def registrarParticipante(self, participante):
        self.participantes.append(participante)
        participante.facultad.estudiantes.append(participante)
        participante.fraternidad.miembros.append(participante)

    def mostrarParticipantes(self):
        print("\n--- LISTA DE PARTICIPANTES ---")
        for p in self.participantes:
            print(f"{p.nombre} → {p.fraternidad.nombre} – {p.facultad.nombre}")

    def mostrarEncargados(self):
        print("\n--- ENCARGADOS DE FRATERNIDADES ---")
        for f in self.fraternidades:
            print(f"{f.nombre} → Encargado: {f.encargado}")

    def mostrarEdades(self):
        print("\n--- EDADES DE PARTICIPANTES ---")
        for p in self.participantes:
            print(f"{p.nombre}: {p.edad} años")

    def verificarRepetidos(self):
        print("\n--- VERIFICACIÓN DE PARTICIPANTES EN VARIAS FRATERNIDADES ---")
        conteo = {}

        for f in self.fraternidades:
            for p in f.miembros:
                conteo[p.ci] = conteo.get(p.ci, 0) + 1

        repetidos = [ci for ci, veces in conteo.items() if veces > 1]

        if not repetidos:
            print("✔ Todos los participantes cumplen: nadie esta en mas de una fraternidad.")
        else:
            print("❌ Participantes repetidos:")
            for ci in repetidos:
                for p in self.participantes:
                    if p.ci == ci:
                        print(f"- {p.nombre}")

s = SistemaEntrada()

fni = Facultad("Ingenieria", "FNI")
fdcp = Facultad("Derecho y Cs. Políticas", "FDCP")

s.facultades.extend([fni, fdcp])

caporales = Fraternidad("Caporales Central", "Luis Mamani")
tobas = Fraternidad("Tobas Zona Sur", "María Villca")

s.fraternidades.extend([caporales, tobas])

p1 = Participante("José Perez", 21, "8239121", fni, caporales)
p2 = Participante("Ana Flores", 20, "9093312", fdcp, caporales)
p3 = Participante("Marco Quispe", 22, "7349122", fni, tobas)
p4 = Participante("Laura Choque", 19, "10023911", fdcp, tobas)
p5 = Participante("Kevin Aramayo", 23, "7783120", fni, caporales)

for p in [p1, p2, p3, p4, p5]:
    s.registrarParticipante(p)
s.mostrarParticipantes()
s.mostrarEncargados()
s.mostrarEdades()
s.verificarRepetidos()

nuevo = Participante("Roberto Molina", 20, "8893311", fni, tobas)
s.registrarParticipante(nuevo)

print("\n--- Nuevo participante registrado ---")
s.mostrarParticipantes()

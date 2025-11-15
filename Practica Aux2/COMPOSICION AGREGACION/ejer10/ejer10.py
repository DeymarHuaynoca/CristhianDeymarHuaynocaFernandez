class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad

class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket

class Charla:
    def __init__(self, lugar, nombreCharla, S, participantes):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.S = S                    
        self.participantes = participantes  
        self.np = len(participantes)        

class Evento:
    def __init__(self, nombre, charlas):
        self.nombre = nombre
        self.charlas = charlas  
        self.nc = len(charlas)

def edad_promedio(evento):
    suma = 0
    contador = 0

    for charla in evento.charlas:
        for p in charla.participantes:
            suma += p.edad
            contador += 1

    if contador == 0:
        return 0

    return suma / contador

def buscar_persona(evento, nombre, apellido):
    for charla in evento.charlas:

        if (charla.S.nombre == nombre and charla.S.apellido == apellido):
            return True

        for p in charla.participantes:
            if (p.nombre == nombre and p.apellido == apellido):
                return True

    return False

def eliminar_charlas_por_speaker(evento, ci_speaker):
    nuevas_charlas = []
    for charla in evento.charlas:
        if charla.S.ci != ci_speaker:
            nuevas_charlas.append(charla)

    evento.charlas = nuevas_charlas
    evento.nc = len(nuevas_charlas)

def ordenar_charlas_por_participantes(evento):
    evento.charlas.sort(key=lambda charla: charla.np)
s1 = Speaker("Ana", "Lopez", 40, 111, "IA")
s2 = Speaker("Luis", "Perez", 35, 222, "Redes")

p1 = Participante("Carlos", "Mendez", 20, 501, 1)
p2 = Participante("Maria", "Diaz", 22, 502, 2)
p3 = Participante("Jose", "Rojas", 25, 503, 3)

c1 = Charla("Auditorio 1", "IA Moderna", s1, [p1, p2])
c2 = Charla("Auditorio 2", "Computación", s2, [p3])

evento = Evento("Tech Day", [c1, c2])

print("Promedio de edad:", edad_promedio(evento))

print("¿Está Maria Diaz?:", buscar_persona(evento, "Maria", "Diaz"))

eliminar_charlas_por_speaker(evento, 111)

print("Charlas luego de eliminar al speaker 111:", len(evento.charlas))

ordenar_charlas_por_participantes(evento)

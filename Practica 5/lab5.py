from datetime import datetime, timedelta

class Pagina:                    
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar(self):
        print(f"  Página {self.numero}: {self.contenido}")

class Libro:                    
    def __init__(self, titulo, isbn, contenido_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i+1, texto) for i, texto in enumerate(contenido_paginas)]

    def leer(self):
        print(f"--- Leyendo libro '{self.titulo}' ---")
        for p in self.paginas:
            p.mostrar()

class Autor:                     
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} - {self.nacionalidad}")

class Estudiante:                
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.codigo} - {self.nombre}")

class Prestamo:                   
    def __init__(self, estudiante, libro, dias=14):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = datetime.now().date()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias)

    def mostrarInfo(self):
        print(f"Préstamo: {self.estudiante.nombre} -> {self.libro.titulo}")
        print(f"  {self.fecha_prestamo}  /  {self.fecha_devolucion}")

class Horario:                   
    def __init__(self, dias, h_ini, h_fin):
        self.dias = dias
        self.h_ini = h_ini
        self.h_fin = h_fin

    def mostrarHorario(self):
        print("Horario:", ", ".join(self.dias), f"{self.h_ini}-{self.h_fin}")

class Biblioteca:
    def __init__(self, nombre, dias=["Lun","Mar","Mie","Jue","Vie"], h_ini="08:00", h_fin="18:00"):
        self.nombre = nombre
        self.libros = []      
        self.autores = []     
        self.prestamos = []   
        self.horario = Horario(dias, h_ini, h_fin) 

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, est, lib):
        prest = Prestamo(est, lib)
        self.prestamos.append(prest)
        return prest

    def mostrarEstado(self):    
        print(f"\n=== ESTADO DE LA BIBLIOTECA: {self.nombre} ===")

        print("\nLibros:")
        if self.libros:
            for l in self.libros:
                print(f" - {l.titulo} ({l.isbn})")
        else:
            print("  No hay libros registrados.")

        print("\nAutores:")
        if self.autores:
            for a in self.autores:
                print(f" - {a.nombre} ({a.nacionalidad})")
        else:
            print("  No hay autores registrados.")

        print("\nPrestamos activos:")
        if self.prestamos:
            for p in self.prestamos:
                print(f" - {p.estudiante.nombre} tiene '{p.libro.titulo}'")
        else:
            print("  No hay prestamos activos.")

        print("\nHorario:")
        if self.horario:
            self.horario.mostrarHorario()
        else:
            print("  Biblioteca cerrada (sin horario)")

    def cerrarBiblioteca(self):
        self.prestamos.clear()
        self.horario = None
        print("\nLa biblioteca ha sido cerrada. Ya no existe el horario ni los prestamos.")

if __name__ == "__main__":

    b = Biblioteca("UMSA – Central")

    a1 = Autor("Gabo", "Colombiano")
    b.agregarAutor(a1)

    l1 = Libro("Cien años de soledad", "ISBN-001", ["Texto1", "Texto2"])
    b.agregarLibro(l1)

    e1 = Estudiante("2025001", "María")

    print("\n >> DEMO COMPOSICION (Libro contiene paginas):")
    l1.leer()

    print("\n >> DEMO ASOCIACION (Prestamo asocia estudiante – libro):")
    p = b.prestarLibro(e1, l1)
    p.mostrarInfo()

    print("\n >> ESTADO ACTUAL DE LA BIBLIOTECA:")
    b.mostrarEstado()

    print("\n >> DEMO COMPOSICION (Biblioteca contiene horario y si cierra desaparece):")
    b.cerrarBiblioteca()

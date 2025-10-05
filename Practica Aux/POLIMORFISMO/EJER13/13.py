class MP4:
    def __init__(self, marca="", capacidadGb=1.0):
        self.marca = marca
        self.capacidadGb = capacidadGb
        self.nroCanciones = 0
        self.nroVideos = 0

        self.canciones = [[""] * 100 for _ in range(3)]

        self.videos = [[""] * 3 for _ in range(100)]

    def borrar_cancion(self, criterio, valor):

        indice = -1
        for i in range(self.nroCanciones):
            if criterio == "nombre" and self.canciones[0][i] == valor:
                indice = i
                break
            elif criterio == "artista" and self.canciones[1][i] == valor:
                indice = i
                break
            elif criterio == "peso" and self.canciones[2][i] == str(valor):
                indice = i
                break

        if indice != -1:
            for j in range(indice, self.nroCanciones - 1):
                for k in range(3):
                    self.canciones[k][j] = self.canciones[k][j+1]
            for k in range(3):
                self.canciones[k][self.nroCanciones - 1] = ""
            self.nroCanciones -= 1
            print(f"Cancion eliminada correctamente por {criterio} = {valor}")
        else:
            print("Cancion no encontrada.")

    def __add__(self, nueva_cancion):

        nombre, artista, peso = nueva_cancion

        for i in range(self.nroCanciones):
            if self.canciones[0][i] == nombre:
                print(" La cancion ya existe en el MP4.")
                return self

        if self.capacidad_disponible() < (int(peso) / 1024):  
            print(" No hay suficiente espacio para esta cancion.")
            return self

        i = self.nroCanciones
        self.canciones[0][i] = nombre
        self.canciones[1][i] = artista
        self.canciones[2][i] = str(peso)
        self.nroCanciones += 1
        print(f" Canción '{nombre}' añadida correctamente.")
        return self

    def __sub__(self, nuevo_video):

        nombre, artista, peso = nuevo_video

        for i in range(self.nroVideos):
            if self.videos[i][0] == nombre:
                print(" El video ya existe en el MP4.")
                return self

        if self.capacidad_disponible() < int(peso):
            print(" No hay suficiente espacio para este video.")
            return self

        i = self.nroVideos
        self.videos[i][0] = nombre
        self.videos[i][1] = artista
        self.videos[i][2] = str(peso)
        self.nroVideos += 1
        print(f" Video '{nombre}' añadido correctamente.")
        return self

    def capacidad_disponible(self):
        total_usado_mb = 0

        for i in range(self.nroCanciones):
            total_usado_mb += int(self.canciones[2][i]) / 1024.0

        for i in range(self.nroVideos):
            total_usado_mb += int(self.videos[i][2])

        return self.capacidadGb * 1024 - total_usado_mb

    def mostrar_capacidad(self):
        print(f" Capacidad disponible: {self.capacidad_disponible():.2f} MB")

    def mostrar_contenido(self):
        print("\n Canciones:")
        for i in range(self.nroCanciones):
            print(f"  - {self.canciones[0][i]} | {self.canciones[1][i]} | {self.canciones[2][i]} Kb")

        print("\n Videos:")
        for i in range(self.nroVideos):
            print(f"  - {self.videos[i][0]} | {self.videos[i][1]} | {self.videos[i][2]} Mb")

if __name__ == "__main__":
    mp4 = MP4("Sony", 1.0) 

    mp4 = mp4 + ("Back To Black", "Amy Winehouse", 100)
    mp4 = mp4 + ("Lost On You", "LP", 150)

    mp4 = mp4 - ("Heathens", "twenty one pilots", 50)
    mp4 = mp4 - ("Harmonica Andromeda", "KSHMR", 70)

    mp4.mostrar_contenido()
    mp4.mostrar_capacidad()

    mp4.borrar_cancion("nombre", "Lost On You")
    mp4.mostrar_contenido()
    mp4.mostrar_capacidad()

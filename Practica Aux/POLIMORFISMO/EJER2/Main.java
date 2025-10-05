package POLIMORFISMO.EJER2;

public class Main {
    public static void main(String[] args) {
        // Crear objetos de Videojuego
        Videojuego v1 = new Videojuego("League of Legends", "PC", 10);
        Videojuego v2 = Videojuego.nombreYPlataforma("God of War", "PlayStation 5");

        System.out.println(" Videojuego 1 ");
        v1.mostrarInfo();

        System.out.println("\n Videojuego 2 ");
        v2.mostrarInfo();

        System.out.println("\n Agregando jugadores ");
        v1.agregarJugadores();       // sin cantidad específica
        v2.agregarJugadores(3);      // con cantidad específica
    }
}

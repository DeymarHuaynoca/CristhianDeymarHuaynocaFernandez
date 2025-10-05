package POLIMORFISMO.EJER2;

public public class Videojuego {
    // Atributos
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    // Constructor por defecto
    public Videojuego() {
        this.nombre = "Desconocido";
        this.plataforma = "Desconocida";
        this.cantidadJugadores = 0;
    }

    // Constructor con parámetros
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    // Constructor alternativo: solo nombre
    public static Videojuego soloNombre(String nombre) {
        return new Videojuego(nombre, "Desconocida", 0);
    }

    // Constructor alternativo: nombre y plataforma
    public static Videojuego nombreYPlataforma(String nombre, String plataforma) {
        return new Videojuego(nombre, plataforma, 0);
    }

    // Método para mostrar la información
    public void mostrarInfo() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Plataforma: " + this.plataforma);
        System.out.println("Cantidad de jugadores: " + this.cantidadJugadores);
    }

    // Sobrecarga de métodos para agregar jugadores
    public void agregarJugadores() {
        this.cantidadJugadores++;
        System.out.println("Se agregó 1 jugador. Total: " + this.cantidadJugadores);
    }

    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
        System.out.println("Se agregaron " + cantidad + " jugadores. Total: " + this.cantidadJugadores);
    }
}
 {
    
}

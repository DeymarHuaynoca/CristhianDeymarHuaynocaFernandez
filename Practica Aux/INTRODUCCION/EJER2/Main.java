package INTRODUCCION.EJER2;

public class Main {
    public static void main(String[] args) {
        Bus miBus = new Bus(30);  

        miBus.subirPasajeros(15);
        miBus.mostrarAsientosDisponibles();
        miBus.cobrarPasaje();

        miBus.subirPasajeros(20); 
        miBus.mostrarAsientosDisponibles();
        miBus.cobrarPasaje();
    }
}

